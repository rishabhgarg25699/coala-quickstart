from coalib.bears.LocalBear import LocalBear
from tests.test_bears.BearB import BearB


class BearA(LocalBear):
    BEAR_DEPS = {BearB}

    def run():
        pass
