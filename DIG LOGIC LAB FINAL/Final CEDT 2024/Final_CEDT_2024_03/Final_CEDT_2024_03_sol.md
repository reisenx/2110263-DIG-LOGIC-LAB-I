# Increasing Number (Final_CEDT_2024_03)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1QeVnTaI-H_FD2S3z-QFDiky2BOBAemHI/view?usp=drive_link)

---
# Step 1: ต่อวงจรในส่วน Memory

ในส่วนของ Memory ของวงจรนี้นั้น จะใช้ D Flip-flop เพราะใช้งานง่ายที่สุด

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_03/Final_CEDT_2024_03_pics/Final_CEDT_2024_03_flipflop.png" width=60% height=60%>

---
# Step 2: ต่อวงจรในส่วนของ `new` และ `busy`

ในขั้นตอนนี้เราต้องการจะต่อวงจรที่ทำสิ่งนี้ได้

- ค่า `max` เปลี่ยนแปลงเมื่อมีการกด `new` เท่านั้น
- ค่า `max` เปลี่ยนแปลงเพียงแค่ 1 ครั้ง ต่อการกดปุ่ม `new` 1 ครั้ง ถ้าหากมีการเปลี่ยนแปลง `N` ระหว่างที่กดปุ่ม `new` ค้างไว้อยู่ ค่า `max` จะต้องไม่เปลี่ยนแปลง ค้างค่าเดิมไว้เรื่อยๆ
- เนื่องจากวงจรนี้สามารถทำงานเสร็จได้ภายใน 1 clock ดังนั้น `busy` จะต้องมีค่าเป็น `1` ในช่วงระยะเวลา 1 clock เท่านั้น

## ต่อ Single Pulser กับ `start`

### อ่านเกี่ยวกับ Single Pulser [Click Here!](https://github.com/reisenx/2110263-DIG-LOGIC-LAB-I/blob/main/Lab%2008/diglab_08_05/diglab_08_05_sol.md)

จากที่เราต้องการให้ `busy` มีค่าเป็น `1` ในช่วงระยะเวลา 1 clock เท่านั้น เราจะสามารถทำได้โดยการต่อ Single Pulser กับ `start` แล้วให้ output ออกมาเป็น `busy` ได้เลย ซึ่งจะได้วงจรดังภาพ

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_03/Final_CEDT_2024_03_pics/Final_CEDT_2024_03_new.png" width=60% height=60%>

## ต่อ `busy` เข้ากับวงจรหลัก

จากที่เราต้องการให้ค่า `max` มีการเปลี่ยนแปลงเมื่อค่าก็ต่อเมื่อมีการกดปุ่ม `new` ไว้เท่านั้น ที่เหลือจะต้องค่าเดิมเอาไว้ ไม่มีการเปลี่ยนแปลงใดๆ จนกว่าจะปล่อยและกดปุ่ม `new` อีกครั้ง

ลองสังเกตการทำงานของ D Flip-flop
- เมื่อ `busy` เท่ากับ `1` จะนำค่า `N` มาเก็บไว้ใน `max`
- เมื่อ `clock` บน D Flip-flop เท่ากับ `1` จะทำการเก็บค่าใหม่
- เมื่อ `busy` เท่ากับ `0` จะค้างค่า `max` ค่าเดิมเอาไว้
- เมื่อ `clock` บน D Flip-flop เท่ากับ `0` จะค้างค่าเดิมเอาไว้

ดังนั้นเราสามารถต่อ `busy` เข้ากับ `clock` ของ D Flip-flop เพื่อ HOLD ค่าหรือ SET ค่าใหม่ได้ ซึ่งจะได้วงจรดังภาพ

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_03/Final_CEDT_2024_03_pics/Final_CEDT_2024_03_new2.png" width=60% height=60%>

---
# Step 3: ต่อวงจรในส่วนของตัวเปรียบเทียบ (Comparator)

ในโปรแกรม Digital จะมีเครื่องมือที่เรียกว่า Comparator อยู่ โดยมีหลักการการทำงานดังนี้

- ถ้า Input `a > b` Output บนช่อง `>` จะมีค่าเท่ากับ `1`
- ถ้า Input `a = b` Output บนช่อง `=` จะมีค่าเท่ากับ `1`
- ถ้า Input `a < b` Output บนช่อง `<` จะมีค่าเท่ากับ `1`

จากข้อมูลดังกล่าวจะสามารถนำมาต่อวงจรได้ดังนี้

