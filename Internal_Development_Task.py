#!/usr/bin/env python
# coding: utf-8

# In[650]:


import os
import time
import shutil
import logging


def periodic_fun():
    #code here
    logging.basicConfig(filename="log.txt", level=logging.INFO,
                    format="%(asctime)s %(message)s", filemode="w")   #location of logfile you will find in the main directory


    def folderSync(SourcePath,replicaPath,synctime):
     filelist = [];
     shutil.rmtree(replicaPath,ignore_errors=True)  #cleaning the destination folder before the sync operation , please update with a proper dealy time in sec
     print("prepareing and checking on",replicaPath)
     time.sleep(synctime)
     for root, dirs, files in os.walk(SourcePath):
        for file in files:
            filelist.append(os.path.join(root,file));
            for file in filelist:   
             shutil.copytree(SourcePath, replicaPath, dirs_exist_ok=True)
             #logging.info("Synced",file,"to",replicaPath)    #unhash to log console into a file
             print("Synced",file,"to",replicaPath)
                                    
    folderSync(r" ",r" ",10)   #add source and destination folder and delaytime      
    time.sleep(60)     #add a suitable time                                                            
while True:
    periodic_fun()


# In[ ]:




