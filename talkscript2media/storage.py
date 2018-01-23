#storage

import os

def Storage(route_images,route_text,route_audio,route_video):

    
    #image storage path,text storage path
    
    if not os.path.exists(route_images) or not os.path.exists(route_text) or not os.path.exists(route_video):
        print('the routes do not exist')
    
    else: 
     #if they extend, a route is created to store the audio
       if not os.path.exists(route_audio): os.makedirs(route_audio)
            
    return 0
            

#verifying the existence of each file


def Existence(file,route_img,route_text):
    
    f = open(file,'r')
    h = f.readlines()
    language = h[0]
    
    img = []
    text = []
    
    for i in range(1,len(h)-1):
        img+=[h[i].split('>')[0]]
        text+=[h[i].split('>')[1].split('\n')[0]]
        
    for i in range(len(img)):
        
        if os.path.isfile(route_img+'/'+img[i]) and  os.path.isfile(route_text+'/'+text[i]):
            print ('exist')
        else:
            print('the files not  exist')
    
    return img,text,language.split('\n')[0]
    


        
        
        
        
        
        



