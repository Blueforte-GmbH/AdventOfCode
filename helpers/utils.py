def open_inputs(inputfile):
    with open(inputfile) as file:
        lines = [line.split() for line in file]
        return lines        



def open_lines(inputfile):
    with open(inputfile) as file:
        lines = [line.strip().split() for line in file]
        return lines  