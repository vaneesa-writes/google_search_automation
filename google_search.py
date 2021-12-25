from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
browser=webdriver.Chrome()
browser.get("https://www.google.co.in/")
from selenium.webdriver.common.keys import Keys
text_box=browser.find_element(By.CSS_SELECTOR,"body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div.SDkEP > div.a4bIc > input")
print(text_box.is_displayed())
text_box.send_keys(sys.argv[1])
button=browser.find_element(By.CSS_SELECTOR,"body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b")
print(button.is_displayed())
button.click()
if(len(sys.argv)>2):
    elems = browser.find_elements_by_xpath("//a[@href]")
    pages=[]
    page_next=""
    if(sys.argv[2]=="yt" or sys.argv[2]=="youtube"):
        page_next="youtube"
    if(sys.argv[2]=="wi" or sys.argv[2]=="wiki" or sys.argv[2]=="youtube"):
        page_next="wikipedia"
    for elem in elems:
        pages.append(elem.get_attribute("href"))
    for page in pages:
        if(page.find(page_next)!=-1):
            browser.get(page)
            break