# user_generator.py
from faker import Faker

# Initialize Faker library
faker = Faker()

# Function to generate fake user data
def registered_user():
    return {
        "name": faker.name(),
        "S.N": faker.aba(),
        "email": faker.email(),
        "address": faker.address()
    }

if __name__ == '__main__':
    print(registered_user())
