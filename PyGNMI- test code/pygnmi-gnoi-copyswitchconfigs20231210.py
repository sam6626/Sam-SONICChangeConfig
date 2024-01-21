from pygnmi.client import gNMIclient, telemetryParser

def copy_sonic_config(target, username, password, source_path, target_path):
    # Create a gNMI client
    with gNMIclient(target=target, username=username, password=password) as client:
        # Prepare the set request with the configuration data
        set_request = [
            {
                "path": source_path.split("/"),
                "val": {"json_ietf_val": {"string_val": "YOUR_CONFIGURATION_DATA"}}
            }
        ]

        # Send the set request
        client.set(set_request)

        #check the response
        response = client.get(source_path)
        print(f"Response after setting configuration: {response}")

        # Copy configuration from source path to target path
        copy_request = [
            {
                "path": source_path.split("/"),
                "alias": {"path": target_path.split("/")}
            }
        ]

        # Send the copy request
        client.set(copy_request)

        # check the response
        response = client.get(target_path)
        print(f"Response after copying configuration: {response}")

if __name__ == "__main__":
    # Define your gNMI target (device details)
    target = "127.0.0.1:9339"
    username = "your_username"
    password = "your_password"

    # Specify the source and target paths for the configuration copy
    source_path = "/system"
    target_path = "/system-new"

    # Call the function to copy Sonic configuration
    copy_sonic_config(target, username, password, source_path, target_path)
