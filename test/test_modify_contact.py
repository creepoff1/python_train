from model.contact import Info
import random
from random import randrange


def test_modify_contact_db(app, db, check_ui):
        if len(db.get_contact_list()) == 0:
                app.contact.create(Info(firstname="test"))
        old_contacts = db.get_contact_list()
        contact = random.choice(old_contacts)
        changed_contact = Info(firstname="111qwerty", lastname="111eeeeeeeeee")
        changed_contact.id = contact.id
        app.contact.modify_contact_by_id(contact.id, changed_contact)
        assert len(old_contacts) == app.contact.count()
        new_contacts = db.get_contact_list()
        old_contacts.remove(contact)
        old_contacts.append(changed_contact)
        assert sorted(old_contacts, key=Info.id_or_max) == sorted(new_contacts, key=Info.id_or_max)
        if check_ui:
                assert sorted(new_contacts, key=Info.id_or_max) == sorted(app.contact.get_contact_list(), key=Info.id_or_max)

