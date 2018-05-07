from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))

    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="Maria")
    contact.id = old_contacts[0].id
    contact.last_name = old_contacts[0].last_name
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

