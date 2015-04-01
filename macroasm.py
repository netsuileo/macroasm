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

label_pattern = re.compile('[a-zA-Z0-9_]+\:')

addr_pattern = re.compile('0x[a-fA-F0-9]{1,4}')


class Lex:
    """Class that represents a lexeme"""
    def __init__(self):
        self.lextype = ''
        self.addr = 0x0
        self.label = ''
        self.body = ''
        self.cmdtype = ''

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
    def make_cmd_lex(cmd, cmdtype):
        """Makes a lexeme for cmd"""
        lex = Lex()
        lex.lextype = 'cmd'
        lex.body = cmd
        lex.cmdtype = cmdtype
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
            'addr': "type: addr    addr: " + hex(self.addr),
            'end': "type: end",
            'label': "type: label   label: " + self.label,
            'cmd': "type: cmd     cmd: " + self.body,
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


def get_cmd_type(line):
    """Checks is line a valid cmd string"""
    cmd = line.strip()
    for command in commands:
        if command['pattern'].match(cmd):
            return command
    return None


def get_lex(line):
    """Makes a lexeme object from input string"""
    cmdtype = get_cmd_type(line)
    if cmdtype:
        return Lex.make_cmd_lex(line, cmdtype)
    parts = line.lower().strip().split(' ')
    if len(parts) == 1:
        if parts[0] == 'end':
            return Lex.make_end_lex()
        if label_pattern.match(parts[0]):
            return Lex.make_label_lex(parts[0][:-1])
    if len(parts) == 2:
        if parts[0] == 'addr' and addr_pattern.match(parts[1]):
            return Lex.make_addr_lex(int(parts[1], 16))
    return Lex.make_unknown_lex(line)


def parse(string):
    """Converts input code to list of lexemes"""
    lines = string.split('\n')
    return [get_lex(line.strip()) for line in lines if line != '']


def generate(lexemes):
    """Generates asm code from list of lexemes"""
    # TODO
    # 1) Give an address to every lexeme: OK
    # 2) Make a table of lables. Give an address to every label: OK
    # 3) Convert every label in lexemes list to address
    # 4) Convert every lexeme and its address to byte form
    # 5) Return bytes in hex form

    # Preparation for generation
    addr_counter = 0
    was_addr = False
    labels = {}
    for lexeme in lexemes:
        if lexeme.lextype == 'end':
            if was_addr:
                was_addr = False
            else:
                raise Exception("Unexpexted end of non-existent address block")
        elif lexeme.lextype == 'addr':
            if was_addr:
                raise Exception("Unexpected begin of address block in existing address block")
            else:
                addr_counter = lexeme.addr
                was_addr = True
        elif lexeme.lextype == 'label':
            if lexeme.label in labels.keys():
                raise Exception("Multiple lables with the same name: " + lexeme.label)
            else:
                labels[lexeme.label] = addr_counter
        elif lexeme.lextype == 'cmd':
            lexeme.addr = addr_counter
            addr_counter += lexeme.cmdtype['bytes']
        elif lexeme.lextype == 'unknown':
            raise Exception("Input lexeme is wrong: " + lexeme.body)
        else:
            raise Exception("Wrong type of lexeme: " + lexeme.lextype + ". \
                Probably, you did something wrong changing code of this file. \
                Don't worry, everything will be OK... or not :)")
    # Generation
    generated = ""
    for lexeme in lexemes:
        if lexeme.lextype == 'cmd':
            cmd_bytes = lexeme.cmdtype['bytes']
            addr = lexeme.addr
            code = format(lexeme.cmdtype['code'], 'x')
            if cmd_bytes == 3:
                # Print addr, code and target addr in 2 bytes
                label_or_addr = re.split(',| ', lexeme.body)[-1]
                arg = labels.get(label_or_addr, None)
                if not arg:
                    arg = int(label_or_addr, 16)
                arg_fst_byte = format(arg & 0x00ff, 'x')
                arg_sec_byte = format((arg & 0xff00) >> 0x8, 'x')
                generated += str(addr) + " " + code + "\n"
                generated += str(addr+1) + " " + arg_fst_byte + "\n"
                generated += str(addr+2) + " " + arg_sec_byte + "\n"
            elif cmd_bytes == 2:
                # Print addr, code and value
                arg_byte = re.split(',| ', lexeme.body)[-1]
                generated += str(addr) + " " + code + "\n"
                generated += str(addr+1) + " " + arg_byte + "\n"
            elif cmd_bytes == 1:
                generated += str(addr) + " " + code + "\n"
        elif lexeme.lextype == 'addr':
            generated += str(lexeme.addr) + '\n'
    return generated


def main():
    filenames = parse_cmd_line()
    with open(filenames[0], 'r') as inp, open(filenames[1], 'w') as out:
        parsed = parse(inp.read())
        for lex in parsed:
            print lex
        out.write(generate(parsed))

if __name__ == "__main__":
    main()
