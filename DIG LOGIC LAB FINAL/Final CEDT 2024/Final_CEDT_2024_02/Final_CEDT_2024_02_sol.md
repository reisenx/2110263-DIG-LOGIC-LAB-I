# Maximum Rectangle Area (Final_CEDT_2024_02)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1CnchQMcLPwW56ep3hJi0VOsAiVZoz9JL/view?usp=drive_link)

---
# Step 1: พิจารณาสี่เหลี่ยมที่มีพื้นที่มากที่สุด

## ข้อมูลจากโจทย์
- `W` คือความกว้างของสี่เหลี่ยม (Width)
- `H` คือความยาวของสี่เหลี่ยม (Height)
- `P` คือความยาวเส้นรอบรูปสี่เหลี่ยม (Perimeter)
- `A` คือพื้นที่ของสี่เหลี่ยม (Area)
- กำหนดให้ `W`, `H`, `P` และ `A` เป็นจำนวนเต็มบวก
- กำหนดให้ `W <= 1` และ `H <= 1` โดยที่ `H <= W`
- กำหนดให้ `P = 2(W + H)` และ `A = W x H`

**ตัวอย่าง:** สี่เหลี่ยมที่มีเส้นรอบรูปเท่ากับ 20 (`P = 20`)
- `H = 1` และ `W = 9` จะได้ `A = 9`
- `H = 2` และ `W = 8` จะได้ `A = 16`
- `H = 3` และ `W = 7` จะได้ `A = 21`
- `H = 4` และ `W = 6` จะได้ `A = 24`
- `H = 5` และ `W = 5` จะได้ `A = 25` (พื้นที่มากที่สุด)

ในตัวอย่างนี้ จะได้คำตอบเป็น `H = 5`, `W = 5` และ `A = 25`

ซึ่งเราสามารถพอสังเกตจากตัวอย่างนี้ได้ว่า รูปสี่เหลี่ยมที่มีพื้นที่มากที่สุด น่าจะเป็นรูปสี่เหลี่ยมจัตุรัส ไม่ก็ใกล้เคียงรูปสี่เหลี่ยมจัตุรัสมากที่สุดเท่าที่เป็นไปได้ (เพราะว่า `W` และ `H` ต้องเป็นจำนวนเต็ม)

## พิจารณาโดยใช้ Calculus

เพื่อทำให้ชัดเจนขึ้น เราสามารถใช้ Calculus ในการหาได้ว่า สี่เหลี่ยมของเราจะต้องมีความสูงเท่ากับเท่าไหร่ จึงจะทำให้สี่เหลี่ยมมีพื้นที่มากที่สุด ซึ่งจะต้องทำตามขั้นตอนดังนี้

1. จัดรูปสมการให้อยู่ในรูปของตัวแปรเดียว ซึ่งในที่นี้จะจัดรูป $W$ ให้อยู่ในรูปของ $H$
2. เขียนฟังก์ชันพื้นที่สี่เหลี่ยมให้อยู่ในรูปตัวแปรเดียว ก็คือตัวแปร $H$
3. หาอนุพันธ์ของฟังก์ชันพื้นที่ $A(H) = \frac{P}{2}H - H^{2}$ เทียบกับ $H$
4. พิจารณาที่จุดวิกฤต ก็คือจุดที่ $A'(H) = 0$ ซึ่งเป็นจุดสูงสุดสัมพัทธ์ของฟังก์ชันพื้นที่

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_02/Final_CEDT_2024_02_pics/Final_CEDT_2024_02_calculus.jpg" width=60% height=60%>

**หมายเหตุ:** ความยาวเส้นรอบรูป $P$ เป็นค่าคงที่

---
# Step 2: ต่อวงจรเพื่อคำนวณค่า `W`, `H` และ `A`

## ต่อวงจรคำนวณค่า `W` และ `H`

จากข้อสรุปจากขั้นตอนที่แล้วจะได้ว่า สี่เหลี่ยมที่มี $H = \frac{P}{4}$ จะมีพื้นที่มากที่สุด

แต่เมื่อลองอ่านโจทย์เราจะทราบได้ว่าค่า `P` จะหารด้วย 2 ลงตัวแน่ๆ แต่ไม่การันตีว่า `P` จะหารด้วย 4 ลงตัว เราจึงต้องพิจารณาทั้ง 2 กรณี

- ถ้าหาก `P` หารด้วย 4 ลงตัว จะได้ว่า $W = H = \frac{P}{4}$
- ถ้าหาก `P` หารด้วย 4 แล้วเหลือเศษ 2 จะได้ว่า $H = \left\lfloor \frac{P}{4} \right\rfloor$ และ $W = H + 1$

ซึ่งเราจะสามารถต่อวงจรเพื่อครอบคลุมทั้ง 2 กรณีได้ดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_02/Final_CEDT_2024_02_pics/Final_CEDT_2024_02_calculate.png" width=60% height=60%>

## ต่อวงจรคำนวณค่า `A`

จากที่เราได้ค่า `W` และ `H` มาแล้ว เราก็แค่เอา `W` และ `H` มาต่อวงจรคูณก็จะได้ค่า `A` ออกมาแล้ว

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_02/Final_CEDT_2024_02_pics/Final_CEDT_2024_02_calculate2.png" width=60% height=60%>

