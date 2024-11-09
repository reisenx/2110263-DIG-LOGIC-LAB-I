# Positive Edge Trigger T Flip-flop (diglab_07_05)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1YXfXM0vEzCiRPlkg4yF5HIltvlN77-V3/view?usp=drive_link)

---
# Step 1: เข้าใจการทำงานของ Positive Edge Trigger T Flip-flop

## หลักการทำงานของ D Flip-flop
- จริงๆแล้ว D Flip-flop มันเหมือนกับ JK Flip-flop เลย เพียงแต่ว่ามันมีเพียงแค่ 1 Input คือ `D`
- เมื่อกดปุ่ม (`D = 1`) จะเป็นการ SET จะทำให้ Output ใน state ถัดไปเท่ากับ `1`
- เมื่อไม่กดปุ่ม (`D = 0`) จะเป็นการ RESET จะทำให้ Output ใน state ถัดไปเท่ากับ `0`

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_05/diglab_07_05_pics/diglab_07_05_Dtable.png" width=40% height=40%>

## หลักการทำงานของ T Flip-flop
- จริงๆแล้ว T Flip-flop มันเหมือนกับ JK Flip-flop เลย เพียงแต่ว่ามันมีเพียงแค่ 1 Input คือ `D`
- เมื่อกดปุ่ม (`T = 1`) จะเป็นการ TOGGLE จะทำให้ Output สลับค่า `0` และ `1` ทุกๆสัญญาณ `Clock`
- เมื่อไม่กดปุ่ม (`T = 0`) จะเป็นการ HOLD จะทำให้ Output ค้างค่าเดิมไว้จนกว่าจะมีการกดปุ่ม

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_05/diglab_07_05_pics/diglab_07_05_Ttable.png" width=40% height=40%>

## หลักการทำงานของวงจรแบบ Positive Edge และ Negative Edge
- วงจรแบบ Positive Edge จะมีการเปลี่ยนแปลงค่า Output ในจังหวะที่ `Clock` เกิดการเปลี่ยนแปลงจาก `0` เป็น `1` **เท่านั้น**
- วงจรแบบ Negative Edge จะมีการเปลี่ยนแปลงค่า Output ในจังหวะที่ `Clock` เกิดการเปลี่ยนแปลงจาก `1` เป็น `0` **เท่านั้น**

ดังนั้นจึงสรุปได้ว่า **Positive Edge Trigger T Flip-flop** คือวงจร T Flip-flop ที่เกิดการเปลี่ยนแปลง Output ในจังหวะที่ `Clock` เกิดการเปลี่ยนแปลงจาก `0` เป็น `1` **เท่านั้น**

---

# Step 2: ต่อวงจร Positive Edge Trigger T Flip-flop

## Negative Edge Trigger D Flip-flop

**Negative Edge Trigger D Flip-flop** คือวงจร D Flip-flop ที่เกิดการเปลี่ยนแปลง Output ในจังหวะที่ `Clock` เกิดการเปลี่ยนแปลงจาก `1` เป็น `0` **เท่านั้น**

ซึ่งนี่คือวงจร Negative Edge Trigger D Flip-flop ที่โจทย์ข้อที่แล้วให้มา

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_05/diglab_07_05_pics/diglab_07_05_DNeg.png" width=60% height=60%>

## Negative Edge Trigger T Flip-flop

**Negative Edge Trigger T Flip-flop** คือวงจร T Flip-flop ที่เกิดการเปลี่ยนแปลง Output ในจังหวะที่ `Clock` เกิดการเปลี่ยนแปลงจาก `1` เป็น `0` **เท่านั้น**

จากที่เรามีวงจร Negative Edge Trigger D Flip-flop อยู่แล้ว เราจะสามารถนำมาดัดแปลงให้กลายเป็น Negative Edge Trigger T Flip-flop ได้เลย โดยดัดแปลงแค่การส่งสัญญาณเข้าวงจร D Flip-flop ให้เป็นดังตาราง

