from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import login



def downloadItalux():
    chromeOptions = webdriver.ChromeOptions()
    pref = {"download.default_directory" : r'C:\Users\User\Desktop\CSV_Download\pliki_csv'}
    chromeOptions.add_experimental_option("prefs", pref)
    driver = webdriver.Chrome(chrome_options=chromeOptions)
    driver.get('https://www.italux.pl/pl/logowanie')

    user = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")

    user.send_keys(login.italuxUser)
    password.send_keys(login.italuxPassword)

    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/form/fieldset/div/button').click()
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/div/ul/li[6]/a').click()
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div[2]/div[8]/div[1]/a').click()
    time.sleep(10)
    driver.close()


def downloadEkoLight():
    chromeOptions = webdriver.ChromeOptions()
    pref = {"download.default_directory" : r'C:\Users\User\Desktop\CSV_Download\pliki_csv'}
    chromeOptions.add_experimental_option("prefs", pref)
    driver = webdriver.Chrome(chrome_options=chromeOptions)
    driver.get('https://b2b.eko-light.com/logowanie')

    user = driver.find_element_by_id('Uzytkownik')
    password = driver.find_element_by_id('Haslo')

    user.send_keys(login.ekolightUser)
    password.send_keys(login.ekolighPassword)

    driver.find_element_by_css_selector('#login-form > div.form-group.sekcja-przyciski.mb-0.d-flex > div.form-group.ml-auto.mt-auto.d-flex.mb-0 > button').click()
    time.sleep(5)
    driver.find_element_by_css_selector('#kontrolka-1564 > div > a').click()
    time.sleep(3)
    driver.get('https://b2b.eko-light.com/pl/xmlapi/2/2/utf8')
    time.sleep(10)
    driver.close()


def seleniumDownload():
   downloadEkoLight()
   downloadItalux()

