# BCD to Seven Segment Decoder (diglab_​03_​01)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1RNgGcbrlr_2TEe9lUSFqrZRoutLsefec/view?usp=drive_link)

---

# Step 1: พิจารณาโจทย์ และเขียน Truth Table

ก่อนอื่นต้องทำความเข้าใจก่อนว่า ใน Seven segment display จะมี แถบ LED ทั้งหมด 8 แถบ แทนเป็นตัวอักษร A-H (แถบ H ไม่ใช้ใน Lab นี้)
- แถบ LED ที่ไม่สว่างจะหมายถึงว่า แถบนั้นๆมีค่าเป็น 0
- แถบ LED ที่สว่างจะหมายถึงว่า แถบนั้นๆมีค่าเป็น 1

**ตัวอย่าง:** การที่จะให้ Seven segment display แสดงผลเลข 4 หมายถึง
- แถบ LED ตัวอักษร A,D,E เป็น 0
- แถบ LED ตัวอักษร B,C,F,G เป็น 1

<img src = "https://github.com/reisenx/2110263-DIG-LOGIC-LAB-I/blob/main/Lab%2003/diglab_03_01/diglab_03_01_pics/diglab_03_01_display.png" width=70% height=70%>

เมื่อทราบหลักการของ Seven segment display แล้ว เราจะสามารถเขียน Truth Table ของการแสดงผลหมายเลขตั้งแต่ 0 ถึง 9 ได้ดังตาราง

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2003/diglab_03_01/diglab_03_01_pics/diglab_03_01_table.png" width=50% height=50%>

---

# Step 2: ใช้งานโปรแกรม ESPRESSO logic minimizer ในการหาสมการ Boolean

## การใช้งานโปรแกรม
การใช้งานโปรแกรม ESPRESSO logic minimizer จะต้องสร้างไฟล์สำหรับ Input และ Output ไว้ก่อน
- ไฟล์ Input จะเป็นไฟล์ที่บรรจุชุดคำสั่งเข้าไป (ไฟล์ `.pla`)
- ไฟล์ Output จะเป็นไฟล์ที่ ESPRESSO logic minimizer จัดเก็บสมการ Boolean หลังจากที่ประมวลผล Input เสร็จสิ้น (ไฟล์ `.pla`)
- แนะนำให้ใช้งาน ESPRESSO logic minimizer แบบ Compile Mode ผ่าน Command Prompt 

## ขั้นตอนการใช้งานโปรแกรม ESPRESSO logic minimizer
1. สร้างไฟล์ Input และไฟล์ Output ผ่าน Text Editor เป็นไฟล์นามสกุล `.pla` (จริงๆ Visual Studio Code ก็ใช้งานได้)
2. กรอก Command line ลงไปในไฟล์ Input แบบในภาพนี้
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2003/diglab_03_01/diglab_03_01_pics/diglab_03_01_input.png" width=80% height=80%>

3. เปิด Command Prompt ไปยัง path ที่อยู่ Folder ที่มีทั้งไฟล์ `.pla` และโปรแกรม `espresso.exe` อยู่ โดยใช้คำสั่งข้างล่างนี้

ถ้าหาก Folder ไม่ได้อยู่ Drive C ให้ทำการเปลี่ยนไดรฟ์ก่อน เช่น ใช้คำสั่ง `D:` เพื่อไปยัง Drive D
แล้วจากนั้นให้ Copy path ของ Folder ผ่าน File Explorer แล้วใช้งานคำสั่งข้างล่างนี้
```
cd [INSERT FOLDER PATH HERE]
```

5. จากนั้นรันคำสั่งข้างนี้ เพื่อให้ ESPRESSO logic minimizer ทำการคำนวณสมการ Boolean และเก็บผลลัพธ์ที่ไฟล์ Output
```
espresso -o eqntott [INSERT INPUT FILE NAME HERE] > [INSERT OUTPUT FILE NAME HERE]
```

6. เปิดไฟล์ Output บน Text Editor ก็จะเห็นผลลัพธ์เป็นสมการ Boolean ดังภาพ
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2003/diglab_03_01/diglab_03_01_pics/diglab_03_01_output.png" width=80% height=80%>


