# Moore Single Pulser (diglab_08_05)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1Xt7Xsm7_B7kqhWxjrkc16WKNJ4SE_HX7/view?usp=drive_link)

---
# Step 1: เข้าใจหลักการทำงานของ Single Pulser

### อ่านเกี่ยวกับ Finite State Machine [Click Here!](https://github.com/reisenx/2110263-DIG-LOGIC-LAB-I/blob/main/Lab%2008/diglab_08_02/diglab_08_02_sol.md#step-1-finite-state-machine)

## Single Pulser คืออะไร
**Single Pulser** เป็นวงจรที่สามารถสร้างสัญญาณ pulse ได้ในช่วงระยะเวลาหนึ่ง ซึ่งมีลักษณะดังนี้
- ถ้าหากไม่มีการกดปุ่ม ก็ไม่ต้องทำอะไร
- ถ้าหากมีการกดปุ่ม `Input` วงจรนี้จะส่งสัญญาณ pulse ออกมาทาง `Output` ความยาว 1 clock
- ไม่ว่าจะกดปุ่ม `Input` นานแค่ไหน สัญญาณที่ออกมาทาง `Output` ก็จะออกมาแค่ครั้งเดียวเท่านั้น ถ้าอยากให้ `Output` ส่งสัญญาณใหม่ ต้องปล่อยและกดปุ่ม `Input` ใหม่อีกครั้ง

เพื่อทำให้เห็นภาพยิ่งขึ้น สามารถดูภาพ Time Diagram ของวงจร Single Pulser ได้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05_pics/diglab_08_05_time.png" width=40% height=40%>

---

# Step 2: สังเกตการทำงานของ D Flip-flop

- ค่าเริ่มต้นของ `Q'` บน D Flip-flop คือ `1`
- D Flip-flop จะ SET ค่า `Q` ให้เท่ากับ `D` ตามสัญญาณ Clock

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05_pics/diglab_08_05_Dflipflop01.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05_pics/diglab_08_05_Dflipflop02.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05_pics/diglab_08_05_Dflipflop03.png" width=60% height=60%>

---

# Step 3: เพิ่มระยะเวลาสัญญาณ Pulse

จากขั้นตอนที่แล้ว ก็จะเห็นได้ว่าตอนนี้วงจรของเราพอส่งสัญญาณ Pulse ได้แล้ว แต่สัญญาณสั้นจนเกินไป และโจทย์ต้องการให้สัญญาณ Pulse มีความยาวเท่ากับ 1 clock ไม่ใช่ติดแล้วดับทันทีแบบในภาพของขั้นตอนที่แล้ว

- สามารถเพิ่มระยะเวลาสัญญาณ Pulse ให้มีความยาว 1 clock ด้วยการต่อ D Flip-flop เพิ่มไปอีกตัว

### เมื่อกดปุ่ม `P` จะมีการส่งสัญญาณ pulse 1 ครั้ง

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05_pics/diglab_08_05_delay01.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05_pics/diglab_08_05_delay02.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05_pics/diglab_08_05_delay03.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05_pics/diglab_08_05_delay04.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05_pics/diglab_08_05_delay05.png" width=60% height=60%>

### เมื่อปล่อยปุ่ม `P` จะเข้าสู่สถานะปกติ (`Z = 1`)

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05_pics/diglab_08_05_delay06.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05_pics/diglab_08_05_delay07.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05_pics/diglab_08_05_delay08.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05_pics/diglab_08_05_delay09.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05_pics/diglab_08_05_delay10.png" width=60% height=60%>

---

# Step 4: ต่อ AND Gate เข้ากับ D Flip-flop

จากที่เราทราบว่า
- เมื่อ `P = 0` วงจรในขั้นตอนที่ 3 จะส่งสัญญาณเป็น `1`
- เมื่อ `P = 1` วงจรในขั้นตอนที่ 3 จะส่งสัญญาณ pulse 1 ครั้ง และจะเป็น `0` จนกว่า `P` จะเท่ากับ `0`

ดังนั้นเราสามารถใช้ AND Gate ในการตรวจสอบว่า ตอนนี้มีการกดปุ่มหรือไม่
- ถ้า `P = 0` ยังไงผลที่ออกมาก็เป็น `0`
- ถ้า `P = 1` จะได้สัญญาณ pulse ที่มาจาก D Flip-flop 2 ตัวล่าง

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_03/diglab_08_03_pics/diglab_08_03_moreDelay.png" width=60% height=60%>

แต่เนื่องจากว่าวงจรนี้เป็นแบบ Moore Machine เราจึงจำเป็นที่จะต้องต่อ D Flip-flop อีกตัวบน Input `P` เพื่อไม่ให้ `P` มีผลต่อ Output Combinational Logic จึงได้วงจรเป็นดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05_pics/diglab_08_05_realMoreDelay01.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05_pics/diglab_08_05_realMoreDelay02.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05_pics/diglab_08_05_realMoreDelay03.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05_pics/diglab_08_05_realMoreDelay04.png" width=60% height=60%>

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05_pics/diglab_08_05_realMoreDelay05.png" width=60% height=60%>

---

# Step 5: ต่อ `\Clr` เข้ากับวงจร

- เนื่องจากว่า `\Clr` เป็น Synchronous Input ดังนั้นเราไม่สามารถนำ `\Clr` ไปต่อกับ Gate บนวงจรได้โดยตรง แต่ต้องต่อกับ Input `P` เท่านั้น
- วงจรจะทำงานก็ต่อเมื่อ `P = 1` และ `\Clr = 0` ดังนั้นเราสามารถต่อ `P` และ `\Clr` ได้ด้วย AND Gate ที่บริเวณ Input ของวงจรดังภาพ

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_05/diglab_08_05.png" width=80% height=80%>

เพียงเท่านี้ก็จะได้วงจร Single Pulser ที่เป็น Moore Machine แล้ว