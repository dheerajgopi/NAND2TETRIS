import re
final_machine_code = []

# lookup dict for comp instruction
comp_dict = {"0":"0101010", "1":"0111111", "-1":"0111010", "D":"0001100",
            "A":"0110000", "M":"1110000", "!D":"0001101", "!A":"0110001",
            "!M":"1110001", "-D":"0001111", "-A":"0110011", "-M":"1110011",
            "D+1":"0011111", "A+1":"0110111", "M+1":"1110111",
            "D-1":"0001110", "A-1":"0110010", "M-1":"1110010",
            "D+A":"0000010", "D+M":"1000010", "D-A":"0010011",
            "D-M":"1010011", "A-D":"0000111", "M-D":"1000111",
            "D&A":"0000000", "D&M":"1000000", "D|A":"0010101",
            "D|M":"1010101"}

# lookup dict for jmp instruction
jmp_dict = {None:"000", "JGT":"001", "JEQ":"010", "JGE":"011", "JLT":"100",
            "JNE":"101", "JLE":"110", "JMP":"111"}

# lookup dict for dest instruction
dest_dict = {"":"000", "M":"001", "D":"010", "MD":"011", "A":"100",
            "AM":"101", "AD":"110", "AMD":"111"}

# symbol table
symbol_table = {'SP':0, 'LCL':1, 'ARG':2, 'THIS':3, 'THAT':4, 'R0':0,
                'R1':1, 'R2':2, 'R3':3, 'R4':4, 'R5':5, 'R6':6, 'R7':7,
                'R8':8, 'R9':9, 'R10':10, 'R11':11, 'R12':12, 'R13':13,
                'R14':14, 'R15':15, 'SCREEN':16384, 'KBD':24576}

# removing all whitespace. Returns a list of assembly instructions
def codelist(asmfile):
    with open(asmfile) as asm_file:
        codelist = []   # list for storing instruc after cmt is removed
        for line in asm_file:
            # removing whitespace chars
            inst_with_cmt = re.split(r"//", line)
            instruction = re.sub("\n|\r|\t| ", "", inst_with_cmt[0])
            if instruction != "":
                codelist.append(instruction)
    return codelist

# parse 1 for identifying symbols
def handle_labels(codelist):
    instructions = []
    next_line = 0
    for line in codelist:
        if line[0] == "(" and line[-1] == ")":
            label_name = line[1:-1]
            symbol_table[label_name] = next_line
        next_line += 1
        instructions.append(line)
    return instructions

# for identifying instructionn type (a or c)
def which_instruction(code):
    for line in code:
        if line[0] == '@':
            a_instruction(line)
        else:
            c_instruction(line)
    return final_machine_code

# a-instruction -> machine code
def a_instruction(code):
    code_2_binary = "{0:015b}".format(int(code[1:]))
    a_inst = "0" + code_2_binary
    final_machine_code.append(a_inst)

# c-instruction -> machine code
def c_instruction(code):
    if "=" in code:
        split_inst = code.split("=")
        dest = split_inst[0]
        code = split_inst[1]

    else:
        dest = None

    if ";" in code:
        split_inst = code.split(";")
        comp = split_inst[0]
        jmp = split_inst[1]

    else:
        comp = code
        jmp = None

    comp_code = comp_dict[comp]
    dest_code = dest_dict[dest]
    jmp_code = jmp_dict[jmp]
    c_inst = "111" + comp_code + dest_code + jmp_code
    final_machine_code.append(c_inst)

a = codelist("code.asm")
print a
b = which_instruction(a)
print b
with open("code.hack", "w") as hack_file:
    for line in b:
        hack_file.write(line + "\n")
