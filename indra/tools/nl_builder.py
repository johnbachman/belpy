from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
import logging
import yaml
from indra.sources import trips


try:
    basestring
except NameError:
    basestring = str


logger = logging.getLogger('NlBuilder')


class NlBuilder(object):
    """Assembles executable models from mechanisms in natural language.

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
        # Initialize the YAML files as an ordered list of modules
        self.modules = []
        for yaml_file in self._yaml_files:
            with open(yaml_file, 'rt') as f:
                yaml_dict = yaml.load(f)
            self.modules.append(NlModule(yaml_dict))

    def all_sentences(self):
        sentences = []
        for mod in self.modules:
            sentences.extend(mod.all_sentences())
        return sentences


class NlModule(object):
    def __init__(self, yaml_dict):
        # Assign module values based on the YAML entries
        self.name = yaml_dict.get('name')
        self.description = yaml_dict.get('description')
        self.units = yaml_dict.get('units')
        self.submodules = yaml_dict.get('modules')
        self.sentences = yaml_dict.get('sentences')
        if self.submodules is None and self.sentences is None:
            raise ValueError("A module must contain either submodules or "
                             "sentences.")
        elif self.submodules is not None and self.sentences is not None:
            raise ValueError("A module cannot contain both submodules and "
                             "sentences.")
        # Process any submodules recursively
        elif self.submodules is not None:
            self.submodules = [NlModule(submod) for submod in self.submodules]
        # Process sentences
        elif self.sentences is not None:
            self.sentences = [NlSentence(s) for s in self.sentences]

    def all_sentences(self):
        """Recursively collect sentences from this module or any submodules.

        Returns
        -------
        list of NlSentence
            List of sentences in this module or any submodules.
        """
        if self.submodules is not None:
            sentences = []
            for mod in self.submodules:
                sentences.extend(mod.all_sentences())
            return sentences
        elif self.sentences is not None:
            return self.sentences


class NlSentence(object):
    def __init__(self, yaml_dict):
        self.text = yaml_dict['text']
        self.policy = yaml_dict.get('policy')
        self.parameters = yaml_dict.get('parameters')
        self.statements = None

