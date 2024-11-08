# RS Latch (NOR) (diglab_07_02)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1cgVfOFPNx1t4308w4uD0ok9ajf8SxC4S/view?usp=drive_link)

---
# Combinatorial and Sequential Logic

| Topic | Combinatorial Logic | Sequential Logic |
| :---: | :--- | :--- |
| **Output** | ขึ้นอยู่กับแค่ Input ที่ใส่เข้าไปเท่านั้น | ขึ้นอยู่กับทั้ง Input ที่ใส่เข้าไป และ Output ของ state ก่อนหน้าด้วย |
| **Memory** | ไม่ต้องการ Memory | ต้องการ Memory (เช่น Latch, Filp-flop) เพื่อเก็บข้อมูล Output ใน state ก่อนหน้า |
| **Timing** | Output ออกมาทันทีที่ใส่ Input เข้าไป | เวลาที่ Output ออก ขึ้นอยู่กับสัญญาณ Clock และ Output ใน state ก่อนหน้า |
| **Example** | Multiplexer, Adder, Encoder | Counters, State Machines |

---

# RS Latch Circuit

## หลักการของวงจร RS Latch

- ปุ่ม `R` คือปุ่ม RESET เมื่อกดแล้ว จะทำให้ Output ใน state ถัดไปเท่ากับ `0`
- ปุ่ม `S` คือปุ่ม SET เมื่อกดแล้ว จะทำให้ Output ใน state ถัดไปเท่ากับ `1`
- ถ้าไม่กดอะไรเลย ก็จะค้าง Output เป็นค่าเดิมไปเรื่อยๆ จนกว่าจะมีการกดปุ่มเกิดขึ้น
- ไม่รองรับการกดปุ่ม `R` และ `S` พร้อมกัน

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_02/diglab_07_02_pics/diglab_07_02_table.png" width=40% height=40%>

## ลักษณะวงจร RS Latch

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_02/diglab_07_02.png" width=80% height=80%>