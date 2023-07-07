import torch

print(torch.cuda.current_device()) # 0
print(torch.cuda.device(0)) # <torch.cuda.device object at 0x7f9543a44040>
print(torch.cuda.device_count()) # 1
print(torch.cuda.get_device_name(0)) # NVIDIA GeForce RTX 3080 Ti
print(torch.cuda.is_available()) # True