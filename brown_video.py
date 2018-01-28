
# coding: utf-8

# In[18]:


import numpy as np
import cv2
import httplib, urllib, base64, json
import requests

val={'sadness': 0.0, 'neutral': 0.0, 'contempt': 0.0, 'disgust': 0.0, 'anger': 0.0, 'surprise': 0.0, 'fear': 0.0, 'happiness': 0.0}



def normalized():
    total=0.0
    for key in val.keys():
        total+=val[key]
    for key in val.keys():
        val[key]/=float(total)
    print 'NORMALIZED RESULT: ',val
    


def get_emotion_dict(s):
    default={'sadness': 0.0, 'neutral': 0.0, 'contempt': 0.0, 'disgust': 0.0, 'anger': 0.0, 'surprise': 0.0, 'fear': 0.0, 'happiness': 0.0}
    emotion = s.split("emotion")[-1]

    store = ""
    bad = ["[", "{", "}", "]", "\""]
    for i in emotion:
        if i not in bad:
            store += i

    temp = ""
    for i in store:
        if i == ":":
            temp += " "
        else:
            temp += i

    emotions = temp.split(",")
    d = {}
    try:
        for i in emotions:
            i = i.rstrip(" ").lstrip(" ")
            get_score = i.split(" ")

            d[get_score[0]] = float(get_score[-1])

        return d
    except:
        return default


def get_data(frame):
    #####################################
    subscription_key='b0a6ce6da90c4eb2adb78ba8e0dc7d6c'
    # Request parameters.
    params = urllib.urlencode({
        'subscription-key': subscription_key,
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
    #     'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
        'returnFaceAttributes': 'emotion',

    })

    headers = {'Content-Type': 'application/octet-stream'}
    body=""
#     print type(body)
#     body=frame.tostring()
    cv2.imwrite("test.jpg",frame)
    image_local_file='test.jpg'
    with open(image_local_file,'rb') as f:
        body=f.read()

    


    conn = httplib.HTTPSConnection('eastus.api.cognitive.microsoft.com')


    conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
    response = conn.getresponse("")
    data = response.read()

#     print data
#     print type(data)
    f=get_emotion_dict(data)
    for key in f.keys():
        val[key]+=f[key]
#     count+=1
        
    print '_________________'

    conn.close()




def web_cam(video_file='rec_0.webm'):
    print 'inside'
    cap = cv2.VideoCapture(video_file)
    frame_no=0


      
    while(cap.isOpened()):
        
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame_no+=1
#         print ret

        if (ret==True):
#             print type(frame)
            if(frame_no%50==0):
                get_data(frame)
#                 print count
            
#             count+=1
        else:
            break
#         print ('COUNT=',count)
    cap.release()
    normalized()
    
def checking():
    print 'INSIDE CHECKING'

# web_cam()
# normalized()



# In[ ]:





# In[ ]:




