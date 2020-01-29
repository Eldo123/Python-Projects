from selenium import webdriver

chrome = webdriver.Chrome(executable_path="/Users/eldo/Desktop/ChromeDriver/chromedriver")
chrome.get("http://quotes.toscrape.com")