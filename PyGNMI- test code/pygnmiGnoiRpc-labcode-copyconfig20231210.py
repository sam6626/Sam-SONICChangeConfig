import grpc
from gnmi import gNMI_pb2
from gnmi import gNMI_pb2_grpc
from google.protobuf import empty_pb2

# Define the Sonic switch gNOI server address
SONIC_SWITCH_ADDRESS = '10.10.10.221:6030'

def create_gnmi_stub():
    channel = grpc.insecure_channel(SONIC_SWITCH_ADDRESS)

    stub = gNMI_pb2_grpc.gNMIServicerStub(channel)

    return stub

def copy_config_file(stub, source_path, target_path):
    copy_config_request = gNMI_pb2.CopyConfigRequest(
        source=source_path,
        target=target_path,
    )

    response = stub.CopyConfig(copy_config_request)

    print("Copy Config Response:")
    print(response)

def main():
    stub = create_gnmi_stub()

    source_path = 'source_config_path_on_switch'
    target_path = 'target_config_path_on_switch'

    
    copy_config_file(stub, source_path, target_path)

if __name__ == "__main__":
    main()
