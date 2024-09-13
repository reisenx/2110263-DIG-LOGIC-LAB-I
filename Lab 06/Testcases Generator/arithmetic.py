# Binary Number
bin = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
singed = [0,1,2,3,4,5,6,7,-8,-7,-6,-5,-4,-3,-2,-1]
dec = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
bin2dec = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': '10', '1011': '11', '1100': '12', '1101': '13', '1110': '14', '1111': '15'}
singed2dec = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, -8: 8, -7: 9, -6: 10, -5: 11, -4: 12, -3: 13, -2: 14, -1: 15}

# Generate arithmetic testcases
# Open file in write mode
file = open("arithmetic.txt", "w")
file.write("A B C M S F\n")

# A+C (S = 0)
for A in singed:
    for C in range(2):
        if(-8 <= A+C <= 7):
            file.write(str(singed2dec[A]) + " 0 " + str(singed2dec[C]) + " 1 0 " + str(singed2dec[A+C]) + "\n")
# A-1+C (S = 1)
for A in singed:
    for C in range(2):
        if(-8 <= A-1+C <= 7):
            file.write(str(singed2dec[A]) + " 0 " + str(singed2dec[C]) + " 1 1 " + str(singed2dec[A-1+C]) + "\n")
# A+B+C (S = 2)
for A in singed:
    for B in singed:
        for C in range(2):
            if(-8 <= A+B+C <= 7):
                file.write(str(singed2dec[A]) + " " + str(singed2dec[B]) + " " + str(singed2dec[C]) + " 1 2 " + str(singed2dec[A+B+C]) + "\n")
# A-B-1+C (S = 3)
for A in singed:
    for B in singed:
        for C in range(2):
            if(-8 <= A-B-1+C <= 7):
                file.write(str(singed2dec[A]) + " " + str(singed2dec[B]) + " " + str(singed2dec[C]) + " 1 3 " + str(singed2dec[A-B-1+C]) + "\n")
# -A-1+C (S = 4)
for A in singed:
    for C in range(2):
        if(-8 <= -A-1+C <= 7):
            file.write(str(singed2dec[A]) + " 0 " + str(singed2dec[C]) + " 1 4 " + str(singed2dec[-A-1+C]) + "\n")
# B+C (S = 5)
for B in singed:
    for C in range(2):
        if(-8 <= B+C <= 7):
            file.write("0 " + str(singed2dec[B]) + " "  + str(singed2dec[C]) + " 1 5 " + str(singed2dec[B+C]) + "\n")
# Shift A left one bit (S = 6)
for A in bin:
    result = A[1:] + "0"
    file.write(bin2dec[A] + " 0 0 1 6 " + bin2dec[result] + "\n")
# Shift A left one bit (S = 7)
for A in bin:
    result = "0" + A[0:3]
    file.write(bin2dec[A] + " 0 0 1 7 " + bin2dec[result] + "\n")

# Close the file
file.close()