import os
import re
import collections

def load_enzyme_data(filename):
    with open(enzyme_file) as f:
        lines = f.readlines()
    enzyme_data = collections.OrderedDict()
    enzyme_class = None
    enzyme_entries = []
    for line in lines:
        g = re.match('^ID\s+([0-9\.]+)$', line)
        if g:
            enzyme_class = g.groups()[0]
            enzyme_entries = []
            continue
        if line[0:2] == '//':
            enzyme_data[enzyme_class] = enzyme_entries
            enzyme_class = None
            continue
        if enzyme_class is not None and line[0:2] == 'DR':
            entries = line[2:].strip().split(';')
            for entry in entries:
                if entry:
                    (up_id, up_mnemonic) = entry.strip().split(',')
                    up_id = up_id.strip()
                    up_mnemonic = up_mnemonic.strip()
                    enzyme_entries.append((up_id, up_mnemonic))
    return enzyme_data

def filter_human(enzyme_data):
    human_data = collections.OrderedDict()
    for enz_class, enz_entries in enzyme_data.items():
        human_entries = [e for e in enz_entries if e[1].endswith('_HUMAN')]
        human_data[enz_class] = human_entries
    return human_data

enzyme_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           '../../data/enzyme.dat')
ed = load_enzyme_data(enzyme_file)
hd = filter_human(ed)