- ถ้าหากช่อง `>` เท่ากับ `1` ให้ Enable เอาค่าไปใส่ใน Memory ได้
- ถ้าหากช่อง `>` เท่ากับ `0` จะไม่ Enable และไม่สามารถเอาไปใส่ใน Memory ได้
- ใช้สัญญาณจากช่อง `>` เป็น clock ของ D Flip-flop เพราะ D Flip-flop ทำงานเมื่อ clock เท่ากับ `1` เท่านั้น กล่าวคือ D Flip-flop จะทำการ SET ค่าใหม่เมื่อ clock เป็น `1` เท่านั้น

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_03/Final_CEDT_2024_03_pics/Final_CEDT_2024_03_compare.png" width=60% height=60%>

---
# Step 4: ต่อวงจรในการนับ `num_inc`

จากขั้นตอนที่แล้ว จะพอทราบได้ว่าเราจะต้องต่อวงจรที่ทำงานดังนี้

- เมื่อสัญญาณจากช่อง `>` เป็น `0` ค่า `num_inc` จะต้องไม่มีการเปลี่ยนแปลงใดๆ
- เมื่อสัญญาณจากช่อง `>` เป็น `1` จะต้องเพิ่ม `num_inc` ไปอีก `1`

ซึ่งจากข้อมูลดังกล่าว เราใช้อุปกรณ์ในการต่อวงจรดังนี้

- ใช้งาน Adder ในการบวก `num_inc` เพิ่มไปอีก `1`
- ใช้งาน D Flip-flop เป็นตัว Enable ที่ต่อ clock เข้ากับสัญญาณ `>` ของ Comparator (สัญญาณ `>` ต้องเป็น `1` เท่านั้นจึงจะมีการอัปเดตค่า)
- ใช้งาน D Flip-flop อีกตัวเป็น Memory เพื่อเก็บค่า `num_inc`

ดังนั้นเราจะสามารถต่อวงจรในการนับ `num_inc` ได้ออกมาแบบนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_03/Final_CEDT_2024_03_pics/Final_CEDT_2024_03_count.png" width=80% height=80%>

---
# Step 5: ต่อวงจรในส่วน `reset`

จากโจทย์ได้ให้ข้อมูลเกี่ยวกับการทำงานของ `reset` มาดังนี้

- เมื่อ `reset` มีค่าเท่ากับ `0` วงจรจะทำงานตามปกติ
- เมื่อ `reset` มีค่าเท่ากับ `1` จะทำให้ค่า `max` และ `num_inc` เป็น `0` ทั้งคู่
- เมื่อ `reset` มีค่าเท่ากับ `1` จะทำให้ค่า `busy` มีค่าเป็น `0`

## ต่อ `reset` เข้ากับวงจรหลัก

ในส่วนนี้เราจะต่อ `reset` เพื่อ RESET ค่า `max` และ `num_inc` เป็น `0` ทั้งคู่ได้

- เราจะใช้ Multiplexer ให้ output ค่าเป็น `0` เมื่อ `reset` มีค่าเท่ากับ `1`
- เนื่องจากวงจรนี้เป็นแบบ synchronous ดังนั้นเราจะต้องต่อ Multiplexer ก่อนหน้า D Flip-flop ที่เป็น Memory เพื่อค่าเปลี่ยนแปลงเป็น `0` ตามสัญญาณ clock
- ไม่ว่าเราจะใส่ค่าอะไรระหว่างที่ `reset` เท่ากับ `1` ค่าของ `max` และ `num_inc` จะต้องเป็น `0` ตลอดไม่เปลี่ยนแปลง ดังนั้นเราจะต้องต่อ Multiplexer อยู่หลัง D Flip-flop ที่เป็น Enable

เราจึงสามารถต่อวงจรออกมาได้แบบนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_03/Final_CEDT_2024_03_pics/Final_CEDT_2024_03_reset.png" width=80% height=80%>

## ต่อ `reset` เข้ากับ `busy`

จากที่เราทราบว่า เมื่อค่า `reset` เท่ากับ `1` นั้น ค่า `busy` จะต้องเท่ากับ `0` ดังนั้นเราจึงจำเป็นที่จะต้องต่อ `reset` เพื่อจัดการกับค่า `busy` ด้วย

จากที่วงจรนี้เป็นแบบ synchronous เราไม่สามารถต่อ `reset` เข้ากับ `busy` ได้โดยตรงได้ เพราะว่าการเปลี่ยนแปลงค่าจะต้องเป็นไปตามสัญญาณ `clock` ดังนั้นเราจะต่อ `reset` เข้ากับ `new` แทน

และเมื่อต่อ `reset` เข้ากับ `new` ก็จะได้วงจรที่มีลักษณะดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/DIG%20LOGIC%20LAB%20FINAL/Final%20CEDT%202024/Final_CEDT_2024_03/Final_CEDT_2024_03.png" width=80% height=80%>

เพียงเท่านี้วงจรก็เป็นอันเสร็จสิ้นแล้ว