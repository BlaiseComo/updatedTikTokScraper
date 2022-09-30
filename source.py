from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Class named ObtainData, but it will only be used on tiktok
# Class takes two arguments, the link to tik tok, and the amount of posts to be scraped
class ObtainData:
    
    def __init__(self, link=None, amountOfPosts=10):
        self.link = link # The link for website to be scraped
        self.amountOfPosts = amountOfPosts # The amount of posts to be scraped, more = higher accuracy but more time
        self.dictOfData = {} # Keys will be hashtags, values will be a list of lists, index 0 being like count, index 1 being follower count, index 2 being ratio (likes/followers)

    def obtainTikTokData(self):

        mainDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # Driver object used to access websites
        mainDriver.get(self.link) # Connects driver to the link

        for i in range(0, self.amountOfPosts):

            listOfHashtags = []
            likeCount = 0
            followerCount = 0

            listOfHashtags = mainDriver.find_elements(By.TAG_NAME, 'strong')
            listOfHashtags = [i.text for i in listOfHashtags if i[0] == '#']

            for i.text in listOfHashtags:
                if i[-1] == 'K':
                    likeCount = i[:-1]
            
            



    def returnSortedData(self):
        return self.dictOfData

    def addDataToFile(self):
        pass






