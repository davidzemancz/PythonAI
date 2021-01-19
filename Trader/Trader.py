import sys
from Base import BaseActionResult

class Trader:
    def start() -> BaseActionResult:
        try:
            ret = None

            return BaseActionResult(True, "", ret)
        except BaseException as err:
            return BaseActionResult(False, str(err), err)


        