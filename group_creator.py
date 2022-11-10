#!/usr/bin/python3
import time
from selenium.webdriver.common.by import By
from easySelenium import easySelenium

chrome = easySelenium()
def getusername(filetext="usernames.txt"):
    listuser=[]
    try:
        f =open(filetext,"r")
        usernamestr=f.read()
        f.close()
    except:
        usernamestr=''
    name =""
    for e in range(0, len(usernamestr)):
        i = usernamestr[e]
        if (not(i == "\n")):
            name += i
        else:  
            listuser.append(name)
            name = ""
    return listuser

def collect_users(url ="https://web.telegram.org/k/#@paxful_uk_community",filetext="usernames.txt"):
    print("collect_users started")
    pos = 1
    stop = False
    while stop == False:
        try:
            chrome.open(url)
            diffgrp = 2
            chrome.waitUntillExist(xpath='//*[@id="column-center"]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div/span')
            if chrome.isExist('//*[@id="column-center"]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div/span/span[1]'):
                totalmembers = chrome.browser.find_element(By.XPATH,('//*[@id="column-center"]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div/span/span[1]')).text
                diffgrp = 3
            else:
                totalmembers = chrome.browser.find_element(By.XPATH,'//*[@id="column-center"]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div/span').text
                diffgrp = 2
            chrome.waitUntillExist('//*[@id="column-center"]/div/div/div[2]')
            chrome.browser.find_element(By.XPATH,'//*[@id="column-center"]/div/div/div[2]').click()
            totalmembers = totalmembers[:-8]
            name =""
            for e in range(0, len(totalmembers)):
                i = totalmembers[e]
                if (not(i == " ")):
                    name += i
            totalmembers = name
            print(totalmembers )
            loop = True
            while loop:
                chrome.waitUntillExist(xpath='//*[@id="column-right"]/div/div/div[2]/div/div/div['+str(diffgrp)+']/div[2]/div[1]/div/ul/a['+str(pos)+']')
                chrome.browser.find_element(By.XPATH,'//*[@id="column-right"]/div/div/div[2]/div/div/div['+str(diffgrp)+']/div[2]/div[1]/div/ul/a['+str(pos)+']').click()
                chrome.waitUntillExist('//*[@id="column-right"]')
                try:
                    username = chrome.browser.find_element(By.XPATH,'//*[@id="column-right"]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[3]')
                    uname = str(username.text)
                except:
                    try:
                        username = chrome.browser.find_element(By.XPATH,'//*[@id="column-right"]/div/div/div[2]/div/div/div[1]/div/div/div[4]/div[3]')
                        uname = str(username.text)
                    except:
                        uname =""
                print(uname)
                f =open(filetext,"a")
                if not(uname ==""):
                    f.write(str(uname)+"\n")
                f.close()                
                chrome.browser.find_element(By.XPATH,'//*[@id="column-center"]/div/div[2]/div[2]/div[1]/button').click()
                pos = pos + 1
                print("pos= "+str(pos))
                if (pos >int(totalmembers)):
                    loop = False
                    stop = True
                    print("grp extraction is done,total is:"+str(pos))
        except:
            print("crush at:"+str(pos))
    print("collect_users ended")

def addUserToGrp(url = "https://web.telegram.org/k/#+HC4K17GVhKI0YmJk",filetext="usernames.txt",pos=0):
    print("addUserToGrp started")
    main = True
    maincount=pos
    while main:
        #try:
            listuser = getusername(filetext)
            if (maincount == len(listuser)):
                    main = False
                    break
            chrome.open(url)
            chrome.waitUntillExist('//*[@id="column-center"]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div/span')
            chrome.waitUntillExist('//*[@id="column-center"]/div/div/div[2]')   
            chrome.browser.find_element(By.XPATH,'//*[@id="column-center"]/div/div/div[2]').click()
            while True:
                if (maincount == len(listuser)):
                    main = False
                    break
                chrome.waitUntillExist('//*[@id="column-right"]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div')   
                chrome.browser.find_element(By.XPATH,'//*[@id="column-right"]/div/div/div[2]/button').click()
                chrome.waitUntillExist('//*[@id="column-right"]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div/input')   
                search = chrome.browser.find_element(By.XPATH,'//*[@id="column-right"]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div/input')
                search.send_keys(listuser[maincount])
                l1=0
                go=True
                time.sleep(10)
                while (not(chrome.isExist('//*[@id="column-right"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/ul/a[1]'))):
                    print("stack here sleep 4")
                    l1=l1+1
                    if (l1==(40)):
                        go=False
                        time.sleep(0.5)
                        chrome.browser.find_element(By.XPATH,'//*[@id="column-right"]/div/div[2]/div[1]/button').click()
                        break
                    time.sleep(0.5)
                time.sleep(1)    
                if go == True:
                    chrome.browser.find_element(By.XPATH,'//*[@id="column-right"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/ul/a[1]').click()
                    chrome.waitUntillExist('//*[@id="column-right"]/div/div[2]/div[2]/button')
                    chrome.browser.find_element(By.XPATH,'//*[@id="column-right"]/div/div[2]/div[2]/button').click()
                    chrome.waitUntillExist('/html/body/div[5]/div/div[2]/button[1]')   
                    chrome.browser.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/button[1]').click()
                maincount += 1
                print(maincount)
                
        #except:
            #print("crush at:"+str(maincount))
    print("addUserToGrp ended")
    

#####choose action
#addUserToGrp()  
collect_users("https://web.telegram.org/k/#@axzczxac8888","new1.txt")
#collect_users("https://web.telegram.org/k/#@sky_sports_group","new1.txt")
#collect_users("https://web.telegram.org/k/#@world_cup_2022_group","new1.txt")
#addUserToGrp(filetext="new1.txt") 