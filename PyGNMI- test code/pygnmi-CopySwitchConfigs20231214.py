pip install pygnmi
import grpc
from pygnmi.client import gNMIclient, telemetryParser
from google.protobuf.json_format import MessageToDict

def get_gnmi_client(target):
    return gNMIclient(target=target)

def copy_configs(source_client, destination_client, paths):
    for path in paths:
        # Get the configuration from the source device
        response = source_client.get(path=path)

        # Extract and convert the configuration to a dictionary
        config_dict = MessageToDict(response.notification[0].update[0].val)

        # Apply the configuration to the destination device
        set_request = destination_client.set(update=[{'path': path, 'val': response.notification[0].update[0].val}])
        destination_client.set(set_request)

        print(f"Configuration copied for path: {path}")
        print(f"Configuration:\n{config_dict}\n")

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
    destination_client = get_gnmi_client(destination_target)

    # Copy configurations from source to destination
    copy_configs(source_client, destination_client, configuration_paths)
