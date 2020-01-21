from selenium import webdriver
from time import sleep
import json

class WordsBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        words = ["fear", "anger", "sadness", "joy", "disgust", "surprise", "trust", "anticipation"]
        collectedWords = {}

        for word in words:
            self.driver.get("https://www.rhymezone.com/r/rhyme.cgi?Word=" + word + "&typeofrhyme=rel&org1=syl&org2=l&org3=y")
            relatedWords = []
            while True:
                try:
                    relWrd = self.driver.find_elements_by_class_name("res")
                    for wrd in relWrd:
                        if wrd.text != "":
                            relatedWords.append(wrd.text)
                    self.driver.find_element_by_xpath("//span[@id='#next_page_marker_0']/button").send_keys('\n')
                except:
                    break
                
            collectedWords[word] = relatedWords
            print(word, collectedWords[word])
        j = json.dumps(collectedWords)
        with open("words.json", "w") as f:
            f.write(j)
            f.close()

WordsBot()