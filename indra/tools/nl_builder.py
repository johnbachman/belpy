from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import yaml
from indra.sources import trips

try:
    basestring
except NameError:
    basestring = str

class NlBuilder(object):
    """Assembles executable models from mechanisms expressed in natural language.

    Parameters
    ----------
    yaml_files : list or str
        List of file paths to the set of YAML files defining the model. If
        only a single file is to be used, a string may be passed.


    Attributes
    ----------
    yaml_files : list
        List of files used to build the model.
    """
    def __init__(self, yaml_files):
        # Initialize YAML files attribute
        if isinstance(yaml_files, basestring):
            self._yaml_files = [yaml_files]
        elif isinstance(yaml_files, tuple) or isinstance(yaml_files, list):
            self._yaml_files = yaml_files
        else:
            raise ValueError('yaml_files must be a string or list/tuple.')


