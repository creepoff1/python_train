from model.group import Group
class GroupHelper:

    group_cashe = None

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def fill_form_group(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_form_group(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.group_cashe = None

    def delete_first_group(self):
        wd = self.app.wd
        self.delete_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[contains(@value, '%s')]" % id).click()


    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cashe = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cashe = None

    def mod_first_group(self):
        self.modify_group_by_index(0)

    def return_to_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("group page").click()


    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_form_group(new_group_data)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cashe = None

    def modify_group_by_id(self, id, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        # Select any group
        self.select_group_by_id(id)
        # Open modification form
        wd.find_element_by_name("edit").click()
        self.fill_form_group(new_group_data)
        # Submit modification
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        if self.group_cashe is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cashe = []
            for element in wd.find_elements_by_css_selector("span.group"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                name = element.text
                self.group_cashe.append(Group(id=id, name=name))
        return list(self.group_cashe)

    def select_group_from_group_list_on_home_page(self, id):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("add")
        wd.find_element_by_css_selector("select[name='to_group'] option[value='%s']" % id).click()