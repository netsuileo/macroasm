# import re
import sys

helpstring = """macroasm.py - an utility for creating i80 code from macrolanguage
usage: macroasm.py [keys] [input file] [output file]
example: macroasm.py code.txt out.i80
keys:
    --lang - returns macrolanguage help
    --help - returns this message \
"""
langstring = """Soon!"""


def parse_cmd_line():
    """Takes arguments from command line and returns input and output filenames
    or prints help or language help, if keys --help or --lang were passed
    """
    if len(sys.argv) < 2:
        print "Too less arguments.\n" + helpstring
        sys.exit()
    if sys.argv[1] == "--help":
        print helpstring
        sys.exit()
    elif sys.argv[1] == "--lang":
        print langstring
        sys.exit()
    elif len(sys.argv) < 3:
        print "Too less arguments.\n" + helpstring
        sys.exit()
    else:
        return sys.argv[1:]


lexeme_patterns = {
    'addr [0-9a-fA-F]+\:': 'block_begin',
    'end': 'end',
    '[a-zA-Z]+\:': 'label',
}


def parse(str):
    pass


def generate(lexemes):
    pass


def main():
    filenames = parse_cmd_line()
    with open(filenames[0], 'r') as inp, open(filenames[1], 'w') as out:
        parsed = parse(inp.read())
        generated = generate(parsed)
        out.write(generated)

if __name__ == "__main__":
    main()
