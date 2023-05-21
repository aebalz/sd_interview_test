
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

def convertNumberToThai(number):
    thaiDigits = {
        '0': 'ศูนย์',
        '1': 'หนึ่ง', # เคส length > 1 เอ็ด
        '2': 'สอง', # เคส length = 2 ยี่
        '3': 'สาม',
        '4': 'สี่',
        '5': 'ห้า',
        '6': 'หก',
        '7': 'เจ็ด',
        '8': 'แปด',
        '9': 'เก้า',
        '10': 'สิบ',
        '100': 'ร้อย',
        '1000': 'พัน',
        '10000': 'หมื่น',
        '100000': 'แสน',
        '1000000': 'ล้าน'
    }

    if number < 1 or number >= 10000000:
        return "ค่าที่รับเข้ามาต้องอยู่ระหว่าง 1 ถึง 9,999,999"

    thaiText = ''
    digits = str(number)
    length = len(digits)

    for i in range(length):
        digitPos = thaiDigits[str(10**(length - i -1))] if length - i != 1 else ""
        thaiText_ = thaiDigits[digits[i]]
        if digits[i] == "1" and length > 1 and length - i == 1:
            thaiText_ = "เอ็ด"
        if digits[i] == "2" and length > 2 and length - i == 2:
            thaiText_ = "ยี่"
        thaiText += thaiText_ + digitPos
    
    return thaiText

number = 1231231
thaiText = convertNumberToThai(number)
print(f"{number} = {thaiText}")