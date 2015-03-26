import sys
import re
from commands import commands

helpstring = """macroasm.py - an utility for translating special
macrolanguage code to i80 code.
usage: macroasm.py [keys] [input file] [output file]
example: macroasm.py code.txt out.i80
keys:
    --lang - returns macrolanguage help
    --help - returns this message \
"""
langstring = """Soon!"""

label_pattern = re.compile('[a-zA-Z0-9]+\:')
addr_pattern = re.compile('[a-fA-F0-9]{4}')


class Lex:
    """Class that represents a lexeme"""
    def __init__(self):
        self.lextype = ''
        self.addr = ''
        self.label = ''
        self.cmd = ''
        self.body = ''

    @staticmethod
    def make_addr_lex(addr):
        """Makes a lexeme for addr"""
        lex = Lex()
        lex.lextype = 'addr'
        lex.addr = addr
        return lex

    @staticmethod
    def make_end_lex():
        """Makes a lexeme for end"""
        lex = Lex()
        lex.lextype = 'end'
        return lex

    @staticmethod
    def make_label_lex(label_name):
        """Makes a lexeme for label"""
        lex = Lex()
        lex.lextype = 'label'
        lex.label = label_name
        return lex

    @staticmethod
    def make_cmd_lex(cmd):
        """Makes a lexeme for cmd"""
        lex = Lex()
        lex.lextype = 'cmd'
        lex.cmd = cmd
        return lex

    @staticmethod
    def make_unknown_lex(lex_str):
        """Makes a lexeme for unknown lexeme"""
        lex = Lex()
        lex.lextype = 'unknown'
        lex.body = lex_str
        return lex

    def __str__(self):
        return {
            'addr': "type: addr    addr: " + self.addr,
            'end': "type: end",
            'label': "type: label   label: " + self.label,
            'cmd': "type: cmd     cmd: " + self.cmd,
            'unknown': "type: unknown   body: " + self.body,
        }.get(self.lextype, None)


def parse_cmd_line():
    """Takes arguments from command line and returns input and output filenames
    or prints help or language help, if keys --help or --lang were passed"""
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


def is_line_a_cmd(line):
    """Checks is line a valid cmd string"""
    cmd = line.strip()
    for command in commands:
        if command['pattern'].match(cmd):
            return True
    return False


def get_lex(line):
    """Makes a lexeme object from input string"""
    parts = line.lower().strip().split(' ')
    if parts[0] == 'addr':
        if addr_pattern.match(parts[1]):
            return Lex.make_addr_lex(parts[1])
    elif parts[0] == 'end':
        return Lex.make_end_lex()
    elif label_pattern.match(parts[0]):
        return Lex.make_label_lex(parts[0])
    elif is_line_a_cmd(line):
        return Lex.make_cmd_lex(line)
    else:
        return Lex.make_unknown_lex(line)


def parse(string):
    """Converts input code to list of lexemes"""
    lines = string.split('\n')
    return [get_lex(line) for line in lines if line != '']


def generate(lexemes):
    """Generates asm code from list of lexemes"""
    return "42"


def main():
    filenames = parse_cmd_line()
    with open(filenames[0], 'r') as inp, open(filenames[1], 'w') as out:
        parsed = parse(inp.read())
        for lex in parsed:
            print lex
        out.write(generate(parsed))

if __name__ == "__main__":
    main()
