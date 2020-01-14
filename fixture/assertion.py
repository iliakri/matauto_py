import inspect
import logging
from allure import step
import requests
import json

logger = logging.getLogger("example." + __name__)


class AssertionHelper:

    def __init__(self, app):
        self.app = app

    @step('Assert that status_code = {ok_status}')
    def status_code(self, res: requests.Response, ok_status=200) -> requests.Response:
        func = inspect.stack()[2][3]
        if isinstance(ok_status, int):
            ok_status = [ok_status]
        if res.status_code not in ok_status:
            allure.attach(res.url, "link", "text/uri-list")
            if res.headers['Content-Type'] == "application/json":
                raise ValueError(
                    f"{func} failed: "
                    f"server responded {res.status_code} "
                    f"with data: \n{json.dumps(res.json(), ensure_ascii=False, indent=2)}"
                )
            else:
                raise ValueError(f"{func} failed: " f"server responded {res.status_code} ")
        else:
            logger.info(
                f"Verified response: function {func} code {res.status_code}"
            )
        return res.status_code

    # allure.attach(json.dumps(res.json(), ensure_ascii=False, indent=2), "Response", "application/json")
