print("이름\t나이\t지역")
print("고수연\t25\t강남시")
print("박지성\t22\t분당시")
print("이강인\t22\t뮌헨")

print("안녕하세요\n안녕하세요")
print("안녕하세요\t안녕하세요")

print("동해물과\n백두산이\n")
print("""동해물과 백두산이
마르고 닳도록
무궁화 삼천리""")
      
print("""\
동해물과 백두산이
하느님이 보우하사
대한으로 갈이보전하세\
""") 

print(273)
print(type(52))
print(type(52.4))

print("5+2=",5+2)
print("53/7=",53/7)
print("53%7=",53%7)

print("42**2=",42**2)
print((type(43.5)))
print("안녕"+"하세요"*3)
print(("안녕"+"하세요")*3)
print("안녕"+("하세요"*3))
print("안녕"+"하세요"*3)

print("문자 선택 연산자에 대해 알아볼까요?")
print("안녕하세요"[0])
print("안녕하세요"[1])

print("문자를 뒤에서부터 선택해 볼까요?")
print("안녕하세요"[-5])
print("안녕하세요"[-3])

print("안녕하세요"[1:4])
print("안녕하세요"[0:2])
print("안녕하세요"[:2])

print(len("안녕하시요"))

print("\\\\\\")
print("-"*8)
print("# 연습문제")
print("3462를 17로 나누었을 때의")
print("-몫:",3462/17)
print("-나머지:",3462%17)

#변수 선언과 할당
pi=3.14159265
r=10

#변수 참조
print("원주율=",pi)
print("반지름=",r)
print("원의 둘레=",2*pi*r) #원의 둘레
print("원의 넓이=",pi*r*r) #원의 넓이

print("")

string=input("인사말을 입력하세요>")
print(string)


#입력을 받습니다
string = input("입력> ")

#출력합니다
print("자료:", string)
print("자료형",type(string))


#입력을 받습니다.
string = input("입력>")

string_a =input("입력A> ")
int_a =int(string_a)

string_b=input("입력B> ")
int_b=int(string_b)
          
print("문자열자료:",string_a+string_b)
print("숫자 자료:",int_a+int_b)
