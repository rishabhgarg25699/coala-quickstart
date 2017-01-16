import inspect
import types
import unittest

from tests.test_bears.AllKindsOfSettingsDependentBear import (
    AllKindsOfSettingsDependentBear)
from coala_quickstart.generation.Utilities import (
    get_default_args, get_all_args,
    search_for_orig, get_language_from_hashbang)


def foo():
    pass


def foo_bar(n):
    def bar():
        return n+1
    return bar


class TestAdditionalFunctions(unittest.TestCase):

    def second(func):
        def wrapper():
            return func()
        return wrapper

    def first():
        pass

    third = second(first)
    fourth = second(second(first))

    def test_search_for_orig(self):
        self.assertEqual(types.MethodType(search_for_orig(self.third, 'first'),
                                          self), self.first)
        self.assertEqual(types.MethodType(search_for_orig(self.fourth,
                                                          'first'),
                                          self), self.first)
        self.assertEqual(search_for_orig(self.first, 'first'), None)
        self.assertEqual(search_for_orig(self.first, "bar"), None)
        self.assertEqual(search_for_orig(self.first, "first"), None)
        # function without closure
        self.assertEqual(search_for_orig(foo, "bar"), None)
        self.assertEqual(search_for_orig(foo, "foo"), None)
        func = foo_bar(3)
        x = func()  # function with closure
        self.assertEqual(search_for_orig(func, "bar"), None)

    def test_get_default_args(self):
        self.assertEqual(get_default_args(AllKindsOfSettingsDependentBear.run),
                         {'chars': False,
                          'dependency_results': {},
                          'max_line_lengths': 1000,
                          'no_chars': 79,
                          'use_spaces': None,
                          'use_tabs': False})

    def test_get_all_args(self):
        empty = inspect._empty
        self.assertEqual(get_all_args(AllKindsOfSettingsDependentBear.run),
                         {'self': empty, 'file': empty, 'filename': empty,
                          'configs': empty,
                          'use_bears': empty, 'no_lines': empty,
                          'use_spaces': None,
                          'use_tabs': False, 'max_line_lengths': 1000,
                          'no_chars': 79,
                          'chars': False, 'dependency_results': {}})

    def test_get_language_from_hashbang(self):
        self.assertEqual(get_language_from_hashbang('#!/usr/bin/env python'),
                         'python')
        self.assertEqual(get_language_from_hashbang('#!bin/bash'),
                         'bash')
