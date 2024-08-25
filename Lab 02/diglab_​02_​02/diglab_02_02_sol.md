# XOR (Product of Sums) (diglab_​02_​02)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/12nkSeHxiNem1i3mO-BABmvpC8ueVb1ZY/view?usp=drive_link)
---

# Step 1: เขียน K-map 2 ตัวแปร เพื่อหาสมการ Boolean

นำ Truth table ของวงจร XOR (ระบุไว้ในโจทย์) มาเขียนอยู่ในรูปของ K-map 2 ตัวแปร จะได้สมการ Boolean ดังภาพ

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_%E2%80%8B02_%E2%80%8B02/diglab_02_02_pics/diglab_02_02_Kmap.png" width="500" height="599">

---

# Step 2: นำสมการ Boolean ไปต่อเป็นวงจร

หลังจากที่ได้สมการ Boolean จาก K-map มาแล้ว ให้นำสมการที่ได้มาต่อเป็นวงจร Digital ก็จะได้ดังภาพเลย

**ข้อควรทราบ:** การต่อวงจรแบบ Product of Sums หมายถึงการต่อวงจรโดยการนำ OR Gate หลายๆอันมาต่อกับ AND Gate

```math
\Huge{Output = (A+B)(A'+B')}
```

![Image](https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_%E2%80%8B02_%E2%80%8B02/diglab_02_02.png)
