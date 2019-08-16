import psycopg2
from model.worker import Worker


class DbFixture:

    def __init__(self, host, dbname, user, password):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.connection = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)

    def get_worker(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name from worker")
            for row in cursor:
                (id, name) = row
                list.append(Worker(id=id, name=name))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

