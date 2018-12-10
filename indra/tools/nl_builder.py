from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import yaml
from indra.sources import trips

try:
    basestring
except NameError:
    basestring = str

class NlBuilder(object):
    def __init__(self, yaml_files):
        if isinstance(yaml_files, basestring):
            self._yaml_files = [yaml_files]
        elif isinstance(yaml_files, tuple) or isinstance(yaml_files, list):
            self._yaml_files = yaml_files
