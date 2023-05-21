"""
2.  เขียนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน Array ด้วยภาษา python เช่น [1,2,1,3,5,6,4] 
    ลำดับที่มีค่ามากที่สุด คือ index = 5 โดยไม่ให้ใช้ฟังก์ชั่นที่มีอยู่แล้ว ให้ใช้แค่ลูปกับการเช็คเงื่อนไข
"""

def findMaxIndexInArray(dataList):
    maxValue = dataList[0]
    maxValueIdx = 0
    
    for i in range(1, len(dataList)):
        if dataList[i] > maxValue:
            maxValue = dataList[i]
            maxValueIdx = i
    
    return maxValueIdx

dataList = [1, 2, 1, 3, 5, 6, 4]
max_index = findMaxIndexInArray(dataList)
print(f"Index ของตัวเลขที่มีค่ามากที่สุดคือ : {max_index}")


# -----------------------------------------------------------------------
import random
randomDataList = [random.randint(1, 100) for i in range(100)]
max_index = findMaxIndexInArray(randomDataList)
print(f"dataList : {randomDataList}")
print(f"Index ของตัวเลขที่มีค่ามากที่สุดคือ : {max_index}")