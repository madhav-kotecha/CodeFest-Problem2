# Algo Problem 2 - Telephone Grid
from itertools import permutations
grids = []

with open("input.txt") as inp:		# Opening Input file
	n = int(inp.readline())			
	for i in range(n):    
		grids.append(int(inp.readline().strip()))  
out = open("output.txt","a")	# For writing output

for i in grids:
	elements = []
	for num in range(i-1):		# Defining elements of combinations
		elements.append(num+1)
	possibleCombination = list(permutations(elements))

	combination = [list(l) for l in possibleCombination]
	for c in combination:	# Iterating for all combination of n
		res = [[i]+c]
		for j in range(i-1):
			uniqueSeq = []
			for k in range(i):
				if res[j][k] == 1:
					val=i
				else:
					val=res[j][k]-1
				uniqueSeq.append(val)
			res.append(uniqueSeq)
		out.write(str(res) + "\n")	# Writing output in file