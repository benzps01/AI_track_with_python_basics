# This was an attempt to test import scripts and using it in another script.
import useful_functions as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print(f"Scores: {scores}")
print(f"Original Mean: {mean}, New Mean: {mean_c}")

# Testing the name of scripts
print(__name__)
print(uf.__name__)
