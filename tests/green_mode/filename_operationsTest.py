import unittest
import yaml
from copy import deepcopy
from pathlib import Path

from coala_quickstart.generation.Utilities import (
    append_to_contents,
    )
from coala_quickstart.green_mode.filename_operations import (
    check_filename_prefix_postfix,
    get_files_list,
    )
from coala_quickstart.green_mode.green_mode import (
    settings_key,
    )


class TestFilenameOperations(unittest.TestCase):

    def test_get_files_list(self):
        file_path = Path(__file__).parent / 'example_.project_data.yaml'
        with file_path.open() as stream:
            contents = yaml.load(stream)
        files_list = get_files_list(contents['dir_structure'])
        test_files_list = ['.coafile', 'example_file_1',
                           'example_file_2', 'example_file_3',
                           'example_file_4', 'example_file_5',
                           'example_file_6']
        self.assertEqual(files_list, test_files_list)

    def test_check_filename_prefix_postfix(self):
        # Files having a common prefix but no suffix.
        file_path = Path(__file__).parent / 'example_.project_data.yaml'
        with file_path.open() as stream:
            contents = yaml.load(stream)
        ret_val_contents = check_filename_prefix_postfix(deepcopy(contents),
                                                         3, 3)
        test_contents = deepcopy(append_to_contents(deepcopy(contents),
                                                    'filename_prefix',
                                                    ['example_file_'],
                                                    settings_key))
        test_contents = append_to_contents(deepcopy(test_contents),
                                           'filename_suffix',
                                           [''],
                                           settings_key)
        self.assertEqual(test_contents, ret_val_contents)

        # Works well when min files and min length of prefix are sufficiently
        # low.
        contents = {'dir_structure': ['py_some_name.xyz', 'py_some_other.c',
                                      'py_yet_another_file.yaml']}
        ret_val_contents = check_filename_prefix_postfix(deepcopy(contents),
                                                         2, 2)
        test_contents = deepcopy(append_to_contents(deepcopy(contents),
                                                    'filename_prefix',
                                                    ['py_'],
                                                    settings_key))
        test_contents = append_to_contents(deepcopy(test_contents),
                                           'filename_suffix',
                                           [''],
                                           settings_key)
        self.assertEqual(test_contents, ret_val_contents)

        # Works when min length of prefix and min files is exactly equal
        # to the paramters passed.
        ret_val_contents = check_filename_prefix_postfix(deepcopy(contents),
                                                         3, 3)
        test_contents = deepcopy(append_to_contents(deepcopy(contents),
                                                    'filename_prefix',
                                                    ['py_'],
                                                    settings_key))
        test_contents = append_to_contents(deepcopy(test_contents),
                                           'filename_suffix',
                                           [''],
                                           settings_key)
        self.assertEqual(test_contents, ret_val_contents)

        # Doesn't work when min length of prefix exceeds the prefix value.
        ret_val_contents = check_filename_prefix_postfix(deepcopy(contents),
                                                         4, 3)
        test_contents = deepcopy(append_to_contents(deepcopy(contents),
                                                    'filename_prefix',
                                                    [''],
                                                    settings_key))
        test_contents = append_to_contents(deepcopy(test_contents),
                                           'filename_suffix',
                                           [''],
                                           settings_key)
        self.assertEqual(test_contents, ret_val_contents)

        # Doesn't work when min files exceed the files for a given prefix.
        ret_val_contents = check_filename_prefix_postfix(deepcopy(contents),
                                                         3, 4)
        test_contents = deepcopy(append_to_contents(deepcopy(contents),
                                                    'filename_prefix',
                                                    [''],
                                                    settings_key))
        test_contents = append_to_contents(deepcopy(test_contents),
                                           'filename_suffix',
                                           [''],
                                           settings_key)
        self.assertEqual(test_contents, ret_val_contents)

        # Files having a prefix and a suffix
        contents = {'dir_structure': ['py_some_name.xyz',
                                      'py_some_other_name.c',
                                      'py_yet_another_name.yaml']}
        ret_val_contents = check_filename_prefix_postfix(deepcopy(contents),
                                                         3, 3)
        test_contents = deepcopy(append_to_contents(deepcopy(contents),
                                                    'filename_prefix',
                                                    ['py_'],
                                                    settings_key))
        test_contents = append_to_contents(deepcopy(test_contents),
                                           'filename_suffix',
                                           ['_name'],
                                           settings_key)
        self.assertEqual(test_contents, ret_val_contents)

        # Both prefix and suffix don't work if the number of files exceed.
        ret_val_contents = check_filename_prefix_postfix(deepcopy(contents),
                                                         3, 4)
        test_contents = deepcopy(append_to_contents(deepcopy(contents),
                                                    'filename_prefix',
                                                    [''],
                                                    settings_key))
        test_contents = append_to_contents(deepcopy(test_contents),
                                           'filename_suffix',
                                           [''],
                                           settings_key)
        self.assertEqual(test_contents, ret_val_contents)

        # Files having 2 prefix and 1 suffix.
        contents = {'dir_structure': ['some_file.xyz',
                                      'another_one.c',
                                      'my_aweesome_file.yaml',
                                      'some_made_up_thing',
                                      'READEME.md',
                                      'some_other_file',
                                      'some_random_string',
                                      'another_file_just_for_prefix',
                                      'another_random_string']}
        ret_val_contents = check_filename_prefix_postfix(deepcopy(contents),
                                                         3, 3)
        test_contents = deepcopy(append_to_contents(deepcopy(contents),
                                                    'filename_prefix',
                                                    ['some_', 'another_'],
                                                    settings_key))
        test_contents = append_to_contents(deepcopy(test_contents),
                                           'filename_suffix',
                                           ['ing'],
                                           settings_key)
        self.assertEqual(test_contents, ret_val_contents)
