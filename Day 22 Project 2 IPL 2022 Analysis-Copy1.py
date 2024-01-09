#!/usr/bin/env python
# coding: utf-8

# # IPL Data Analysis Project

# In[23]:


import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt


# In[25]:


data = pd.read_csv("IPL 2022.csv")


# In[14]:


data


# In[15]:


data.head()


# #### The dataset contains all the information needed to summarize the story of IPL 2022 so far. So let’s start by looking at the number of matches won by each team in IPL 2022

# ### Number of Matches Won by each Team in IPL 2022

# In[16]:


figure  = px.bar(data, x = data['match_winner'], title  = "number of matches won in IPL 2022")
figure.show()


# #### So, currently, Gujrat is leading the tournament by winning eight matches. It is an achievement as a new team for Gujrat in IPL. Now let’s see how most of the teams win. Here we will analyze whether most of the teams win by defending (batting first) or chasing (batting second):

# ### Number of Matches Won by Defending or  Chasing

# In[17]:


#pie chart
data['won_by'] = data['won_by'].map({'Wickets':'Chasing','Runs': 'Defending'})

won_by = data['won_by'].value_counts()
label = won_by.index
counts = won_by.values

colors = ["red","lightgreen"]

fig = go.Figure(data = [go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = "Number of matches won by Chaseing Or defending")
fig.update_traces(hoverinfo = 'label+percent', textinfo = 'value', textfont_size = 30,
                marker = dict(colors = colors, line = dict(color = 'black', width = 3)))
fig.show()


# #### 37 matches are won while chasing the target and 377 matches are won while defending the target.

# #### Now let’s have a look at the bowlers with the best bowling figures in most of the matches:

# ## Best Bowler

# In[18]:


figure = px.bar(data, x = data['best_bowling'], title = "best bowler of ipl 2022")
figure.show()


# ### Yuzvendra Chahal having the best bowling figures in IPL 2022

# ### Now let’s have a look at the most player of the match awards in IPL 2022

# In[19]:


figure  = px.bar(data, x = ['player_of_the_match'], title = " Most player of the match" )
figure.show()


# In[20]:


figure  = px.bar(data, x = data['player_of_the_match'], title = " Most player of the match" )
figure.show()


# ### So Kuldeep Yadav has won the most player of the match in IPL 2022 

# #### Now let’s see the top scorers of most IPL 2022.

# In[21]:


figure = px.bar(data, x = data['top_scorer'], y = data['highscore'], title = "Top scorer of the match")
figure.show()


# ### Jos Buttler  is the top scorer of IPL 2022.

# ### Let’s analyze it deeply by including the runs scored by the top scorers:

# In[30]:


figure = px.bar(data, x = data['top_scorer'], y = data['highscore'],
                color = data['highscore'],title = "Top scorer of IPL 2022")
figure.show()


# In[ ]:





# In[ ]:




