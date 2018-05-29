
# coding: utf-8

# In[1]:


from sqlalchemy import create_engine
import pandas as pandas
import io
engine = create_engine('postgres://hassans:8z4Lj7FMxAHwFbQH@svv-rs-prod-bi.cjddijbnvfpr.eu-west-1.redshift.amazonaws.com:5439/svv')


# In[2]:


data_frame = pandas.read_sql_query('''select registered_user_id as svv, case when avg_per_active_day >= 0 and avg_per_active_day < 0.45 then 'light'
  when avg_per_active_day >= 0.45 and avg_per_active_day < 0.89 then 'medium'
  when avg_per_active_day >= 0.89 and avg_per_active_day < 1.43 then 'heavy'
  when avg_per_active_day >= 1.43 and avg_per_active_day < 2.57 then 'super_heavy'
  when avg_per_active_day >= 2.57  then 'super_heavy_plus' end as ufreq
from(
select registered_user_id, sum(consum_hours/dau) as avg_per_active_day
from(
select registered_user_id,sum(stream_playing_time_combined)/3600 as consum_hours, count(distinct date_id) as dau
  from core.vw_viewing_combined v
--inner join core.date_dimension d ON v.date_id = d.date_id
where date_id >= CAST(TO_CHAR(dateadd(DAY,-90,getdate()),'YYYYMMDD') as int)
group by  registered_user_id)
group by registered_user_id)''', engine)


# In[12]:


data_frame.head()


# In[4]:


data_frame.to_csv('C:\\Users\HassSarw\\Documents\Analysis\\adops_segments\\full_file.csv',index=False)


# In[5]:


import urllib
import requests
import json
from requests import Request, Session
import os


# In[6]:


headers = {'content-type': 'text/plain'}
access_key = 'n0qYYGM7FkZYFvr6qVgx'
file_name = 'full_file.csv'
file_path = 'C:\\Users\\HassSarw\\Documents\\Analysis\\adops_segments\\full_file.csv'
url = "https://itv.aimatch.com/ads/userRegistrationUrl.json?api_key="+access_key+"&name="+file_name


# In[8]:


r = requests.get(url,headers = headers)
r


# In[9]:


url2 = json.loads(r.text)['url']
url2


# In[10]:


with open('C:\\Users\\HassSarw\\Documents\\\Analysis\\\adops_segments\\full_file.csv','rb') as csv_file:
    r_post = requests.put(url2,data=csv_file,headers = headers)


# In[11]:


r_post.headers

