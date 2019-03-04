from model.member import Member
class MemberHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
            wd.get("http://localhost/addressbook/")

    def fill_form_member(self, member):
        wd = self.app.wd
        self.change_field_value_member("firstname", member.firstname)
        self.change_field_value_member("lastname", member.lastname)
        self.change_field_value_member("home", member.phone)

    def change_field_value_member(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def create(self, member):
        wd = self.app.wd
        # init create new member
        wd.find_element_by_link_text("add new").click()
        # fill member form
        self.fill_form_member(member)
        # submit member creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.member_cashe = None


    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
            wd.find_element_by_link_text("home page").click()

    def select_member_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_member_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_member_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.member_cashe = None

    def delete_first_member(self):
        self.delete_member_by_index(0)

    def mod_member_by_index(self, index, member):
        wd = self.app.wd
        self.open_home_page()
        self.select_member_by_index(index)
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill member form
        self.fill_form_member(member)
        # Submit
        wd.find_element_by_name("update").click()
        self.member_cashe = None

    def mod_first_member(self):
        self.mod_member_by_index(0)

    def count_member(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    member_cashe = None

    def get_member_list(self):
        if self.member_cashe is None:
            wd = self.app.wd
            self.open_home_page()
            self.member_cashe = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = element.find_elements_by_tag_name("td")
                l_name = cells[1].text
                f_name = cells[2].text
                self.member_cashe.append(Member(firstname=f_name, lastname=l_name, id=id))
        return list(self.member_cashe)
