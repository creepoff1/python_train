class MemberHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")

    def create_member(self, member):
        wd = self.app.wd
        # init create new member
        wd.find_element_by_link_text("add new").click()
        # fill member form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(member.firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(member.lastname)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(member.phone)
        wd.find_element_by_name("theform").click()
        # submit member creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()


    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()