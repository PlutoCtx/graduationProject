# @Version: python3.10
# @Time: 2023/10/25 23:36
# @Author: PlutoCtx
# @Email: 15905898514@163.com
# @File: __init__.py
# @Software: PyCharm
# @User: chent

import pandas as pd

data = pd.read_table('wifi_localization.txt', header=None, delim_whitespace=True)

feature = data.iloc[:, 0:7]
label = data.iloc[:, 7]

from sklearn.model_selection import train_test_split

train_features, test_features, train_labels, test_labels = train_test_split(feature, label)

from sklearn.svm import SVC

model = SVC()

parameters = {'kernel': ('linear', 'rbf'), 'C': [1, 10]}

# model = grid_search.GridSearchCV(model, parameters)

model.fit(train_features, train_labels)
prediction = model.predict(test_features)

from sklearn.metrics import classification_report

labels = [1, 2, 3, 4]
classes = [
    'position 1',
    'position 2',
    'position 3',
    'position 4',
]

# 使用函数生成总体的报告
print(classification_report(
    test_labels,
    prediction,
    target_names=classes,
    labels=labels,
    digits=4
))
