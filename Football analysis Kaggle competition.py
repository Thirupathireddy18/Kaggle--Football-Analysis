#!/usr/bin/env python
# coding: utf-8

# In[43]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[38]:


matches = pd.read_csv("E:\\Datasets\\DataSet\\Football 1872-2019.csv")


# In[39]:


matches.head()


# In[77]:


matches.shape


# In[40]:


matches.isnull().sum()


# In[192]:


matches.describe()


# In[41]:


matches = matches.astype({'date':'datetime64[ns]'})


# In[82]:


tournament = matches['tournament'].value_counts()
tournament = tournament[:5]
plt.figure(figsize = (10,5))
barplot = sns.barplot(y=tournament.index, x=tournament.values)
barplot.set_ylabel('Tournament', size=16)
barplot.set_xlabel('Number of tournaments', size=16)
barplot.set_title("TOP 5 Types of MATCH TOURNAMENTS")


# In[255]:


tournament1 = matches['city'].value_counts()
tournament1 = tournament1[:5]

plt.figure(figsize = (10,5))
barplot = sns.barplot(y=tournament1.index, x=tournament1.values,color='pink')
barplot.set_ylabel('Cities', size=16)
barplot.set_xlabel('Number of Cities', size=16)
barplot.set_title("TOP 5 ""Match hosting cities""")


# In[123]:


tournament1 = matches['country'].value_counts()
tournament1 = tournament1[:5]

plt.figure(figsize = (10,5))
barplot = sns.swarmplot(y=tournament1.index, x=tournament1.values)
barplot.set_ylabel('Countries', size=16)
barplot.set_xlabel('Number of Countries', size=16)
barplot.set_title("TOP 5 ""Match hosting Countries""")


# In[109]:


plt.plot(matches['home_score'])
plt.plot(matches['away_score'])


# In[112]:


matches['date'] = pd.to_datetime(matches['date'])
matches['year'] = matches['date'].dt.year


# In[199]:


matches['year'].plot(kind='hist',color='green')


# In[189]:


print("Total number of tournaments:{0}".format(len(matches['tournament'].unique())))
print("Total number of countries participated: {0}".format(len(matches['country'].unique())))
print("Total number of cities hosted for matches: {0}".format(len(matches['city'].unique())))


# In[196]:


sns.scatterplot(x="home_score", y="away_score",hue="neutral",data=matches)
plt.show()


# In[218]:


print(len(matches.loc[matches['tournament'] == 'FIFA World Cup']))


# In[248]:


wins = matches.home_score>matches.away_score
lost = matches.home_score<matches.away_score
draw = matches.home_score==matches.away_score


# In[251]:


print("Total match wins = {0}".format(len(matches[wins])))
print("Total match lost = {0}".format(len(matches[lost])))
print("Total match drawn = {0}".format(len(matches[draw])))

