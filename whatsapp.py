#program by Akshayjyoti Bordoloi
#version 2.0
#testing date: September 4, 2021

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

#Chrome opens
#Scan the QR code

print("\n\nPlease MAXIMIZE the WhatsApp window before proceeding...")
print("\n\nPlease ignore all warnings and enter name of user or group...\n\n")

name = input('Enter the name of user or group: ')
msg = input('Enter your message: ')
count = int(input('Enter the count: '))
gap = float(input('Interval (in seconds) between messages: '))
bot_prompt = input('Do you want to add bot prompt to your message? (Y/N) ').upper()

input('Enter anything after scanning QR code...')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

#Entered the chat

msg_box = driver.find_element_by_xpath('//div[@data-tab = "9"]')    #updated from last version: @data-tab = "1"   #May require further updates based on Chrome version.

for i in range(count):
    if bot_prompt == 'Y':
        msg_final = '<Status: ' + str(i+1) + '/' + str(count) + '>' + msg
    msg_box.send_keys(msg_final)
    button = driver.find_element_by_class_name('_4sWnG')            #updated from last version: _35EW6      #May require further updates based on Chrome version.
    button.click()
    if gap > 0:
        time.sleep(gap)

msg_final = 'Hacking Complete!'
msg_box.send_keys(msg_final)
button = driver.find_element_by_class_name('_4sWnG')                #updated from last version: _35EW6      #May require further updates based on Chrome version.
button.click()

driver.close()
