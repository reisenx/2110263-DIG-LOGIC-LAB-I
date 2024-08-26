# Comparator (Sum of Products) (diglab_​02_​05)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1Sne5lBG-NsupPsBlxRyze35h4b-5ZpJw/view?usp=drive_link)

---

# Step 1: พิจารณาโจทย์ และเขียน Truth Table

จากโจทย์กล่าวไว้ว่า
- **N1** คือเลขฐานสองจำนวนที่หนึ่ง ประกอบไปด้วย A และ B (เช่น A = 1 และ B = 1 หมายถึงว่า N1 มีค่าเท่ากับ 3)
- **N2** คือเลขฐานสองจำนวนที่หนึ่ง ประกอบไปด้วย C และ D (เช่น C = 1 และ D = 0 หมายถึงว่า N2 มีค่าเท่ากับ 2)
- **Z1** เป็นการเปรียบเทียบ N1 < N2 (ถ้าเป็นเท็จ Z1 = 0 และถ้าเป็นจริง Z2 = 1)
- **Z2** เป็นการเปรียบเทียบ N1 > N2 (ถ้าเป็นเท็จ Z1 = 0 และถ้าเป็นจริง Z2 = 1)
- **Z3** เป็นการเปรียบเทียบ N1 = N2 (ถ้าเป็นเท็จ Z1 = 0 และถ้าเป็นจริง Z2 = 1)

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_%E2%80%8B02_%E2%80%8B05/diglab_02_05_pics/diglab_02_05_table.png" width="619" height="676">

---

# Step 2: เขียน K-map 4 ตัวแปร เพื่อหาสมการ Boolean

นำ Truth table ของวงจร Full-Adder (ระบุไว้ในโจทย์) มาเขียนอยู่ในรูปของ K-map 4 ตัวแปร จะได้สมการ Boolean ดังภาพ

### K-map 4 ตัวแปรสำหรับ Output **Z<sub>1</sub>**
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_%E2%80%8B02_%E2%80%8B05/diglab_02_05_pics/diglab_02_05_Kmap_01.png" width="600" height="693">

### K-map 4 ตัวแปรสำหรับ Output **Z<sub>2</sub>**
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_%E2%80%8B02_%E2%80%8B05/diglab_02_05_pics/diglab_02_05_Kmap_02.png" width="600" height="680">

### K-map 4 ตัวแปรสำหรับ Output **Z<sub>3</sub>**
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_%E2%80%8B02_%E2%80%8B05/diglab_02_05_pics/diglab_02_05_Kmap_03.png" width="600" height="687">

---

# Step 3: นำสมการ Boolean ไปต่อเป็นวงจร

หลังจากที่ได้สมการ Boolean จาก K-map มาแล้ว ให้นำสมการที่ได้มาต่อเป็นวงจร Digital ก็จะได้ดังภาพเลย

**ข้อควรทราบ:** การต่อวงจรแบบ Sum of Products หมายถึงการต่อวงจรโดยการนำ AND Gate หลายๆอันมาต่อกับ OR Gate
## $Z_{1} = BC'D' + ABD' + AC'$
## $Z_{2} = A'C + A'B'D + B'CD$
## $Z_{3} = A'B'C'D' + A'B'C'D + ABCD + AB'CD'$

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_%E2%80%8B02_%E2%80%8B05/diglab_%E2%80%8B02_%E2%80%8B05.png" width="716" height="1152">
