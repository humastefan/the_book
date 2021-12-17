# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
options = Options()
options.add_argument("start-maximized")
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# cu sleep puten pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(1)

# gasim first name si scriem valori in formular
first_name = chrome.find_element(By.XPATH, '//*[@id="first-name"]')
first_name.send_keys("Stefanita")
#sleep(1)

# vom completa la workshop last name si job title

last_name = chrome.find_element(By.XPATH, '//*[@id="last-name"]')
last_name.send_keys("HUMA")
#sleep(1)

job_title = chrome.find_element(By.XPATH, '//*[@id="job-title"]')
job_title.send_keys("gropar")
#sleep(1)

# gasim butonul de Submit si dam click pe el
submit_btn = chrome.find_element(By.LINK_TEXT, 'Submit')
submit_btn.click()
sleep(3)

# gasim titlul si verificam mesajul
thank_you_msg = chrome.find_element(By.XPATH, '//h1')
assert thank_you_msg.text == 'Thanks for submitting your form'

# veti gasi voi mesaul pt. succes

text = chrome.find_element(By.XPATH,'/html/body/div/div')
print(type(text))
print(text)


# printam in consola un mesaj de succes
print('SUCCES - TEST PASSED')