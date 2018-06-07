from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))

    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))

    contacts = db.get_contact_list()
    random_contact = random.choice(contacts)
    groups_without_contact = orm.get_new_groups_for_contact(random_contact)
    while len(groups_without_contact) < 1:
        contacts.remove(random_contact)
        if len(contacts) == 0:
            app.contact.create(Contact(firstname="test"))
            contacts = db.get_contact_list()[-1:]

        random_contact = random.choice(contacts)
        groups_without_contact = orm.get_new_groups_for_contact(random_contact)

    random_group = random.choice(groups_without_contact)
    app.contact.select_contact_by_id(random_contact.id)
    app.contact.select_group_for_contact_by_id(random_group.id)
    contacts_in_group = orm.get_contacts_in_group(random_group)
    new_list = [x for x in contacts_in_group if x.id == random_contact.id]

    assert len(new_list) == 1
    assert random_contact == new_list[0]
