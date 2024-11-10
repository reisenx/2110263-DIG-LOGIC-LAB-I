# Serial Adder (diglab_08_02)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1lYRzRPoFt2EDzB2NOLTPXLn_0udDn-V9/view?usp=drive_link)

---
# Step 1: Finite State Machine

### อ่านเกี่ยวกับ Combinational and Sequential Logic [Click Here!](https://github.com/reisenx/2110263-DIG-LOGIC-LAB-I/blob/main/Lab%2007/diglab_07_02/diglab_07_02_sol.md#combinational-and-sequential-logic)

### เนื้อหาส่วนนี้อ้างอิงมาจากคลิปวีดิโอ
- Finite State Machine Explained By ALL ABOUT ELECTRONICS [Click Here!](https://youtu.be/kb-Ww8HaHuE?si=wfXp5DtsXp9Oxp97)

## Finite State Machine คืออะไร

**Finite State Machine** คือวงจรแบบ Sequential Logic ที่มีสถานะ (state) ของวงจรออกเป็นหลายๆสถานะ โดย state ปัจจุบัน ของวงจรจะเปลี่ยนแปลงขึ้นอยู่กับ Input และ state ก่อนหน้า
- เราสามารถเขียนความสัมพันธ์ของแต่ละ state ในวงจรด้วย State Diagram
- แต่ละ state จะแทนด้วยช่องวงกลม พร้อมระบุค่าของ state นั้นๆ
- ลูกศรที่ชี้ระหว่าง state แสดงการเปลี่ยนแปลงไปยัง state ต่างๆ เมื่อใส่ Input ที่เขียนไว้บนลูกศร

**ตัวอย่าง:** State Diagram ของ RS Latch

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_02/diglab_08_02_pics/diglab_08_02_stateDiagram.jpg" width=60% height=60%>


Finite State Machine จะสามารถแบ่งออกได้เป็น 2 ประเภทคือ Mealy Machine และ Moore Machine

## Mealy Machine
**Mealy Machine** คือวงจรที่ใช้งาน Input ทั้งในวงจรในการหา state ถัดไป และในวงจรที่หา Output ด้วย

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_02/diglab_08_02_pics/diglab_08_02_mealy.png" width=60% height=60%>

## Moore Machine
**Moore Machine** คือวงจรที่ใช้งาน Input ในวงจรในการหา state ถัดไปเพียงอย่างเดียว

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_02/diglab_08_02_pics/diglab_08_02_moore.png" width=60% height=60%>

---

# Step 2: เข้าใจการทำงานของ Serial Adder

### เนื้อหาส่วนนี้อ้างอิงมาจากคลิปวีดิโอ
- Serial Adder Explained By ALL ABOUT ELECTRONICS [Click Here!](https://youtu.be/mhHwA_f4qpc?si=RcLhvR4Bf-Io7zwk)

## หลักการทำงานของ Serial Adder
- `A` และ `B` ใช้เก็บเลขที่จะนำมาบวกกัน
- `S` ใช้เก็บผลบวก `A + B`
- ค่า $C_{out}$ ถูกเก็บไว้ใน Memory (D Flip-flop) เพื่อใช้เป็น $C_{in}$ ในการบวกเลขหลักถัดไป

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_02/diglab_08_02_pics/diglab_08_02_serialAdder.png" width=60% height=60%>

---

# Step 3: ต่อวงจร Serial Adder

## ต่อ Serial Adder แบบที่ยังไม่มีปุ่ม `\Clear`

- ต่อ Input `A` และ `B` เข้ากับ Adder
- ต่อ Output `Z` เข้ากับ Adder
- ต่อ $C_{out}$ เข้ากับ D Flip-flop เพื่อเก็บตัวทดไปใช้กับการบวกเลขหลักถัดไป

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_02/diglab_08_02_pics/diglab_08_02_adder.png" width=60% height=60%>

## ต่อปุ่ม `\Clear` เข้าไปในวงจร

เนื่องจากว่าโจทย์ต้องการในต่อวงจรแบบ Mealy Machine เราจึงสามารถต่อ Input `\Clear` กับวงจรที่หา Output `Z` ได้โดยตรง
- ต่อ Multiplexer ให้ RESET `Z = 0` เมื่อ `\Clear = 0`
- ต่อ Multiplexer ให้ RESET Memory ที่เก็บตัวทดให้เท่ากับ 0 เมื่อ `\Clear = 0`

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_02/diglab_08_02.png" width=80% height=80%>

เพียงเท่านี้ก็จะได้ Serial Adder ขนาด 1 Bit ที่เป็น Mealy Machine แล้ว