# Counter 74163 (diglab_08_01)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1-Htl6e35KW_D3sOeCGtP83ouiJdpTkGr/view?usp=drive_link)

---
# Step 1: เข้าใจการทำงานของ Counter 74163

## หลักการทำงานของ Counter 74163

**Counter 74163** เป็นวงจรนับเลขฐาน 2 ขนาด 4 Bits จาก `0000` ไป `1111` วนซ้ำไปเรื่อยๆ โดยจะนับเพิ่มทีละ 1 ตามจังหวะ Positive Edge ของสัญญาณ `Clock` ซึ่งวงจรนี้จะมี Input และ Output ดังนี้

### Input
- `D`, `C`, `B` และ `A` ใช้กำหนดค่าเริ่มต้นของการนับ
- `P` และ `T` คือ Enable Input
- `\Load = 0` คือการ SET ค่า `QD`, `QC`, `QB` และ `QA` ตามค่าของ `D`, `C`, `B` และ `A`
- `\Clr = 0` คือการ RESET ค่า `QD`, `QC`, `QB` และ `QA` เป็นค่าเริ่มต้น

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_01/diglab_08_01_pics/diglab_08_01_signalTable.png" width=40% height=40%>

### Output
- `QD`, `QC`, `QB` และ `QA` ใช้แสดงค่าของเลขใน state ปัจจุบัน
- `RCO = 1` ก็ต่อเมื่อวงจรนับถึงเลข `1111`

## ออกแบบวงจร Counter แบบคร่าวๆ
เมื่อนำข้อมูลข้างต้นมาออกแบบวงจรแบบคร่าวๆ จะได้ดังนี้
- ใช้ Adder ในการเพิ่มค่าทีละ 1
- ใช้ Memory (D Flip-flop) ในการเก็บค่า Output ใน state ที่ผ่านมา

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_01/diglab_08_01_pics/diglab_08_01_circuit.jpg" width=60% height=60%>

---

# Step 2: ต่อวงจร Counter 74163

## ต่อวงจรในส่วนของ Input, Output และ Memory
- สร้าง Input `A`, `B`, `C` และ `D` และเชื่อมด้วย Merger ให้เป็นเลขฐานสองขนาด 4 Bits
- เขื่อม Input กับ Memory (D Flip-flop) เพื่อเก็บค่า Output ใน state ที่ผ่านมา
- ใช้ Splitter เพื่อแยกเลขฐานสองขนาด 4 Bits ให้ Output ออกมาเป็น `QA`, `QB`, `QC` และ `QD`
- ใช้ Multiplexer เชื่อมกับ Input เพื่อให้วงจรเก็บค่า `A`, `B`, `C` และ `D` เมื่อ `\Load = 0` เท่านั้น

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_01/diglab_08_01_pics/diglab_08_01_memory.png" width=60% height=60%>

## ต่อวงจรในส่วนของ Adder
- ใช้วงจร Adder ในการบวก Output ใน state ก่อนหน้าเพิ่มอีก 1
- เชื่อมผลบวกกับ Multiplexer ในภาพที่แล้ว โดยให้วงจรเก็บค่าผลบวกจากวงจร Adder เมื่อ `\Load = 1` เท่านั้น
- สามารถแสดงผล `RCO` เป็น $C_{out}$ ของวงจร Adder ได้เลย เพราะว่าในขณะ Output เป็น `1111` ตัววงจร Adder ตอนนั้นมันได้เอา `1111` มาบวก `1` ไปแล้ว ซึงจะได้ $Sum$ เท่ากับ `0000` และ $C_{out}$ เป็น `1` ดังนั้น `RCO` จะแสดงผลเป็น `1` ในขณะที่ Output เป็น `1111` นั่นเอง

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_01/diglab_08_01_pics/diglab_08_01_adder.png" width=60% height=60%>

เนื่องจากวงจรนี้จะนับเลขก็ต่อเมื่อ `P` และ `T` เท่ากับ `1` ทั้งคู่ ถ้าหากมีตัวใดตัวหนึ่งเป็น `0` ให้ HOLD ค่าเดิมเอาไว้ ดังนั้นเราจะต้อง
- ใช้ Multiplexer ที่มีช่องหนึ่งเชื่อมกับวงจร Adder เพื่อให้วงจรบวกเลขไปเรื่อยๆ
- อีกช่องหนึ่งต่อกับ Output ใน State ที่แล้ว เพื่อ HOLD ค่าเดิมเอาไว้
- ใช้ $Selector = PT$ เพื่อให้ Selector เท่ากับ `1` เมื่อ `P` และ `T` เท่ากับ `1` ทั้งคู่เท่านั้น

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_01/diglab_08_01_pics/diglab_08_01_adderEnable.png" width=60% height=60%>

## ต่อวงจรในส่วนของการ Clear

- ถ้าหาก `\Load = 1` และ `\Clear = 0` จะ RESET ค่า Output เป็น `0000`
- ถ้าหาก `\Load = 0` จะ SET ค่า Output เป็น `D`, `C`, `B` และ `A` เสมอ

จากเงื่อนไขที่กล่าวมา เราสามารถต่อ `\Clear` เข้ากับ Multiplexer ตามวงจรได้ดังภาพ

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_01/diglab_08_01.png" width=80% height=80%>

เพียงเท่านี้เราก็จะได้วงจร Counter 74163 ที่เสร็จสมบูรณ์แล้ว