---
# Step 3: ต่อวงจรในส่วนของ Memory

ในส่วนของ Memory นั้น เราก็จะใช้ตัวของ D Flip-flop เพราะว่าเป็นตัวที่ใช้ง่ายที่สุดแล้ว

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_02/Final_CEDT_2024_02_pics/Final_CEDT_2024_02_flipflop.png" width=60% height=60%>

---
# Step 4: ต่อวงจรในส่วนของ `start` และ `busy`

## ต่อ Single Pulser กับ `start`

### อ่านเกี่ยวกับ Single Pulser [Click Here!](https://github.com/reisenx/2110263-DIG-LOGIC-LAB-I/blob/main/Lab%2008/diglab_08_05/diglab_08_05_sol.md)

จากที่โจทย์บอกว่า `busy` จะเท่ากับ `1` ก็ต่อเมื่อวงจรกำลังคำนวณค่า `W`, `H` และ `A` อยู่ ถ้าคำนวณเสร็จแล้วให้เปลี่ยนเป็น `0` ทันที

จากที่เราได้ใช้ความรู้ Calculus ไปในขั้นตอนแรก ทำให้เราต้องการใช้ระยะเวลาคำนวณค่า `W`, `H` และ `A` เพียงแค่ 1 clock เท่านั้น

ดังนั้นถ้าเราต้องการให้สัญญาณ `busy` มีค่าเท่ากับ `1` เพียงแค่ 1 clock จะได้ว่าเราสามารถต่อ `start` กับ Single Pulser แล้วให้ Output ออกเป็น `busy` ได้เลย

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_02/Final_CEDT_2024_02_pics/Final_CEDT_2024_02_start.png" width=60% height=60%>

## ต่อ `busy` เข้ากับวงจร

จากโจทย์บอกว่า ถ้าหากคำนวณเสร็จแล้วจะต้องค้างค่าเอาไว้ ถ้ายังไม่ได้กด `reset` ค่า `H`, `W` และ `A` จะต้องไม่เปลี่ยนแปลงถึงแม้ว่าจะมีการเปลี่ยนแปลงค่า `P` ระหว่างนั้นก็ตาม

ในวงจรปัจจุบัน ถ้าหากเราเปลี่ยนค่า `P` ไป ค่า `H`, `W` และ `A` ก็จะเปลี่ยนแปลงตามไปด้วย ซึ่งเราไม่ต้องการให้เป็นเช่นนั้น

ลองสังเกตการทำงานของ D Flip-flop
- เมื่อ `busy` เท่ากับ `1` จะนำค่า `P` มาคำนวณใหม่
- เมื่อ `clock` บน D Flip-flop เท่ากับ `1` จะทำการเก็บค่าใหม่
- เมื่อ `busy` เท่ากับ `0` จะค้างค่า `P` ค่าเดิมเอาไว้
- เมื่อ `clock` บน D Flip-flop เท่ากับ `0` จะค้างค่าเดิมเอาไว้

ดังนั้นเราสามารถต่อ `busy` เข้ากับ `clock` ของ D Flip-flop เพื่อ HOLD ค่าหรือ SET ค่าใหม่ได้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_02/Final_CEDT_2024_02_pics/Final_CEDT_2024_02_start2.png" width=60% height=60%>

---
# Step 5: ต่อวงจรในส่วนของ `reset`

ในส่วนนี้ก็เป็นส่วนสุดท้ายของการต่อวงจรแล้ว โดยเมื่อมีการกดปุ่ม `reset` นั้น จะรีเซ็ตทุกค่าวงจรให้กลับไปเป็นค่าเริ่มต้น ก็คือ

- ค่า `W`, `H` และ `A` เท่ากับ `0` ทั้งหมด
- ค่า `busy` เท่ากับ `0`

## ต่อ `reset` เข้ากับวงจรหลัก

- ใช้งาน Multiplexer ให้ output ค่า `0` ออกมา เมื่อค่า `reset` เท่ากับ `1`
- เนื่องจากวงจรเป็นแบบ synchronous จึงต้องต่อ Multiplexer หน้า `clock` ของ D Flip-flop ที่ใช้เก็บ Memory
- ในระหว่างที่ `reset` เท่ากับ `1` ไม่ว่าจะเปลี่ยนแปลงค่า `P` อย่างไร ค่าจะต้องเป็น `0` ตลอด จึงต้องต่อ Multiplexer หลัง D Flip-flop ที่ใช้ HOLD และ SET ค่า

เราจะต่อ `reset` เข้ากับวงจรหลักได้ดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_02/Final_CEDT_2024_02_pics/Final_CEDT_2024_02_reset.png" width=60% height=60%>

## ต่อ `reset` เข้ากับ `busy`

- ในระหว่างที่ `reset` เท่ากับ `1` ค่า `busy` จะต้องเท่ากับ `0`
- เนื่องจากวงจรเป็นแบบ synchronous เราจะไม่สามารถต่อ `reset` กับค่า `busy` โดยตรงได้ เราจะต้องนำ `reset` ไปต่อกับ `start` แทน

ซึ่งสามารถต่อวงจรออกมาได้ดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_02/Final_CEDT_2024_02.png" width=80% height=80%>

เพียงเท่านี้ วงจรของเราก็เป็นอันเสร็จสิ้น