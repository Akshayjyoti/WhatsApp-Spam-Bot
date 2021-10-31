#program by Akshayjyoti Bordoloi
#version 2.01
#testing date: September 7, 2021

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

#Chrome opens
#Scan the QR code

print("\n\nPlease MAXIMIZE the WhatsApp window before proceeding...")
print("\n\nPlease ignore all warnings and enter name of user or group...\n\n")

name = input('Enter the name of user or group: Lambdadelta 2.0')
msg = input('Enter your message:NipahNipahNipahNipahNipahNipahNipahNipahNipahNipahNipahNipahNipahNipahNipahNipahNipahNipahNipahNipahNipahNipahNipahNipahNipahNipahNipahNipah ')
count = int(input('Enter the count:69420 '))
gap = float(input('Interval (in seconds) between messages:1 '))
bot_prompt = input('Do you want to add bot prompt to your message? (Y/N) N').upper()

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

time.sleep(30)              #update: gives time for messages to be sent before closing the window
driver.close()
