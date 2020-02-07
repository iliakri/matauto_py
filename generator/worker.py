import datetime
import random
import string
from faker import Faker
from fixture.dbase import DbFixture
from conftest import db

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


def load_from_bd(object):
    transporter_id = DbFixture(host='192.168.12.10', dbname='dev_production', user='vlad', password='1').get_all_transporters_id(object)
    '''for item in transporter_id:
        return item'''
    return transporter_id


# end_date = datetime.date(2019, 9, 1)
start_date = [(transporter_id, fake.date_between(start_date="-25d", end_date="now")) for transporter_id in range(1, 5)]
trid_and_date = [(transporter_id, fake.date_between(start_date="-25d", end_date="now")) for transporter_id in load_from_bd("transporter")]

transporter_id = []
transporter_id.extend(load_from_bd("transporter"))