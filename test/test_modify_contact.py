from model.contact import Contact
import random


def test_modify_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    random_contact = random.choice(old_contacts)
    contact = Contact(firstname="Maria")
    contact.id = random_contact.id
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts[old_contacts.index(random_contact)].merge(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)