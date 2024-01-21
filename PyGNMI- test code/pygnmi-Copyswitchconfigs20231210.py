import grpc
from pygnmi.client import gNMIStub
from pygnmi.proto import gnmi_pb2

def copy_config_from_sonic(switch_ip, switch_port, username, password, target_path, output_file):
    # gRPC connection details
    channel = grpc.insecure_channel(f"{switch_ip}:{switch_port}")
    stub = gNMIStub(channel)

    # gNMI authentication details
    credentials = grpc.ssl_channel_credentials()
    auth = grpc.metadata_call_credentials(lambda _, cb: cb([('username', username), ('password', password)], None))

    # Combine channel and authentication credentials
    composite_credentials = grpc.composite_channel_credentials(credentials, auth)
    channel = grpc.secure_channel(f"{switch_ip}:{switch_port}", composite_credentials)
    stub = gNMIStub(channel)

    # Create a gNMI Capabilities request
    capabilities_request = gnmi_pb2.CapabilityRequest()
    response = stub.Capabilities(capabilities_request)

    # Check for supported encoding and version
    supported_encodings = response.supported_encodings
    supported_versions = response.supported_versions

    # Choose the first supported encoding and version
    encoding = supported_encodings[0]
    version = supported_versions[0]

    # Create a gNMI Get request
    get_request = gnmi_pb2.GetRequest()
    get_request.encoding = encoding
    get_request.version = version
    get_request.path.extend([gnmi_pb2.PathElem(name=elem) for elem in target_path.split("/")])

    # Send the gNMI Get request
    get_response = stub.Get(get_request)

    # Write the received configuration to a file
    with open(output_file, 'wb') as f:
        f.write(get_response.notification[0].update[0].val.binary_val)

if __name__ == "__main__":
    # Replace these values with your Sonic switch details
    switch_ip = "192.168.1.1"
    switch_port = 9339
    username = "your_username"
    password = "your_password"
    target_path = "system/config"
    output_file = "config_backup.txt"

    copy_config_from_sonic(switch_ip, switch_port, username, password, target_path, output_file)
