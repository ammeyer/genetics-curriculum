import random

def random_mutation(subs_rate, ins_rate, del_rate):
	"""
	Uses a random number generator to return a random class of mutation with
	the specified probabilities ('substitution', 'insertion', 'deletion', or
	None). Returns None with probability 1 - (subs_rate + ins_rate + del_rate).
	"""
	r = random.uniform(0,1)
	if r <= subs_rate:
		return 'substitution'
	elif r > subs_rate and r <= subs_rate+ins_rate:
		return 'insertion'
	elif r > subs_rate+ins_rate and r <= subs_rate+ins_rate+del_rate:
		return 'deletion'
	else:
		return None

def random_base():
	"""
	Returns a string representing a random nucleotide base from A, C, T, G.
	"""
	bases = ['A','T','C','G']
	return random.choice(bases)


def mutate_sequence(sequence, subs_rate, ins_rate, del_rate):
	if subs_rate + ins_rate + del_rate > 1:
		print("ERROR: rates must sum to a number between 0 and 1")
		return None

	mutated = ""
	# FILL ME IN!!!
	for char in sequence:
		mutation = random_mutation(subs_rate, ins_rate, del_rate)
		if mutation == None:
			mutated += char
		elif mutation == 'substitution':
			base = random_base()
			mutated += base
		elif mutation == 'insertion':
			mutated += char + random_base()
		else: #deletion
			mutated += ""
	print(mutated)
	return mutated

# mutate_sequence("AAAAAAAAAAAA", 0.00001, 0.0000005, 0.0000005)

def mutate_over_generations(sequence, num_generations, subs_rate=0.00001, ins_rate=0.000005, del_rate=0.000005):
	"""
	Simulates mutating a sequence over num_generations generations and
	returns the mutated sequence.
	"""
	for i in range(num_generations):
		sequence = mutate_sequence(sequence, subs_rate, ins_rate, del_rate)
	return sequence






