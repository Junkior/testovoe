from faker import Faker

fake = Faker()


class CreateModel:
    @staticmethod
    def random():
        name = fake.name()
        job = fake.job()
        return {"name": name, "job": job}




