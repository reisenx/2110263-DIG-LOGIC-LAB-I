# Half Adder (Onsite) (diglab_04_01)
### อ่านคู่มือแลปได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1cWwg5P7O8KAnXi60t8aw2gi7A2KyzH53/view?usp=drive_link)

---

# Step 1: ต่อวงจร Half Adder แบบ Sum of Product (SOP)
## Truth Table

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_01/Half_Adder_Additional/Half_Adder_TruthTable.png" width="672" height="424">

## ต่อวงจร Half Adder แบบ Sum of Product
เมื่อนำ Truth Table มาวาด K-map แบบ 2 ตัวแปรจะได้ดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_01/Half_Adder_Additional/Half_Adder_Kmap01.png" width="473" height="501">

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_01/Half_Adder_Additional/Half_Adder_Kmap02.png" width="473" height="501">

ซึ่งจาก K-map จะได้สมการ Boolean ทั้งหมด 2 สมการ ดังนี้

## $Sum = A'B + AB'$ หรือก็คือ $Sum = A \oplus B$
## $C_{out} = AB$

และเขียนวงจรจากสมการดังกล่าวได้ดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_01/Half_Adder_Additional/Half_Adder_SOP.png" width="644" height="313">

---

# Step 2: แปลงวงจร Half Adder จากแบบ Sum of Product (SOP) เป็น NAND Gate

จากวงจร Sum of Product (SOP) วงจรนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_01/Half_Adder_Additional/Half_Adder_SOP.png" width="644" height="313">

เราจะพิจารณาที่สมการของ `Sum` ก่อน ซึ่งเราจะสามารถเขียน NOT Gate ให้อยู่ในรูป Bubble ได้ลักษณะแบบนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_01/Half_Adder_Additional/Half_Adder_toNAND01.png" width="683" height="188">

จากนั้นเติม Bubble ที่หัวของ AND Gate เพื่อแปลง AND Gate ให้กลายเป็น NAND Gate และเติม Bubble ที่บริเวณ Input ทั้งสองของ OR Gate เพื่อให้สมการ Boolean ยังคงเป็นสมการเดิมอยู่

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_01/Half_Adder_Additional/Half_Adder_toNAND02_Annotation.jpg" width="834" height="230">

**พิจารณาวงจรบริเวณกรอบสีแดง**

จาก De Morgan's Law ได้กล่าวไว้ว่า $A' + B' = (AB)'$ จะได้ว่า เราสามารถแปลง OR Gate ที่มี Bubble บริเวณ Input ทั้ง 2 ตัวให้กลายเป็น NAND Gate ได้เลย

**พิจารณาวงจรบริเวณกรอบสีเขียว**

ในวงจรบริเวณสีแดง เราสามารถจัดรูปสมการ Boolean เพื่อให้สามารถใช้งาน NAND Gate เพียงแค่ 3 Gate ในการต่อได้ดังนี้

**สมการ Boolean ที่ 1**

$(AB')' = A' + B$

$(AB')' = A' + AB$

$(AB')' = (A(AB)')'$

**สมการ Boolean ที่ 2**

$(A'B)' = A + B'$

$(AB')' = B' + AB$

$(AB')' = (B(AB)')'$

เมื่อพิจารณาวงจรบนกรอบสีแดงและสีเขียวเสร็จสิ้น เราจะเห็นว่าเราจะสามารถต่อ NAND Gate ได้ดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_01/Half_Adder_Additional/Half_Adder_toNAND03_Annotation.jpg" width="828" height="217">

และจากที่เราทราบกันว่า Sum สามารถเขียนได้อยู่ในรูปของ XOR ได้ดังนี้ $Sum = A \oplus B$

ภาพวงจรข้างล่างนี้ จึงเป็นการต่อวงจร XOR ด้วย NAND Gate จำนวนน้อยที่สุดซึ่งก็คือ 4 Gate 

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_01/Half_Adder_Additional/Half_Adder_toNAND03.png" width="828" height="217">

หากยังไม่เข้าใจ สามารถดูคลิปสอนการต่อ Gate แบบต่างๆโดยใช้แค่ NAND Gate เพื่อเสริมความเข้าใจกับแลปนี้เพิ่มเติมได้
- NAND Gate as Universal Gate (Part 1) By Neso Academy - [Click Here](https://youtu.be/ChtmE09BSy0?si=AbYdJKjGZTbH2O7K)
- NAND Gate as Universal Gate (Part 2) By Neso Academy - [Click Here](https://youtu.be/MZ_Pd40F4MU?si=wl_3_hroa-zqHp27)


เมื่อต่อวงจร NAND Gate ของสมการ Sum เสร็จสิ้น ก็ถึงเวลาที่จะไปต่อวงจรของสมการ Cout ต่อ

$C_{out} = AB$

$C_{out} = ((AB)')'$

$C_{out} = ((AB)'(AB)')'$

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_01/Half_Adder_Additional/Half_Adder_NAND_Annotation.jpg" width="834" height="403">

---

# Step 3: แปลงวงจร Half Adder แบบ NAND Gate เป็นวงจรที่ต่อด้วย IC 7400

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

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_01/Half_Adder_Additional/Half_Adder_to7400.jpg" width="834" height="403">

เมื่อร่างเสร็จแล้ว เราสามารถที่จะต่อวงจรด้วย IC 7400 บนโปรแกรม Digital ได้ดังนี้เลย

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_01/Half_Adder_7400.png" width="469" height="670">

เมื่อนำวงจรที่ต่อบน Digital มาต่อเป็นวงจรจริงๆก็จะมีลักษณะหน้าตาประมาณนี้เลย

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2004/diglab_04_01/Half_Adder_Circuit.png" width="768" height="303">
