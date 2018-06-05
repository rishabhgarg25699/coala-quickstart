from coalib.bears.LocalBear import LocalBear
from tests.test_bears.BearC import BearC


class BearB(LocalBear):
    BEAR_DEPS = {BearC}

    def run():
        pass
