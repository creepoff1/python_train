from model.contact import Info
from model.group import Group
import random


def test_remove_contact_from_group_db(app, orm):
        if len(orm.get_contact_list()) == 0:
                app.contact.create(Info(firstname="test"))
        if len(orm.get_group_list()) == 0:
                app.group.create(Group(groupname="test"))
        groups = orm.get_group_list()
        group = random.choice(groups)
        old_contacts_in_group = orm.get_contacts_in_group(group)
        if len(old_contacts_in_group) == 0:
                selected_contact_to_add = random.choice(orm.get_contact_list())
                app.contact.add_contact_to_group_by_id(selected_contact_to_add.id, group.id)
                old_contacts_in_group = orm.get_contacts_in_group(group)
        selected_contact = random.choice(old_contacts_in_group)
        app.contact.remove_contact_from_group_by_id(selected_contact.id, group.id)
        old_contacts_in_group.remove(selected_contact)
        new_contacts_in_group = orm.get_contacts_in_group(Group(id=group.id))
        assert sorted(new_contacts_in_group, key=Info.id_or_max) == sorted(old_contacts_in_group,
                                                                  key=Info.id_or_max)

