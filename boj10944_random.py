import random as r
from time import sleep
from selenium import webdriver
browser = webdriver.Chrome(executable_path=r"/Volumes/APPLE/Users/nova/git/baekjoon/chromedriver")
browser.get('https://www.acmicpc.net/')
#/html/body/div[3]/div[1]/div[1]/div/ul/li[3]/a
sleep(r.randint(1,6))
browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/ul/li[3]/a').click()
#browser.get('https://www.acmicpc.net/login?next=%2F')
sleep(r.randint(1,30))
ID = "아이디"
PW = "비밂번호"
elem_login = browser.find_element_by_name("login_user_id")
elem_login.send_keys(ID)
sleep(r.randint(1,5))
elem_login = browser.find_element_by_name("login_password")
elem_login.send_keys(PW)
sleep(r.randint(1,3))
browser.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/form/div[4]/div[2]/button').click()
sleep(r.randint(1,6))
browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/ul/li[1]/a').click()
sleep(r.randint(1,6))
browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/span[1]/a').click()
sleep(r.randint(1,6))
browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[2]/ul/li[10]/a').click()
chk=0
browser.execute_script("window.scrollTo(%d, %d)"%(400,600))

while True:
  sleep(r.randint(1,30))
  browser.find_element_by_xpath('//*[@id="solution-11602552"]/td[7]/a[2]').click()
  sleep(r.randint(1,120))
  if chk==1:
    browser.execute_script("window.scrollTo(%d, %d)"%(600,400))
    chk=0
  else:chk=1
  browser.find_element_by_xpath('//*[@id="submit_button"]').click()
  sleep(72)
