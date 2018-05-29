
# coding: utf-8

# In[6]:


from sqlalchemy import create_engine
import pandas as pandas
import io
engine = create_engine('postgres://[RedShiftUser]:[RedShiftPassword]@svv-rs-prod-bi.cjddijbnvfpr.eu-west-1.redshift.amazonaws.com:5439/svv')


# # Import Avg 000s View

# In[ ]:


data_frame = pandas.read_sql_query("""select * from sandbox.avg_viewer_000s""", engine)


# In[ ]:


data_frame.head()


# # Save as CSV

# In[32]:


data_frame.to_csv('C:\\Users\\HassSarw\\automation\\avg_viewer_000s.csv',index=False)


# # Send Email

# In[7]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# In[8]:


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("[GMAILEMAIL], [SMTPPASSGMAILAPPPASS])


# In[19]:


to1 = '[Recepient1]'
to2 = '[Recepient2]'
to3 = '[Recepient3]'


# In[29]:


fromaddr = "[GMAILEMAIL]
toaddr = [to1,to2,to3]


# In[28]:


for mail in toaddr:
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = mail
    msg['Subject'] = "Avg Viewer 000s Report"

    body = "Please find attached the latest avg 000s report"

    msg.attach(MIMEText(body, 'plain'))

    filename = "avg_viewer_000s.csv"
    attachment = open("C:\\Users\\HassSarw\\automation\\avg_viewer_000s.csv", "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)
    text = msg.as_string()
    server.sendmail(fromaddr, mail, text)


# In[ ]:


server.quit()

