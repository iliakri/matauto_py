import datetime
import random
import string
from faker import Faker


constant_for_create_worker = [
    {"name": "Иванов Иван Иванович", "clock_num": "123456"},
    {"name": "Губенджоев Улугбек Хамзатович", "clock_num": "654321"},
    {"name": "Ках Лев Робертович", "clock_num": "333333"}
]

# cs_CZ, lv_LV, pl_PL, uk_UA, sl_SI, ru_RU
fake = Faker('ru_RU')

data_for_create_worker = [
    {"name": fake.name(), "clock_num": str(fake.pyint())} for i in range(3)
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return prefix + " " + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + " " \
           + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata2 = [{"name": '', "clock_num": ''}] + [
    {"name": random_string("Auto", 12), "clock_num": random.randint(1, 99999)} for i in range(5)
]


def random_worker():
    return {
        "name": fake.name(),
        "clock_num": fake.pyint()
    }


fake_end_date = datetime.date(2019, 9, 24)
start_date = [(transporter_id, fake.date_between(start_date="-25d", end_date=fake_end_date)) for transporter_id in range(1, 5)]