from pony.orm import *
from datetime import datetime
from model.group import Group
from model.member import Member
from pymysql.converters import decoders

class ORMFixture:


    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        members = Set(lambda: ORMFixture.ORMMember, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMMember(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_members_to_model(self, members):
        def convert(member):
            return Member(id=str(member.id), firstname=member.firstname, lastname=member.lastname)
        return list(map(convert, members))

    @db_session
    def get_member_list(self):
        return self.convert_members_to_model(select(c for c in ORMFixture.ORMMember if c.deprecated is None))

    @db_session
    def get_members_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_members_to_model(orm_group.members)

    @db_session
    def get_members_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_members_to_model(
            select(c for c in ORMFixture.ORMMember if c.deprecated is None and orm_group not in c.groups))