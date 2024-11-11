# Mealy Single Pulser (diglab_08_02)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1fxxtJ6EBOt1pud1IWCopFBBKMG1IgAq4/view?usp=drive_link)

---
# Step 1: เข้าใจหลักการทำงานของ Single Pulser

### อ่านเกี่ยวกับ Finite State Machine [Click Here!](https://github.com/reisenx/2110263-DIG-LOGIC-LAB-I/blob/main/Lab%2008/diglab_08_02/diglab_08_02_sol.md#step-1-finite-state-machine)

## Single Pulser คืออะไร
**Single Pulser** เป็นวงจรที่สามารถสร้างสัญญาณ pulse ได้ในช่วงระยะเวลาหนึ่ง ซึ่งมีลักษณะดังนี้
- ถ้าหากไม่มีการกดปุ่ม ก็ไม่ต้องทำอะไร
- ถ้าหากมีการกดปุ่ม `Input` วงจรนี้จะส่งสัญญาณ pulse ออกมาทาง `Output` ความยาว 1 clock
- ไม่ว่าจะกดปุ่ม `Input` นานแค่ไหน สัญญาณที่ออกมาทาง `Output` ก็จะออกมาแค่ครั้งเดียวเท่านั้น ถ้าอยากให้ `Output` ส่งสัญญาณใหม่ ต้องปล่อยและกดปุ่ม `Input` ใหม่อีกครั้ง

เพื่อทำให้เห็นภาพยิ่งขึ้น สามารถดูภาพ Time Diagram ของวงจร Single Pulser ได้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_03/diglab_08_03_pics/diglab_08_03_time.png" width=40% height=40%>

---

# Step 2: ต่อวงจร Single Pulser

## สังเกตการทำงานของ D Flip-flop

- ค่าเริ่มต้นของ `Q'` บน D Flip-flop คือ `1`
- D Flip-flop จะ SET ค่า `Q` ให้เท่ากับ `D` ตามสัญญาณ Clock

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_03/diglab_08_03_pics/diglab_08_03_Dflipflop01.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_03/diglab_08_03_pics/diglab_08_03_Dflipflop02.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_03/diglab_08_03_pics/diglab_08_03_Dflipflop03.png" width=60% height=60%>

## ต่อ AND Gate เข้ากับ D Flip-flop

- ค่าเริ่มต้นของ `Q'` บน D Flip-flop คือ `1`
- D Flip-flop จะ SET ค่า `Q` ให้เท่ากับ `D` ตามสัญญาณ Clock
- เนื่องจาก D Flip-flop SET ค่า `Q` ตามสัญญาณ Clock ดังนั้นก่อนหน้าที่จะเกิดการ SET จะเห็นว่าค่า `Q' = 1` และ `D = 1` พร้อมกัน
- เราสามารถตรวจสอบว่า `Q' = 1` และ `D = 1` พร้อมกัน โดยการใช้ AND Gate

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_03/diglab_08_03_pics/diglab_08_03_delay01.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_03/diglab_08_03_pics/diglab_08_03_delay02.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_03/diglab_08_03_pics/diglab_08_03_delay03.png" width=60% height=60%>

## เพิ่มระยะเวลาสัญญาณ Pulse
จากขั้นตอนที่แล้ว ก็จะเห็นได้ว่าตอนนี้วงจรของเราพอส่งสัญญาณ Pulse ได้แล้ว แต่สัญญาณสั้นจนเกินไป และโจทย์ต้องการให้สัญญาณ Pulse มีความยาวเท่ากับ 1 clock ไม่ใช่ติดแล้วดับทันทีแบบในภาพของขั้นตอนที่แล้ว

- เนื่องจากโจทย์ต้องการให้ต่อแบบ Mealy Machine ดังนั้นค่า `P` สามารถต่อกับ AND Gate ได้เลย เพราะถือว่า AND Gate เป็น Output Combinational Logic
- สามารถเพิ่มระยะเวลาสัญญาณ Pulse ให้มีความยาว 1 clock ด้วยการต่อ D Flip-flop เพิ่มไปอีกตัว

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_03/diglab_08_03_pics/diglab_08_03_moreDelay01.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_03/diglab_08_03_pics/diglab_08_03_moreDelay02.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_03/diglab_08_03_pics/diglab_08_03_moreDelay03.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_03/diglab_08_03_pics/diglab_08_03_moreDelay04.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_03/diglab_08_03_pics/diglab_08_03_moreDelay05.png" width=60% height=60%>

## ต่อ `\Clr` เข้ากับวงจร

- เนื่องจากว่า `\Clr` เป็น Synchronous Input ดังนั้นเราไม่สามารถนำ `\Clr` ไปต่อกับ Gate บนวงจรได้โดยตรง แต่ต้องต่อกับ Input `P` เท่านั้น
- วงจรจะทำงานก็ต่อเมื่อ `P = 1` และ `\Clr = 0` ดังนั้นเราสามารถต่อ `P` และ `\Clr` ได้ด้วย AND Gate ที่บริเวณ Input ของวงจรดังภาพ

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_03/diglab_08_03.png" width=80% height=80%>

เพียงเท่านี้ก็จะได้วงจร Single Pulser ที่เป็น Mealy Machine แล้ว