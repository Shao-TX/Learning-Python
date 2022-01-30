#%%
import numpy as np
import torch

#%%
original_data = torch.tensor([[1, 2, 3, 4, 5],
                              [6, 7, 8, 9, 10]], dtype = torch.float32)

torch_mean = original_data.mean(dim=0, keepdims=True)
torch_std = original_data.std(dim=0, keepdim=True)

#%%

torch_normalize_data = (original_data - torch_mean) / torch_std
# %%
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().fit(original_data)
sklearn_normalize_data = scaler.transform(original_data)

# %%
print("Original Data：\n", original_data)
print()

print("torch mean : ", torch_mean)
print("sklearn mean : ", scaler.mean_)

print()

print("torch std : ", torch_std)       # torch   : 樣本標準差
print("sklearn std : ", scaler.scale_) # sklearn : 母體標準差

print()

print("torch normalize：\n", torch_normalize_data)
print("sklearn normalize： \n", sklearn_normalize_data)

# %%