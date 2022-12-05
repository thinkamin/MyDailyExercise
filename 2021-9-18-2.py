from selenium import webdriver
link = 'http://www.zongheng.com'
browser = webdriver.Chrome('/home/song/新安装/chromedriver')
browser.get(link)
browser.close()
