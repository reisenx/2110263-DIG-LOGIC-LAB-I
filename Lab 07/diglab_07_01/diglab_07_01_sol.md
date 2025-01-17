# Simple Memory (diglab_07_01)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/1NrgipxT8azCAr3fIpAGgJQ7WSB5bVbyB/view?usp=drive_link)

---
# Driver (Tri-State Gate)

- มี Input เพิ่มมาอีก 1 ตัว คือ `OE` (Output Enable)
- มี Output ได้ 3 แบบ ได้แก่ `0`, `1` และ `Z` (High Impedance)

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_01/diglab_07_01_pics/diglab_07_01_triState.png" width=50% height=50%>

**`Z` (High Impedance)** คือสถานะที่ Gate มีความต้านทานไฟฟ้าสูงมาก จนเสมือนว่าไม่ได้เชื่อมต่อวงจร

## การใช้งาน Driver
<div>
    <img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_01/diglab_07_01_pics/diglab_07_01_driver01_01.png" width=40% height=40%>
    <img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_01/diglab_07_01_pics/diglab_07_01_driver01_02.png" width=40% height=40%>
</div>

## การใช้งาน Driver (Inverted OE)

<div>
    <img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_01/diglab_07_01_pics/diglab_07_01_driver02_01.png" width=40% height=40%>
    <img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_01/diglab_07_01_pics/diglab_07_01_driver02_02.png" width=40% height=40%>
</div>

---

# การต่อวงจร และหลักการทำงาน

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2007/diglab_07_01/diglab_07_01.png" width=80% height=80%>

- ถ้าหาก `Load` เป็น `0` จะค้างค่า `Z` ไว้ ไม่เปลี่ยนแปลงตาม Input `A`
- ถ้าหาก `Load` เป็น `0` จะทำให้ Driver ที่ต่อกับ `A` ไม่ปล่อยให้ค่า `A` ผ่านตัวมันไปได้ (`OE` = 0)
- ถ้าหาก `Load` เป็น `1` จะปล่อยให้ค่า `Z` เปลี่ยนแปลงตาม Input `A` ได้
- ถ้าหาก `Load` เป็น `1` จะทำให้ Driver ที่ต่อกับ `Load` ไม่ปล่อยให้ค่า `Load` ผ่านตัวมันไปได้ (`OE` = 0)