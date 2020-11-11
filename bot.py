from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def subscribe_action(email, password, channel):
    #set true for firefox otherwise false for chrome
    if(True):
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

        driver = webdriver.Firefox(firefox_profile=firefox_profile)
        driver.get("https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")
        # using stackoverflow because gmail doesnt allow automated email password typing directly
        driver.find_element_by_xpath("//div[@id='openid-buttons']/button").click()
    else: 
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")

        caps = options.to_capabilities()

        driver = webdriver.Chrome(desired_capabilities=caps)
        driver.get('https://mail.google.com')
   
    driver.find_element_by_name("identifier").send_keys(email)
    time.sleep(6.0)
    driver.find_element_by_name("identifier").send_keys(Keys.ENTER)
    time.sleep(1.0)
    
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("password").send_keys(Keys.ENTER)
    time.sleep(8.0)
    #login done

    #lets open youtube now
    driver.get(channel)
    time.sleep(5.0)
    #click subscribe

    driver.find_element_by_id("subscribe-button").click()
    print("Subscribed :)")
    driver.close()

subscribe_action("email", "password", "https://www.youtube.com/channel/link")
