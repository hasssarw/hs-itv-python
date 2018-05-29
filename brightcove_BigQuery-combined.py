
# coding: utf-8

# In[1]:


import http.client
import json
import httplib2, urllib, base64, json, sys
import requests
import pandas as pd
import numpy as np
import time


# In[2]:


def getAuthToken():
    credsFile=open('C:\\Users\\HassSarw\\brightcove\\brightcove_oauth.txt')
    creds = json.load(credsFile)
    conn = httplib2.HTTPSConnectionWithTimeout("oauth.brightcove.com")
    url =  "/v4/access_token"
    params = {
    "grant_type": "client_credentials"
    }
    client = creds["client_id"];
    client_secret = creds["client_secret"];
    b = bytes(('%s:%s' % (client, client_secret)).replace('\n', ''), 'utf-8')
    authString = base64.b64encode(b)
    requestUrl = url + "?" + urllib.parse.urlencode(params)
    headersMap = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": "Basic " + authString.decode('utf-8')
        };
    conn.request("POST", requestUrl, headers=headersMap)
    response = conn.getresponse()
    return json.loads(response.read())['access_token']


# In[3]:


token = getAuthToken()
while True:
    headers = { 'Authorization': 'Bearer ' + token, "Content-Type": "application/json" }
    url = "https://analytics.api.brightcove.com/v1/data?accounts=3227927989001,2635130839001,2656425235001,3887645597001,2821697655001,1686375418001,3986618146001,2660431238001,1614493085001,1898278999&dimensions=account,video&fields=video_view,video_seconds_viewed,video_name&limit=all&sort=-video_view&from=-7d&to=now"
    r = requests.get(url, headers=headers)
    print(r.status_code)
    if (r.status_code== 200):break
    elif (r.status_code== 503):
        time.sleep(240)
        token = getAuthToken()
        headers = { 'Authorization': 'Bearer ' + token, "Content-Type": "application/json" }
        url = "https://analytics.api.brightcove.com/v1/data?accounts=3227927989001,2635130839001,2656425235001,3887645597001,2821697655001,1686375418001,3986618146001,2660431238001,1614493085001,1898278999&dimensions=account,video&fields=video_view,video_seconds_viewed,video_name&limit=all&sort=-video_view&from=-7d&to=now"
        r = requests.get(url, headers=headers)
        print(r.status_code)
        if (r.status_code== 200):break
    else:
        token = getAuthToken()
        headers = { 'Authorization': 'Bearer ' + token, "Content-Type": "application/json" }
        url = "https://analytics.api.brightcove.com/v1/data?accounts=3227927989001,2635130839001,2656425235001,3887645597001,2821697655001,1686375418001,3986618146001,2660431238001,1614493085001,1898278999&dimensions=account,video&fields=video_view,video_seconds_viewed,video_name&limit=all&sort=-video_view&from=-7d&to=now"
        r = requests.get(url, headers=headers)
        print(r.status_code)
        if (r.status_code== 200):break


# In[5]:


while True:
    headers = { 'Authorization': 'Bearer ' + token, "Content-Type": "application/json" }
    url = "https://analytics.api.brightcove.com/v1/data?accounts=3227927989001,2635130839001,2656425235001,3887645597001,2821697655001,1686375418001,3986618146001,2660431238001,1614493085001,1898278999&dimensions=date&fields=video_view,video_seconds_viewed,daily_unique_viewers,video_impression,video_engagement_75&limit=all&sort=-video_view&from=-60d&to=-1d"
    r2 = requests.get(url, headers=headers)
    print(r2.status_code)
    if (r2.status_code== 200):break
    else:
        token = getAuthToken()
        headers = { 'Authorization': 'Bearer ' + token, "Content-Type": "application/json" }
        url = "https://analytics.api.brightcove.com/v1/data?accounts=3227927989001,2635130839001,2656425235001,3887645597001,2821697655001,1686375418001,3986618146001,2660431238001,1614493085001,1898278999&dimensions=date&fields=video_view,video_seconds_viewed,daily_unique_viewers,video_impression,video_engagement_75&limit=all&sort=-video_view&from=-60d&to=-1d"
        r2 = requests.get(url, headers=headers)
        print(r2.status_code)
        if (r2.status_code== 200):break


# In[13]:


token = getAuthToken()
while True:
    headers = { 'Authorization': 'Bearer ' + token, "Content-Type": "application/json" }
    url = "https://analytics.api.brightcove.com/v1/data?accounts=3227927989001,2635130839001,2656425235001,3887645597001,2821697655001,1686375418001,3986618146001,2660431238001,1614493085001,1898278999&dimensions=account,video&fields=video_view,video_seconds_viewed,video_name&limit=all&sort=-video_view&from=-1d&to=-1d"
    r3 = requests.get(url, headers=headers)
    print(r3.status_code)
    if (r3.status_code== 200):break
    elif (r3.status_code== 503):
        time.sleep(240)
        token = getAuthToken()
        headers = { 'Authorization': 'Bearer ' + token, "Content-Type": "application/json" }
        url = "https://analytics.api.brightcove.com/v1/data?accounts=3227927989001,2635130839001,2656425235001,3887645597001,2821697655001,1686375418001,3986618146001,2660431238001,1614493085001,1898278999&dimensions=account,video&fields=video_view,video_seconds_viewed,video_name&limit=all&sort=-video_view&from=-1d&to=-1d"
        r = requests.get(url, headers=headers)
        print(r.status_code)
        if (r3.status_code== 200):break
    else:
        token = getAuthToken()
        headers = { 'Authorization': 'Bearer ' + token, "Content-Type": "application/json" }
        url = "https://analytics.api.brightcove.com/v1/data?accounts=3227927989001,2635130839001,2656425235001,3887645597001,2821697655001,1686375418001,3986618146001,2660431238001,1614493085001,1898278999&dimensions=account,video&fields=video_view,video_seconds_viewed,video_name&limit=all&sort=-video_view&from=-1d&to=-1d"
        r3 = requests.get(url, headers=headers)
        print(r3.status_code)
        if (r3.status_code== 200):break


