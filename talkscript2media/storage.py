#storage

import os

def Storage(route_images,route_text,route_audio,route_video):

    
    #image storage path ,text storage path,video output path  
    
    if not os.path.exists(route_images) or not os.path.exists(route_text) or not os.path.exists(route_video):
        print('the routes do not exist')
    
    else: 
     #if they extend, a route is created to store the audio
       if not os.path.exists(route_audio): os.makedirs(route_audio)
            
    return 0
            




def Existence(file):
    
    #Verifying the existence of each file (images and text) specified and extracts information from file paths
    f = open(file,'r')
    file = f.readlines()
    
    language = file[0].split(' \n')[0]

    
    
    #stores names of img
    img = [] 
    text = []
    
    file_1 = file[1:file.index('\n')] #list image and text information
    file_2 = file[file.index('\n')+1:]

    
    #get image name and text name
    
    img = [i.split('>')[0] for i in file_1]
    text = [i.split('>')[1].split('\n')[0] for i in file_1]
    
    #get routes specified in the file
    
    routes = [i.split('=')[1].split('\n')[0] for i in file_2]  
    
    return img,text,language,routes
    


        
        
        
        



