import sys

trees = {}
total = 0

for line in sys.stdin:
    species = line.rstrip()
    if not species:
        continue
    
    trees[species] = trees.get(species, 0) + 1
    total += 1

for species in sorted(trees.keys()):
    percentage = (trees[species] / total) * 100
    print(f"{species} {percentage:.4f}")