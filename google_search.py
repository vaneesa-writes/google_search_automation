from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

#Importing some required modules
browser=webdriver.Chrome()

#creating an object of webdriver (Open's a new google web page)
browser.get("https://www.google.co.in/")

#Address of the site which is to be loaded

#Selecting the textbox where the search contents are to be palced

text_box=browser.find_element(By.CSS_SELECTOR,"body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div.SDkEP > div.a4bIc > input")

text_box.send_keys(sys.argv[1])

#sending the word to be searched

button=browser.find_element(By.CSS_SELECTOR,"body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b")

#selecting the submit button

button.click()

#Clicking the submit

#If user deserves to move to wikipedia or youtube
if(len(sys.argv)>2):

    #Finding out the next page where we are supossed to move

    page_next = ""
    if (sys.argv[2] == "yt" or sys.argv[2] == "youtube"):
        page_next = "youtube"
    if (sys.argv[2] == "wi" or sys.argv[2] == "wiki" or sys.argv[2] == "youtube"):
        page_next = "wikipedia"

    #Loading all the webpage links in the current page

    elems = browser.find_elements_by_xpath("//a[@href]")
    pages=[]

    for elem in elems:
        pages.append(elem.get_attribute("href"))

    for page in pages:
        if(page.find(page_next)!=-1):
            #Navigating to the next page
            browser.get(page)
            break
