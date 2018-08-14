from coalib.bears.LocalBear import LocalBear


class AnotherTestLocalIndepBear(LocalBear):
    CAN_FIX = {}
    LANGUAGES = {}

    def run(self, filename, file, x=2):
        pass
