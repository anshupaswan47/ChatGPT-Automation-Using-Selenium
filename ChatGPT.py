Link1 = 'https://jphgpt.vercel.app/'
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


chrome_option = Options()
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
chrome_option.add_argument(f"user-agent={user_agent}")
# chrome_option.add_argument("--headless=new")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_option)
# driver.maximize_window()
driver.get(url=Link1)
text_areaPath = '//*[@id="__next"]/div/main/div[2]/div[2]/div/div[2]/div[1]/div/textarea'
sendbuttonXpath = '//*[@id="__next"]/div/main/div[2]/div[2]/div/div[2]/div[1]/div/button[2]'
def sendtext(Text):
    try:
        sleep(1)
        driver.find_element(By.XPATH,value=text_areaPath).send_keys(Text)
        driver.find_element(By.XPATH,value=sendbuttonXpath).click()
        # print("Message send")
        sleep(4)
        
    except:
        pass
def recivetext(i):
    try:
        opxpath = f'//*[@id="__next"]/div/main/div[2]/div[2]/div/div[1]/div[{i}]/div/div[2]/div/div[1]/p'
        output = driver.find_element(By.XPATH,value=opxpath)
        text = output.text
        print("AI : ",text)
    except:
        pass
i=3
print("Automation Started !!!!!!!!!!!!")
while True:
    Text = input("\nYour Input : ")
    sendtext(Text) 
    recivetext(i)
    i+=2 
