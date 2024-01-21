import grpc
from your_generated_proto_file import gnoi_service_pb2, gnoi_service_pb2_grpc

# Set the gRPC server details
server_address = 'your_sonic_switch_address'
server_port = 50051  # Replace with the actual gRPC port

# Establish a gRPC channel
channel = grpc.insecure_channel(f"{server_address}:{server_port}")

# Create a gRPC stub
stub = gnoi_service_pb2_grpc.GNOIStub(channel)

# Create a request for file copy
request = gnoi_service_pb2.CopyRequest(
    source="/path/to/source/config.xml",
    destination="/path/to/destination/config.xml"
)

# Make the gNOI RPC call for file copy
response = stub.Copy(request)

# Handle the response (check for success or error)
print(f"Copy Response: {response}")
