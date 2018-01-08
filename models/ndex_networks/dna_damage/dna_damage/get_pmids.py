import yaml
from indra.literature import pubmed_client

pmids = set()

with open('config.yaml', 'rt') as f:
    config = yaml.load(f)

for term in config['search_terms'] + config['search_genes']:
    term_pmids = pubmed_client.get_ids(term, quoted=True, retmax=100000)
    print("%s: %d PMIDs" % (term, len(term_pmids)))
    pmids |= set(term_pmids)

print()
print("Getting genes")
print()

for gene in config['search_genes']:
    gene_pmids = pubmed_client.get_ids_for_gene(gene, retmax=100000)
    print("%s: %d PMIDs" % (gene, len(gene_pmids)))
    pmids |= set(gene_pmids)

with open('pmids.txt', 'wt') as f:
    for pmid in pmids:
        f.write('%s\n' % pmid)