## กรอก Command line ลงในไฟล์ Input
**จากข้อมูลข้างต้น จะทราบว่า**
- ข้อมูล Input ทั้งหมด มีขนาด 4 Bits
- ข้อมูล Output ทั้งหมด มีขนาด 7 Bits
- ตัวแปรในข้อมูล Input ประกอบไปด้วย X3, X2, X1, X0
- ตัวแปรในข้อมูล Output ประกอบไปด้วย A, B, C, D, E, F, G
- จำนวนเคสที่พิจารณามีทั้งหมด 16 เคส ดังตาราง Truth Table ข้างบน

เราจะสามารถกรอกข้อมูลดังกล่าวในรูปของ command line ได้ดังนี้

```
.i 4
.o 7
.ilb X3 X2 X1 X0
.ob A B C D E F G
.p 16
0000 1111110
0001 0110000
0010 1101101
0011 1111001
0100 0110011
0101 1011011
0110 1011111
0111 1110010
1000 1111111
1001 1111011
1010 -------
1011 -------
1100 -------
1101 -------
1110 -------
1111 -------
.e
```
**หมายเหตุ:** ส่วนที่เป็น Don't care ให้ใช้เครื่องหมาย `-` แทนเลข `0` กับ `1` ได้เลย

## ทำความเข้าใจ Output
เบื้องต้นต้องเข้าใจก่อนว่า สมการ Boolean ใน ESPRESSO logic minimizer จะใช้สัญลักษณ์ที่แตกต่างไปจากที่เรียนไปเล็กน้อย
- เครื่องหมาย `&` หมายถึง AND
- เครื่องหมาย `|` หมายถึง OR
- เครื่องหมาย `!` หมายถึง NOT

ซึ่งเมื่อเราใส่ข้อมูลไป แล้วรันด้วย Command Prompt เสร็จสิ้น ผลลัพธ์จะออกมาเป็นลักษณะนี้

```
A = (X2&X1&X0) | (!X2&X1) | (X2&!X1&X0) | (!X2&!X0) | (X2&X1&!X0) | (X3);
B = (!X2&X0) | (!X1&!X0) | (X2&X1&X0) | (!X2&!X0);
C = (!X2&X0) | (!X1&!X0) | (X2&X1&X0) | (X2&!X1&X0) | (X2&X1&!X0);
D = (!X2&X1) | (X2&!X1&X0) | (!X2&!X0) | (X2&X1&!X0) | (X3);
E = (!X2&!X0) | (X2&X1&!X0);
F = (!X1&!X0) | (X2&X1&X0) | (X2&!X1&X0) | (X2&X1&!X0) | (X3);
G = (X2&!X1) | (!X2&X1) | (X2&X1&!X0) | (X3);
```

---

# Step 3: ลดรูปสมการ Boolean ต่อจาก ESPRESSO logic minimizer

เนื่องจากว่า ESPRESSO logic minimizer อาจจะไม่ได้ลดรูปให้อยู่ในรูปอย่างง่ายที่สุด ดังนั้นเราจะมาลดรูปสมการกันต่อ

## Simplification Theorems
- $X + 1 = 1$
- $X \cdot 1 = X$
- $X + X' = 1$
- $XY + XY' = X$
- $X + X'Y = X + Y$

## พิจารณาสมการ Boolean ของ A
```
A = (X2&X1&X0) | (!X2&X1) | (X2&!X1&X0) | (!X2&!X0) | (X2&X1&!X0) | (X3);
```
$A = X_{2}X_{1}X_{0} + X_{2}'X_{1} + X_{2}X_{1}'X_{0} + X_{2}'X_{0}' + X_{2}X_{1}X_{0}' + X_{3}$

