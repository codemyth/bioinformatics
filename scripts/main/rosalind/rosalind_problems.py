"""client file to call functions from other modules."""

# from rosalind.problems import group_one
from modules.rosalind import group_two


def main():
    """Main method serving as the entry point to the script file."""

    """count dna nucleotides"""
    # group_one.counting_dna_nucleotides(open(
    # '../data/rosalind/rosalind_dna.txt', 'r'))

    """transcribing dna to rna"""
    # group_one.transcribing_dna_into_rna(open(
    # '../data/rosalind/rosalind_rna.txt', 'r'))
    # print(group_one.rabbit_and_recurrence_relations(5, 3))

    """gc content"""
    with open('../data/rosalind/gc_content.txt') as f:
        group_two.gc_content(f)


if __name__ == "__main__":
    main()
