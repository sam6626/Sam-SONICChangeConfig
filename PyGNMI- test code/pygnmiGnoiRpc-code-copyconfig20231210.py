import grpc
from gnmi import gNMI_pb2
from gnmi import gNMI_pb2_grpc
from google.protobuf import empty_pb2

# Define the Sonic switch gNOI server address
SONIC_SWITCH_ADDRESS = 'your_sonic_switch_ip:6030'

def create_gnmi_stub():
    # Create a gRPC channel to connect to the Sonic switch gNOI server
    channel = grpc.insecure_channel(SONIC_SWITCH_ADDRESS)

    # Create a gNMI stub
    stub = gNMI_pb2_grpc.gNMIServicerStub(channel)

    return stub

def copy_config_file(stub, source_path, target_path):
    # Create the CopyConfigRequest message
    copy_config_request = gNMI_pb2.CopyConfigRequest(
        source=source_path,
        target=target_path,
    )

    # Make the RPC call to copy the configuration file
    response = stub.CopyConfig(copy_config_request)

    # Print the RPC response
    print("Copy Config Response:")
    print(response)

def main():
    # Connect to the Sonic switch gNOI server
    stub = create_gnmi_stub()

    # Specify the source and target paths for the configuration file
    source_path = 'source_config_path_on_switch'
    target_path = 'target_config_path_on_switch'

    # Copy the configuration file
    copy_config_file(stub, source_path, target_path)

if __name__ == "__main__":
    main()
