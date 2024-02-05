# Complementing a Strand of DNA

with open("data/rosalind_revc.txt") as f:
	s = f.readline().strip()

complements = {
	'A':'T',
	'T':'A',
	'C':'G',
	'G':'C',
}

reverse = ''

for base in s[::-1]:
	reverse += complements[base]
	
print(reverse)