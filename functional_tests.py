from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://josephdewitt8.pythonanywhere.com')

assert "Django" in browser.title