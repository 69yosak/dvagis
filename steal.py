coding='utf-8'

arr=[]
# print(open('output.json',encoding=coding).read())
# print(arr[1])



import json
from random import randint
import time


from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

def sleepRan():
    time.sleep(1.5+randint(-5,5)/10.)
options = Options()
# options.add_argument("headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://2gis.ru/moscow/search/Поесть?m=37.610328%2C55.717649%2F11.14%2Fp%2F3.57%2Fr%2F-75.77")
# time.sleep(5)
input()
elements=driver.find_element(by=By.XPATH,value="/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div").click()
driver.set_window_size(1200, 8000)
nowRest=0
data=[]

while True:
    #  try:
    debug=1
    debug+=1
    nowRest+=1
    try:
        print(nowRest)
        driver.find_element(by=By.XPATH,value=('/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div['+str(nowRest)+']')).click()
        

        
        debug+=1
        sleepRan()
        sleepRan()
        sleepRan()
        
        # driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[4]/div[2]/div/button').click()
        
        
        # debug+=1
        # sleepRan()
        
        debug+=1
        text1=driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/div[2]').text
        
        debug+=1
        
        text2=driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]').text
        
        debug+=1
        driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div/a').click()
        
        
        debug+=1
        sleepRan()
        
        debug+=1
        text3=driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div').text
        
        debug+=1
        # data.append([text1,text2,text3])
        
        debug+=1
        open('output.json','a', encoding=coding).write('@@@@@@@@@@@@@@@@@@@\n'+text1+'\n#####\n'+text2+'\n#####\n'+text3+'\n#####\n')
        print('ok')
    except:
        print('can`t',nowRest)
        print('last debug',debug)
        if nowRest>14:
            time.sleep(5)
            # arr[1]        
            nowRest=0
            driver.find_element(by=By.XPATH,value=('/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div[2]/div[2]')).click()

        
        
    # except:
        # print('smth wrong')
    
    # print(open('output.json',encoding=coding).read().decode('unicode_escape'))
    # nowRest+=1