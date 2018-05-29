
# coding: utf-8

# In[216]:


import requests
import json
import pandas as pd


# In[217]:


LoveIslandAccessToken = [$ACCESSTOKEN]


# In[218]:


headers = {'Authorization': 'Bearer ' + LoveIslandAccessToken}


# In[219]:


r = requests.get("https://graph.facebook.com/v3.0/539463929527443/insights/page_video_views",headers = headers)
r2 = requests.get("https://graph.facebook.com/v3.0/539463929527443/insights/page_fans",headers=headers)


# In[220]:


data = r.json()
data2 = r2.json()


# In[221]:


data1 = []
for c in data['data']:
    title =c['title']
    period = c['period']
    for e in c['values']:
        endtime = e['end_time']
        value = e['value']
        data1.append({'Title': title,'Period':period, 'Requests': value, 'Date': endtime})
df =pd.DataFrame(data1)


# In[222]:


data3 = []
for c in data2['data']:
    title =c['title']
    period = c['period']
    for e in c['values']:
        endtime = e['end_time']
        value = e['value']
        data3.append({'Title': title,'Period':period, 'Likes': value, 'Date': endtime})
df2 =pd.DataFrame(data3)


# In[225]:


import gspread_dataframe as gd
import gspread
import google.cloud as gc
from oauth2client.service_account import ServiceAccountCredentials


# In[226]:


scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\HassSarw\\gcs_service_account_file\\itv-ds-dev-6cd968b7542d.json', scope)
gc = gspread.authorize(credentials)


# In[252]:


ws = gc.open("LoveIsland Facebook Video Views").sheet1
existing = gd.get_as_dataframe(ws)
updated = existing.append(df)
updated = updated.drop_duplicates(['Date','Period'],keep='last').sort_values(by=['Date','Period'])
cell_list = ws.range('A2:D600')
for cell in cell_list:
    cell.value = ''
ws.update_cells(cell_list)
gd.set_with_dataframe(ws, updated)


# In[251]:


ws2 = gc.open("LoveIsland Facebook Video Views").worksheet('Sheet3')
existing2 = gd.get_as_dataframe(ws2)
updated2 = existing2.append(df2)
updated2 = updated2.drop_duplicates(subset='Date')
cell_list2 = ws2.range('A2:D500')
for cell in cell_list2:
    cell.value = ''
ws2.update_cells(cell_list2)
gd.set_with_dataframe(ws2, updated2)


# In[119]:


#for d in data['data']:
#    for e in d['values']:
#        print(e['end_time'])


# In[120]:


#for d in data['data']:
#    for e in d['values']:
#        print(e['value'])


# In[121]:


#for d in data['data']:
#    print (d['title'])


# In[122]:


#for c in data['data']:
#    print (c['period'])


# In[106]:


#### sandbox ####

