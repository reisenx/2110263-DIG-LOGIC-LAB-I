# Glitch I (diglab_05_01)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1-pgU_dNTRe6GDTKPcwK-nZ2icEwXbQET/view?usp=drive_link)

---

# Step 1: เขียน K-map เพื่อพิจารณา Hazard ที่เกิดขึ้น
## $Before = A' + C'D + AB'D$
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2005/diglab_05_01/diglab_05_01_pics/diglab_05_01_Kmap.jpg" width="600" height="600">

จาก K-map จะเห็นได้ว่าถ้าเกิดมีการเปลี่ยนแปลงจาก `ABCD` จาก `0011` ไปยัง `1011` จะสามารถเกิด Static 1-hazard ได้ ดังนั้นถ้าต้องการแก้ Static 1-Hazard เราจะต้องครอบบริเวณช่อง `0011` และ `1011` ดังภาพต่อไปนี้
## $After = A' + C'D + B'D$
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2005/diglab_05_01/diglab_05_01_pics/diglab_05_01_Kmap02.jpg" width="600" height="600">

เพียงแค่นี้เราก็จะวงจรที่ไม่เกิด Hazard (Hazard-free) เป็นที่เรียบร้อย

---

# Step 2: ต่อวงจร Digital ของ `Before` และ `After`
## $Before = A' + C'D + AB'D$
## $After = A' + C'D + B'D$
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2005/diglab_05_01/diglab_05_01.png" width="825" height="540">

---

# Step 3: เขียน Testcases เพื่อทดสอบ Glitch ของวงจร

ก่อนอื่นให้ไปตั้งค่าที่ `Edit` > `Circuit specific settings` > `Advanced` > `Show measurement graph in single gate step mode at simulation start`

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2005/diglab_05_01/diglab_05_01_pics/diglab_05_01_settings.png" width="600" height="600">

จากนั้นสร้าง Testcases โดยการกด `Components` > `Misc.` > `Test case` แล้วก็วางที่ไหนก็ได้ของวงจรของเรา

เมื่อวางเสร็จแล้วให้ทำการกดคลิกขวาที่ `Test case` แล้วกด `Edit` จากนั้นก็กรอก testcases ที่เราต้องการจะตรวจสอบลงไป ดังนี้
```
A B C D Before
0 0 1 1 1
1 0 1 1 1
1 0 1 1 1
```

เมื่อสร้าง Testcases เสร็จแล้ว เราสามารถทดสอบได้โดยการกด `Run all testcases in the circuit` (ปุ่มเครื่องหมายรันแต่มีติ้กถูกสีเขียว) แล้วกดที่แถบของ testcases อันสุดท้าย ก็จะสามารถตรวจสอบ Glitch ของการเปลี่ยน Input ระหว่าง `0011` เป็น `1011` แบบนี้เลย
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2005/diglab_05_01/diglab_05_01_pics/diglab_05_01_glitch.png" width="956" height="516">
