import pymysql.connections
from model.group import Group
from model.member import Member


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_list_of_groups_names_and_ids(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name from group_list")
            for row in cursor:
                (id, name) = row
                list.append(Group(id=str(id), name=name))
        finally:
            cursor.close()
        return list


    def get_member_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated ='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                list.append(Member(id=str(id), firstname=firstname, lastname=lastname, address=address, home=home, mobile=mobile, work=work, phone2=phone2, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list


    def get_member_list_with_merged_emails_and_phones(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                list.append(
                    Member(id=str(id), firstname=firstname, lastname=lastname, address=address,
                            all_phones_from_home_page=home + mobile + work + phone2, all_emails_from_home_page=email + email2 + email3))
        finally:
            cursor.close()
        return list

    def get_member_list_as_at_ui(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2 from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2) = row
                list.append(
                    Member(id=str(id), firstname=firstname, lastname=lastname, address=address, home=home, mobile=mobile, work=work, phone2=phone2, email=email, email2=email2, email3=email3,
                           all_emails_from_db=email + email2 + email3, all_phones_from_db=home +
                                    mobile + work + phone2))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()