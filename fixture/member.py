class MemberHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
            wd.get("http://localhost/addressbook/")

    def fill_form_member(self, member):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(member.firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(member.lastname)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(member.phone)


    def create(self, member):
        wd = self.app.wd
        # init create new member
        wd.find_element_by_link_text("add new").click()
        # fill member form
        self.fill_form_member(member)
        # submit member creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()


    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
            wd.find_element_by_link_text("home page").click()

    def delete_first_member(self):
        wd = self.app.wd
        self.open_home_page()
        # select first member
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def mod_first_member(self, member):
        wd = self.app.wd
        self.open_home_page()
        # select first member
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill member form
        self.fill_form_member(member)
        # Submit
        wd.find_element_by_name("update").click()

    def count_member(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))