import inspect
import logging
import allure
import requests
import json

logger = logging.getLogger("example." + __name__)


class AssertionHelper:

    def __init__(self, app):
        self.app = app

    @allure.step("Проверка ответа")
    def status_code(self, res: requests.Response, ok_status=200) -> requests.Response:
        func = inspect.stack()[2][3]
        if isinstance(ok_status, int):
            ok_status = [ok_status]
        if res.status_code not in ok_status:
            allure.attach(res.url, "link", "text/uri-list")
            #allure.attach(json.dumps(res.json(), ensure_ascii=False, indent=2), "Response", "application/json")
            raise ValueError(
                f"{func} failed: "
                f"server responded {res.status_code} "
                f"with data: \n{json.dumps(res.json(), ensure_ascii=False, indent=2)}"
            )
        else:
            logger.info(
                f"Verified response: function {func} code {res.status_code}"
            )
        return res.status_code
