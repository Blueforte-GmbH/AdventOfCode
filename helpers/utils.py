def open_inputs(inputfile):
    with open(inputfile) as file:
        lines = [line.split() for line in file]
        return lines        