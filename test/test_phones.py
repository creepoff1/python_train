import re
from model.contact import Info
from random import randrange


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter (lambda x: x is not None,
                                                            [contact.homedid, contact.cellular, contact.workdid, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter (lambda x: x is not None,
                                                            [contact.email, contact.email2, contact.email3]))))



def test_all_params_on_home_page(app, orm):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Info.id_or_max)
    contacts_from_db = orm.get_contact_list()
    assert contacts_from_db == sorted(contacts_from_home_page, key=Info.id_or_max)
    n = 0
    for contact in contacts_from_home_page:
        assert contact.firstname == contacts_from_db[n].firstname.strip()
        assert contact.lastname == contacts_from_db[n].lastname.strip()
        assert contact.address == contacts_from_db[n].address.strip()
        assert contact.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[n])
        assert contact.all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[n])
        n = n + 1



