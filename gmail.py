from selenium import webdriver
import time

# Add incognito mode option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
browser = webdriver.Chrome(chrome_options=chrome_options)

# Open Gmail
browser.maximize_window()
browser.get('https://www.gmail.com')

# Sign In to Gmail
email = browser.find_element_by_id('identifierId')
email.send_keys("email")
next = browser.find_element_by_class_name('CwaK9')
next.click()
time.sleep(5)
password = browser.find_element_by_xpath('//input[@name="password"]')
password.send_keys("password")
sign_in = browser.find_element_by_class_name('CwaK9')
sign_in.click()

# Compose and send email
compose = driver.find_element_by_class_name('z0')
compose.click()
to = driver.find_element_by_class_name('vO')
to.send_keys('email')
subject = driver.find_element_by_class_name('aoT')
subject.send_keys('This is Subject')
content = driver.find_element_by_id(':qs')
content.send_keys('This is some content')
send = driver.find_element_by_id(':pf')
send.click()