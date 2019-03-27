from model.member import Member
from model.group import Group
import random




def test_add_member_to_random_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="name", header="header", footer="footer"))
    selected_group = random.choice(orm.get_group_list())
    members_out_of_group_list = orm.get_members_not_in_group(selected_group)
    members_in_group_list = orm.get_members_in_group(selected_group)
    members_before_adding_counted = len(members_in_group_list)
    if len(members_out_of_group_list) == 0:
        app.member.create(Member(firstname="First name", lastname="Last name", address="Address", home="+375 1721111 11",
                                   mobile="+3752(91111112)", work="+3751721-111-13", phone2="+375172111114", email="test1@test.com", email2="test2@test.com",
                                   email3="test3@test.com"))
    members_out_of_group_list = orm.get_members_not_in_group(selected_group)
    selected_member = random.choice(members_out_of_group_list)
    app.group.select_group_from_group_list_on_home_page(selected_group.id)
    app.member.add_member_to_group(selected_member.id)
    new_members = orm.get_members_in_group(selected_group)
    count_members_in_group_after_adding_contact = len(new_members)
    assert members_before_adding_counted + 1 == count_members_in_group_after_adding_contact