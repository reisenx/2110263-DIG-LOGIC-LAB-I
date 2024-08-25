# FullAdder (Sum of Products) (diglab_​02_​03)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1W0zyqn9E_a2-WQ19l-L3xpcZyvcE8bzV/view?usp=drive_link)
---

# Step 1: เขียน K-map 3 ตัวแปร เพื่อหาสมการ Boolean

นำ Truth table ของวงจร Full-Adder (ระบุไว้ในโจทย์) มาเขียนอยู่ในรูปของ K-map 3 ตัวแปร จะได้สมการ Boolean ดังภาพ

### K-map 3 ตัวแปรสำหรับ Output **C<sub>out</sub>**

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_%E2%80%8B02_%E2%80%8B03/diglab_02_03_pics/diglab_02_03_Kmap_01.png" width="695" height="500">

### K-map 3 ตัวแปรสำหรับ Output **Sum**
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_%E2%80%8B02_%E2%80%8B03/diglab_02_03_pics/diglab_02_03_Kmap_02.png" width="695" height="500">

---

# Step 2: นำสมการ Boolean ไปต่อเป็นวงจร

หลังจากที่ได้สมการ Boolean จาก K-map มาแล้ว ให้นำสมการที่ได้มาต่อเป็นวงจร Digital ก็จะได้ดังภาพเลย

**ข้อควรทราบ:** การต่อวงจรแบบ Sum of Products หมายถึงการต่อวงจรโดยการนำ AND Gate หลายๆอันมาต่อกับ OR Gate

## $C_{out} = AC_{in} + BC_{in} + AB$
## $Sum = AB'C_{in} ' + A'B'C_{in} + ABC_{in} + A'BC'_{in}$

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_%E2%80%8B02_%E2%80%8B03/diglab_02_03.png" width="790" height="935">
