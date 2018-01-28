
# coding: utf-8

# In[35]:


import speech
import brown_video
import threading
import time


# In[37]:


def testing():
    for i in range(10):
        print i
        time.sleep(1)


def first_call():
    try:
#         print 'hello'
#         brown_video.web_cam()
        t1=threading.Thread(target=speech.speech)
        t2=threading.Thread(target=brown_video.web_cam)
#         t3=threading.Thread(target=testing)
        t1.daemon=True
        t2.daemon=True
        t1.start()
        t2.start()
        
    #     t3.start()

    except:
        print'NOOOOOOOOO'

# first_call()
# video.checking()


# In[ ]:




