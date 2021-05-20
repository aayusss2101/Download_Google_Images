from selenium import webdriver
import time
import urllib.request
import os
from selenium.webdriver.common.keys import Keys


def download_images_from_google(chrome_driver_path, download_path, key_word, scrolls):
    
    '''
    
    Parameters:
    chrome_driver_path (String) : Path of the chrome webdriver executable
    download_path (String) : Path of directory where images will be downloaded
    key_word (String) : Keyword to search on google
    scrolls (Int) : Number of scrolls to perform on the page
    
    '''
    
    # Setting options to run Chrome webdriver in headless mode
    chrome_options=webdriver.ChromeOptions()    
    chrome_options.headless=True
    
    # Webdriver object
    browser=webdriver.Chrome(chrome_driver_path, options=chrome_options)

    # Open google.com
    browser.get("https://google.com/")

    # Get the search element
    search=browser.find_element_by_name('q')

    # Entering the key word
    search.send_keys(key_word,Keys.ENTER)

    # Find the Images tab and opening it
    images=browser.find_element_by_link_text('Images')
    images.get_attribute('href')
    images.click()

    # Scroll the page to load images
    value=0
    for i in range(scrolls):
        browser.execute_script("scrollBy("+ str(value) +", +1000);")
        value+=1000
        time.sleep(3)

    # Find div containing images
    elem=browser.find_element_by_id("islmp")

    # Find all images
    img_tags=elem.find_elements_by_tag_name("img")

    # Download images
    count=0
    for img in img_tags:
        src=img.get_attribute("src")
        try:
            if src==None:
                raise TypeError
            src=str(src)
            count+=1
            urllib.request.urlretrieve(src,os.path.join(download_path,f"image{count}.jpg"))
        except TypeError:
            continue
