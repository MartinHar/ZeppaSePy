import random

from faker import Faker

fake = Faker()
# fake_eng_description = fake.bs()    // short version of description
fake_eng_description = fake.sentence(nb_words=20)
fake_eng_post_name = fake.catch_phrase()
fake_eng_word = fake.word()
fake_am = Faker('hy_AM')

print(fake.localized_ean8())