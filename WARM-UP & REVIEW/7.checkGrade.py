'''
7.เขียนโปรแกรมรับ input 1 ตัว ที่เป็นจำนวนจริง และตรวจสอบว่าจำนวนที่รับมามีค่ามากกว่าหรือเท่ากับ 0 หรือไม่
    -ถ้ามีค่าน้อยกว่า 0 ให้พิมพ์ Please inseart the number that is greater or equal zero
    -ตรวจสอบว่าจำนวนที่รับมามีค่ามากกว่าหรือเท่ากับ 80 หรือไม่ ถ้ามีค่าดังที่กล่าวมาพิมพ์ A
    -ตรวจสอบว่าจำนวนที่รับมามีค่ามากกว่าหรือเท่ากับ 70 หรือไม่ ถ้ามีค่าดังที่กล่าวมาพิมพ์ B
    -ตรวจสอบว่าจำนวนที่รับมามีค่ามากกว่าหรือเท่ากับ 60 หรือไม่ ถ้ามีค่าดังที่กล่าวมาพิมพ์ C
    -ตรวจสอบว่าจำนวนที่รับมามีค่ามากกว่าหรือเทากับ 50 หรือไม่ ถ้ามค่าดังที่กล่าวมาพิมพ์ D
    -ตรวจสอบว่าจำนวนที่รับมามีค่าน้อยกว่า 50 พิมพ์ F
'''

pointInput = int(input('Point : '))

if(pointInput >= 0):
    if(pointInput >= 80):
        print('A')
    elif(pointInput >= 70):
        print('B')
    elif(pointInput >= 60):
        print('C')
    elif(pointInput >= 50):
        print('D')
    elif(pointInput >= 40):
        print('F')
else:
    print('Please insert the number that is greater or equal zero')