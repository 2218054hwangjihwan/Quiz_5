#클래스 만들기
class 붕어빵 :
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.total = 0
    def sell(self):
        print(self.name,"붕어빵을 ",self.price,"에 팔았습니다.",sep="")
        self.total+=1000
    def eat(self):
        print(self.name,"붕어빵을 먹었습니다. 냠냠굿",sep="")

#오브젝트 생성    이름 = 붕어빵("이름", 가격)
슈크림 = 붕어빵("슈크림", 1000)
김치 = 붕어빵("김치", 1000)
슈크림.sell()
슈크림.sell()
슈크림.sell()
슈크림.sell()
print(슈크림.total)
김치.sell()
김치.eat()
슈크림.eat()
오이 = 붕어빵("오이",99999)
오이.sell()
