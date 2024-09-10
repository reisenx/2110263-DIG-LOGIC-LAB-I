# Glitch I (diglab_05_01)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1-pgU_dNTRe6GDTKPcwK-nZ2icEwXbQET/view?usp=drive_link)

---

# Step 1: เขียน K-map เพื่อพิจารณา Hazard ที่เกิดขึ้น
## $Before = A' + C'D + AB'D$
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2005/diglab_05_01/diglab_05_01_pics/diglab_05_01_Kmap.jpg" width="600" height="600">

จาก K-map จะเห็นได้ว่าถ้าเกิดมีการเปลี่ยนแปลงจาก `ABCD` จาก `0011` ไปยัง `1011` จะสามารถเกิด Static 1-hazard ได้ ดังนั้นถ้าต้องการแก้ Static 1-Hazard เราจะต้องครอบบริเวณช่อง `0011` และ `1011` ดังภาพต่อไปนี้
## $After = A' + C'D + B'D$
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2005/diglab_05_01/diglab_05_01_pics/diglab_05_01_Kmap02.jpg" width="600" height="600">

เพียงแค่นี้เราก็จะวงจรที่ไม่เกิด Hazard (Hazard-free) เป็นที่เรียบร้อย

---

# Step 2: ต่อวงจร Digital ของ `Before` และ `After`
## $Before = A' + C'D + AB'D$
## $After = A' + C'D + B'D$
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2005/diglab_05_01/diglab_05_01.png" width="825" height="540">

---

# Step 3: เขียน Testcases เพื่อทดสอบ Glitch ของวงจร

ก่อนอื่นให้ไปตั้งค่าที่ `Edit` > `Circuit specific settings` > `Advanced` > `Show measurement graph in single gate step mode at simulation start`

จากนั้นสร้าง Testcases โดยการกด `Components` > `Misc.` > `Test case` จากนั้นวางที่ไหนก็ได้ของวงจรของเรา

เมื่อวางเสร็จแล้วให้ทำการกดคลิกขวาที่ `Test case` แล้วกด `Edit` จากนั้นก็กรอก testcases ที่เราต้องการจะตรวจสอบลงไป ดังนี้
```
A B C D Before
0 0 1 1 1
1 0 1 1 1
1 0 1 1 1
```

เมื่อสร้าง Testcases เสร็จแล้ว เราสามารถทดสอบได้โดยการกด `Run all testcases in the circuit` (ปุ่มเครื่องหมายรันแต่มีติ้กถูกสีเขียว) แล้วกดที่ testcases อันสุดท้าย
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_02/Full_Adder_Additional/Full_Adder_SOP.png" width="538" height="729">

เราจะพิจารณาที่สมการของ `Sum` ก่อน ซึ่งจากที่เราทราบกันว่าเราสามารถเขียนสมการ Boolean ของ `Sum` ให้อยู่ใน XOR Gate ได้เป็น $Sum = A \oplus B \oplus C$

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_02/Full_Adder_Additional/Full_Adder_toNAND01.png" width="543" height="118">

