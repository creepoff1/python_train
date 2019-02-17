from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.member import MemberHelper
class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.member = MemberHelper(self)


    def open_home_page(self):
      wd = self.wd
      wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()