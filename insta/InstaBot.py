from selenium import webdriver
from googleVision import detect_faces_uri

class InstaBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/barackobama/")
        self.driver.implicitly_wait(2)
        self.imgUrls = []
    def getPostsURLs(self):
        path = self.driver.find_elements_by_xpath("//*[@class='v1Nh3 kIKUG  _bz0w']//a")   
        self.url = [url.get_attribute("href") for url in path]
        self.url = self.url[:3]

    def getPostPics(self):
        for u in self.url:
            self.driver.execute_script("window.open('"+u+"', '_self')")
            self.driver.implicitly_wait(2)
            images = self.driver.find_elements_by_xpath("//*[@class='FFVAD']")
            for i in images:
                img = i.get_attribute("srcset").split(",")[-1].split()[0]
                self.imgUrls.append(img)





t = InstaBot()
t.getPostsURLs()
t.getPostPics()
for img in t.imgUrls:
    print(detect_faces_uri(img))