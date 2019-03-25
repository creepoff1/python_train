from sys import maxsize
class Member:
    def __init__(self, id = None, firstname = None, lastname = None, home = None, mobile = None, work = None, phone2 = None,
                 all_phones_from_home_page = None, email = None, address = None, email2 = None, email3 = None, all_emails_from_home_page = None, new_group = None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.home = home
        self.mobile = mobile
        self.work = work
        self.phone2 = phone2
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.new_group = new_group
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:" % (self.id, self.firstname, self.lastname, self.address, self.home, self.mobile, self.work, self.phone2, self.address, self.email, self.email2, self.email3)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               or self.lastname == other.last_name \
               or self.firstname == other.first_name \
               or self.address == other.address \
               or self.email == other.email \
               or self.email2 == other.email_2 \
               or self.email3 == other.email_3 \
               or self.home == other.home \
               or self.work == other.work_phone \
               or self.mobile == other.mobile \
               or self.phone2 == other.phone2 \

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize