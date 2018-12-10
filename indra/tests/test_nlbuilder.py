from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from os.path import abspath, join, dirname
from nose.tools import raises
from indra.tools.nl_builder import NlBuilder, NlModule

test_data_dir = join(dirname(abspath(__file__)), 'nl_builder_test_data')

def test_constructor():
    nlb = NlBuilder([])


def test_load_yaml():
    filename = join(test_data_dir, 'apoptosis.yaml')
    nlb = NlBuilder([filename])
    assert nlb._yaml_files == [join(test_data_dir, 'apoptosis.yaml')]


@raises(ValueError)
def test_invalid_yaml():
    nlb = NlBuilder(5)


def test_load_module():
    filename = join(test_data_dir, 'apoptosis.yaml')
    nlm = NlModule(filename)


@raises(ValueError)
def test_invalid_sent_and_submod():
    """A module YAML file should not contain both sentences and submodules."""
    filename = join(test_data_dir, 'sentences_and_submodules.yaml')
    nlm = NlModule(filename)
