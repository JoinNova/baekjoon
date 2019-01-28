from time import sleep
from selenium import webdriver
browser = webdriver.Chrome(executable_path=r"/Volumes/APPLE/Users/nova/git/baekjoon/chromedriver")
browser.get('https://www.acmicpc.net/login?next=%2F')
ID = "사용자아이디"
PW = "사용자비밀번호"
elem_login = browser.find_element_by_name("login_user_id")
elem_login.send_keys(ID)
elem_login = browser.find_element_by_name("login_password")
elem_login.send_keys(PW)
browser.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/form/div[4]/div[2]/button').click()
while True:
  browser.get('https://www.acmicpc.net/submit/10945/11557266') # 이전에 제출한 곳의 주소
  browser.find_element_by_xpath('//*[@id="submit_form"]/div[4]/div/button').click()
  sleep(72)
