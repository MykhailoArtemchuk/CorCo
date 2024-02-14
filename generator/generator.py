from data.data import Person
from faker import Faker

faker_u = Faker('ru_Ru')


def generated_person():
    yield Person(
        full_name=faker_u.first_name() + " " + faker_u.last_name() + ' ' + faker_u.middle_name(),
        email=faker_u.email(),
        current_address=faker_u.address(),
        permanent_address=faker_u.address()
    )