จาก XOR Gate สามารถต่ออยู่ในรูปของ NAND Gate จำนวน 4 Gate ([สามารถอ่านวิธีการแปลงวงจร XOR เป็น NAND เพิ่มเติมได้ที่นี่](https://github.com/reisenx/2110263-DIG-LOGIC-LAB-I/blob/main/Lab%2004/diglab_04_01/diglab_04_01_sol.md#step-2-%E0%B9%81%E0%B8%9B%E0%B8%A5%E0%B8%87%E0%B8%A7%E0%B8%87%E0%B8%88%E0%B8%A3-half-adder-%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B9%81%E0%B8%9A%E0%B8%9A-sum-of-product-sop-%E0%B9%80%E0%B8%9B%E0%B9%87%E0%B8%99-nand-gate))

เราจึงสามารถแปลงวงจร XOR แบบ 2 Gate ตามข้างบน ให้อยู่ในรูปของวงจร NAND Gate จำนวน 8 Gate ได้ดังภาพ

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_02/Full_Adder_Additional/Full_Adder_toNAND02_Annotation.jpg" width="832" height="177">

**พิจารณาวงจรของ $C_{out}$**

$C_{out} = AC_{in} + AB + BC_{in}$

$C_{out} = A(C_{in} + B) + BC_{in}$

$C_{out} = A(B'C_{in} + B) + BC_{in}$

$C_{out} = AB'C_{in} + AB + BC_{in}$

$C_{out} = AB'C_{in} + B(A + C_{in})$

$C_{out} = AB'C_{in} + B(A + A'C_{in})$

$C_{out} = AB'C_{in} + AB + A'BC_{in}$

$C_{out} = C_{in}(A'B + AB') + AB$

$C_{out} = C_{in}(A \oplus B) + AB$

$C_{out} = (((A \oplus B)C_{in})'(AB)')'$

เมื่อพิจารณาวงจรของ $C_{out}$ เสร็จสิ้น จะสามารถเขียนวงจรได้ดังนี้

<img src="https://github.com/reisenx/2110263-DIG-LOGIC-LAB-I/blob/main/Lab%2004/diglab_04_02/Full_Adder_Additional/Full_Adder_NAND_Annotation.jpg" width="834" height="274">

---

# Step 3: แปลงวงจร Full Adder แบบ NAND Gate เป็นวงจรที่ต่อด้วย IC 7400

## รายละเอียดของ IC 7400

สำหรับการต่อวงจรในแลปนี้ จะใช้ Integrated Circuit (IC) รุ่น 7400 ที่ประกอบไปด้วย NAND Gate ภายในจำนวน 4 Gate ดังภาพ
- ขา `VCC` จะต่อเข้ากับแหล่งจ่ายไฟฟ้า ซึ่งในแลปนี้จะจ่ายกระแสไฟฟ้าด้วย USB
- ขา `GND` คือจะต่อเข้ากับ Ground
- ขา `1A` และ `1B` เป็น Input ของ NAND Gate และจะ Output ทางขา `1Y`
- ขา `2A` และ `2B` เป็น Input ของ NAND Gate และจะ Output ทางขา `2Y`
- ขา `3A` และ `3B` เป็น Input ของ NAND Gate และจะ Output ทางขา `3Y`
- ขา `4A` และ `4B` เป็น Input ของ NAND Gate และจะ Output ทางขา `4Y`

**หมายเหตุ:** บนโปรแกรม Digital ถ้าหากไม่ได้ใช้ Input ขาไหนให้ต่อลง Ground ให้หมด

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_01/Half_Adder_Additional/IC7400.jpg" width="354" height="491">

เมื่อเข้าใจหลักการแล้ว เราสามารถร่างการต่อวงจรบนวงจร NAND Gate ที่เราต่อมาอยู่แล้วได้ ดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_02/Full_Adder_Additional/Full_Adder_to7400.jpg" width="873" height="312">

เมื่อร่างเสร็จแล้ว เราสามารถที่จะต่อวงจรด้วย IC 7400 บนโปรแกรม Digital ได้ดังนี้เลย

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_02/Full_Adder_7400.png" width="577" height="1070">

เมื่อนำวงจรที่ต่อบน Digital มาต่อเป็นวงจรจริงๆก็จะมีลักษณะหน้าตาประมาณนี้เลย

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_02/Full_Adder_Circuit.png" width="768" height="303">

ส่วนอันนี้คือวงจร Full Adder ที่ต่อในคาบจริง (ดูยากมากๆ 555555)

<img src="https://github.com/reisenx/2110263-DIG-LOGIC-LAB-I/blob/main/Lab%2004/diglab_04_02/Full_Adder_RealCircuit.jpg" width="771" height="579">
