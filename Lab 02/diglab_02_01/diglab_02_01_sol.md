# XOR (Sum of Products) (diglab_​02_​01)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1X58ZSczfBssWzQGDQZVs-rJgAqAgLOG5/view?usp=drive_link)
---

# Step 1: เขียน K-map 2 ตัวแปร เพื่อหาสมการ Boolean

นำ Truth table ของวงจร XOR (ระบุไว้ในโจทย์) มาเขียนอยู่ในรูปของ K-map 2 ตัวแปร จะได้สมการ Boolean ดังภาพ

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_02_01/diglab_02_01_pics/diglab_02_01_Kmap.png" width=40% height=40%>

---

# Step 2: นำสมการ Boolean ไปต่อเป็นวงจร

หลังจากที่ได้สมการ Boolean จาก K-map มาแล้ว ให้นำสมการที่ได้มาต่อเป็นวงจร Digital ก็จะได้ดังภาพเลย

**ข้อควรทราบ:** การต่อวงจรแบบ Sum of Products หมายถึงการต่อวงจรโดยการนำ AND Gate หลายๆอันมาต่อกับ OR Gate

## $Output = A'B + AB'$

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_02_01/diglab_02_01.png" width=80% height=80%>