| `T` | `Q(t)` | `D` | `Q(t+1)` | State |
| :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | RESET |
| 0 | 1 | 1 | 1 | SET |
| 1 | 0 | 1 | 1 | SET |
| 1 | 1 | 0 | 0 | RESET |

จากตารางเราจะสรุปได้ว่า $D = T \oplus Q_{t}$ นั่นเอง และสามารถดัดแปลง Negative Edge Trigger D Flip-flop ให้เป็น Negative Edge Trigger T Flip-flop ได้ ดังภาพ

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_05/diglab_07_05_pics/diglab_07_05_TNeg.png" width=60% height=60%>

## Positive Edge Trigger T Flip-flop

**Positive Edge Trigger T Flip-flop** คือวงจร T Flip-flop ที่เกิดการเปลี่ยนแปลง Output ในจังหวะที่ `Clock` เกิดการเปลี่ยนแปลงจาก `0` เป็น `1` **เท่านั้น**

จากการที่เรามีวงจร Negative Edge Trigger T Flip-flop ไว้อยู่แล้ว เราสามารถต่อ NOT Gate ที่ `Clock` ได้เลย เพื่อให้สัญญาณ `Clock` ที่เข้าไปในวงจร T Flip-flop ตรงข้ามกับสัญญาณ `Clock` ที่ส่งไป

- สัญญาณ `Clock` ที่ส่งไปเท่ากับ `0` แต่ค่า `1` เข้าวงจร T Flip-flop
- สัญญาณ `Clock` ที่ส่งไปเท่ากับ `1` แต่ค่า `0` เข้าวงจร T Flip-flop
- เพียงเท่านี้ T Flip-flop ก็จะเปลี่ยนแปลงเมื่อ `Clock` เกิดการเปลี่ยนแปลงจาก `0` เป็น `1` แล้ว โดยที่แทบไม่ต้องแก้วงจรอะไรเลย

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_05/diglab_07_05_pics/diglab_07_05_TPos.png" width=60% height=60%>

---

# Step 3: ต่อ `\Clear` เข้ากับวงจร Positive Edge Trigger T Flip-flop

จากขั้นตอนที่ 2 เราได้ดัดแปลงสัญญาณ `T` ให้กลายเป็นสัญญาณ `D` เฉยๆ เพราะว่าวงจรข้างในจริงๆยังทำงานแบบ D Flip-flop อยู่

ดังนั้นเราจะมองว่าสัญญาณที่ออกมาจาก XOR Gate หรือก็คือ $D = T \oplus Q_{t}$ นั้นเป็นสัญญาณ `D`

ซึ่งจะเห็นได้ว่า การที่จะทำให้ค่า `Q` เท่ากับ `0` ได้นั้น จะต้องทำให้ `D` เท่ากับ `0` ก็คือต้องเอาค่า `0` ไปเข้าวงจร flip-flop ให้ได้นั่นเอง

จากที่ `\Clear` เป็น Synchronous Input ก็คือถึงแม้จะกดปุ่ม `\Clear` ไปแล้ว วงจรจะยังไม่เกิดการเปลี่ยนแปลงทันที ต้องรอสัญญาณ `Clock` ก่อนจึงจะทำให้ `Q` เท่ากับ `0` ดังนั้นเราไม่สามารถต่อ `\Clear` เข้ากับ Gate บนวงจร D Flip-flop ได้โดยตรง และต้องต่อ `Clear` กับ Input `D` เท่านั้น

จากข้อมูลข้างต้น ค่า Input ที่จะเข้า D Flip-flop จะต้องเป็นดังตาราง

| `\Clear` | `D` | Input ที่เข้าวงจร |
| :---: | :---: | :---: |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

จากตารางข้างต้น จะได้ว่า Input ที่เข้าวงจร D Flip-flop คือ

$Input = D(Clear)'$

$Input = (T \oplus Q_{t})(Clear)'$

ดังนั้นเราจะสามารถต่อวงจร Positive Edge Trigger T Flip-flop ที่มีปุ่ม `\Clear` ได้ดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_05/diglab_07_05.png" width=80% height=80%>