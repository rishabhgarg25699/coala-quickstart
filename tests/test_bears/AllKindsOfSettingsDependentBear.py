from coalib.bears.LocalBear import LocalBear
from tests.test_bears.AllKindsOfSettingsBaseBear import \
    AllKindsOfSettingsBaseBear


class AllKindsOfSettingsDependentBear(LocalBear):
    BEAR_DEPS = {AllKindsOfSettingsBaseBear}

    def run(self, file, filename, configs, use_bears: bool,
            no_lines: int, use_spaces: bool = None,
            use_tabs: bool = False, max_line_lengths: int = 1000,
            no_chars=79, chars=False, dependency_results=dict()):
        pass
