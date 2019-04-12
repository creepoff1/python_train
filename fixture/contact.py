from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from model.contact import Info
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app


    def create(self, info):
        self.app.return_to_home()
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill in personal info
        self.fill_info(info)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_home()
        # wd.find_element_by_name("selected[]")
        self.contact_cache = None

    contacts_in_group = []

    def add_contact_to_group_by_index(self, index, group_id):
        wd = self.app.wd
        self.app.return_to_home()
        self.select_contact_by_index(index)
        Select(wd.find_element_by_name('to_group')).select_by_value(group_id)
        wd.find_element_by_name("add").click()
        self.app.return_to_home()
        self.contact_cache = None


    def add_contact_to_group_by_id(self, contact_id, group_id):
        wd = self.app.wd
        self.app.return_to_home()
        self.select_contact_by_id(contact_id)
        Select(wd.find_element_by_name('to_group')).select_by_value(group_id)
        wd.find_element_by_name("add").click()
        self.app.return_to_home()
        self.contact_cache = None


    def remove_contact_from_group_by_id(self, contact_id, group_id):
        wd = self.app.wd
        self.open_group_with_contacts_page(group_id)
        Select(wd.find_element_by_name('to_group')).select_by_value(group_id)
        self.select_contact_by_id(contact_id)
        Select(wd.find_element_by_name('to_group')).select_by_value(group_id)
        wd.find_element_by_name("remove").click()
        self.app.return_to_home()
        self.contact_cache = None

    def open_group_with_contacts_page(self, group_id):
        wd = self.app.wd
        self.app.return_to_home()
        Select(wd.find_element_by_name('group')).select_by_value(group_id)


    def modify(self):
        self.modify_contact_by_index(0)



    def modify_contact_by_index(self, index, info):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_info(info)
        # confirm changes
        wd.find_element_by_name("update").click()
        wd.find_elements_by_css_selector("div.msgbox")
        self.app.return_to_home()
        self.contact_cache = None


    def modify_contact_by_id(self, id, info):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        self.fill_info(info)
        # confirm changes
        wd.find_element_by_name("update").click()
        wd.find_elements_by_css_selector("div.msgbox")
        self.app.return_to_home()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def open_contact_to_edit_by_index(self, index):
         wd = self.app.wd
         self.app.return_to_home()
         row = wd.find_elements_by_name("entry")[index]
         cell = row.find_elements_by_tag_name("td")[7]
         cell.find_element_by_tag_name("a").click()


    def open_contact_to_edit_by_id(self, id):
         wd = self.app.wd
         self.app.return_to_home()
         wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()
         # row = wd.find_element_by_id(id)
         # cell = row.find_elements_by_tag_name("td")[7]
         # cell.find_element_by_tag_name("a").click()


    def open_contact_to_view_by_index(self, index):
         wd = self.app.wd
         self.app.return_to_home()
         row = wd.find_elements_by_name("entry")[index]
         cell = row.find_elements_by_tag_name("td")[6]
         cell.find_element_by_tag_name("a").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_info(self, info):
        wd = self.app.wd
        # fill in personal info
        self.change_field_value("firstname", info.firstname)
        self.change_field_value("middlename", info.middlename)
        self.change_field_value("lastname", info.lastname)
        self.change_field_value("nickname", info.nick)
        self.change_field_value("title", info.title)
        self.change_field_value("company", info.cname)
        self.change_field_value("address", info.address)
        # fill in  phone numbers
        self.change_field_value("home", info.homedid)
        self.change_field_value("mobile", info.cellular)
        self.change_field_value("work", info.workdid)
        self.change_field_value("fax", info.fax)

        # fill in  emails and website
        self.change_field_value("email", info.email)
        self.change_field_value("email2", info.email2)
        self.change_field_value("email3", info.email3)
        self.change_field_value("homepage", info.website)
        # choose birthday and anniversary day
        # wd.find_element_by_name("bday").click()
        # wd.find_element_by_name("bday").click()
        # Select(wd.find_element_by_name("bday")).select_by_visible_text("15")
        # wd.find_element_by_xpath("//option[@value='15']").click()
        # wd.find_element_by_name("bmonth").click()
        # Select(wd.find_element_by_name("bmonth")).select_by_visible_text("November")
        # wd.find_element_by_xpath("//option[@value='November']").click()
        # wd.find_element_by_name("byear").click()
        # wd.find_element_by_name("byear").clear()
        # wd.find_element_by_name("byear").send_keys(info.byear)
        # wd.find_element_by_name("aday").click()
        # Select(wd.find_element_by_name("aday")).select_by_visible_text("13")
        # wd.find_element_by_xpath("(//option[@value='13'])[2]").click()
        # wd.find_element_by_name("amonth").click()
        # Select(wd.find_element_by_name("amonth")).select_by_visible_text("August")
        # wd.find_element_by_xpath("(//option[@value='August'])[2]").click()
        # wd.find_element_by_name("ayear").click()
        # wd.find_element_by_name("ayear").clear()
        # wd.find_element_by_name("ayear").send_keys(info.ayear)
        # fill in secondary info

        self.change_field_value("address2", info.address2)
        self.change_field_value("phone2", info.secondaryphone)
        self.change_field_value("notes", info.notes)



    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.return_to_home()
        self.select_contact_by_index(index)
        # submit contact deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # self.accept_next_alert = True
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.return_to_home()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # self.accept_next_alert = True
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.contact_cache = None


    def count(self):
        wd = self.app.wd
        self.app.return_to_home()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.return_to_home()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = element.find_elements_by_tag_name("td")
                l_name = cells[1].text
                f_name = cells[2].text
                address = cells[3].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Info(firstname=f_name, lastname=l_name, id=id, address=address,
                                               all_phones_from_home_page=all_phones,
                                               all_emails_from_home_page=all_emails))
        return list(self.contact_cache)



    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homedid = wd.find_element_by_name("home").get_attribute("value")
        workdid = wd.find_element_by_name("work").get_attribute("value")
        cellular = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Info(firstname=firstname, lastname=lastname, id=id, address=address, homedid=homedid, workdid=workdid,
                       cellular=cellular, secondaryphone=secondaryphone, email=email, email2=email2, email3=email3)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homedid = re.search("H: (.*)", text).group(1)
        workdid = re.search("W: (.*)", text).group(1)
        cellular = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Info(homedid=homedid, workdid=workdid,
                    cellular=cellular, secondaryphone=secondaryphone)


    def get_list_of_contacts_in_group_by_id(self, group_id):
        wd = self.app.wd
        self.app.return_to_home()
        self.open_group_with_contacts_page(group_id)
        for element in wd.find_elements_by_css_selector("tr[name='entry']"):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            cells = element.find_elements_by_tag_name("td")
            l_name = cells[1].text
            f_name = cells[2].text
            address = cells[3].text
            all_phones = cells[5].text
            all_emails = cells[4].text
            self.contacts_in_group.append(Info(firstname=f_name, lastname=l_name, id=id, address=address,
                                               all_phones_from_home_page=all_phones,
                                               all_emails_from_home_page=all_emails))
        return self.contacts_in_group