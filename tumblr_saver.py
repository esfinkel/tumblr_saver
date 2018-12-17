import selenium
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def save(blog, num):
    more = True
    i = 1
    if (num == 0):
        more = False
        i = i - 1
    with webdriver.Chrome('/Applications/chromedriver') as driver:
        while more:
            driver.get('https://web.archive.org/save/https://'+blog+'.tumblr.com/page/'+str(i))
            while (driver.current_url=='https://web.archive.org/save/https://'+blog+'.tumblr.com/page/'+str(i)+'/'):
                time.sleep(1)
            try:
                driver.find_element_by_css_selector('#page > div.posts-no-posts.content').text
                more = False
                i = i - 1
            except:
                i = i + 1
            if (num > 0 and i > num):
                more = False
                i = i - 1
    print('saved pages with indices 1 through',i)                

if __name__ == '__main__':
    from sys import argv
    try:
        num = int(argv[2])
    except:
        num = -1
    num = num
    blog = argv[1]
    try:
        blog = argv[1]
        save(blog, num)
    except:
        print('please enter your blog name (which appears in its url) after the name of this program.')
