from model.worker import Worker

testdata = [
    {"name": "Иванов Иван Иванович", "clock_num": "123456"},
    {"name": "Губенджоев Улугбек Хамзатович", "clock_num": "654321"},
    {"name": "Ках Лев Робертович", "clock_num": "333333"}
]

testdata2 = [
    Worker(name="Иванов Иван Иванович", clock_num="123456"),
    {"name": "Иванов Иван Иванович", "clock_num": "123456"},
    {"name": "Губенджоев Улугбек Хамзатович", "clock_num": "654321"},
    {"name": "Ках Лев Робертович", "clock_num": "333333"}
]



