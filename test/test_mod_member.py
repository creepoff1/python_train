from model.member import Member

def test_mod_first_member(app):
    if app.member.count_member() == 0:
        app.member.create(Member(firstname="test", lastname="test", phone="88888888888"))
    app.member.mod_first_member(Member(firstname='Gleb', lastname='Voinov', phone='89005006040'))