from model.member import Member

def test_delete_first_member(app):
    if app.member.count_member() == 0:
        app.member.create(Member(firstname="test"))
    app.member.delete_first_member()