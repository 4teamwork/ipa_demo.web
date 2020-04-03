from isort import SortImports
import os
import pep8
import unittest


class TestPEP8(unittest.TestCase):

    def test_pep8(self):
        style = pep8.StyleGuide()
        style.options.max_line_length = 125
        filenames = []
        base_path = os.path.abspath(__file__).rstrip(
            'tests/test_style_conventions.py')
        for root, _, files in os.walk(base_path):
            python_files = [f for f in files if f.endswith('.py')]
            for file in python_files:
                filename = '{0}/{1}'.format(root, file)
                filenames.append(filename)
        check = style.check_files(filenames)
        self.assertEqual(
            check.total_errors, 0,
            'PEP8 style errors: {}'.format(check.total_errors))


class TestImportOrdering(unittest.TestCase):

    def test_import_order(self):
        base_path = os.path.abspath(__file__).rstrip(
            'ipa_demo/web/tests/test_style_conventions.py')
        isort_settings = os.path.join(base_path, '.isort.cfg')
        for root, _, files in os.walk(os.path.join(base_path, 'ipa_demo/web')):
            python_files = [f for f in files if f.endswith('.py')]
            for file in python_files:
                file_string = self.get_str_from_file(file)
                isort_obj = SortImports(file_contents=file_string,
                                        check=True,
                                        settings_path=isort_settings)
                self.assertFalse(isort_obj.incorrectly_sorted,
                                 'Import sort error in {}'.format(file))

    @staticmethod
    def get_str_from_file(path):
        with open(path, mode='r') as f_:
            f_.seek(0)
            out = f_.read()
        return out
