import re
from random import randrange
from model.contact import Contact

def test_all_on_home_page(app, db):
    app.open_home_page()
    db_contacts = db.get_contact_list()
    contacts_from_home_page = app.contact.get_contact_list()
    sorted_db_contacts = sorted(db_contacts, key=Contact.id_or_max)
    sorted_contacts_from_home_page = sorted(contacts_from_home_page, key=Contact.id_or_max)
    assert sorted_db_contacts == sorted_contacts_from_home_page

    for index, contact in enumerate(sorted_db_contacts):
        app.open_home_page()
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page_by_id(contact.id)
        assert contact.address == contact_from_edit_page.address
        assert merge_phones_like_on_home_page(contact) == merge_phones_like_on_home_page(contact_from_edit_page)
        assert merge_emails_like_on_home_page(contact) == merge_emails_like_on_home_page(contact_from_edit_page)
        assert contact.firstname == contact_from_edit_page.firstname
        assert contact.lastname == contact_from_edit_page.lastname


def clear(s):
    return re.sub("[() -]", "", s.split('"')[0])


def clear_email(s):
    return re.sub(" ", "", s.split('"')[0])


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.homephone, contact.mobilephone, contact.workphone,
                                                            contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_email(x), filter(lambda x: x is not None,
                                                           [contact.email, contact.email2, contact.email3]))))
