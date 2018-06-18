from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options

print('What\'s the message, Sir !')
msg = input() # Put your status here.
options = Options()
options.add_argument("--disable-notifications")
browser = webdriver.Chrome(chrome_options=options)
browser.maximize_window()
browser.get('https://www.facebook.com')

browser.find_element_by_id('email').send_keys('***********') # Your email id
browser.find_element_by_id('pass').send_keys('*************') # Your password
browser.find_element_by_id('loginbutton').click()

browser.find_element_by_id('u_ps_0_6_1').click()
sleep(2)
browser.find_element_by_xpath("//*[@name='xhpc_message']").click()
browser.switch_to.active_element.send_keys(msg)
browser.find_element_by_css_selector('._1mf7._4r1q._4jy0._4jy3._4jy1._51sy.selected._42ft').click()
