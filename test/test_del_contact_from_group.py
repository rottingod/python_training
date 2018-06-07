from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))

    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))

    contacts = db.get_contact_list()
    random_contact = random.choice(contacts)
    groups = orm.get_contact_groups(random_contact)

    if len(groups) < 1:
        all_groups = db.get_group_list()
        random_group = random.choice(all_groups)
        app.contact.select_contact_by_id(random_contact.id)
        app.contact.select_group_for_contact_by_id(random_group.id)
        groups = orm.get_contact_groups(random_contact)

    random_group = random.choice(groups)

    app.contact.delete_contact_from_group_by_id(random_contact.id, random_group.id)

    contacts_not_in_group = orm.get_contacts_not_in_group(random_group)
    new_list = [x for x in contacts_not_in_group if x.id == random_contact.id]

    assert len(new_list) == 1
    assert random_contact == new_list[0]
