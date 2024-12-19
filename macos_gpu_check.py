import torch
import time

# Set the device to MPS (Metal Performance Shaders)
device = torch.device('mps')

# Create random tensors
x = torch.rand((10000, 10000), dtype=torch.float32)
y = torch.rand((10000, 10000), dtype=torch.float32)

# Move tensors to MPS device
x = x.to(device)
y = y.to(device)

# Time the multiplication
start_time = time.time()
result = torch.matmul(x, y)
end_time = time.time()

# Print the execution time
print(f"Time taken for multiplication: {end_time - start_time} seconds")
