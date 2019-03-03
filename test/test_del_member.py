from model.member import Member

def test_delete_first_member(app):
    if app.member.count_member() == 0:
        app.member.create(Member(firstname="test"))
    old_members = app.member.get_member_list()
    app.member.delete_first_member()
    assert len(old_members) - 1 == app.member.count_member()
    new_members = app.member.get_member_list()
    old_members[0:1] = []
    assert old_members == new_members


