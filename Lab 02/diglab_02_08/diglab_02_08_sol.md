# Multiplexer (Product of Sums) (diglab_​02_​08)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1cgN1CoPt-9dDRTEL3GCghg49iHBdRUZr/view?usp=drive_link)

---

# Step 1: พิจารณาโจทย์ และเขียน Truth Table

จากโจทย์กล่าวไว้ว่า
- ถ้า **Selector** มีค่าเท่ากับ 0 ให้ Output ตามค่า **X0**
- ถ้า **Selector** มีค่าเท่ากับ 1 ให้ Output ตามค่า **X1**

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_02_07/diglab_02_07_pics/diglab_02_07_table.png" width="401" height="501">

---

# Step 2: เขียน K-map 3 ตัวแปร เพื่อหาสมการ Boolean

นำ Truth table ของวงจร Multiplexer มาเขียนอยู่ในรูปของ K-map 3 ตัวแปร จะได้สมการ Boolean ดังภาพ

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_02_08/diglab_02_08_pics/diglab_02_08_Kmap.png" width="843" height="600">

---

# Step 3: นำสมการ Boolean ไปต่อเป็นวงจร

หลังจากที่ได้สมการ Boolean จาก K-map มาแล้ว ให้นำสมการที่ได้มาต่อเป็นวงจร Digital ก็จะได้ดังภาพเลย

**ข้อควรทราบ:** การต่อวงจรแบบ Product of Sums หมายถึงการต่อวงจรโดยการนำ OR Gate หลายๆอันมาต่อกับ AND Gate
## $Z_{1} = (S + X_{0})(S' + X_{1})$

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_02_08/diglab_02_08.png" width="675" height="481">
