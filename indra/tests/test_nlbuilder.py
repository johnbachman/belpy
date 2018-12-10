from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from os.path import abspath, join, dirname
from indra.tools.nl_builder import NlBuilder

test_data_dir = join(dirname(abspath(__file__)), 'nl_builder_test_data')

def test_constructor():
    nlb = NlBuilder([])

def test_load_yaml():
    filename = join(test_data_dir, 'apoptosis.yml')
    nlb = NlBuilder([filename])
    assert nlb._yaml_files == [join(test_data_dir, 'apoptosis.yml')]

