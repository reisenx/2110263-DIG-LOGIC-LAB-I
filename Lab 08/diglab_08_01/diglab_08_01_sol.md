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

[INSERT IMAGE HERE]

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_05/diglab_07_05_pics/diglab_07_05_Dtable.png" width=40% height=40%>

### Output
- `QD`, `QC`, `QB` และ `QA` ใช้แสดงค่าของเลขใน state ปัจจุบัน
- `RCO = 1` ก็ต่อเมื่อวงจรนับถึงเลข `1111`

---

# Step 2: 