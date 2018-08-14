from coalib.bears.LocalBear import LocalBear
from tests.test_bears.TestLocalIndepBear import TestLocalIndepBear


class TestLocalDepBear(LocalBear):
    CAN_FIX = {}
    LANGUAGES = {}
    BEAR_DEPS = {TestLocalIndepBear}

    def run(self, filename, file, yield_results=False):
        if yield_results:
            yield 1
