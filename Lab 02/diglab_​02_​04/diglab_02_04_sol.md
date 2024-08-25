# FullAdder (Product of Sums) (diglab_​02_​04)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/16HCbbrqRba3GJ2d0AD0ZKvdQQFeRKjz1/view?usp=drive_link)
---

# Step 1: เขียน K-map 3 ตัวแปร เพื่อหาสมการ Boolean

นำ Truth table ของวงจร Full-Adder (ระบุไว้ในโจทย์) มาเขียนอยู่ในรูปของ K-map 3 ตัวแปร จะได้สมการ Boolean ดังภาพ

### K-map 3 ตัวแปรสำหรับ Output **C<sub>out</sub>**

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_%E2%80%8B02_%E2%80%8B04/diglab_02_04_pics/diglab_02_04_Kmap_01.png" width="718" height="500">

### K-map 3 ตัวแปรสำหรับ Output **Sum**
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_%E2%80%8B02_%E2%80%8B04/diglab_02_04_pics/diglab_02_04_Kmap_02.png" width="810" height="500">

---

# Step 2: นำสมการ Boolean ไปต่อเป็นวงจร

หลังจากที่ได้สมการ Boolean จาก K-map มาแล้ว ให้นำสมการที่ได้มาต่อเป็นวงจร Digital ก็จะได้ดังภาพเลย

**ข้อควรทราบ:** การต่อวงจรแบบ Product of Sums หมายถึงการต่อวงจรโดยการนำ OR Gate หลายๆอันมาต่อกับ AND Gate

```math
\Huge{C_{out} = (A + B)(A + C_{in})(B + C_{in})}
```
```math
\Huge{Sum = (A + B + C_{in})(A' + B + C'_{in})(A + B' + C'_{in})(A' + B' + C_{in})}
```

![Image](https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_%E2%80%8B02_%E2%80%8B04/diglab_%E2%80%8B02_%E2%80%8B04.png)
