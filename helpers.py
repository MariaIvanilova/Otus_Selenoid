from faker import Faker


def user_registration_information():
    faker = Faker("en")
    return faker.first_name(), faker.last_name(), faker.email(), faker.password()
