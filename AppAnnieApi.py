
# coding: utf-8

# In[127]:


import datetime
from datetime import timedelta
import requests
import json
import pandas as pd
import numpy as np


# In[37]:


StartDate = (datetime.datetime.today() - timedelta(days=2)).strftime('%Y-%m-%d')
EndDate = (datetime.datetime.today() - timedelta(days=2)).strftime('%Y-%m-%d')
url ="https://api.appannie.com/v1.2/accounts/409517/sales?break_down=product+date&start_date="+StartDate+"&end_date="+EndDate+"&product_id=994494368currency=GBP&regions=WW&page_index=0"
token = 'c4ca0cded229be6a165dcc52ac9f038a27d30a7f'
headers = { 'Authorization': 'Bearer ' + token}


# In[46]:


r = requests.get(url,headers = headers)


# In[ ]:


data = r.json()


# In[124]:


data4 = []
for c in data['sales_list']:
    Downloads = c['units']['product']['downloads']
    Product_id = c['product_id']
    Date = c['date']
    data4.append({'Date': Date,'Product_ID':Product_id, 'Downloads': Downloads})
df4 =pd.DataFrame(data4)


# In[125]:


df4


# In[128]:


conditions =[
(df4['Product_ID'] == '1050630221'),
(df4['Product_ID'] == '1178004933'),
(df4['Product_ID'] == '1193660829'),
(df4['Product_ID'] == '1194069590'),
(df4['Product_ID'] == '1316995225'),
(df4['Product_ID'] == '446079916'),
(df4['Product_ID'] == '489808876'),
(df4['Product_ID'] == '907113454'),
(df4['Product_ID'] == '994494368'),]
choices = ['Im A Celebrity','The Voice UK','ITV Racing','5 Gold Rings UK','Survival Of The Fittest','ITV Hub','Dancing on Ice','ITV News','Love Island']
df4['Title'] = np.select(conditions,choices,default='none')
df4.head()


# In[130]:


import gspread_dataframe as gd
import gspread
import google.cloud as gc
from oauth2client.service_account import ServiceAccountCredentials


# In[131]:


scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\HassSarw\\gcs_service_account_file\\itv-ds-dev-6cd968b7542d.json', scope)
gc = gspread.authorize(credentials)


# In[141]:


ws2 = gc.open("LoveIsland Facebook Video Views").worksheet('Sheet4')
existing2 = gd.get_as_dataframe(ws2)
updated2 = existing2.append(df4)
updated2 = updated2.drop_duplicates(['Date','Title'],keep='last')
cell_list2 = ws2.range('A2:D500')
for cell in cell_list2:
    cell.value = ''
ws2.update_cells(cell_list2)
gd.set_with_dataframe(ws2, updated2)

