from selenium import webdriver
import os 
from time import sleep
from serviceScripts_time import daysInMonth2020, calculateTime

driver = webdriver.Chrome()
username = os.environ.get("TWT_USER")
password = os.environ.get("TWT_PASS")
driver.get("https://twitter.com/")
driver.implicitly_wait(2)

# logging in
driver.find_element_by_xpath("//input[@name=\"session[username_or_email]\"]").send_keys(username)
driver.find_element_by_xpath("//input[@name=\"session[password]\"]").send_keys(password)
try:
    driver.find_element_by_xpath('//input[@type="submit"]').click()
except:
    driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/form/div/div[3]/div').click()
driver.implicitly_wait(4)

#navigating to the tweets
driver.find_element_by_xpath("/html/body/div/div/div/div/header/div/div/div/div/div[2]/nav/a[7]").click()
driver.implicitly_wait(4)

#select all the tweets
tweets = driver.find_elements_by_xpath("//div[@data-testid='tweet']")
tweetsDate = driver.find_elements_by_xpath("//time")
tweetTxt = []
tweetsDict = {}
twtDate = []

for t in tweetsDate:
    twtDate.append(t.get_attribute("datetime"))

for tweet in tweets:
    tweetTxt.append(tweet.text)
#format tweets into date:tweet dict
for twt, twtTime in zip(tweetTxt,twtDate):
    newTwt = twt.split('\n')
    tweetsDict[twtTime] = newTwt[4]

for key in list(tweetsDict.keys()):
    if not calculateTime(key):
        del tweetsDict[key]
