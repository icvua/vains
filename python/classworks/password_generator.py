import random
import string


def pw_maker():
    a = random.randint(1, 5)
    b = random.randint(1, 6 - a)
    c = random.randint(1, 7 - a - b)
    d = 8 - a - b - c
    temp = [a, b, c, d]
    random.shuffle(temp)
    pswd = random.sample(string.digits, temp[0]) + random.sample(string.ascii_lowercase, temp[1]) + \
        random.sample(string.ascii_uppercase, temp[2]) + random.sample(string.punctuation, temp[3])
    random.shuffle(pswd)
    print("Random Generated Password :", "".join(pswd))


def main():
    pw_maker()


if __name__ == "__main__":
    main()
