# Full Adder (Onsite) (diglab_04_02)
### อ่านคู่มือแลปได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1cWwg5P7O8KAnXi60t8aw2gi7A2KyzH53/view?usp=drive_link)

---

# Step 1: ต่อวงจร Full Adder แบบ Sum of Product (SOP)
## Truth Table

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_02/Full_Adder_Additional/Full_Adder_TruthTable.png" width="555" height="464">

## ต่อวงจร Full Adder แบบ Sum of Product
เมื่อนำ Truth Table มาวาด K-map แบบ 3 ตัวแปรจะได้ดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_02/Full_Adder_Additional/Full_Adder_Kmap01.png" width="460" height="346">

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_02/Full_Adder_Additional/Full_Adder_Kmap02.png" width="460" height="346">

ซึ่งจาก K-map จะได้สมการ Boolean ทั้งหมด 2 สมการ ดังนี้

## $Sum = A'B'C_{in} + A'BC_{in}' + AB'C_{in}' + ABC_{in}$ หรือก็คือ $Sum = A \oplus B \oplus C$
## $C_{out} = AC_{in} + AB + BC_{in}$

และเขียนวงจรจากสมการดังกล่าวได้ดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_02/Full_Adder_Additional/Full_Adder_SOP.png" width="538" height="729">

---

# Step 2: แปลงวงจร Full Adder จากแบบ Sum of Product (SOP) เป็น NAND Gate

จากวงจร Sum of Product (SOP) วงจรนี้

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
