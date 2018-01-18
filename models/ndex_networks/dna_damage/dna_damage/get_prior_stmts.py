import yaml
import pickle
from indra.tools import gene_network
from indra.sources import bel
from indra.tools import assemble_corpus as ac

with open('config.yaml', 'rt') as f:
    config = yaml.load(f)
genes = config['search_genes']
# Biopax
gn = gene_network.GeneNetwork(genes, 'dna_dmg_prior')
biopax_stmts = gn.get_biopax_stmts()
# BEL
bel_file = '../../../../data/large_corpus_nodelink.json'
pbp = bel.process_json_file(bel_file)

prior_stmts = ac.filter_direct(biopax_stmts + pbp.statements)
prior_stmts = ac.filter_gene_list(prior_stmts, genes, policy='one')
with open('prior_stmts.pkl', 'wb') as f:
    pickle.dump(prior_stmts, f)

