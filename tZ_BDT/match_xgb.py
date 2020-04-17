import pandas as pd
import numpy as np
import re
import sklearn
import xgboost as xgb
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import sklearn as sk
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
import pickle
import sys
import torch
import scipy


inFile = sys.argv[1]
inDF = pd.read_csv(inFile)

maxDepth = 5

inDF = sk.utils.shuffle(inDF)
#inDF = inDF[inDF['topMassReco']>0]
inDF[abs(inDF) < 0.01] = 0
train, test = train_test_split(inDF, test_size=0.3)

y_train = train['signal']
y_test = test['signal']

train = train.drop(['signal'],axis=1)
test = test.drop(['signal'],axis=1)

xgb_train = xgb.DMatrix(train, label=y_train, feature_names=list(train))
xgb_test = xgb.DMatrix(test, label=y_test, feature_names=list(train))

params = {
    'learning_rate' : 0.01,
    'max_depth': maxDepth,
    'min_child_weight': 2,
    'gamma': 0.9,
    'subsample' : 0.6,
    'colsample_bytree' : 0.6,
    'eval_metric': 'auc',
    'nthread': -1,
    'scale_pos_weight':1
}

gbm = xgb.cv(params, xgb_train, num_boost_round=1200, verbose_eval=True)

best_nrounds = pd.Series.idxmax(gbm['test-auc-mean'])
print( best_nrounds)

bst = xgb.train(params, xgb_train, num_boost_round=best_nrounds, verbose_eval=True)
pickle.dump(bst, open('models/xgb_signal.dat', "wb"), protocol=2)
#bst.save_model('models/xgb_signal_test.model')

y_test_pred = bst.predict(xgb_test)
y_train_pred = bst.predict(xgb_train)

test_loss = sk.metrics.mean_absolute_error(y_test, y_test_pred)
train_loss = sk.metrics.mean_absolute_error(y_train, y_train_pred)

testPredTrue = y_test_pred[y_test==1]
testPredFalse = y_test_pred[y_test==0]

trainPredTrue = y_train_pred[y_train==1]
trainPredFalse = y_train_pred[y_train==0]

plt.figure()
plt.hist(testPredTrue, 30, log=False, alpha=0.5, label='WZ')
plt.hist(testPredFalse[:len(testPredTrue)], 30, log=False, alpha=0.5, label='tZ')
plt.title("BDT Output, Test Data")
plt.xlabel('BDT Score')
plt.ylabel('NEvents')
plt.legend(loc='upper right')
plt.savefig('plots/test_score.png')

plt.figure()
plt.hist(trainPredTrue, 30, log=False, alpha=0.5, label='WZ')
plt.hist(trainPredFalse[:len(trainPredTrue)], 30, log=False, alpha=0.5, label='tZ')
plt.title("BDT Output, Train Data")
plt.xlabel('BDT Score')
plt.ylabel('NEvents')
plt.legend(loc='upper right')
plt.savefig('plots/train_score.png')

plt.figure()
plt.hist(testPredTrue[:len(testPredFalse)], 30, range=(-0.1,1.1), log=False, alpha=0.5, label='WZ - Test')
plt.hist(testPredFalse[:len(testPredFalse)], 30, range=(-0.1,1.1), log=False, alpha=0.5, label='tZ - Test')
plt.hist(trainPredTrue[:len(testPredFalse)], 30, range=(-0.1,1.1), log=False, histtype='step', alpha=0.5, label='WZ - Train')
plt.hist(trainPredFalse[:len(testPredFalse)], 30, range=(-0.1,1.1), log=False, histtype='step', alpha=0.5, label='tZ - Train')
plt.title("BDT Output, max depth=%i" %(maxDepth))
plt.xlabel('BDT Score')
plt.ylabel('NEvents')
plt.legend(loc='upper left')
plt.savefig('plots/xgb_score.png')

plt.figure()
fip = xgb.plot_importance(bst)
plt.title("xgboost feature important")
plt.legend(loc='lower right')
plt.savefig('plots/feature_importance.png')

plt.figure()
auc = sk.metrics.roc_auc_score(y_test, y_test_pred)
fpr, tpr, _ = sk.metrics.roc_curve(y_test, y_test_pred)
plt.plot(fpr, tpr, label='test AUC = %.3f' %(auc))

auc = sk.metrics.roc_auc_score(y_train, y_train_pred)
fpr, tpr, _ = sk.metrics.roc_curve(y_train, y_train_pred)
plt.plot(fpr, tpr, label='train AUC = %.3f' %(auc))
plt.legend(loc='lower right')
plt.title('XGBoost tZ ROC')
plt.savefig('plots/roc.png')

y_test_bin = np.where(y_test_pred > 0.5, 1, 0)
print(y_test_bin)
print('Confusion Matrix:', sklearn.metrics.confusion_matrix(y_test, y_test_bin))

