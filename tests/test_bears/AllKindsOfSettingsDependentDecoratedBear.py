from coalib.bears.LocalBear import LocalBear
from coalib.bearlib import deprecate_settings
from tests.test_bears.AllKindsOfSettingsBaseDecoratedBear import \
    AllKindsOfSettingsBaseDecoratedBear


class AllKindsOfSettingsDependentDecoratedBear(LocalBear):
    BEAR_DEPS = {AllKindsOfSettingsBaseDecoratedBear}

    @deprecate_settings(max_line_lengths='tab_width')
    def run(self, file, filename, configs, use_bears: bool,
            no_lines: int, use_spaces: bool = None,
            use_tabs: bool = False, max_line_lengths: int = 1000,
            no_chars=79, chars=False, dependency_results=dict()):
        pass
