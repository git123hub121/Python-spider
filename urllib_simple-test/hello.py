from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://baidu.com')
print(browser.current_url)
#测试成功！