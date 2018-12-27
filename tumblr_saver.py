from selenium import webdriver
import time

def operate(blog, num, safari):
    if safari:
        with webdriver.Safari() as driver:
            save(blog,num,driver)
    else:
        import os
        with webdriver.Chrome(str(os.getcwd())+'/chromedriver') as driver:
            save(blog,num,driver)

def save(blog, num, driver):
    more = True
    i = 1
    if (num == 0):
        more = False
        i = i - 1

    while more:
        driver.get('https://web.archive.org/save/https://'+blog+'.tumblr.com/page/'+str(i))
        while ('web.archive.org/web/' not in driver.current_url): # when page is saved, web.archive redirects to url web.archive.org/web/something-or-other
            time.sleep(0.2)
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
        blog = argv[1]
    except:
        blog = input('What is your blog name (which appears in its url) ?\n')
    
    num = -1
    for arg in argv:
        try:
            num = int(arg)
        except:
            num = num
    if num == -1:
        num = input('Save the first N pages. Leave blank to save them all.\nN: ')
        try:
            num = int(num)
        except:
            num = -1
    
    browser = 'safari' in input('Safari or Chrome?\n').lower()
    print('Using '+browser*'Safari'+(not browser)*'Chrome')
    
    #try:
    operate(blog, num, safari=browser)
    #except:
     #   print('program terminated prematurely.')
