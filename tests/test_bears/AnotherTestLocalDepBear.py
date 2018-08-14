from coalib.bears.LocalBear import LocalBear
from tests.test_bears.AnotherTestLocalIndepBear import AnotherTestLocalIndepBear


class AnotherTestLocalDepBear(LocalBear):
    CAN_FIX = {}
    LANGUAGES = {}
    BEAR_DEPS = {AnotherTestLocalIndepBear}

    def run(self, filename, file, yield_results=False):
        pass
