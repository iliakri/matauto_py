import inspect
import logging
from allure import step, attach
import requests
import json

logger = logging.getLogger("example." + __name__)


class AssertionHelper:

    def __init__(self, app):
        self.app = app

    @step('Assert that status_code = {ok_status}')
    def status_code(self, res: requests.Response, ok_status=200) -> requests.Response:
        func = inspect.stack()[0][3]
        if isinstance(ok_status, int):
            ok_status = [ok_status]
        if res.status_code not in ok_status:
            attach(res.url, "link", "text/uri-list")
            if res.headers['Content-Type'] == "application/json":
                raise ValueError(
                    f"verify {func} failed: "
                    f"server responded code {res.status_code} "
                    f"with data: \n{json.dumps(res.json(), ensure_ascii=False, indent=2)}"
                )
            else:
                raise ValueError(f"verify {func} failed: " f"server responded code {res.status_code} ")
        else:
            logger.info(
                f"Verified response: function {func} code {res.status_code}"
            )
        return res.status_code

    @step('Assert that headers contains a {ok_header}')
    def headers(self, res: requests.Response, ok_header='server') -> requests.Response:
        #print(inspect.stack())
        func = inspect.stack()[0][3]
        if ok_header not in res.headers:
            attach(res.url, "link", "text/uri-list")
            raise ValueError(
                f"verify {func} failed: "
                f"server responded code {res.status_code} "
                f"with headers: \n{json.dumps(dict(res.headers), ensure_ascii=False, indent=2)}"
            )
        else:
            logger.info(
                f"Verified response: function {func} code {res.headers}"
            )
        return res.headers

    # allure.attach(json.dumps(res.json(), ensure_ascii=False, indent=2), "Response", "application/json")
