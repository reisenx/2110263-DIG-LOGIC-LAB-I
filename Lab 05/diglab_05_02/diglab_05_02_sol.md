# Glitch II (diglab_05_02)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1rwpKxKqkvpPQrHwt-uyCA7oQgyZU3fYO/view?usp=drive_link)

---

# Step 1: เขียน K-map เพื่อพิจารณา Hazard ที่เกิดขึ้น
## $Before(A,B,C,D,E) = \Sigma m(0,1,3,4,7,11,12,15,16,17,20,28)$
$Before = A'B'C'D'E' + A'B'C'D'E + A'B'C'DE + A'B'CD'E' + A'B'CDE + A'BC'DE + A'BCD'E' + A'BCDE + AB'C'D'E' + AB'C'D'E + AB'CD'E' + ABCD'E'$
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2005/diglab_05_02/diglab_05_02_pics/diglab_05_02_Kmap01.jpg" width=60% height=60%>

จาก K-map จะเห็นได้ว่าวงจรของ `Before` นั้นจะเป็นการต่อ minterm แบบตรงๆเลย ทำให้สามารถ Static 1-Hazard เมื่อมีการกระโดดข้าม minterm ได้ ดังนั้นเราจึงต้องทำการครอบบริเวณช่องบน K-map เพื่อไม่ให้เกิด Hazard ได้ ดังภาพต่อไปนี้
## $After = CD'E' + B'C'D' + A'DE + B'D'E' + A'B'C'E$
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2005/diglab_05_02/diglab_05_02_pics/diglab_05_02_Kmap02.jpg" width=60% height=60%>

เพียงแค่นี้เราก็จะวงจรที่ไม่เกิด Hazard (Hazard-free) เป็นที่เรียบร้อย

---

# Step 2: ต่อวงจร Digital ของ `Before` และ `After`
$Before = A'B'C'D'E' + A'B'C'D'E + A'B'C'DE + A'B'CD'E' + A'B'CDE + A'BC'DE + A'BCD'E' + A'BCDE + AB'C'D'E' + AB'C'D'E + AB'CD'E' + ABCD'E'$
## $After = CD'E' + B'C'D' + A'DE + B'D'E' + A'B'C'E$
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2005/diglab_05_02/diglab_05_02.png" width=100% height=100%>

---

# Step 3: เขียน Testcases เพื่อทดสอบ Glitch ของวงจร

ก่อนอื่นให้ไปตั้งค่าที่ `Edit` > `Circuit specific settings` > `Advanced` > `Show measurement graph in single gate step mode at simulation start`

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2005/diglab_05_01/diglab_05_01_pics/diglab_05_01_settings.png" width=60% height=60%>

จากนั้นสร้าง Testcases โดยการกด `Components` > `Misc.` > `Test case` แล้วก็วางที่ไหนก็ได้ของวงจรของเรา

เมื่อวางเสร็จแล้วให้ทำการกดคลิกขวาที่ `Test case` แล้วกด `Edit` จากนั้นก็กรอก testcases ที่เราต้องการจะตรวจสอบลงไป ดังนี้

(หลักคือเขียน testcases ทั้งหมด ที่การเปลี่ยนแปลงข้าม minterm ทีละ 1 ช่องบน K-map)

```
A B C D E Before After
1 1 1 0 0 1 1
1 0 1 0 0 1 1
1 0 0 0 0 1 1
1 0 0 0 1 1 1
0 1 1 0 0 1 1
0 0 1 0 0 1 1
0 0 0 0 0 1 1
0 0 0 0 1 1 1
0 0 0 1 1 1 1
0 0 1 1 1 1 1
0 1 1 1 1 1 1
0 1 0 1 1 1 1
```

เมื่อสร้าง Testcases เสร็จแล้ว เราสามารถทดสอบได้โดยการกด `Run all testcases in the circuit` (ปุ่มเครื่องหมายรันแต่มีติ้กถูกสีเขียว) แล้วกดที่แถบของ testcases อันสุดท้าย ก็จะสามารถตรวจสอบ Glitch ของการเปลี่ยน Input ระหว่าง `0011` เป็น `1011` แบบนี้เลย
<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/main/Lab%2005/diglab_05_02/diglab_05_02_pics/diglab_05_02_glitch.png" width=80% height=80%>
