from coalib.bears.LocalBear import LocalBear
from coalib.bearlib import deprecate_settings


class AllKindsOfSettingsBaseDecoratedBear(LocalBear):

    @deprecate_settings(max_line_lengths='tab_width')
    def run(self, file, filename, config, use_bear: bool,
            max_line_lengths, no_line: int, use_space: bool = None,
            use_tab: bool = False, max_line_length: int = 1000,
            no_char=79, dependency_result=dict()):
        pass
