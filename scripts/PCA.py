#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns



# In[2]:


import warnings
warnings.filterwarnings("ignore")


# In[3]:


#Read Data 
table = pd.read_csv(snakemake.input[0])
table.head()

table.columns


# In[4]:


def standardise(i):
    return i/table['Pl']

tablelist = ['W', 'D', 'L', 'F', 'A']

for column in tablelist:
    table[column] = standardise(table[column])


table.head()


# In[5]:


table = table.drop({'Unnamed: 0', 'Pts', 'Position', 'Win_Perc', 'Pl'}, axis=1)
table.head()


# In[6]:


features = ['W', 'D', 'L', 'F', 'A']


# Separating out the features
x = table.loc[:, features].values



# Standardizing the features
x = StandardScaler().fit_transform(x)



# In[7]:


pca = PCA(n_components=2)

principalComponents = pca.fit_transform(x)

principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])


# In[8]:


finalDf = pd.concat([principalDf, table[['Team', 'League_name']]], axis = 1)





# In[13]:


# Create a scatter plot
fig, ax = plt.subplots(figsize=(15, 15))
ax = sns.scatterplot(data=finalDf, x='principal component 1', y='principal component 2', hue='League_name', s = 100)

# Add data labels
for i in range(len(finalDf)):
    plt.text(finalDf['principal component 1'][i], finalDf['principal component 2'][i], finalDf['Team'][i],
             ha='right', fontsize=12)  # Adjust fontsize as needed

ax.set_xlabel('PCA 1', fontsize = 20)
ax.set_ylabel('PCA 2', fontsize = 20)
plt.xticks(fontsize=11)
plt.yticks(fontsize = 11)
plt.legend(fontsize = 15)
plt.savefig(snakemake.output[0])

plt.show()


# In[11]:


print(pca.explained_variance_ratio_) #Principal component 1 explains 69% of the variance, and Principal component 2 explains 21% of the variance , together explaining 90% of the variance




# In[ ]:




