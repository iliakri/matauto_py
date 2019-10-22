import allure


def test_create_allure_locust():
    allure.attach.file("test_result_distribution.csv", name="result_locust_dis", attachment_type="text/csv", extension=".csv")
    allure.attach.file("test_result_requests.csv", name="result_locust_req", attachment_type="text/csv", extension=".csv")