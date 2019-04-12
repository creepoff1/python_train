from model.contact import Info
from model.group import Group
import pytest
import random
from fixture.orm import ORMfixture


def test_add_contact_to_group_db(app, orm):
        if len(orm.get_contact_list()) == 0:
                app.contact.create(Info(firstname="test"))
        if len(orm.get_group_list()) == 0:
                app.group.create(Group(groupname="test"))
        groups = orm.get_group_list()
        group = random.choice(groups)
        old_contacts = orm.get_contact_list()
        old_contacts_in_group = orm.get_contacts_in_group(Group(id=group.id))
        contact = random.choice(old_contacts)
        app.contact.add_contact_to_group_by_id(contact.id, group.id)
        old_contacts_in_group.append(contact)
        new_contacts_in_group = orm.get_contacts_in_group(Group(id=group.id))
        assert sorted(new_contacts_in_group, key=Info.id_or_max) == sorted(old_contacts_in_group,
                                                                  key=Info.id_or_max)