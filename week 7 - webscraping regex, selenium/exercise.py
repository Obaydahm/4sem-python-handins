#Exercise by group happy county
import re
import bs4
import requests
from selenium import webdriver



def get_copenhagen_schools():
    phone_num_reg = re.compile(r'\d{2} \d{2} \d{2} \d{2}')

    #Open google.dk
    browser = webdriver.Firefox()
    browser.get('https://google.dk')
    browser.implicitly_wait(3)

    #Fill out search input and submit
    search_field = browser.find_element_by_name('q')
    search_field.send_keys('Copenhagen Schools')
    search_field.submit()
    
    #Click Flere adresser
    browser.find_element_by_class_name("zkIadb").click()

    soup = bs4.BeautifulSoup(browser.page_source, 'html.parser')
    schools = []

    for school in soup.find_all("div", {"class": "cXedhc"}):
        name = school.find("div", {"class":"dbg0pd"}).find("div").getText()
        details = school.find("span", {"class": "rllt__details"})
        phone = phone_num_reg.search(details.getText())
        ratings = details.find("span", {"class": "BTtC6e"})
        schools.append({
            "name": name,
            "phone": phone.group() if phone != None else "No phonenumber",
            "ratings": ratings.getText() if ratings != None else 0
        })

    print(schools)


get_copenhagen_schools()