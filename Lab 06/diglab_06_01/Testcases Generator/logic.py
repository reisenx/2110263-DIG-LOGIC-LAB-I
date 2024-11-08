# Binary Number
bin = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
bin2dec = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': '10', '1011': '11', '1100': '12', '1101': '13', '1110': '14', '1111': '15'}

# Logic gates
def NOT(a):
    return str(int(not int(a)))
def AND(a,b):
    return str(int(int(a) and int(b)))
def OR(a,b):
    return str(int(int(a) or int(b)))
def NAND(a,b):
    return NOT(AND(a,b))
def NOR(a,b):
    return NOT(OR(a,b))
def XOR(a,b):
    return str(int(int(a) != int(b)))
def XNOR(a,b):
    return str(int(int(a) == int(b)))

# Generate logic testcases
# Open file in write mode
file = open("logic1.txt", "w")
file.write("A B M S F\n")

# NOT Gate (S = 0)
for A in bin:
    result = ""
    for i in range(4):
        result += NOT(A[i])
    file.write(bin2dec[A] + " 0 0 0 " + bin2dec[result] + "\n")
# NAND Gate (S = 1)
for A in bin:
    for B in bin:
        result = ""
        for i in range(4):
            result += NAND(A[i],B[i])
        file.write(bin2dec[A] + " " + bin2dec[B] + " 0 1 " + bin2dec[result] + "\n")
# NOR Gate (S = 2)
for A in bin:
    for B in bin:
        result = ""
        for i in range(4):
            result += NOR(A[i],B[i])
        file.write(bin2dec[A] + " " + bin2dec[B] + " 0 2 " + bin2dec[result] + "\n")
# XNOR Gate (S = 3)
for A in bin:
    for B in bin:
        result = ""
        for i in range(4):
            result += XNOR(A[i],B[i])
        file.write(bin2dec[A] + " " + bin2dec[B] + " 0 3 " + bin2dec[result] + "\n")

# Close the file
file.close()

# Open file in write mode
file = open("logic2.txt", "w")
file.write("A B M S F\n")

# AND Gate (S = 4)
for A in bin:
    for B in bin:
        result = ""
        for i in range(4):
            result += AND(A[i],B[i])
        file.write(bin2dec[A] + " " + bin2dec[B] + " 0 4 " + bin2dec[result] + "\n")
# OR Gate (S = 5)
for A in bin:
    for B in bin:
        result = ""
        for i in range(4):
            result += OR(A[i],B[i])
        file.write(bin2dec[A] + " " + bin2dec[B] + " 0 5 " + bin2dec[result] + "\n")
# A AND NOT(B) (S = 6)
for A in bin:
    for B in bin:
        result = ""
        for i in range(4):
            result += AND(A[i],NOT(B[i]))
        file.write(bin2dec[A] + " " + bin2dec[B] + " 0 6 " + bin2dec[result] + "\n")
# A (S = 7)
for A in bin:
    file.write(bin2dec[A] + " 0 0 7 " + bin2dec[A] + "\n")

# Close the file
file.close()