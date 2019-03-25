from model.member import Member
from model.group import Group
import random
from random import randrange

def test_add_group_to_contact(app, db, json_members, orm):
    app.group.open_group_page()
    group_list = orm.get_group_list()
    if len(group_list) == 0:
       app.group.open_group_page()
       app.group.create(Group(name="Group for adding contact"))
    new_group_list = orm.get_group_list()
    selected_group = random.choice(new_group_list)
    old_contacts = orm.get_members_not_in_group(selected_group)
    members_in_group = orm.get_members_in_group(selected_group)
    count_members_in_group_before_adding_contact = len(members_in_group)
    if len(old_contacts) == 0:
        app.group.open_group_page()
        app.group.create(Member(firstname="test", lastname="test", home="88888888888", phone2='77777777', mobile='566666', work='555555',
                                email='g@g.ru',email2='r@f.ru', email3='gg@gg.ru'))
    new_member_list = orm.get_members_not_in_group(selected_group)
    app.group.open_group_page()
    selected_member = random.choice(new_member_list)
    app.group.select_group_from_group_list_on_home_page(selected_group.id)
    app.member.add_group_to_member(selected_member.id)
    new_members = orm.get_members_in_group(selected_group)
    count_members_in_group_after_adding_member = len(new_members)
    assert count_members_in_group_before_adding_contact + 1 == count_members_in_group_after_adding_member