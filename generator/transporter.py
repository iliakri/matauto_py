from fixture.dbase import DbFixture
from model.transporter import Transporter
import random
import string
import os.path
import jsonpickle

n = 5
f = "data/transporters.json"


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


data_transporter = [Transporter(name="", id="")] + [
    Transporter(name=random_string("name", 10), id=random.randint(1, 99999))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(data_transporter))
