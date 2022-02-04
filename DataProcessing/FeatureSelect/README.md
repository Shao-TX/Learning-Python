# Sklearn-SelectBest


## **f_regression :** 
F-value between label/feature for regression tasks.

* The correlation between each regressor and the target is computed,that is, ((X[:, i] - mean(X[:, i])) * (y - mean_y)) / (std(X[:, i]) * std(y)).
* It is converted to an F score then to a p-value.

### Correlation Coefficient : 

#### 參數 : 
* 共變異數(cov) : <img src="http://chart.googleapis.com/chart?cht=tx&chl= \frac{1}{n-1}{\sum_{i=1}^n(x_i - \mu_x)(y_i - \mu_y)}" style="border:none;">
* 標準差(std) : <img src="http://chart.googleapis.com/chart?cht=tx&chl= \sqrt{\frac{1}{n-1}\sum_{i=1}^n(x_i - \mu_x)^2}" style="border:none;">
* 變異數(var) : std<img src="http://chart.googleapis.com/chart?cht=tx&chl= ^2" style="border:none;">

#### 公式 : 
* r = <img src="http://chart.googleapis.com/chart?cht=tx&chl= \frac {\sum_{i=1}^n(x_i - \mu_x)(y_i - \mu_y)}{\sqrt{\sum_{i=1}^n(x_i - \mu_x)^2}\sqrt{\sum_{i=1}^n(y_i - \mu_y)^2}}" style="border:none;">

#### 原理 : 
若x與y分佈一樣，r(相關係數)就會越接近 +-1 ，此時代表兩者完全相關，r>0 為正相關、r<0 為負相關，而除以標準差是為了讓兩者的值落在 +-1 之間，

#### 計算 : 
| ID  | Feature | Target |
|:---:|:-------:|:------:|
| ID1 |   -2    |  -20   |
| ID2 |   -1    |  -10   |
| ID3 |    1    |   10   |
| ID4 |    2    |   20   |

* <img src="http://chart.googleapis.com/chart?cht=tx&chl= \mu_x" style="border:none;"> = (-2 + -1 + 1 + 2) / 4 = 0
* <img src="http://chart.googleapis.com/chart?cht=tx&chl= \mu_y" style="border:none;"> = (-20 + -10 + 10 + 20) / 4 = 0
* <img src="http://chart.googleapis.com/chart?cht=tx&chl= \sum_{i=1}^n(x_i - \mu_x)(y_i - \mu_y)" style="border:none;">$$ = (-2 x -20) + (-1 x -10) + (1 x 10) + (2 x 20) = 100
* <img src="http://chart.googleapis.com/chart?cht=tx&chl= \sqrt{\sum_{i=1}^n(x_i - \mu_x)^2}" style="border:none;"> = <img src="http://chart.googleapis.com/chart?cht=tx&chl= \sqrt{(-2 - 0)^2 + (-1 - 0)^2 + (1 - 0)^2 + (2 - 0)^2}" style="border:none;"> = <img src="http://chart.googleapis.com/chart?cht=tx&chl= \sqrt{10}" style="border:none;">
* <img src="http://chart.googleapis.com/chart?cht=tx&chl= \sqrt{\sum_{i=1}^n(y_i - \mu_y)^2}" style="border:none;"> = <img src="http://chart.googleapis.com/chart?cht=tx&chl= \sqrt{(-20 - 0)^2 + (-10 - 0)^2 + (10 - 0)^2 + (20 - 0)^2}" style="border:none;"> = <img src="http://chart.googleapis.com/chart?cht=tx&chl= \sqrt{1000}"

Result : r = <img src="http://chart.googleapis.com/chart?cht=tx&chl= \frac{100}{\sqrt{10}\sqrt{1000}}" style="border:none;"> = 1

### P-Value : 
P-Value 的使用方式較複雜，以下是自行觀察的結果 : 
* 觀察到比觀察到的值更極端的機率是多少
* SelectKBest 中會選擇值較小的


### Code :
#### Input :
```
x_train = np.array([[1,2,3,4,5], [5,4,3,2,1], [1,9,10,4,8]])
y_train = np.array([1,2,1])
```
#### Output :
```
特徵分數 : 
 [-2.25179981e+15  6.12244898e-02  3.33333333e-01  4.50359963e+15
  4.48148148e+00]

p-values : 
 [1.00000000e+00 8.45579042e-01 6.66666667e-01 9.48637385e-09
 2.80944401e-01]

特徵位置 : 
 [2 3 4]

挑選過的特徵 : 
 [[ 3  4  5]
 [ 3  2  1]
 [10  4  8]]
```

### Reference : 
* [Correlation Coefficient and Covariance](https://chih-sheng-huang821.medium.com/%E7%9B%B8%E9%97%9C%E4%BF%82%E6%95%B8%E8%88%87%E5%85%B1%E8%AE%8A%E7%95%B0%E6%95%B8-correlation-coefficient-and-covariance-c9324c5cf679)
* [sklearn.feature_selection.SelectKBest](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html)
* [李柏堅-統計學課程 : 相關](https://www.youtube.com/watch?v=z-21v0EoFh4)
* [Wiki : P-Value](https://zh.wikipedia.org/wiki/P%E5%80%BC)