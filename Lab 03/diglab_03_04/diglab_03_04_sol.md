# Hamming Code (diglab_​03_​04)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1KsU_OyQdPX_kcYIvL20WfOx6rToq5-o-/view?usp=drive_link)

---

# Step 1: พิจารณาโจทย์ และเขียน Truth Table
## Hamming Code คืออะไร
Hamming Code เป็นการเข้ารหัสที่ใช้ในการส่งข้อมูล โดยที่ผู้รับจะสามารถตรวจสอบความถูกต้องของข้อมูลที่ส่งได้ ซึ่ง Hamming แบ่งเป็น 2 ส่วน ได้แก่
- Data bits คือชุดข้อมูลที่ผู้ส่งต้องการจะส่ง
- Pairity bits คือชุดข้อมูลที่ใช้ในการตรวจสอบว่า Data bits ถูกต้องหรือไม่

ซึ่งในโจทย์ข้อนี้จะให้พิจารณา Hamming Code ขนาด 7 bits ประกอบไปด้วย
- Data bits ขนาด 4 bits แทนด้วย `M1`, `M2`, `M3` และ `M4`
- Pairity bits ขนาด 3 bits แทนด้วย `P1`, `P2` และ `P3`

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2003/diglab_03_04/diglab_03_04_pics/diglab_03_04_hamming.png" width="471" height="151">