$A = (X_{2}X_{1}X_{0} + X_{2}'X_{1}) + X_{2}X_{1}'X_{0} + (X_{2}'X_{0}' + X_{2}X_{1}X_{0}') + X_{3}$

$A = X_{1}(X_{2}X_{0} + X_{2}') + X_{2}X_{1}'X_{0} + X_{0}'(X_{2}' + X_{2}X_{1}) + X_{3}$

$A = X_{1}(X_{2}' + X_{0}) + X_{2}X_{1}'X_{0} + X_{0}'(X_{2}' + X_{1}) + X_{3}$

$A = X_{2}'X_{1} + X_{1}X_{0} + X_{2}X_{1}'X_{0} + X_{2}'X_{0}' + X_{1}X_{0}' + X_{3}$

$A = X_{2}'X_{1} + X_{2}X_{1}'X_{0} + X_{2}'X_{0}' + (X_{1}X_{0}' + X_{1}X_{0}) + X_{3}$

$A = X_{2}'X_{1} + X_{2}X_{1}'X_{0} + X_{2}'X_{0}' + X_{1} + X_{3}$

$A = X_{2}X_{1}'X_{0} + X_{2}'X_{0}' + (X_{1} + X_{2}'X_{1}) + X_{3}$

$A = X_{2}X_{1}'X_{0} + X_{2}'X_{0}' + X_{1}(1 + X_{2}') + X_{3}$

$A = X_{2}X_{1}'X_{0} + X_{2}'X_{0}' + X_{1} \cdot 1 + X_{3}$

$A = X_{2}X_{1}'X_{0} + X_{2}'X_{0}' + X_{1} + X_{3}$

$A = X_{2}'X_{0}' + (X_{1} + X_{1}'X_{2}X_{0}) + X_{3}$

$A = X_{2}'X_{0}' + (X_{1} + X_{2}X_{0}) + X_{3}$

$A = X_{2}X_{0} + X_{2}'X_{0}' + X_{3} + X_{1}$


## พิจารณาสมการ Boolean ของ B
```
B = (!X2&X0) | (!X1&!X0) | (X2&X1&X0) | (!X2&!X0);
```
$B = X_{2}'X_{0} + X_{1}'X_{0}' + X_{2}X_{1}X_{0} + X_{2}'X_{0}'$

$B = (X_{2}'X_{0}+ X_{2}'X_{0}') + X_{1}'X_{0}' + X_{2}X_{1}X_{0}$

$B = X_{2}' + X_{1}'X_{0}' + X_{2}X_{1}X_{0}$

$B = (X_{2}' + X_{2}X_{1}X_{0}) + X_{1}'X_{0}'$

$B = (X_{2}' + X_{1}X_{0}) + X_{1}'X_{0}'$

$B = X_{1}X_{0} + X_{1}'X_{0}' + X_{2}'$

## พิจารณาสมการ Boolean ของ C
```
C = (!X2&X0) | (!X1&!X0) | (X2&X1&X0) | (X2&!X1&X0) | (X2&X1&!X0);
```
$C = X_{2}'X_{0} + X_{1}'X_{0}' + X_{2}X_{1}X_{0} + X_{2}X_{1}'X_{0} + X_{2}X_{1}X_{0}'$

$C = X_{2}'X_{0} + X_{1}'X_{0}' + (X_{2}X_{0}X_{1} + X_{2}X_{0}X_{1}') + X_{2}X_{1}X_{0}'$

$C = X_{2}'X_{0} + X_{1}'X_{0}' + X_{2}X_{0} + X_{2}X_{1}X_{0}'$

$C = (X_{2}'X_{0} + X_{2}X_{0}) + X_{1}'X_{0}' + X_{2}X_{1}X_{0}'$

$C = X_{0} + 'X_{0}'X_{1} + X_{2}X_{1}X_{0}'$

$C = X_{0} + X_{1}' + X_{1}X_{2}X_{0}'$

$C = X_{0} + X_{1}' + X_{2}X_{0}'$

$C = (X_{0} + X_{0}'X_{2}) + X_{1}'$

$C = (X_{0} + X_{2}) + X_{1}'$

$C = X_{0} + X_{1}' + X_{2}$

## พิจารณาสมการ Boolean ของ D
```
D = (!X2&X1) | (X2&!X1&X0) | (!X2&!X0) | (X2&X1&!X0) | (X3);
```
$D = X_{2}'X_{1} + X_{2}X_{1}'X_{0} + X_{2}'X_{0}' + X_{2}X_{1}X_{0}' + X_{3}$

$D = (X_{2}'X_{1} + X_{2}X_{1}X_{0}') + X_{2}X_{1}'X_{0} + X_{2}'X_{0}' + X_{3}$

$D = X_{1}(X_{2}' + X_{2}X_{0}') + X_{2}X_{1}'X_{0} + X_{2}'X_{0}' + X_{3}$

$D = X_{1}(X_{2}' + X_{0}') + X_{2}X_{1}'X_{0} + X_{2}'X_{0}' + X_{3}$

$D = X_{2}'X_{1} + X_{1}X_{0}' + X_{2}X_{1}'X_{0} + X_{2}'X_{0}' + X_{3}$

$D = X_{2}X_{1}'X_{0} + X_{2}'X_{1} + X_{2}'X_{0}' + X_{1}X_{0}' + X_{3}$

## พิจารณาสมการ Boolean ของ E
```
E = (!X2&!X0) | (X2&X1&!X0);
```
$E = X_{2}'X_{0}' + X_{2}X_{1}X_{0}'$

$E = X_{0}'(X_{2}' + X_{2}X_{1})$

$E = X_{0}'(X_{2}' + X_{1})$

$E = X_{2}'X_{0}' + X_{1}X_{0}'$

## พิจารณาสมการ Boolean ของ F
```
F = (!X1&!X0) | (X2&X1&X0) | (X2&!X1&X0) | (X2&X1&!X0) | (X3);
```
$F = X_{1}'X_{0}' + X_{2}X_{1}X_{0} + X_{2}X_{1}'X_{0} + X_{2}X_{1}X_{0}' + X_{3}$

$F = (X_{1}'X_{0}' + X_{2}X_{1}X_{0}') + (X_{2}X_{0}X_{1} + X_{2}X_{0}X_{1}') + X_{3}$

$F = X_{0}'(X_{1}' + X_{1}X_{2}) + X_{2}X_{0} + X_{3}$

$F = X_{0}'(X_{1}' + X_{2}) + X_{2}X_{0} + X_{3}$

$F = X_{1}'X_{0}' + X_{2}X_{0}' + X_{2}X_{0} + X_{3}$

$F = X_{1}'X_{0}' + X_{2} + X_{3}$

$F = X_{1}'X_{0}' + X_{3} + X_{2}$

## พิจารณาสมการ Boolean ของ G
```
G = (X2&!X1) | (!X2&X1) | (X2&X1&!X0) | (X3);
```
$G = X_{2}X_{1}' + X_{2}'X_{1} + X_{2}X_{1}X_{0}' + X_{3}$

$G = X_{2}X_{1}' + (X_{2}'X_{1} + X_{2}X_{1}X_{0}') + X_{3}$

$G = X_{2}X_{1}' + X_{1}(X_{2}' + X_{2}X_{0}') + X_{3}$

$G = X_{2}X_{1}' + X_{1}(X_{2}' + X_{0}') + X_{3}$

$G = X_{2}X_{1}' + X_{2}'X_{1} + X_{0}'X_{1} + X_{3}$

---

# Step 4: นำสมการ Boolean ไปต่อเป็นวงจร

หลังจากที่ได้สมการ Boolean มาแล้ว ให้นำสมการที่ได้มาต่อเป็นวงจร Digital ก็จะได้ดังภาพเลย

## $A = X_{2}X_{0} + X_{2}'X_{0}' + X_{3} + X_{1}$
## $B = X_{1}X_{0} + X_{1}'X_{0}' + X_{2}'$
## $C = X_{0} + X_{1}' + X_{2}$
## $D = X_{2}X_{1}'X_{0} + X_{2}'X_{1} + X_{2}'X_{0}' + X_{1}X_{0}' + X_{3}$
## $E = X_{2}'X_{0}' + X_{1}X_{0}'$
## $F = X_{1}'X_{0}' + X_{3} + X_{2}$
## $G = X_{2}X_{1}' + X_{2}'X_{1} + X_{0}'X_{2} + X_{3}$

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2003/diglab_03_01/diglab_03_01.png" width=80% height=80%>
