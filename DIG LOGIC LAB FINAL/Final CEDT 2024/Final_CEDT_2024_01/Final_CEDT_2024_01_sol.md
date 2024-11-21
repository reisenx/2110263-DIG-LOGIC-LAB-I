# Customized Coun (Final_CEDT_2024_01)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1DvqnHA6jqbcGCZNRFNP_SnzFDtsfz0UN/view?usp=drive_link)

---
# Step 1: วิเคราะห์ State Diagram

จากโจทย์ได้กำหนด State Diagram ของ Counter มาดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_01/Final_CEDT_2024_01_pics/Final_CEDT_2024_01_diagram.png" width=60% height=60%>

เพื่อเป็นการประหยัดเวลา เราสามารถใช้งาน `Analysis` ของโปรแกรม Digital ได้
- ไปยังแถบเมนูข้างบน แล้วกดปุ่ม `Analysis`
- จากนั้นกด `Synthesis` แล้วจะมีตารางเด้งขึ้นมาบนหน้าจอ
- เพิ่ม Output ให้มีจำนวน 3 ตัว โดยกดไปที่ `Edit` จากนั้น `Add Output Column`
- เราสามารถเปลี่ยนชื่อของตัวแปรได้โดยการกดคลิกขวาที่ชื่อของตัวแปรนั้นๆ แล้วเปลี่ยนค่า `Label`
- ถ้าหากต้องการเปลี่ยนค่า Output สามารถทำได้โดยการกดคลิกซ้ายที่ตัวเลข แล้วเปลี่ยนเป็นตัวเลขที่ต้องการ
- ฝั่ง Input คือ Current State
- ฝั่ง Output คือ Next State

จาก State Diagram จะสามารถเขียนตาราง Synthesis ได้ออกมาเป็นลักษณะนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_01/Final_CEDT_2024_01_pics/Final_CEDT_2024_01_truth_table.png" width=40% height=40%>

เมื่อกรอกเสร็จสิ้นแล้ว ให้ทำการกด `Create` จากนั้น `Circuit` ตัวโปรแกรม Digital ก็จะสร้างวงจรขึ้นมาอัตโนมัติได้เป็นวงจรลักษณะนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_01/Final_CEDT_2024_01_pics/Final_CEDT_2024_01_combinational.png" width=40% height=40%>

---
# Step 2: ติดตั้ง D Flip-flop บน Counter

ในการต่อวงจร Counter นั้นนิยมใช้งาน D Flip-flop เนื่องจากสามารถออกแบบวงจรง่ายที่สุดในบรรดา Flip-flop ทุกตัว

บนวงจร Counter จะใช้งาน Output `A`, `B` และ `C` ของ State ก่อนหน้า มาใช้เป็น Input ใน State ปัจจุบัน ซึ่งค่าพวกนี้เราจะใช้ D Flip-flop ในการเก็บค่าไว้ทุกๆสัญญาณ `clock` ดังนั้นเราจะต้องต่อวงจรที่มีลักษณะดังภาพ

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_01/Final_CEDT_2024_01_pics/Final_CEDT_2024_01_flipflop.png" width=60% height=60%>

เมื่อลองกด Run วงจร จะเห็นได้ว่าวงจรนี้สามารถนับเลขตาม State Diagram ของโจทย์ได้แล้ว

**หมายเหตุ:** บน `clock` อย่าลืมกดติ๊ก `Start real time clock` ด้วยนะ

---
# Step 3: ติดตั้ง `load` บน Counter

จากโจทย์กล่าวไว้ว่า
- เมื่อ `load` เป็น 1 ค่า `A`, `B` และ `C` จะต้องเป็นไปตามค่า `X`, `Y` และ `Z`
- วงจรนี้ต้องทำงานแบบ synchronous ก็คือจะต้องเปลี่ยนค่าตามสัญญาณ `clock`

ด้วยข้อมูลพวกนี้ จะทราบได้ว่า
- เราจะใช้งาน Multiplexer ให้แสดงผลค่า `X`, `Y` และ `Z` เมื่อ `load` เท่ากับ 1
- เนื่องจากวงจรนี้ต้องทำงานแบบ synchronous ดังนั้นเราจะต้องต่อ Multiplexer บริเวณก่อนหน้า D Flip-flop เพื่อให้ค่า `Output` เกิดการเปลี่ยนแปลงตามสัญญาณ `clock`

จึงได้วงจรที่มีลักษณะดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_01/Final_CEDT_2024_01_pics/Final_CEDT_2024_01_load.png" width=60% height=60%>

---
# Step 4: ติดตั้ง `reset` บน Counter

จากโจทย์กล่าวไว้ว่า
- เมื่อ `reset` เป็น 1 ค่า `A`, `B` และ `C` จะเท่ากับ 0 ทั้งหมด
- ปุ่ม `reset` มีความสำคัญมากที่สุด ก็คือถ้ากดปุ่ม `reset` กับ `load` พร้อมกัน จะถือว่าเป็นการรีเซ็ตค่า ค่า `A`, `B` และ `C` เป็น 0 ทั้งหมด
- วงจรนี้ต้องทำงานแบบ synchronous ก็คือจะต้องเปลี่ยนค่าตามสัญญาณ `clock`

ด้วยข้อมูลพวกนี้ จะทราบได้ว่า
- เราจะใช้งาน Multiplexer ให้แสดงผลค่า `0` เมื่อ `reset` เท่ากับ 1
- เนื่องจากปุ่ม `reset` มีความสำคัญมากกว่าปุ่ม `load` ดังนั้นเราจะต้องต่อ Multiplexer ของปุ่ม `reset` หลัง Multiplexer ของปุ่ม `load`
- เนื่องจากวงจรนี้ต้องทำงานแบบ synchronous ดังนั้นเราจะต้องต่อ Multiplexer บริเวณก่อนหน้า D Flip-flop เพื่อให้ค่า `Output` เกิดการเปลี่ยนแปลงตามสัญญาณ `clock`

จึงได้วงจรที่มีลักษณะดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_01/Final_CEDT_2024_01.png" width=80% height=80%>

เพียงเท่านี้ก็จะได้วงจร Counter มาเรียบร้อยแล้ว

---
# Sample Testcases

```
X Y Z reset load clock A B C
0 0 0 1 0 0 x x x
0 0 0 1 0 1 0 0 0
1 1 0 0 1 0 0 0 0
1 1 0 0 1 1 1 1 0
0 0 0 0 0 0 1 1 0
0 0 0 0 0 1 1 1 1
0 0 0 0 0 0 1 1 1
0 0 0 0 0 1 0 0 1
0 0 0 0 0 0 0 0 1
0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 1 0 0
0 0 0 0 0 1 0 1 0
0 0 0 0 0 0 0 1 0
0 0 0 0 0 1 0 1 1
0 0 0 0 0 0 0 1 1
0 0 0 0 0 1 1 0 1
0 0 0 0 0 0 1 0 1
0 0 0 0 0 1 1 1 1
0 0 0 0 0 0 1 1 1
0 0 0 0 0 1 0 0 1
0 0 0 0 0 0 0 0 1
```