สำหรับโจทย์ในข้อนี้ จะให้แก้ไข Hamming Code ที่ผิดพลาดไม่เกิน 1 bit โดยที่แนวทางการต่อวงจรสามารถอ่านได้ที่[คู่มือการทำ LAB 03](https://drive.google.com/file/d/1aTJvKOEmSuCjasI7azTFhIKsR9h_Zdn1/view?usp=drive_link) ซึ่งในใบงานจะให้เราต่อวงจรทั้งหมด 3 ชุดได้แก่ `Circuit A`, `Circuit B` และ `Circuit C`

## พิจารณา Truth Table ของ `Circuit A`
จากคู่มือการต่อวงจร จะสามารถสรุปการต่อ `Circuit A` ได้ดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2003/diglab_03_04/diglab_03_04_pics/diglab_03_04_table_A.png" width="426" height="251">

## $C_{1} = P_{3} \oplus M_{2} \oplus M_{3} \oplus M_{4}$
## $C_{2} = P_{2} \oplus M_{1} \oplus M_{3} \oplus M_{4}$
## $C_{3} = P_{1} \oplus M_{1} \oplus M_{2} \oplus M_{4}$

## พิจารณา Truth Table ของ `Circuit B`
จากคู่มือการต่อวงจร จะสามารถสรุป Truth Table ของ `Circuit B` ได้ดังนี้
- ถ้า `C1` `C2` `C3` เป็น `0` `0` `0` ทุกตัวจะเป็น `0`
- ถ้า `C1` `C2` `C3` เป็น `0` `0` `1` จะได้ว่า `B1` เป็น `1`
- ถ้า `C1` `C2` `C3` เป็น `0` `1` `0` จะได้ว่า `B2` เป็น `1`
- ถ้า `C1` `C2` `C3` เป็น `0` `1` `1` จะได้ว่า `B3` เป็น `1`
- ถ้า `C1` `C2` `C3` เป็น `1` `0` `0` จะได้ว่า `B4` เป็น `1`
- ถ้า `C1` `C2` `C3` เป็น `1` `0` `1` จะได้ว่า `B5` เป็น `1`
- ถ้า `C1` `C2` `C3` เป็น `1` `1` `0` จะได้ว่า `B6` เป็น `1`
- ถ้า `C1` `C2` `C3` เป็น `1` `1` `1` จะได้ว่า `B7` เป็น `1`

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2003/diglab_03_04/diglab_03_04_pics/diglab_03_04_table_B.png" width="551" height="551">

## พิจารณา Truth Table ของ `Circuit C`
จากคู่มือการต่อวงจร จะสามารถสรุป Truth Table ของ `Circuit B` ได้ดังนี้
- ถ้า `B1` เป็น `1` ให้สลับ `P1` จาก `0` เป็น `1` และจาก `1` เป็น `0`
- ถ้า `B2` เป็น `1` ให้สลับ `P2` จาก `0` เป็น `1` และจาก `1` เป็น `0`
- ถ้า `B3` เป็น `1` ให้สลับ `M1` จาก `0` เป็น `1` และจาก `1` เป็น `0`
- ถ้า `B4` เป็น `1` ให้สลับ `P3` จาก `0` เป็น `1` และจาก `1` เป็น `0`
- ถ้า `B5` เป็น `1` ให้สลับ `M2` จาก `0` เป็น `1` และจาก `1` เป็น `0`
- ถ้า `B6` เป็น `1` ให้สลับ `M3` จาก `0` เป็น `1` และจาก `1` เป็น `0`
- ถ้า `B7` เป็น `1` ให้สลับ `M4` จาก `0` เป็น `1` และจาก `1` เป็น `0`

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2003/diglab_03_04/diglab_03_04_pics/diglab_03_04_table_C.png" width="720" height="521">

ถ้าดูจาก Truth Table ของ `Circuit C` แล้วจะเห็นว่าแต่ละ Bits จะมีการดำเนินการแบบ XOR ทั้งหมดเลย ก็คือ
- $Z_{1} = P_{1} \oplus B_{1}$
- $Z_{2} = P_{2} \oplus B_{2}$
- $Z_{3} = M_{1} \oplus B_{3}$
- $Z_{4} = P_{3} \oplus B_{4}$
- $Z_{5} = M_{2} \oplus B_{5}$
- $Z_{6} = M_{3} \oplus B_{6}$
- $Z_{7} = M_{4} \oplus B_{7}$

---

# Step 2: ใช้งานโปรแกรม ESPRESSO logic minimizer ในการหาสมการ Boolean

## การใช้งานโปรแกรม
การใช้งานโปรแกรม ESPRESSO logic minimizer จะต้องสร้างไฟล์สำหรับ Input และ Output ไว้ก่อน
- ไฟล์ Input จะเป็นไฟล์ที่บรรจุชุดคำสั่งเข้าไป (ไฟล์ `.pla`)
- ไฟล์ Output จะเป็นไฟล์ที่ ESPRESSO logic minimizer จัดเก็บสมการ Boolean หลังจากที่ประมวลผล Input เสร็จสิ้น (ไฟล์ `.pla`)
- แนะนำให้ใช้งาน ESPRESSO logic minimizer แบบ Compile Mode ผ่าน Command Prompt
- สามารถอ่านขั้นตอนการใช้งานโปรแกรม ESPRESSO logic minimizer แบบละเอียด [ได้ที่นี่](https://github.com/reisenx/2110263-DIG-LOGIC-LAB-I/blob/main/Lab%2003/diglab_03_01/diglab_03_01_sol.md#%E0%B8%82%E0%B8%B1%E0%B9%89%E0%B8%99%E0%B8%95%E0%B8%AD%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B9%82%E0%B8%9B%E0%B8%A3%E0%B9%81%E0%B8%81%E0%B8%A3%E0%B8%A1-espresso-logic-minimizer)

## หาสมการ Boolean `Circuit B`
### กรอก Command line ลงในไฟล์ Input
```
.i 3
.o 7
.ilb C1 C2 C3
.ob B1 B2 B3 B4 B5 B6 B7
.p 8
000 0000000
001 1000000
010 0100000
011 0010000
100 0001000
101 0000100
110 0000010
111 0000001
.e
```
**หมายเหตุ:** ส่วนที่เป็น Don't care ให้ใช้เครื่องหมาย `-` แทนเลข `0` กับ `1` ได้เลย

### ทำความเข้าใจ Output
- เครื่องหมาย `&` หมายถึง AND
- เครื่องหมาย `|` หมายถึง OR
- เครื่องหมาย `!` หมายถึง NOT
```
B1 = (!C1&!C2&C3);
B2 = (!C1&C2&!C3);
B3 = (!C1&C2&C3);
B4 = (C1&!C2&!C3);
B5 = (C1&!C2&C3);
B6 = (C1&C2&!C3);
B7 = (C1&C2&C3);
```
- $B_{1} = C_{1}'C_{2}'C_{3}'$
- $B_{2} = C_{1}'C_{2}C_{3}'$
- $B_{3} = C_{1}'C_{2}C_{3}$
- $B_{4} = C_{1}C_{2}'C_{3}'$
- $B_{5} = C_{1}C_{2}'C_{3}$
- $B_{6} = C_{1}C_{2}C_{3}'$
- $B_{7} = C_{1}C_{2}C_{3}$

---

# Step 4: นำสมการ Boolean ไปต่อเป็นวงจร

หลังจากที่ได้สมการ Boolean มาแล้ว ให้นำสมการที่ได้มาต่อเป็นวงจร Digital ก็จะได้ดังภาพเลย

## การต่อวงจร `Circuit A`
### $C_{1} = P_{3} \oplus M_{2} \oplus M_{3} \oplus M_{4}$
### $C_{2} = P_{2} \oplus M_{1} \oplus M_{3} \oplus M_{4}$
### $C_{3} = P_{1} \oplus M_{1} \oplus M_{2} \oplus M_{4}$

## การต่อวงจร `Circuit B`
### $B_{1} = C_{1}'C_{2}'C_{3}'$
### $B_{2} = C_{1}'C_{2}C_{3}'$
### $B_{3} = C_{1}'C_{2}C_{3}$
### $B_{4} = C_{1}C_{2}'C_{3}'$
### $B_{5} = C_{1}C_{2}'C_{3}$
### $B_{6} = C_{1}C_{2}C_{3}'$
### $B_{7} = C_{1}C_{2}C_{3}$

## การต่อวงจร `Circuit C`
- $Z_{1} = P_{1} \oplus B_{1}$
- $Z_{2} = P_{2} \oplus B_{2}$
- $Z_{3} = M_{1} \oplus B_{3}$
- $Z_{4} = P_{3} \oplus B_{4}$
- $Z_{5} = M_{2} \oplus B_{5}$
- $Z_{6} = M_{3} \oplus B_{6}$
- $Z_{7} = M_{4} \oplus B_{7}$

จากสมการดังกล่าวจะเห็นว่าทุก Bits ของ Output จะดำเนินการด้วย XOR ทั้งหมด ดังนั้นเราสามารถลดขนาดวงจรโดยการต่อวงจรลักษณะนี้
1. รวม Bits ของตัวแปร `P1`, `P2`, `M1`, `P3`, `M2`, `M3` และ `M4` Merge เป็น 7 Bits
2. รวม Bits ของตัวแปร `B1`, `B2`, `B3`, `B4`, `B5`, `B6` และ `B7` Merge เป็น 7 Bits
3. นำข้อมูลจาก 2 ข้อแรกมา XOR กันเป็น Output

### Output 
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2003/diglab_03_04/diglab_03_04.png" width="1002" height="671">
