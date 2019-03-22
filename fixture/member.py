from model.member import Member
import re
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
        self.change_field_value_member("home", member.home)
        self.change_field_value_member("phone2", member.phone2)
        self.change_field_value_member("mobile", member.mobile)
        self.change_field_value_member("work", member.work)
        self.change_field_value_member("email", member.email)
        self.change_field_value_member("email2", member.email2)
        self.change_field_value_member("email3", member.email3)

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

    def select_member_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()

    def edit_member_click(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()
        self.member_cashe = None

    def delete_member_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_member_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.member_cashe = None

    def delete_member_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_member_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.member_cashe = None

    def delete_first_member(self):
        self.delete_member_by_index(0)

    def mod_member_by_index(self, index, member):
        wd = self.app.wd
        self.app.open_home_page()
        self.edit_member_click(index)
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
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = row.find_element_by_name("selected[]").get_attribute("id")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.member_cashe.append(Member(id=id, firstname=firstname, lastname=lastname, address=address,
                                                 all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.member_cashe)


    def open_member_to_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()
        self.contact_cache = None

    def get_member_info_from_edit_page(self, index):
        wd = self.app.wd
        self.edit_member_click(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Member(id=id, firstname=firstname, lastname=lastname, home=home, mobile=mobile,
                       work=work, phone2=phone2, address=address, email=email, email2=email2, email3=email3)

    def get_member_from_view_page(self, index):
        wd = self.app.wd
        self.open_member_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Member(home=home, work=work, mobile=mobile, phone2=phone2)

    def modify_member_by_id(self, id, member):
        wd = self.app.wd
        self.select_member_by_id(id)
        self.fill_form_member(member)
        wd.find_element_by_xpath("//input[22]").click()
        self.contact_cache = None

