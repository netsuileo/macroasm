import re

commands = [
    {
        "pattern": re.compile("^NOP$"),
        "code": 0x0,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^STAX B$"),
        "code": 0x2,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^INX B$"),
        "code": 0x3,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^INR B$"),
        "code": 0x4,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^DCR B$"),
        "code": 0x5,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RLC$"),
        "code": 0x7,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^\*$"),
        "code": 0x8,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^DAD B$"),
        "code": 0x9,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^LDAX B$"),
        "code": 0xa,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^DCX B$"),
        "code": 0xb,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^INR C$"),
        "code": 0xc,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^DCR C$"),
        "code": 0xd,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RRC$"),
        "code": 0xf,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^\*$"),
        "code": 0x10,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^STAX D$"),
        "code": 0x12,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^INX D$"),
        "code": 0x13,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^INR D$"),
        "code": 0x14,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^DCR D$"),
        "code": 0x15,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RAL$"),
        "code": 0x17,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^\*$"),
        "code": 0x18,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^DAD D$"),
        "code": 0x19,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^LDAX D$"),
        "code": 0x1a,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^DCX D$"),
        "code": 0x1b,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^INR E$"),
        "code": 0x1c,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^DCR E$"),
        "code": 0x1d,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RAR$"),
        "code": 0x1f,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^\*$"),
        "code": 0x20,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^INX H$"),
        "code": 0x23,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^INR H$"),
        "code": 0x24,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^DCR H$"),
        "code": 0x25,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^DAA$"),
        "code": 0x27,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^\*$"),
        "code": 0x28,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^DAD H$"),
        "code": 0x29,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^DCX H$"),
        "code": 0x2b,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^INR L$"),
        "code": 0x2c,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^DCR L$"),
        "code": 0x2d,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^CMA$"),
        "code": 0x2f,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^\*$"),
        "code": 0x30,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^INX SP$"),
        "code": 0x33,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^INR M$"),
        "code": 0x34,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^DCR M$"),
        "code": 0x35,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^STC$"),
        "code": 0x37,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^\*$"),
        "code": 0x38,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^DAD SP$"),
        "code": 0x39,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^DCX SP$"),
        "code": 0x3b,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^INR A$"),
        "code": 0x3c,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^DCR A$"),
        "code": 0x3d,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^CMC$"),
        "code": 0x3f,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV B,B$"),
        "code": 0x40,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV B,C$"),
        "code": 0x41,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV B,D$"),
        "code": 0x42,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV B,E$"),
        "code": 0x43,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV B,H$"),
        "code": 0x44,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV B,L$"),
        "code": 0x45,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV B,M$"),
        "code": 0x46,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV B,A$"),
        "code": 0x47,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV C,B$"),
        "code": 0x48,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV C,C$"),
        "code": 0x49,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV C,D$"),
        "code": 0x4a,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV C,E$"),
        "code": 0x4b,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV C,H$"),
        "code": 0x4c,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV C,L$"),
        "code": 0x4d,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV C,M$"),
        "code": 0x4e,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV C,A$"),
        "code": 0x4f,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV D,B$"),
        "code": 0x50,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV D,C$"),
        "code": 0x51,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV D,D$"),
        "code": 0x52,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV D,E$"),
        "code": 0x53,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV D,H$"),
        "code": 0x54,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV D,L$"),
        "code": 0x55,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV D,M$"),
        "code": 0x56,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV D,A$"),
        "code": 0x57,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV E,B$"),
        "code": 0x58,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV E,C$"),
        "code": 0x59,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV E,D$"),
        "code": 0x5a,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV E,E$"),
        "code": 0x5b,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV E,H$"),
        "code": 0x5c,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV E,L$"),
        "code": 0x5d,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV E,M$"),
        "code": 0x5e,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV E,A$"),
        "code": 0x5f,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV H,B$"),
        "code": 0x60,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV H,C$"),
        "code": 0x61,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV H,D$"),
        "code": 0x62,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV H,E$"),
        "code": 0x63,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV H,H$"),
        "code": 0x64,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV H,L$"),
        "code": 0x65,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV H,M$"),
        "code": 0x66,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV H,A$"),
        "code": 0x67,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV L,B$"),
        "code": 0x68,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV L,C$"),
        "code": 0x69,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV L,D$"),
        "code": 0x6a,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV L,E$"),
        "code": 0x6b,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV L,H$"),
        "code": 0x6c,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV L,L$"),
        "code": 0x6d,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV L,M$"),
        "code": 0x6e,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV L,A$"),
        "code": 0x6f,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV M,B$"),
        "code": 0x70,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV M,C$"),
        "code": 0x71,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV M,D$"),
        "code": 0x72,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV M,E$"),
        "code": 0x73,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV M,H$"),
        "code": 0x74,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV M,L$"),
        "code": 0x75,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^HLT$"),
        "code": 0x76,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV M,A$"),
        "code": 0x77,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV A,B$"),
        "code": 0x78,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV A,C$"),
        "code": 0x79,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV A,D$"),
        "code": 0x7a,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV A,E$"),
        "code": 0x7b,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV A,H$"),
        "code": 0x7c,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV A,L$"),
        "code": 0x7d,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV A,M$"),
        "code": 0x7e,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MOV A,A$"),
        "code": 0x7f,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ADD B$"),
        "code": 0x80,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ADD C$"),
        "code": 0x81,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ADD D$"),
        "code": 0x82,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ADD E$"),
        "code": 0x83,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ADD H$"),
        "code": 0x84,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ADD L$"),
        "code": 0x85,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ADD M$"),
        "code": 0x86,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ADD A$"),
        "code": 0x87,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ADC B$"),
        "code": 0x88,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ADC C$"),
        "code": 0x89,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ADC D$"),
        "code": 0x8a,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ADC E$"),
        "code": 0x8b,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ADC H$"),
        "code": 0x8c,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ADC L$"),
        "code": 0x8d,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ADC M$"),
        "code": 0x8e,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ADC A$"),
        "code": 0x8f,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^SUB B$"),
        "code": 0x90,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^SUB C$"),
        "code": 0x91,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^SUB D$"),
        "code": 0x92,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^SUB E$"),
        "code": 0x93,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^SUB H$"),
        "code": 0x94,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^SUB L$"),
        "code": 0x95,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^SUB M$"),
        "code": 0x96,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^SUB A$"),
        "code": 0x97,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^SBB B$"),
        "code": 0x98,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^SBB C$"),
        "code": 0x99,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^SBB D$"),
        "code": 0x9a,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^SBB E$"),
        "code": 0x9b,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^SBB H$"),
        "code": 0x9c,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^SBB L$"),
        "code": 0x9d,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^SBB M$"),
        "code": 0x9e,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^SBB A$"),
        "code": 0x9f,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ANA B$"),
        "code": 0xa0,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ANA C$"),
        "code": 0xa1,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ANA D$"),
        "code": 0xa2,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ANA E$"),
        "code": 0xa3,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ANA H$"),
        "code": 0xa4,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ANA L$"),
        "code": 0xa5,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ANA M$"),
        "code": 0xa6,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ANA A$"),
        "code": 0xa7,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^XRA B$"),
        "code": 0xa8,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^XRA C$"),
        "code": 0xa9,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^XRA D$"),
        "code": 0xaa,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^XRA E$"),
        "code": 0xab,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^XRA H$"),
        "code": 0xac,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^XRA L$"),
        "code": 0xad,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^XRA M$"),
        "code": 0xae,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^XRA A$"),
        "code": 0xaf,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ORA B$"),
        "code": 0xb0,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ORA C$"),
        "code": 0xb1,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ORA D$"),
        "code": 0xb2,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ORA E$"),
        "code": 0xb3,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ORA H$"),
        "code": 0xb4,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ORA L$"),
        "code": 0xb5,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ORA M$"),
        "code": 0xb6,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^ORA A$"),
        "code": 0xb7,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^CMP B$"),
        "code": 0xb8,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^CMP C$"),
        "code": 0xb9,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^CMP D$"),
        "code": 0xba,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^CMP E$"),
        "code": 0xbb,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^CMP H$"),
        "code": 0xbc,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^CMP L$"),
        "code": 0xbd,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^CMP M$"),
        "code": 0xbe,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^CMP A$"),
        "code": 0xbf,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RNZ$"),
        "code": 0xc0,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^POP B$"),
        "code": 0xc1,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^PUSH B$"),
        "code": 0xc5,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RST 0$"),
        "code": 0xc7,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RZ$"),
        "code": 0xc8,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RET$"),
        "code": 0xc9,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^\*$"),
        "code": 0xcb,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RST 8$"),
        "code": 0xcf,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RNC$"),
        "code": 0xd0,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^POP D$"),
        "code": 0xd1,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^PUSH D$"),
        "code": 0xd5,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RST 16$"),
        "code": 0xd7,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RC$"),
        "code": 0xd8,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^\*$"),
        "code": 0xd9,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^\*$"),
        "code": 0xdd,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RST 24$"),
        "code": 0xdf,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RPO$"),
        "code": 0xe0,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^POP H$"),
        "code": 0xe1,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^XTHL$"),
        "code": 0xe3,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^PUSH H$"),
        "code": 0xe5,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RST 32$"),
        "code": 0xe7,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RPE$"),
        "code": 0xe8,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^PCHL$"),
        "code": 0xe9,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^XCHG$"),
        "code": 0xeb,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^\*$"),
        "code": 0xed,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RST 40$"),
        "code": 0xef,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RP$"),
        "code": 0xf0,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^POP PSW$"),
        "code": 0xf1,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^DI$"),
        "code": 0xf3,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^PUSH PSW$"),
        "code": 0xf5,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RST 48$"),
        "code": 0xf7,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RM$"),
        "code": 0xf8,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^SPHL$"),
        "code": 0xf9,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^EI$"),
        "code": 0xfb,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^\*$"),
        "code": 0xfd,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^RST 56$"),
        "code": 0xff,
        "bytes": 1,
    },
    {
        "pattern": re.compile("^MVI B,[a-fA-F0-9]{1,2}$"),
        "code": 0x6,
        "bytes": 2,
    },
    {
        "pattern": re.compile("^MVI C,[a-fA-F0-9]{1,2}$"),
        "code": 0xe,
        "bytes": 2,
    },
    {
        "pattern": re.compile("^MVI D,[a-fA-F0-9]{1,2}$"),
        "code": 0x16,
        "bytes": 2,
    },
    {
        "pattern": re.compile("^MVI E,[a-fA-F0-9]{1,2}$"),
        "code": 0x1e,
        "bytes": 2,
    },
    {
        "pattern": re.compile("^MVI H,[a-fA-F0-9]{1,2}$"),
        "code": 0x26,
        "bytes": 2,
    },
    {
        "pattern": re.compile("^MVI M,[a-fA-F0-9]{1,2}$"),
        "code": 0x36,
        "bytes": 2,
    },
    {
        "pattern": re.compile("^MVI L,[a-fA-F0-9]{1,2}$"),
        "code": 0x2e,
        "bytes": 2,
    },
    {
        "pattern": re.compile("^MVI A,[a-fA-F0-9]{1,2}$"),
        "code": 0x3e,
        "bytes": 2,
    },
    {
        "pattern": re.compile("^OUT [a-fA-F0-9]{1,2}$"),
        "code": 0xd3,
        "bytes": 2,
    },
    {
        "pattern": re.compile("^IN [a-fA-F0-9]{1,2}$"),
        "code": 0xdb,
        "bytes": 2,
    },
    {
        "pattern": re.compile("^ADI [a-fA-F0-9]{1,2}$"),
        "code": 0xc6,
        "bytes": 2,
    },
    {
        "pattern": re.compile("^SUI [a-fA-F0-9]{1,2}$"),
        "code": 0xd6,
        "bytes": 2,
    },
    {
        "pattern": re.compile("^ANI [a-fA-F0-9]{1,2}$"),
        "code": 0xe6,
        "bytes": 2,
    },
    {
        "pattern": re.compile("^ORI [a-fA-F0-9]{1,2}$"),
        "code": 0xf6,
        "bytes": 2,
    },
    {
        "pattern": re.compile("^ACI [a-fA-F0-9]{1,2}$"),
        "code": 0xce,
        "bytes": 2,
    },
    {
        "pattern": re.compile("^SBI [a-fA-F0-9]{1,2}$"),
        "code": 0xde,
        "bytes": 2,
    },
    {
        "pattern": re.compile("^XRI [a-fA-F0-9]{1,2}$"),
        "code": 0xee,
        "bytes": 2,
    },
    {
        "pattern": re.compile("^CPI [a-fA-F0-9]{1,2}$"),
        "code": 0xfe,
        "bytes": 2,
    },

    {
        "pattern": re.compile("^LXI B,(0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0x01,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^LXI D,(0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0x11,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^LXI H,(0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0x21,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^SHLD (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0x22,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^LHLD (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0x2a,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^LXI SP,(0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0x31,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^STA (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0x32,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^LDA (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0x3a,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^JNZ (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0xc2,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^JMP (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0xc3,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^CNZ (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0xc4,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^JZ (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0xca,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^CZ (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0xcc,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^CALL (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0xcd,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^JNC (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0xd2,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^CNC (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0xd4,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^JC (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0xda,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^CC (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0xdc,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^JPO (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0xe2,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^CPO (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0xe4,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^JPE (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0xea,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^CPE (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0xec,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^JP (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0xf2,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^CP (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0xf4,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^JM (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0xfa,
        "bytes": 3,
    },
    {
        "pattern": re.compile("^CM (0x[a-fA-F0-9]{1,4}|[a-zA-Z0-9]+)$"),
        "code": 0xfc,
        "bytes": 3,
    },
]
