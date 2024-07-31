from faker import Faker
faker = Faker()

def registered_user():
    return {
        "name":faker.name(),
        "S.N":faker.aba(),
        "email":faker.email(),
        "address":faker.address()
    }    


if __name__== '__main__':
    print(registered_user())