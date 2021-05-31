from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def Init(PATH = "C:\\Program Files (x86)\\chromedriver.exe"):
    global driver
    driver = webdriver.Chrome(PATH)

def Sign_in(WaitTime = 4,Email = "{Introduce tu Gmail aqui}",Password = "{Introduce tu contraseña aqui}"):
    global driver
    global isSignIn
    time.sleep(WaitTime)
    driver.get("https://accounts.google.com/signin/v2/identifier?hl=es&passive=true&continue=https%3A%2F%2Fwww.google.es%2F&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    MailParmareter = driver.find_element_by_id("identifierId")
    MailParmareter.send_keys(Email)
    MailParmareter.send_keys(Keys.RETURN)
    time.sleep(WaitTime)
    MailParmareter = driver.find_element_by_name("password")
    MailParmareter.send_keys(Password)
    MailParmareter.send_keys(Keys.RETURN)
    isSignIn = True

def Sign_off(WaitTime = 1):
    global driver
    time.sleep(WaitTime)
    driver.get("https://accounts.google.com/SignOutOptions?hl=es&continue=https://www.google.es/")
    Sign_off_Button = driver.find_element_by_id("signout")
    Sign_off_Button.click()

def Go_ClassRoom(WaitTime = 1):
    global driver
    time.sleep(WaitTime)
    driver.get("https://classroom.google.com/h")
    Google_Apps = driver.find_element_by_class_name("gb_D")
    Google_Apps.click()
    Google_ClassRoom = driver.find_element_by_class_name("tX9u1b")
    Google_ClassRoom.click()

def Go_ClassRoom_XarxesLocals(WaitTime = 1):
    global driver
    time.sleep(WaitTime)
    driver.get("https://classroom.google.com/c/MTc3ODM5NTUwNDk1")

def Go_ClassRoom_M1I(WaitTime = 1):
    global driver
    time.sleep(WaitTime)
    driver.get("https://classroom.google.com/c/MTY3Mjk5ODYzMTkx")

def Go_ClassRoom_Fol(WaitTime = 1):
    global driver
    time.sleep(WaitTime)
    driver.get("https://classroom.google.com/c/MTQ3MjYwNjk3OTYz")



isSignIn = False

if __name__ == "__main__":
    Init()
    Sign_in()
    Go_ClassRoom()
