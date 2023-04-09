import random


class Bulls_and_cows:
    def __init__(self):
        cows = random.sample(range(0, 10), 3)  # 랜덤한 값 3개를 가져오는데 중복되지 않게 가져옴
        self.cows = cows
        self.count = 0
        print("숫자야구\n0부터 9 사이의 숫자 3개를 입력하세요. 중복된 숫자는 입력할 수 없어요.")
        self.guess()

    def guess(self):
        bulls = []
        while len(bulls) < 3:
            inputnum = input(f"{len(bulls)+1}번째 숫자 : ")
            if inputnum.isdigit() is False:  # inputnum에 숫자가 아닌 값이 들어왔는지 체크해서 걸러냄
                print('숫자만 입력할 수 있어요.')
                continue  # continue를 사용하면 while의 처음으로 돌아간다
            inputnum = int(inputnum)  # 숫자가 아닌 값은 미리 걸러지기 때문에 int로 변환해도 에러가 나지 않음
            if inputnum > 9:  # -는 위에서 걸러지기 때문에 0~9까지의 값은 9 이상의 값만 걸러주면 됨
                print('0부터 9 사이의 수만 입력할 수 있어요.')
                continue
            if inputnum in bulls:  # 중복되는 숫자는 들어가지 않는다
                print('이미 입력한 숫자에요. 중복되지 않는 수를 입력해 주세요.')
                continue
            bulls.append(inputnum)
        self.check(bulls)

    def check(self, bulls):
        self.count += 1
        if bulls == self.cows:  # 정답을 맞출 시 바로 종료 프로세스로 넘어간다
            self.win()
        strike = 0
        ball = 0
        for idx, num in enumerate(bulls):
            if num == self.cows[idx]:  # num과 정답 리스트의 동일 인덱스 값이 동일하다면 스트라이크
                strike += 1
            else:
                if num in self.cows:  # num이 정답 리스트에 있을 시 볼
                    ball += 1
                else:
                    pass
        if strike == 0 and ball == 0:
            print("OUT")
        else:
            print(f"{strike}STRIKE {ball}BALL")
        print(f"시도 횟수 : {self.count}")
        self.guess()

    def win(self):
        print(f"{self.count}번 만에 맞추셨습니다.")
        print(f"정답은 {self.cows} 입니다.")
        whether = input("다시 한번 하시겠습니까? (Y) : ")
        if whether in ['y', 'Y']:  # 다시 할 수 있게 한다
            self.__init__()
        else:
            quit()


def main():
    game = Bulls_and_cows()  # 실행시키기 위해 class 안에 값을 하나 생성한다


if __name__ == "__main__":
    main()
