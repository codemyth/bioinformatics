"""problem set one."""


def counting_dna_nucleotides(f):
    """Problem one."""
    """P1. Number of occurrences of a character within a text"""
    """P2. Opening a file and reading its content"""
    input = f.read()
    print('ACGT=' + str(input.count('A')) + ' ' +
          str(input.count('C')) + ' ' +
          str(input.count('G')) + ' ' +
          str(input.count('T')))


def transcribing_dna_into_rna(f):
    """Problem two."""
    """P1. Replace occurrences of a text sequence"""
    input = f.read()
    print(input.replace('T', 'U'))


def rabbit_and_recurrence_relations(generations, offsprings=1):
    return rabbit_generations((1, generations), (0, 1), offsprings)


def rabbit_generations(generation_tuple, population_tuple, offsprings):
    if generation_tuple[0] == generation_tuple[1]:
        return population_tuple[1]
    else:
        new_population_tuple = (
            population_tuple[1],
            population_tuple[1] + population_tuple[0] * offsprings)
        return rabbit_generations(
            (generation_tuple[0] + 1, generation_tuple[1]),
            new_population_tuple, offsprings)
