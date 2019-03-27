from model.member import Member
from model.group import Group
import random



def test_delete_member_from_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="name", header="header", footer="footer"))
    group_list = orm.get_group_list()
    if len(orm.get_member_list()) == 0:
        app.member.create(Member(firstname="First name", lastname="Last name", address="Address", home="+375 1721111 11",
                                   mobile="+3752(91111112)", work="+3751721-111-13", phone2="+375172111114", email="test1@test.com", email2="test2@test.com",
                                   email3="test3@test.com"))
    member_list = orm.get_member_list()
    selected_group = random.choice(group_list)
    member_list_from_group = orm.get_members_in_group(selected_group)
    if len(member_list_from_group) == 0:
        selected_member = random.choice(member_list)
        app.group.select_group_from_group_list_on_home_page(selected_group.id)
        app.member.add_member_to_group(selected_member.id)
        member_list_from_group = orm.get_members_in_group(selected_group)
    count_members_in_group_before_deleting = len(member_list_from_group)
    selected_member = random.choice(member_list_from_group)
    app.member.open_group_page_with_members(selected_group.name)
    member_index = member_list_from_group.index(selected_member)
    app.member.delete_member_from_group(selected_group.name, member_index)
    member_list = orm.get_members_in_group(selected_group)
    count_members_in_group_after_deleting_member = len(member_list)
    assert count_members_in_group_before_deleting - 1 == count_members_in_group_after_deleting_member