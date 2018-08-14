from coalib.bears.LocalBear import LocalBear


class TestLocalIndepBear(LocalBear):
    CAN_FIX = {}
    LANGUAGES = {}

    def run(self, filename, file, x=2):
        yield 1
