#!/usr/bin/env python
# coding: utf-8

# # Scraping BBC website
# We are going to write a scraper
# 
# # Class_v-->17_Automatic scraper

# In[20]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[21]:


#pulling in the bbc webpage:-

response = requests.get("https://www.bbc.com/")

doc = BeautifulSoup(response.text)


# In[22]:


# now we want to scrape all the headlines on the page.
# Checking the web structure of the page

# Headline here is in h3 with a class of "media__title"


# In[23]:


# Just as a test we try to find everything with the class of "media__title"

# So we are grabbing all of the titles:-

doc.select(".media__title")


# In[24]:


titles = doc.select(".media__title")
titles


# In[25]:


# Now we want to go through each one of those titles and pull out the link.
#(We can do this by list comprehension too)

# But here we will do do it through for loop:-


# In[26]:


for title in titles:
    print(title.text)


# In[27]:


# We do not like the look of the text that we got and would like to get rid of the text space,new lines etc that are present
    #...between these headlines.So we will use the strip function for that:-
    
for title in titles:
    print(title.text.strip())
    


# In[ ]:


# Now we want to get the url for each one of these.Here the "h3" does not have the "href" under it.We have to go into the "a"..
    # tag under h3 and then pull out the link under "href" from there.


# In[28]:


# So now we can change our above code saying get the links(that are under "a" tag) that are insde of "media__title"(This we..
    #..could have earlier too but for our learning, this process is expressed in detail)
    
titles = doc.select(".media__title a")
titles


# In[29]:


# Now we can also pull our headline links along with the text in our headlines:-

for title in titles:
    #title
    print(title.text.strip())
    #links
    print(title['href'])
    
# So we see that our code works here


# In[ ]:


# Now, we would also like to get the media tag(e.g. EUROPE, US,FOOTBALL,WORLD etc) which is present under most of the headlines.
    # Note: - Notice that the media tags are written in capital letters.
    
# The media tag is under the class of "media__tag"    

# Note:--This was left here, to be tried on ourselves later.
############################################################


# In[ ]:


# Now what we want to do is --- all the time when we scrape,we want to turn our headlines that we gathered into...
    #....a csv,into a dataframe.Because working with for loops every time is a pain and want to use pandas.
    
    #In order to turn this into pandas,we will create a list of dictionaries with the heading under title and its url..
        #...under link
    
    # We do this below:-
    # 1.First we create an empty dictionary called "row"
    # 2.then we say our row['title'] is the title code for heading and row['url'] is the url code that we wrote above...
        #...in for loop.
    #3.Because what we want is a list of dictionaries, we create a dictionar at the very top called rows


# In[31]:


# Start with an empty list:-
rows = []

for title in titles:
    #Go through each title, building a dictionary with a 'title' and a 'url'
    row = {}
    #title
    row['title'] = title.text.strip()
    #links
    row['url'] = title['href']
    
    # Then add it to our list of rows:-
    rows.append(row)
    
    #append means to add--it works like the plus symbol we had in our for loop at the top

# then we are going to make a dataframe from it!     
rows

# We turn this into a dataframe:-

df = pd.DataFrame(rows)
df.head()


# In[32]:


#Now we have a dataframe.
# We now save this as csv in our working directory:
df.to_csv("bbc.csv",index = False)


# In[ ]:


# Now we want to scrape the bbc website every few minutes to keep track of what they are doing

# We now create a folder called automatic-scraper in our working directory.
# Now we want to run our code every hour to check the changes.This we want to be done automatically

# The way running thing autromatocally works is by using python files.(ie. py files in VS code) 

# So we are now going to do is ---> export a python file from our Jupyter notebook

# Go to file --> Download as--> Python(.py) file


# Now we are going to take our downloaded file --> scraper.py and we are going to put it in our automatic-scraper ...
    #.. folder.
    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




