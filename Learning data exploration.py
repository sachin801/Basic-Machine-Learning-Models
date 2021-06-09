#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns


# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


df_train=pd.read_csv('train_house_Kaggle.csv')


# In[9]:


df_train.columns


# In[11]:


df_train['SalePrice'].describe()


# In[12]:


sns.distplot(df_train['SalePrice'])


# In[14]:


print("Skewness is:" ,df_train['SalePrice'].skew())


# In[15]:


print("Kurtosis is:",df_train['SalePrice'].kurt() )


# In[20]:


#scatter plot grlivearea/SalePrice
data=pd.concat([df_train['SalePrice'],df_train['GrLivArea']],axis=1)
data.plot.scatter(x='GrLivArea',y='SalePrice',ylim=(0.800000))


# In[22]:


data2=pd.concat([df_train['SalePrice'],df_train['TotalBsmtSF']],axis=1)
data2.plot.scatter(x='TotalBsmtSF',y='SalePrice',ylim=(0,900000))


# In[23]:


data3=pd.concat([df_train['OverallQual'],df_train['SalePrice']],axis=1)
f,ax=plt.subplots(figsize=(8,6))
fig=sns.boxplot(x='OverallQual', y='SalePrice',data=data3)
fig.axis(ymin=0,ymax=800000)


# In[24]:


data4=pd.concat([df_train['SalePrice'],df_train['YearBuilt']],axis=1)
f,ax=plt.subplots(figsize=(16,8))
fig=sns.boxplot(x='YearBuilt',y='SalePrice',data=data4)
fig.axis(ymin=0,ymax=800000)
plt.xticks(rotation=90)


# In[27]:


df_train.corr()


# In[29]:


corrmat=df_train.corr()
f,ax=plt.subplots(figsize=(12,9))
sns.heatmap(corrmat,vmax=.8,square=True)


# In[32]:


#saleprice correlation matrix
k=10 #number of variables for heatmap
cols=corrmat.nlargest(k,'SalePrice')['SalePrice'].index
cm=np.corrcoef(df_train[cols].values.T)
sns.set(font_scale=1.25)
hm=sns.heatmap(cm,cbar=True,annot=True,square=True,fmt='.2f',annot_kws={'size': 10}, yticklabels=cols.values,xticklabels=cols.values)
plt.show()


# In[34]:


#scatter plot
sns.set()
cols=['SalePrice','OverallQual','GrLivArea','GarageCars','TotalBsmtSF','FullBath','YearBuilt']
sns.pairplot(df_train[cols],size=2.5)
plt.show()


# In[35]:


#deleting points
df_train.sort_values(by='GrLivArea',ascending=False)[:2]


# In[42]:


df_train=df_train.drop([1298])


# In[44]:


df_train.sort_values(by='GrLivArea',ascending=False)[:2]


# In[47]:


df_train=df_train.drop(df_train[df_train['Id']==524].index)


# In[49]:


#bivariate analysis
data=pd.concat([df_train['TotalBsmtSF'],df_train['SalePrice']],axis=1)


# In[51]:


data.plot.scatter(x='TotalBsmtSF',y='SalePrice',ylim=(0,800000))


# In[54]:


#histogram and normal probability plot
sns.distplot(df_train['SalePrice'],fit=norm)
fig=plt.figure()
res=stats.probplot(df_train['SalePrice'],plot=plt)


# In[55]:


#applying log transformation
df_train['SalePrice']=np.log(df_train['SalePrice'])


# In[56]:


#transformed histogeam and normal probability plot
sns.distplot(df_train['SalePrice'],fit=norm)
fig=plt.figure()
res=stats.probplot(df_train['SalePrice'],plot=plt)


# In[58]:


sns.distplot(df_train['TotalBsmtSF'],fit=norm)
fig=plt.figure()
res=stats.probplot(df_train['TotalBsmtSF'],plot=plt)


# In[64]:


#considering area==0 as separate case
df_train['HasBsmt']=pd.Series(df_train['TotalBsmtSF']>0)


# In[133]:


df_train['GrLivArea']=np.log(df_train['GrLivArea'])


# In[ ]:





# In[62]:


df_train['HasBsmt'].head(20)


# In[65]:


df_train.loc[df_train['HasBsmt']==True,'TotalBsmtSF']=np.log(df_train['TotalBsmtSF'])


# In[70]:


sns.distplot(df_train[df_train['TotalBsmtSF']>0]['TotalBsmtSF'],fit=norm)
fig=plt.figure()
res=stats.probplot(df_train[df_train['TotalBsmtSF']>0]['TotalBsmtSF'],plot=plt)


# In[79]:


data=pd.concat([df_train['GrLivArea'],df_train['SalePrice']],axis=1)
data.plot.scatter(x='GrLivArea',y='SalePrice',ylim=(10,14))


# In[134]:


#scatter plot
plt.scatter(df_train['GrLivArea'],df_train['SalePrice'])


# In[135]:


df_train =pd.get_dummies(df_train)


# In[136]:


df_train.head()


# In[82]:


from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
features=['GrLivArea','TotalBsmtSF','GarageArea','FullBath','YearBuilt','OverallQual'] 


# In[137]:


train_x=df_train[features]
val_x=df_train['SalePrice']


# In[138]:


forest_model=RandomForestRegressor(random_state=1)
forest_model.fit(train_x,val_x)


# In[90]:


df_test=pd.read_csv('test_house_Kaggle.csv')
df_test.head()


# In[92]:


test_y=df_test[features]


# In[98]:


total=df_test.isnull().sum().sort_values(ascending=False)
percent=(df_test.isnull().sum()/df_test.isnull().count()).sort_values(ascending=False)
missing_data=pd.concat([total,percent],axis=1, keys=['Total','Percent'])
missing_data.head(40)


# In[99]:


garage_null=df_test[df_test['GarageArea'].isnull()]


# In[102]:


gar=['GarageArea','GarageCars','GarageYrBlt']
garage_null[gar]


# In[104]:


df_test.loc[1116]['GarageArea']=0


# In[108]:


gar_c=df_test[df_test['GarageArea'].isnull()]


# In[114]:


df_test['GarageArea'].fillna(0,inplace=True)


# In[115]:


df_test[df_test['GarageArea'].isnull()].count()


# In[117]:


#handling nan value of TotalBsmtSF
bsmt_null=df_test[df_test['TotalBsmtSF'].isnull()]
che=['BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF']
bsmt_null[che]


# In[118]:


df_test['TotalBsmtSF'].fillna(0,inplace=True)


# In[119]:


df_test.iloc[660]['TotalBsmtSF']


# In[139]:


df_test['GrLivArea']=np.log(df_test['GrLivArea'])


# In[140]:


df_test.loc[df_test['TotalBsmtSF']>0,'TotalBsmtSF']=np.log(df_test['TotalBsmtSF'])


# In[142]:


test_y=df_test[features]
test_y=pd.get_dummies(test_y)


# In[143]:


val_y=pd.Series(forest_model.predict(test_y))


# In[147]:


val_y = np.exp(val_y)


# In[148]:


final=pd.concat([df_test['Id'],val_y],axis=1,keys=['Id','SalePrice'])


# In[150]:


final.head()


# In[151]:


final.to_csv('kaggle_house1.csv',index=False)


# In[ ]:




