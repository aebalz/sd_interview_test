"""
3.  เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python 
    โดยห้ามใช้ math.factorial เช่น 7! = 5040 
    มีเลข 0 ต่อท้าย 1 ตัว, 10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว
"""

def factorial(n):
    return 1 if n == 1 or n == 0 else n * factorial(n - 1)

def countTrailingZeros(intNumberValue):
    numberToString = str(intNumberValue)
    count = 0
    while True:
        if numberToString[-1] == "0":
            numberToString = numberToString[:-1]
            count += 1
        else:
            return count

factorialValue = factorial(10)
countZeros = countTrailingZeros(factorialValue)
print(f"factorialValue : {factorialValue}")
print(f"countZeros : {countZeros}")