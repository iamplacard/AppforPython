## Bit operation example code
## ord() It convert character to ASCII code value. A = 65(ASCII code value) / a = 97(ASCII Code value)
## 문자 A 와 a 의 차이인 32 를 가지고, 문자 A 를 Masking 하면 ==> 문자 a 가 되네요
## 문자 A 와 a 의 차이인 32 를 가지고, 문자 a 를 Masking 하면 ==> 문자 A 가 되네요

## 변수 선언 ##

## 함수 선언 ##

## 화면에서 마우스 왼쪽 버튼을 누르면 클릭한 위치에 다양한 색상, 크기, 각도의

## Main Code ##
if __name__ == "__main__" :
       a =ord('A')
       mask = 0x0F

       print("%x & %x = %x" % (a, mask, a & mask))
       print("%x | %x = %x" % (a, mask, a | mask))

       mask = ord('a') - ord('A')

       b = a ^ mask
       print("%c ^ %d = %c" % (a, mask, b))
       print(" 문자 A 와 a 의 차이인 32 를 가지고, 문자 A 를 Masking 하면 ==> 문자 a 가 되네요")
       a = b ^ mask
       print("%c ^ %d = %c" % (b, mask, a))
       print(" 문자 A 와 a 의 차이인 32 를 가지고, 문자 a 를 Masking 하면 ==> 문자 A 가 되네요")

       print("\n\n 정수 값에 비트 부정을 한 후 1을 더하면 그 수의 음수값이 나온다. ")
       a = 12345
       b = ~a
       print("a = %d, b = ~a + 1, b = %d" % (a, b + 1))

       print("\n\n Shift 연산")
       print(" a = %d"% a)
       print(" a = ", bin(a))
       print("\n 1bit left shift")
       print(" a = %d" % (a << 1))
       print(" a = ", bin(a << 1))
       print("\n 2bit left shift")
       print(" a = %d" % (a << 2))
       print(" a = ", bin(a << 2))
       print("\n 3 bit left shift")
       print(" a = %d" % (a << 3))
       print(" a = ", bin(a << 3))

       print("\n 1bit right shift")
       print(" a = %d" % (a >> 1))
       print(" a = ", bin(a >> 1))
       print("\n 2bit right shift")
       print(" a = %d" % (a >> 2))
       print(" a = ", bin(a >> 2))
       print("\n 3 bit right shift")
       print(" a = %d" % (a >> 3))
       print(" a = ", bin(a >> 3))
       


       


             

