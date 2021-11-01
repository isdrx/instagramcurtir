from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe')


    # //input[@name='username']
    #//input[@name='password']
    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(2)
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.curtir_fotos('hastag_para_curtir')

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(5)     
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' fotos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_class_name('fr66n').click() #//button[@class="fr66n"] 
                print('Curtido')
                time.sleep(19)
            except Exception as e:
                print('não foi curtido')
                time.sleep(5)


detoxBot = InstagramBot('usuario','senha')
detoxBot.login()

