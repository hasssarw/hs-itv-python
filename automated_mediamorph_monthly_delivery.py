
# coding: utf-8

# In[25]:


from sqlalchemy import create_engine
import pandas as pandas
import io
engine = create_engine('postgres://[$RedShiftUsername]:[$RedShiftPassword]@svv-rs-prod-bi.cjddijbnvfpr.eu-west-1.redshift.amazonaws.com:5439/svv')


# In[ ]:


import datetime
import time
today = datetime.date.today()
first = today.replace(day=1)
lastMonth = first - datetime.timedelta(days=1)
last_month = (lastMonth.strftime("%Y%m"))
ts = time.strftime("%Y%m%d")


# In[26]:


data_frame = pandas.read_sql_query('''select c.date_actual,d.platform_label, a.production_id, b.programme_title, b.genre_id, b.episode_title, b.episode_id,sum(a.stream_requests) as stream_requests
from core.vw_viewing_combined a
LEFT JOIN core.production b ON a.production_id = b.production_id
LEFT JOIN core.date_dimension c ON a.date_id = c.date_id
LEFT join core.platform d ON a.platform_id = d.platform_id
where date_actual >= cast(date_trunc('month', current_date) - interval '1 month' as date) and date_actual<= cast(date_trunc('month', current_date) - interval '1 day' as date)
group by c.date_actual,d.platform_label, a.production_id, b.programme_title, b.genre_id, b.episode_title, b.episode_id''', engine)


# In[51]:


data_frame.to_csv('C:\\Users\\HassSarw\\automation\\'+last_month+'_mediamorph'+'_'+ts+'.csv',index=False)


# In[88]:


import ftplib
session = ftplib.FTP('ftp2.mediamorph.com','[FTPUSERNAME]','[FTPPASSWORD]')
session.cwd('//SVV')


# In[89]:


filename= 'C:\\Users\\HassSarw\\automation\\'+last_month+'_mediamorph'+'_'+ts+'.csv'


# In[90]:


file = open(filename,'rb')


# In[91]:


session.storbinary('STOR ' + filename,file)


# In[92]:


file.close()


# In[93]:


session.quit()

