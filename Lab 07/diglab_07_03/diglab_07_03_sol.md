# Master-Slave JK Flip-flop (diglab_07_03)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1Vu4y7l2ZnqPItOq-FGoYFCJG_-sVJYZJ/view?usp=drive_link)

---
# Step 1: เข้าใจการทำงานของ Master-Slave JK Flip-flop

## หลักการทำงานของ JK Flip-flop
- ปุ่ม `J` คือปุ่ม SET เมื่อกดแล้ว จะทำให้ Output ใน state ถัดไปเท่ากับ `1`
- ปุ่ม `K` คือปุ่ม RESET เมื่อกดแล้ว จะทำให้ Output ใน state ถัดไปเท่ากับ `0`
- ถ้าไม่กดอะไรเลย ก็จะค้าง Output เป็นค่าเดิมไปเรื่อยๆ จนกว่าจะมีการกดปุ่มเกิดขึ้น
- เมื่อกดปุ่ม `J` และ `K` พร้อมกัน จะเกิดการ Toggle คือ Output จะสลับค่า `0` และ `1` ไปเรื่อยๆทุกๆสัญญาณ `Clock = 1`
- วงจร JK Flip-flop ทำงานเมื่อสัญญาณ `Clock = 1` เท่านั้น

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_03/diglab_07_03_pics/diglab_07_03_JKtable.png" width=40% height=40%>

## หลักการทำงานของ Master-Slave JK Flip-flop
- วงจรแบบ Master-Slave จะประกอบไปด้วย 2 Stage คือ Master Stage และ Slave Stage
- เมื่อสัญญาณ `Clock = 1` จะพบว่าวงจร JK Flip-flop ที่เป็น Master Stage จะเปลี่ยนแปลงค่า แต่ Slave Stage จะยังไม่เปลี่ยนแปลงค่า
- เมื่อสัญญาณ `Clock = 0` (สัญญาณถัดไป) วงจร JK Flip-flop ที่เป็น Slave Stage ค่อยเปลี่ยนแปลงค่าตาม Master Stage

## ลักษณะวงจร Master-Slave JK Flip-flop
วงจร Master-Slave JK Flip-flop ที่ยังไม่มีปุ่ม `\Clear` มีลักษณะดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_03/diglab_07_03_pics/diglab_07_03_JK_MS.png" width=60% height=60%>

---

# Step 2: สังเกตวงจร Master-Slave JK Flip-flop

## Master-Slave JK Flip-flop (SET)

| Step | `Clock` | `J` | `K` | `P` | `Q` | Description |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | 0 | 1 | 0 | 0 | 0 | สถานะเริ่มต้น ยังไม่มีการเปลี่ยนแปลง |
| 2 | 1 | 1 | 0 | 1 | 0 | Master Stage เปลี่ยนค่า `P = 1` |
| 3 | 0 | 1 | 0 | 1 | 1 | Slave Stage เปลี่ยนค่า `Q = 1` |

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_03/diglab_07_03_pics/diglab_07_03_JK01_01.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_03/diglab_07_03_pics/diglab_07_03_JK01_02.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_03/diglab_07_03_pics/diglab_07_03_JK01_03.png" width=60% height=60%>

## Master-Slave JK Flip-flop (RESET)

| Step | `Clock` | `J` | `K` | `P` | `Q` | Description |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | 0 | 0 | 1 | 1 | 1 | สถานะเริ่มต้น ยังไม่มีการเปลี่ยนแปลง |
| 2 | 1 | 0 | 1 | 0 | 1 | Master Stage เปลี่ยนค่า `P = 0` |
| 3 | 0 | 0 | 1 | 0 | 0 | Slave Stage เปลี่ยนค่า `Q = 0` |

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_03/diglab_07_03_pics/diglab_07_03_JK02_01.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_03/diglab_07_03_pics/diglab_07_03_JK02_02.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_03/diglab_07_03_pics/diglab_07_03_JK02_03.png" width=60% height=60%>

## Master-Slave JK Flip-flop (TOGGLE)

| Step | `Clock` | `J` | `K` | `P` | `Q` | Description |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | 0 | 1 | 1 | 0 | 0 | สถานะเริ่มต้น ยังไม่มีการเปลี่ยนแปลง |
| 2 | 1 | 1 | 1 | 1 | 0 | Master Stage เปลี่ยนค่า `P = 1` |
| 3 | 0 | 1 | 1 | 1 | 1 | Slave Stage เปลี่ยนค่า `Q = 1` |
| 4 | 1 | 1 | 1 | 0 | 1 | Master Stage เปลี่ยนค่า `P = 0` |
| 5 | 0 | 1 | 1 | 0 | 0 | Slave Stage เปลี่ยนค่า `Q = 0` |

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_03/diglab_07_03_pics/diglab_07_03_JK03_01.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_03/diglab_07_03_pics/diglab_07_03_JK03_02.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_03/diglab_07_03_pics/diglab_07_03_JK03_03.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_03/diglab_07_03_pics/diglab_07_03_JK03_04.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_03/diglab_07_03_pics/diglab_07_03_JK03_05.png" width=60% height=60%>

---

# Step 3: ต่อ `\Clear` เข้ากับวงจร Master-Slave JK Flip-flop

จากขั้นตอนที่ 2 เราจะเห็นได้ว่า การที่จะทำให้ค่า `Q` เท่ากับ `1` ได้นั้น จะเกิดขึ้นได้จาก
- บน Master Stage มีการ Output ค่า `P` เท่ากับ `1`
- บน Slave Stage มีการ Output ค่า `Q` เท่ากับ `1`

จากที่ `\Clear` เป็น Asynchronous Input ก็คือถ้าหากกดปุ่ม `\Clear` ก็จะทำให้ค่า `Q` เท่ากับ `0` ทันทีโดยที่ไม่ขึ้นกับสัญญาณ `Clock` นั่นหมายความว่าเราสามารถต่อ `\Clear` เข้ากับ Gate บนวงจรได้โดยตรง

จากที่ NOR Gate จะ Output เป็น `1` ก็ต่อเมื่อ Input ทั้งหมดเท่ากับ `0` เท่านั้น เราก็จะได้ว่า
- ถ้าหากต่อ `\Clear` เข้ากับ NOR Gate ที่ Output `P` ก็จะได้ว่าเมื่อ `\Clear = 1` จะได้ `P` เท่ากับ `0` เสมอ
- ถ้าหากต่อ `\Clear` เข้ากับ NOR Gate ที่ Output `Q` ก็จะได้ว่าเมื่อ `\Clear = 1` จะได้ `Q` เท่ากับ `0` เสมอ

ดังนั้นเราจะสามารถต่อวงจร Master-Slave JK Flip-flop ที่มีปุ่ม `\Clear` ได้ดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_03/diglab_07_03.png" width=80% height=80%>