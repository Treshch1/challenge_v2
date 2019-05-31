import os


WILDFLY_HOST = os.environ.get('WILDFLY_HOST', 'localhost')



class MainPage:
    
    article_xpath = '//span[.="Article"]'
    new_xpath = '//span[.="New"]'
    hotel_xpath = '//span[.="Hotel"]'

    def __init__(self, browser):
        self.browser = browser

    @property
    def article_li(self):
        return self.browser.find_element_by_xpath(self.article_xpath)


    @property
    def new_li(self):
        return self.browser.find_element_by_xpath(self.new_xpath)


    @property
    def hotel_li(self):
        return self.browser.find_element_by_xpath(self.hotel_xpath)
    

    def visit(self):
        self.browser.get(f'http://{WILDFLY_HOST}:8080/article/faces/welcome.xhtml')
