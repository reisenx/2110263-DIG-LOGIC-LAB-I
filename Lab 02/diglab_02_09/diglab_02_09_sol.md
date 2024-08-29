# Mux4:1 (Sum of Products) (diglab_​02_​09)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1ngDn0xtNYtUdcPsC_CHHoyIEIOocsJhk/view?usp=drive_link)

---

# Step 1: เขียนสมการ Boolean จาก Truth Table ที่โจทย์กำหนดให้

เมื่อพิจารณา Truth Table ที่โจทย์กำหนดให้ จะสามารถเขียนสมการ Boolean แบบ Sum of Products (SOP) ได้ดังภาพ

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_02_09/diglab_02_09_pics/diglab_02_09_Equation.png" width="800" height="600">

---

# Step 2: นำสมการ Boolean ไปต่อเป็นวงจร

หลังจากที่ได้สมการ Boolean จาก Truth Table มาแล้ว ให้นำสมการที่ได้มาต่อเป็นวงจร Digital ก็จะได้ดังภาพเลย

**ข้อควรทราบ:** การต่อวงจรแบบ Sum of Products หมายถึงการต่อวงจรโดยการนำ AND Gate หลายๆอันมาต่อกับ OR Gate
## $Z = S_{1}'S_{0}'X_{0} + S_{1}'S_{0}X_{1} + S_{1}S_{0}'X_{2} + S_{1}S_{0}X_{3}$

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2002/diglab_02_09/diglab_02_09.png" width="844" height="602">
