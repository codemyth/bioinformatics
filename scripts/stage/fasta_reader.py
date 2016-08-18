def translate_fasta_file(file):
    input = file.read()
    return [(sequence[0].split('|'), sequence[2].replace(
        '\n', '')) for sequence in (element.partition(
            '\n') for element in input.split('>')[1:])]


def count_base(sequence, base=None):
    if base is None:
        output = len(sequence[1])
    else:
        output = sequence[1].count(base)
    return output
