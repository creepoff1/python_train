from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.member import MemberHelper
class Application:

    def __init__(self, browser, base_url, user, password):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.member = MemberHelper(self)
        self.base_url = base_url
        self.user = user
        self.password = password

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()