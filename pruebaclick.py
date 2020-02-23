import os;
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

os.environ["PATH"] += os.pathsep + r'C:\geckodriver-v0.26.0-win64';
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True
cap['handleAlerts'] = True
cap['acceptSslCerts'] = True
cap['acceptInsecureCerts'] = True
opts = Options()
opts.add_argument("-new-tab")
firefox_profile = webdriver.FirefoxProfile()
#firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
for i in range(1,3):
    firefox_profile.set_preference("browser.tabs.remote.autostart."+str(i+1), True)
    browser = webdriver.Firefox(capabilities=cap, firefox_binary=binary )
    browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    browser.get('https://google.com/')
    # Get button you are going to click by its id ( also you could us find_element_by_css_selector to get element by css selector)
    #button_element = browser.find_element_by_id('close_entrance_terms')
    #button_element.click()
    
    
