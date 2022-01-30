# Normalize

## 公式：

* μ : [算術平均數](https://zh.wikipedia.org/wiki/%E7%AE%97%E6%9C%AF%E5%B9%B3%E5%9D%87%E6%95%B0)
* σ : [標準差](https://zh.wikipedia.org/wiki/%E6%A8%99%E6%BA%96%E5%B7%AE)

<img src="https://i.imgur.com/mVp33sv.png" width="40%" height="40%">

## 標準差：
標準差分為**母體標準差**跟**樣本標準差**，主要分別在於：
* 母體標準差：√Σ(x-μ)²/n
* 樣本標準差：√Σ(x-μ)²/(n-1)

## PyTorch & Sklearn：
**Input：**
```
original_data = torch.tensor([[1, 2, 3, 4, 5],
                              [6, 7, 8, 9, 10]], dtype = torch.float32)
                              
# Pytorch
torch_std = original_data.std(dim=0, keepdim=True)
print("torch std : ", torch_std)

# Sklearn
scaler = StandardScaler().fit(original_data)
print("sklearn std : ", scaler.scale_)
```
* Pytorch Output：
```
torch std :  tensor([[3.5355, 3.5355, 3.5355, 3.5355, 3.5355]])
```

* Sklearn Output : 
```
sklearn std :  [2.5 2.5 2.5 2.5 2.5]
```

輸出值不同，問題在於 **Pytorch** 是使用**樣本標準差**計算，而 **Sklearn** 是使用**母體標準差**計算

## 計算：
此處為方便計算只使用第1行 : [[1], [6]]
* Pytorch : 
μ = (1+6) / 2 = 3.5
σ = √((1-3.5)² + (6-3.5)²) / (2-1) = 3.5355
`Normalize Result = [[(1-3.5) / 3.5355], [(6-3.5) / 3.5355]] = [[-0.707], [0.707]]`

* Sklearn : 
μ = (1+6) / 2 = 3.5
σ = √((1-3.5)² + (6-3.5)²) / 2 = 2.5
`Normalize Result = [[(1-3.5) / 2.5], [(6-3.5) / 2.5]]　=　[[-1], [1]]`

## Code Output : 
```
Original Data：
tensor([[ 1.,  2.,  3.,  4.,  5.],
        [ 6.,  7.,  8.,  9., 10.]])

torch mean :  tensor([[3.5000, 4.5000, 5.5000, 6.5000, 7.5000]])
sklearn mean :  [3.5 4.5 5.5 6.5 7.5]

torch std :  tensor([[3.5355, 3.5355, 3.5355, 3.5355, 3.5355]])
sklearn std :  [2.5 2.5 2.5 2.5 2.5]

torch normalize：
tensor([[-0.7071, -0.7071, -0.7071, -0.7071, -0.7071],
        [ 0.7071,  0.7071,  0.7071,  0.7071,  0.7071]])
sklearn normalize： 
 [[-1. -1. -1. -1. -1.]
 [ 1.  1.  1.  1.  1.]]
```

## Reference : 
* [torch.std](https://pytorch.org/docs/stable/generated/torch.std.html)
* [sklearn.preprocessing.StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
* [Normalization](https://zh.wikipedia.org/wiki/%E6%A0%87%E5%87%86%E5%8C%96_(%E7%BB%9F%E8%AE%A1%E5%AD%A6))