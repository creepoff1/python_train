from model.member import Member

def test_mod_first_member(app):
    old_members = app.member.get_member_list()
    member = Member(firstname='Gleb', lastname='Voinov', phone='89005006040')
    member.id = old_members[0].id
    if app.member.count_member() == 0:
        app.member.create(Member(firstname="test", lastname="test", phone="88888888888"))
    app.member.mod_first_member(member)
    assert len(old_members) == app.member.count_member()
    new_members = app.member.get_member_list()
    old_members[0] = member
    assert sorted(old_members, key=Member.id_or_max) == sorted(new_members, key=Member.id_or_max)
