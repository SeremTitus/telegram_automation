#!/usr/bin/python3
import sys
import os
import  time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
if sys.platform ==('linux1' or'linux2') :
    chrome_data = "/home/serem_empire/Development/web_dev/bg/telegram_automation/data"
    driver_location ="/usr/bin/chromedriver"
    chrome_location ="/usr/bin/google-chrome"
    options.binary_location = chrome_location
elif sys.platform == 'win32':
    chrome_data = "C:\\Users\\ADMIN\\Development\\telegram_automation\\data"
    driver_location ="C:\\Users\\ADMIN\\Development\\telegram_automation\\chromedriver.exe"
options.add_argument("user-data-dir="+str(chrome_data))
browser = webdriver.Chrome(executable_path=driver_location,options=options)

def isexist(name =""):
    try:
        browser.find_element(By.XPATH,value = name)
        return True
    except:
        return False
def scroll(posx=""):    
    height = browser.execute_script("return document.body.scrollHeight;")
    lastheight = 0
    count = 0
    while True:
        print ("scrolling "+str(height)+" to " +str(lastheight))
        
        #if lastheight == height:
            #break
        if (isexist(posx)):
            break
        count = count + 1
        lastheight = height
        #browser.execute_script("window.scrollBy(0, " + str(height) + ");")
        #frame = browser.find_element(By.XPATH,'//*[@id="RightColumn"]/div[2]/div/div')
        #frame_y = frame.rect['y']
        act = ActionChains(browser)
        act.scroll_by_amount(0, height+500)
        act.perform()
        
        time.sleep(10)
        height = browser.execute_script("return document.body.scrollHeight;")
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
            browser.get(url)
            diffgrp = 2
            while (not(isexist('//*[@id="column-center"]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div/span'))):
                time.sleep(0.5)
                print("stack here sleep 1")
            time.sleep(1)
            if isexist('//*[@id="column-center"]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div/span/span[1]'):
                totalmembers = browser.find_element(By.XPATH,('//*[@id="column-center"]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div/span/span[1]')).text
                diffgrp = 3
            else:
                totalmembers = browser.find_element(By.XPATH,'//*[@id="column-center"]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div/span').text
                diffgrp = 2
            while (not(isexist('//*[@id="column-center"]/div/div/div[2]'))):
                print("stack here sleep 1.1")
                time.sleep(0.5)
            browser.find_element(By.XPATH,'//*[@id="column-center"]/div/div/div[2]').click()
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
                time.sleep(1)
                while (not(isexist(name='//*[@id="column-right"]/div/div/div[2]/div/div/div['+str(diffgrp)+']/div[2]/div[1]/div/ul/a['+str(pos)+']'))):
                    print("stack here scrolling: "+str(pos))
                    time.sleep(0.5)
                    #stop = True
                    #break
                    #scroll("//*[@id='column-right']/div/div/div[2]/div/div/div[3]/div[2]/div[1]/div/ul/a["+str(pos)+"]")
                browser.find_element(By.XPATH,'//*[@id="column-right"]/div/div/div[2]/div/div/div['+str(diffgrp)+']/div[2]/div[1]/div/ul/a['+str(pos)+']').click()
                while (not(isexist('//*[@id="column-right"]'))):
                    print("stack here sleep 3")
                    time.sleep(0.5)
                try:
                    time.sleep(1)
                    username = browser.find_element(By.XPATH,'//*[@id="column-right"]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[3]')
                    uname = str(username.text)
                except:
                    try:
                        username = browser.find_element(By.XPATH,'//*[@id="column-right"]/div/div/div[2]/div/div/div[1]/div/div/div[4]/div[3]')
                        uname = str(username.text)
                    except:
                        uname =""
                print(uname)
                f =open(filetext,"a")
                if not(uname ==""):
                    f.write(str(uname)+"\n")
                f.close()                
                browser.find_element(By.XPATH,'//*[@id="column-center"]/div/div[2]/div[2]/div[1]/button').click()
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
        try:
            listuser = getusername(filetext)
            if (maincount == len(listuser)):
                    main = False
                    break
            browser.get(url)
            time.sleep(1)
            while (not(isexist('//*[@id="column-center"]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div/span'))):
                print("stack here sleep 1")
                time.sleep(0.5)
            time.sleep(1)
            while (not(isexist('//*[@id="column-center"]/div/div/div[2]'))):
                print("stack here sleep 1.1")
                time.sleep(0.5)    
            browser.find_element(By.XPATH,'//*[@id="column-center"]/div/div/div[2]').click()
            while True:
                if (maincount == len(listuser)):
                    main = False
                    break
                while ((isexist('//*[@id="column-right"]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div'))):
                    print("stack here sleep 2")
                    try:                    
                        browser.find_element(By.XPATH,'//*[@id="column-right"]/div/div[2]/div[1]/button').click()
                    except:
                        pass
                    time.sleep(0.5)
                time.sleep(1)    
                browser.find_element(By.XPATH,'//*[@id="column-right"]/div/div/div[2]/button').click()
                while (not(isexist('//*[@id="column-right"]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div/input'))):
                    print("stack here sleep 3")
                    time.sleep(0.5)
                time.sleep(1)    
                search = browser.find_element(By.XPATH,'//*[@id="column-right"]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div/input')
                search.send_keys(listuser[maincount])
                l1=0
                go=True
                time.sleep(10)
                while (not(isexist('//*[@id="column-right"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/ul/a[1]'))):
                    print("stack here sleep 4")
                    l1=l1+1
                    if (l1==(40)):
                        go=False
                        time.sleep(0.5)
                        browser.find_element(By.XPATH,'//*[@id="column-right"]/div/div[2]/div[1]/button').click()
                        break
                    time.sleep(0.5)
                time.sleep(1)    
                if go == True:
                    browser.find_element(By.XPATH,'//*[@id="column-right"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/ul/a[1]').click()
                    while (not(isexist('//*[@id="column-right"]/div/div[2]/div[2]/button'))):
                        print("stack here sleep 5")
                        time.sleep(0.5)
                    time.sleep(1)    
                    browser.find_element(By.XPATH,'//*[@id="column-right"]/div/div[2]/div[2]/button').click()
                    while (not(isexist('/html/body/div[5]/div/div[2]/button[1]'))):
                        print("stack here sleep 5")
                        time.sleep(0.5)
                    time.sleep(1)    
                    browser.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/button[1]').click()
                    time.sleep(1) 

                maincount += 1
                print(maincount)
        except:
            print("crush at:"+str(maincount))
    print("addUserToGrp ended")
    

#####choose action
addUserToGrp()  
#collect_users("https://web.telegram.org/k/#@axzczxac8888","new1.txt")
#collect_users("https://web.telegram.org/k/#@sky_sports_group","new1.txt")
#collect_users("https://web.telegram.org/k/#@world_cup_2022_group","new1.txt")
#addUserToGrp(filetext="new1.txt") 