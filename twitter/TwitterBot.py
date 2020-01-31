from selenium import webdriver
import os 
from time import sleep
from serviceScripts_time import daysInMonth2020, calculateTime, dateParser

class TwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.username = os.environ.get("TWT_USER")
        self.password = os.environ.get("TWT_PASS")
        self.driver.get("https://twitter.com/")
        self.driver.implicitly_wait(2)

    def login(self):
        # logging in
        self.driver.find_element_by_xpath("//input[@name=\"session[username_or_email]\"]").send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@name=\"session[password]\"]").send_keys(self.password)
        try:
            self.driver.find_element_by_xpath('//input[@type="submit"]').click()
        except:
            self.driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/form/div/div[3]/div').click()
        self.driver.implicitly_wait(4)

    def scrapeTweets(self):
        #navigating to the tweets
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/header/div/div/div/div/div[2]/nav/a[7]").click()
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div/div/div[2]/div/div/nav/div[2]/div[2]/a").click()
        self.driver.implicitly_wait(4)

        #select all the tweets
        tweets = self.driver.find_elements_by_xpath("//div[@data-testid='tweet']")
        tweetsDate = self.driver.find_elements_by_xpath("//time")
        tweetTxt = []
        self.tweetsDict = {}
        twtDate = []

        twtDate = [ n.get_attribute("datetime") for n in tweetsDate]

     
        tweetTxt = [n.text for n in tweets]
      

        #format tweets into date:tweet dict
        for twt, twtTime in zip(tweetTxt,twtDate):
            newTwt = twt.split('\n')
            if 'Replying to ' in newTwt:
                self.tweetsDict[twtTime] = newTwt[-1]
            else:
                self.tweetsDict[twtTime] = newTwt[4]

        for key in list(self.tweetsDict.keys()):
            if not calculateTime(key):
                del self.tweetsDict[key]

        #liked tweets

        self.driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div/div/div[2]/div/div/nav/div[2]/div[4]/a").click()

        #select all the tweets
        tweets = self.driver.find_elements_by_xpath("//div[@data-testid='tweet']")
        tweetsDate = self.driver.find_elements_by_xpath("//time")
        a = self.driver.find_elements_by_xpath("//a")
        tweetTxt = []
        twtDate = []


        time = [ n.get_attribute("title") for n in a if n.get_attribute("title") != '']


        for t in tweetsDate:
            for n in time:
                if dateParser(n, t.get_attribute("datetime")):
                    twtDate.append(t.get_attribute("datetime"))

        tweetsDate = list(set(tweetsDate))


        tweetTxt = [n.text for n in tweets]



        for twt, twtTime in zip(tweetTxt,twtDate):
            newTwt = twt.split('\n')
            if 'Replying to ' in newTwt:
                self.tweetsDict[twtTime] = newTwt[-1]
            else:
                self.tweetsDict[twtTime] = newTwt[4]

        for key in list(self.tweetsDict.keys()):
            if not calculateTime(key):
                del self.tweetsDict[key]

        self.tweets = [self.tweetsDict[n] for n in self.tweetsDict.keys()]
    def scrapeMessages(self):
        #navigate to messages
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/header/div/div/div/div/div[2]/nav/a[4]").click()
        conversations = self.driver.find_elements_by_xpath("//div[@data-testid='conversation']")
        for conversion in conversations:
            conversion.click()
            self.messages = self.driver.find_elements_by_xpath("//div[@data-testid='messageEntry']")
            self.messages = [ m.text for m in self.messages]
            months= ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            self.messages = [ m.split('\n')[0] for m in self.messages if m.split('\n')[-1].split()[0] not in months]



t = TwitterBot()
t.login()
t.scrapeTweets()
t.scrapeMessages()
tweets = t.tweets
messages = t.messages


#scrape messages