# In[20]:


data = r.json()
data2 = r2.json()
data3 = r3.json()
df2 = pd.DataFrame(data2['items'])


# In[7]:


df = pd.DataFrame(data['items'])
conditions =[
(df['account'] == '3227927989001'),
(df['account'] == '2635130839001'),
(df['account'] == '2656425235001'),
(df['account'] == '3887645597001'),
(df['account'] == '2821697655001'),
(df['account'] == '1686375418001'),
(df['account'] == '3986618146001'),
(df['account'] == '2660431238001'),
(df['account'] == '1614493085001'),
(df['account'] == '1898278999'),
(df['account'] == '1582188683001')]
choices = ['Freemantle','Daytime','Entertainment','Marketing','News','PeoplesProject','Press','Soaps','GlobalEnt','SignedStories','Sport']
df['account_name'] = np.select(conditions,choices,default='none')
df.head()


# In[16]:


df3 = pd.DataFrame(data3['items'])
conditions =[
(df3['account'] == '3227927989001'),
(df3['account'] == '2635130839001'),
(df3['account'] == '2656425235001'),
(df3['account'] == '3887645597001'),
(df3['account'] == '2821697655001'),
(df3['account'] == '1686375418001'),
(df3['account'] == '3986618146001'),
(df3['account'] == '2660431238001'),
(df3['account'] == '1614493085001'),
(df3['account'] == '1898278999'),
(df3['account'] == '1582188683001')]
choices = ['Freemantle','Daytime','Entertainment','Marketing','News','PeoplesProject','Press','Soaps','GlobalEnt','SignedStories','Sport']
df3['account_name'] = np.select(conditions,choices,default='none')
df3.head()


# In[8]:


import gspread_dataframe as gd
import gspread
import google.cloud as gc
from oauth2client.service_account import ServiceAccountCredentials


# In[9]:


scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\HassSarw\\gcs_service_account_file\\itv-ds-dev-6cd968b7542d.json', scope)
gc = gspread.authorize(credentials)


# In[18]:


df.to_csv('C:\\Users\\HassSarw\\brightcove\\brightcove_alltime_video.csv',index=False)
df2.to_csv('C:\\Users\\HassSarw\\brightcove\\brightcove_daily_views.csv',index=False)
df3.to_csv('C:\\Users\\HassSarw\\brightcove\\brightcove_top_videos_yesterday.csv',index=False)


# In[11]:


from google.cloud import bigquery

def load_data_from_file(dataset_id, table_id, source_file_name):
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    with open(source_file_name, 'rb') as source_file:
        # This example uses CSV, but you can use other formats.
        # See https://cloud.google.com/bigquery/loading-data
        job_config = bigquery.LoadJobConfig()
        job_config.write_disposition = 'WRITE_TRUNCATE'
        job_config.source_format = 'text/csv'
        job_config.autodetect =True
        job = bigquery_client.load_table_from_file(
            source_file, table_ref, job_config=job_config)

    job.result()  # Waits for job to complete

    print('Loaded {} rows into {}:{}.'.format(
        job.output_rows, dataset_id, table_id))

dataset_id = 'BI_Sandbox'
table_id = 'brightcove_alltime_video'
#project = 'itv-ds-dev'
source_file_name = 'C:\\Users\\HassSarw\\brightcove\\brightcove_alltime_video.csv'

load_data_from_file(dataset_id, table_id, source_file_name)


# In[12]:


def load_data_from_file(dataset_id, table_id, source_file_name):
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    with open(source_file_name, 'rb') as source_file:
        # This example uses CSV, but you can use other formats.
        # See https://cloud.google.com/bigquery/loading-data
        job_config = bigquery.LoadJobConfig()
        job_config.write_disposition = 'WRITE_TRUNCATE'
        job_config.source_format = 'text/csv'
        job_config.autodetect =True
        job = bigquery_client.load_table_from_file(
            source_file, table_ref, job_config=job_config)

    job.result()  # Waits for job to complete

    print('Loaded {} rows into {}:{}.'.format(
        job.output_rows, dataset_id, table_id))

dataset_id = 'BI_Sandbox'
table_id = 'brightcove_daily_views'
#project = 'itv-ds-dev'
source_file_name = 'C:\\Users\\HassSarw\\brightcove\\brightcove_daily_views.csv'

load_data_from_file(dataset_id, table_id, source_file_name)


# In[19]:


def load_data_from_file(dataset_id, table_id, source_file_name):
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    with open(source_file_name, 'rb') as source_file:
        # This example uses CSV, but you can use other formats.
        # See https://cloud.google.com/bigquery/loading-data
        job_config = bigquery.LoadJobConfig()
        job_config.write_disposition = 'WRITE_TRUNCATE'
        job_config.source_format = 'text/csv'
        job_config.autodetect =True
        job = bigquery_client.load_table_from_file(
            source_file, table_ref, job_config=job_config)

    job.result()  # Waits for job to complete

    print('Loaded {} rows into {}:{}.'.format(
        job.output_rows, dataset_id, table_id))

dataset_id = 'BI_Sandbox'
table_id = 'brightcove_yesterday_video'
#project = 'itv-ds-dev'
source_file_name = 'C:\\Users\\HassSarw\\brightcove\\brightcove_top_videos_yesterday.csv'

load_data_from_file(dataset_id, table_id, source_file_name)

