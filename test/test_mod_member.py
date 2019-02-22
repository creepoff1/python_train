from model.member import Member

def test_mod_first_member(app):
    app.member.mod_first_member(Member(firstname='Gleb', lastname='Voinov', phone='89005006040'))