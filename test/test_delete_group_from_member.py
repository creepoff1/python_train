from model.member import Member
from model.group import Group
import random

def test_delete_group_from_member(app, orm):
    group_list = orm.get_group_list()
    if len(group_list) == 0:
        app.group.open_group_page()
        app.group.create(Group(name="Group for adding contact"))
    new_group_list = orm.get_group_list()
    selected_group = random.choice(new_group_list)
    members_in_group = orm.get_members_in_group(selected_group)
    count_members_in_group_before_deleting_contact = len(members_in_group)
    if len(members_in_group) == 0:
        app.group.open_group_page()
        app.group.create(Member(firstname="test", lastname="test", home="88888888888", phone2='77777777', mobile='566666', work='555555',
                                email='g@g.ru',email2='r@f.ru', email3='gg@gg.ru'))
    new_member_list = orm.get_members_in_group(selected_group)
    selected_member = random.choice(new_member_list)
    app.member.delete_group_from_contact(selected_member.id)