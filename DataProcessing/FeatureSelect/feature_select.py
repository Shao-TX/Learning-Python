#%%
import sklearn
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
import numpy as np

#%%
x_train = np.array([[1,2,3,4,5], [5,4,3,2,1], [1,9,10,4,8]])
y_train = np.array([1,2,1])

#%%

# score_func : 特徵選擇函數 , k : 要取的特徵數量
selector = SelectKBest(score_func=f_regression, k=3)

selector.fit(x_train, y_train)                 # 獲取適應的特徵

Scores = selector.scores_                      # 特徵分數
Pvalues = selector.pvalues_                    # p-values

GetSupport = selector.get_support(True)        # 獲取特徵位置
new_x_train = selector.transform(x_train)      # 將原特徵取代為選取過的特徵

#%%
print("特徵分數 : \n", Scores)
print()

print("p-values : \n", Pvalues)
print()

print("特徵位置 : \n", GetSupport)
print()

print("挑選過的特徵 : \n", new_x_train)

#%%