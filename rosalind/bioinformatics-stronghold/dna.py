# Counting DNA Nucleotides 

from collections import Counter

with open("data/rosalind_dna.txt") as f:
    s = f.readline().strip()

counts = Counter(s)

print(counts['A'], counts['C'], counts['G'], counts['T'])
