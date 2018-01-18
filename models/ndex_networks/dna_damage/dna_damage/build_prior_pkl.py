import pickle

reach_stmts_file = 'dna_dmg_reach_stmts.pkl'
sparser_stmts_file = 'dna_dmg_sparser_stmts.pkl'

print("Loading pickle files")
with open(reach_stmts_file, 'rb') as f:
    reach_stmts = pickle.load(f)

with open(sparser_stmts_file, 'rb') as f:
    sparser_stmts = pickle.load(f)

num_reach_stmts = len([s for stmt_list in reach_stmts.values()
                     for s in stmt_list])
num_sparser_stmts = len([s for stmt_list in sparser_stmts.values()
                     for s in stmt_list])
print("%d reach stmts" % num_reach_stmts)
print("%d sparser stmts" % num_sparser_stmts)

# Combine by PMID
print("Iterating over reach stmts by PMID")
for pmid, reach_stmt_list in reach_stmts.items():
    if pmid in sparser_stmts:
        sparser_stmts[pmid].extend(reach_stmt_list)
    else:
        sparser_stmts[pmid] = reach_stmt_list

# Sanity check
model = sparser_stmts
model_stmts = len([s for stmt_list in model.values()
                     for s in stmt_list])
assert model_stmts == num_reach_stmts + num_sparser_stmts

# Load database prior
with open('prior_stmts.pkl', 'rb') as f:
    prior_stmts = pickle.load(f)

model['prior'] = prior_stmts

# Save final model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

