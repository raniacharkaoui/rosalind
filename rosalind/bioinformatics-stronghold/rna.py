# Transcribing DNA into RNA

with open("data/rosalind_rna.txt") as f:
    s = f.readline().strip()

print(s.replace('T','U'))