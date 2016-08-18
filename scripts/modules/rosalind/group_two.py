"""problem set one."""

from stage import fasta_reader


def gc_content(f):

    input = fasta_reader.translate_fasta_file(f)

    [print(item[0], compute_gc_percent(item[1])) for item in input]


def compute_gc_percent(sequence):
    gc = sum(sequence.count(x) for x in ('G', 'C'))
    return 100 * (gc / len(sequence))
