# Mealy Single Pulser with Synchronizer (diglab_08_04)
### อ่านโจทย์ได้ที่นี่ [Click Here!](https://drive.google.com/file/d/18AVGglHz6wFCLuAc27jLK6epjX_P1rHt/view?usp=drive_link)

---
# Step 1: ต่อ Synchronizer เข้าไปในวงจร Single Pulser

### อ่านเกี่ยวกับวิธีการต่อวงจร Single Pulser (`diglab_08_03`) [Click Here!]()

## วงจรเดิม

จากแลปก่อนหน้า จะได้วงจร Single Pulser แบบ Mealy Machine มาดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_04/diglab_08_04_pics/diglab_08_04_old.png" width=60% height=60%>

## วงจรใหม่

แต่จากโจทย์บอกว่าให้ต่อ Synchronizer เข้าไปในวงจรเพิ่มด้วย ซึ่ง Synchronizer ในที่นี้จะใช้ D Flip-flop โดย Flip-flop ตัวนี้จะมีบทบาทในการการันตีได้ว่าสัญญาณ `P` จะเข้าวงจร Single Pulser ตามสัญญาณของ clock นั่นเอง

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_04/diglab_08_04_pics/diglab_08_04_diagram.jpg" width=60% height=60%>

และเมื่อต่อลงวงจร Digital ก็จะได้ดังนี้

<img src="https://raw.githubusercontent.com/reisenx/2110263-DIG-LOGIC-LAB-I/refs/heads/main/Lab%2008/diglab_08_04/diglab_08_04.png" width=60% height=60%>