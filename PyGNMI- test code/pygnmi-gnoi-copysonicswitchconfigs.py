import grpc
from pygnmi.client import gNMIclient
from gnmi import gNMI_pb2, gNMI_pb2_grpc

def get_gnmi_client(target):
    return gNMIclient(target=target)

def get_gnoi_client(target):
    channel = grpc.insecure_channel(target)
    return gNMI_pb2_grpc.gNOIStub(channel)

def copy_configs_gnmi(source_client, destination_client, paths):
    for path in paths:
        # Get the configuration from the source device
        response = source_client.get(path=path)

        # Apply the configuration to the destination device
        set_request = destination_client.Set(
            requests=[gNMI_pb2.SetRequest(
                update=[gNMI_pb2.Update(
                    path=response.notification[0].update[0].path,
                    val=response.notification[0].update[0].val
                )]
            )]
        )
        destination_client.Set(set_request)

        print(f"Configuration copied for path: {path}")

if __name__ == "__main__":
    # Replace these values with your actual device details
    source_target = 'source_device:57400'
    destination_target = 'destination_device:57400'

    # Specify the configuration paths to copy
    configuration_paths = [
        "/system",
        "/interfaces",
        # Add more paths as needed
    ]

    # Create gNMI clients for the source and destination devices
    source_client = get_gnmi_client(source_target)
    
    # Create gNOI client for the destination device
    destination_client = get_gnoi_client(destination_target)

    # Copy configurations from source to destination using gNMI
    copy_configs_gnmi(source_client, destination_client, configuration_paths)
