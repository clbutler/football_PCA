#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


import warnings
warnings.filterwarnings("ignore")


# In[3]:


file_paths = [snakemake.input[0], snakemake.input[1]]
dfs = [pd.read_csv(i) for i in file_paths]

national_league, premier_league = dfs


# In[4]:


def win_perc(i):
    i['Win_Perc'] = ((i['W']/i['Pl'])*100).round(2)

def position(i):
    i['Position'] = i.index +1





# In[5]:


win_perc(premier_league)
win_perc(national_league)
position(premier_league)
position(national_league)


# In[6]:


premier_league['League_name'] = 'Premier League'
national_league['League_name'] = 'National League'


# In[7]:


tot_table = pd.concat([premier_league, national_league])


# In[8]:


tot_table.head()
tot_table.to_csv(snakemake.output[1])


# In[9]:


tot_table.loc[tot_table['League_name'] == 'National League', 'Position'] /= 24/20




# In[11]:


tot_table = tot_table[tot_table['Team'] != "Everton *"] #removing everton as anomoly due to points deduction 


# In[16]:


fig, ax = plt.subplots(figsize = (15,18))

ax = sns.lineplot(data = tot_table, x = 'Position', y = 'Win_Perc', hue = 'League_name', linewidth = 5)
ax.set_xlabel('\nLeague Position (standardised)', fontsize = 15)
ax.set_ylabel('Win Percentage\n', fontsize = 15)
ax.axvline(x=17, color='grey', linestyle='--')
ax.axvline(x=4, color='grey', linestyle='--')
ax.axvline(x=7, color='grey', linestyle='--')
plt.xticks(fontsize=11)
plt.yticks(fontsize = 11)
plt.savefig(snakemake.output[0])
plt.legend(fontsize = 15)
plt.show()

