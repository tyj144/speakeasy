
# coding: utf-8

# In[8]:


import speech_recognition as sr


# In[13]:


def write_to_file(name='output_text.txt',data='Nothing'):
#     data=data.encode('utf8')
    text_file = open(name, "w")
    text_file.write(data)
    text_file.close()

# def write_syn_to file(name='output_syn.txt',data='Nothing'):
    


# path = os.getcwd() + "/tt.wav"
def speech(sound_file='rec_2.wav'):
    r = sr.Recognizer()

    with sr.AudioFile(sound_file) as source:
        audio = r.record(source) 
    r = sr.Recognizer()
    with sr.AudioFile(sound_file) as source:
        audio = r.record(source)
    print(audio)

    try:
        write_to_file(data=(r.recognize_google(audio)).encode('utf8'))
#         print (r.recognize_google(audio))
        print'Speech Work Done'
#         return(r.recognize_google(audio))
        
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
#         print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
#         print(type(r.recognize_google(audio)))

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
# speech()


# In[ ]:




