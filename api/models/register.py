from faker import Faker

fake = Faker()


class RegisterModel:
    @staticmethod
    def random():
        email = fake.email()
        password = fake.password()
        return {"email": email, "password": password}
