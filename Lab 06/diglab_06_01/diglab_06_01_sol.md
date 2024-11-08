# ALU (diglab_06_01)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1wdO0rKlXc6ZgF-pjNcouAHFiz2i_ggcQ/view?usp=drive_link)

---

# Step 1: พิจารณา Truth Table ของวงจร

**ALU (Arithmetic and Logic Unit)** คือวงจรที่สามารถดำเนินการทางตรรกศาสตร์ (Logical Function) และดำเนินการทางคณิตศาสตร์ (Arithmetic Function) ได้ในตัวเดียว

จากตาราง Truth Table ในโจทย์

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2006/diglab_06_01/diglab_06_01_pics/diglab_06_01_Table.png" width=60% height=60%>

เราจะสามารถปรับรูปแบบของ Truth Table เพื่อให้สามารถต่อวงจรได้ง่ายขึ้น ดังตาราง

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2006/diglab_06_01/diglab_06_01_pics/diglab_06_01_ModTable.png" width=60% height=60%>

ซึ่งจากตารางนี้เอง จะสามารถออกแบบวงจรได้คร่าวๆดังนี้
- ในส่วนของ `Logical Unit` จะมีหน้าที่ตาม Truth Table ในส่วนของ Logical Functions
- ในส่วนของ `Arithmetic Unit` จะมีหน้าที่ตาม Truth Table ในส่วนของ Arithmetic Functions
- ใช้ `Multiplexer 2:1` ในการเลือกว่าจะให้ Output เป็นของ `Logical Unit` หรือ `Arithmetic Unit`

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2006/diglab_06_01/diglab_06_01_pics/diglab_06_01_circuit.jpg" width=60% height=60%>

---

# Step 2: ต่อวงจร Digital ในส่วนของ `Logical Unit`

ต่อวงจรตาม Logical Functions บนตาราง Truth Table

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2006/diglab_06_01/diglab_06_01_pics/diglab_06_01_logic01.png" width=40% height=40%>

จากวงจรแบบคร่าวๆที่เราได้วาดขึ้นมาข้างบน เราจะทราบว่า
- วงจร `Logical Unit` จะมี Input คือ `A` (4 Bits) และ `B` (4 Bits)
- วงจร `Logical Unit` จะมี Selector คือ `S` (3 Bits)
- วงจร `Logical Unit` จะมี Output ขนาด 4 Bits

ซึ่งวงจรที่มีหน้าที่ลักษณะนี้ คือ `Multiplexer 8:1` ดังนั้นเราจะต้องนำวงจรที่ต่อขึ้นมาทั้งหมด มารวมกันได้ดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2006/diglab_06_01/diglab_06_01_pics/diglab_06_01_logic02.png" width=60% height=60%>

---

# Step 3: ต่อวงจร Digital ในส่วนของ `Arithmetic Unit`

จากตาราง Truth Table ในส่วนของ Arithmetic Functions จะสามารถแบ่งประเภทได้ 2 แบบดังนี้

## วงจรบวกเลข (Adder)

ในการบวกเลขในที่นี้ จะใช้ระบบ 2's Complement กล่าวคือ
- `0000` มีค่าเท่ากับ 0
- `1111` มีค่าเท่ากับ -1
- การใช้ NOT Gate กับเลข `A` คือการกลับบิต ซึ่งค่าที่ได้เท่ากับ `-A-1`
- เพื่อความง่ายต่อการตรวจสอบวงจร สามารถตั้งค่าให้ Constant Value ที่ต่อกับวงจร Adder แสดงค่าเป็น Signed decimal ได้ ดังภาพข้างล่าง

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2006/diglab_06_01/diglab_06_01_pics/diglab_06_01_settings.png" width=40% height=40%>

วงจร Adder จะสามารถใส่ได้ 3 Input คือ
- Input `a` และ `b` ให้ใส่เลขที่ต้องการบวก มีขนาดกี่บิตก็ได้ แต่ต้องเท่ากัน
- Input `c` ให้ใส่ตัวทด มีค่าได้แค่ `0` หรือ `1` (ขนาด 1 Bit) เท่านั้น
- Output เป็นค่า `a+b` มีขนาดบิตเท่ากับ `a` และ `b`

เมื่อทราบรายละเอียดข้างบน และดูจาก Truth Table ก็จะสามารถต่อได้ดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2006/diglab_06_01/diglab_06_01_pics/diglab_06_01_arithmetic01.png" width=40% height=40%>

## วงจรเลื่อนบิต (Shifter)

จากโจทย์จะทราบได้ว่า
- `Shift left` จะทิ้งบิตซ้ายสุด และบิตขวาสุดจะเท่ากับ `0`
- `Shift right` จะทิ้งบิตขวาสุด และบิตซ้ายสุดจะเท่ากับ `0`

เราจึงสามารถใช้ Splitter/Merger ในการเลื่อนบิต และใส่ค่า `0` ให้กับบิตซ้ายสุด หรือขวาสุดได้เลย

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2006/diglab_06_01/diglab_06_01_pics/diglab_06_01_arithmetic02.png" width=60% height=60%>

จากวงจรแบบคร่าวๆที่เราได้วาดขึ้นมาข้างบน เราจะทราบว่า
- วงจร `Arithmetic Unit` จะมี Input คือ `A` (4 Bits), `B` (4 Bits) และ `C` (1 Bit)
- วงจร `Arithmetic Unit` จะมี Selector คือ `S` (3 Bits)
- วงจร `Arithmetic Unit` จะมี Output ขนาด 4 Bits

ซึ่งวงจรที่มีหน้าที่ลักษณะนี้ คือ `Multiplexer 8:1` ดังนั้นเราจะต้องนำวงจรที่ต่อขึ้นมาทั้งหมด มารวมกันได้ดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2006/diglab_06_01/diglab_06_01_pics/diglab_06_01_arithmetic03.png" width=60% height=60%>

---

# Step 4: รวมวงจรทั้งหมดเข้าด้วยกัน

ในขั้นตอน 2 และ 3 จะได้วงจรในส่วน `Logical Unit` และ `Arithmetic Unit` มาแล้ว เหลือเพียงนำวงจร 2 ชุดนี้มาต่อเข้าด้วยกันด้วย `Multiplexer 2:1` เท่านั้น ซึ่งจะได้วงจรออกมาลักษณะนี้เลย

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2006/diglab_06_01/diglab_06_01.png" width=100% height=100%>
