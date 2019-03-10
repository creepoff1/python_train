import re


def test_phones_on_home_page(app):
    member_from_home_page = app.member.get_member_list()[0]
    member_from_edit_page = app.member.get_member_info_from_edit_page(0)
    assert member_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(member_from_edit_page)



def test_phones_on_member_view_page(app):
    member_from_view_page = app.member.get_member_from_view_page(0)
    member_from_edit_page = app.member.get_member_info_from_edit_page(0)
    assert member_from_view_page.phone == member_from_edit_page.phone
    assert member_from_view_page.mobile == member_from_edit_page.mobile
    assert member_from_view_page.work == member_from_edit_page.work
    assert member_from_view_page.phone2 == member_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(member):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [member.phone, member.mobile, member.work, member.phone2]))))


def merge_phones_like_on_view_page(member):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [member.phone, member.mobile, member.work, member.phone2, member.group2]))))

