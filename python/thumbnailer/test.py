import time
from multiprocessing import Process, Queue


def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.put(total)
    return


if __name__ == "__main__":
    start_time = time.time()
    START, END = 0, 1000000000
    result = Queue()

    # th1 = Process(target=work, args=(1, 0, 5000000000, result))
    # th2 = Process(target=work, args=(2, 5000000001, 10000000000, result))
    #
    # th1.start()
    # th2.start()
    #
    # th1.join()
    # th2.join()

    th1 = Process(target=work, args=(1, 0, 100000000, result))
    th2 = Process(target=work, args=(2, 500000001, 1000000000, result))
    th3 = Process(target=work, args=(3, 1000000001, 1500000000, result))
    th4 = Process(target=work, args=(4, 1500000001, 2000000000, result))
    th5 = Process(target=work, args=(5, 2000000001, 2500000000, result))
    th6 = Process(target=work, args=(6, 2500000001, 3000000000, result))
    th7 = Process(target=work, args=(7, 3000000001, 3500000000, result))
    th8 = Process(target=work, args=(8, 3500000001, 4000000000, result))
    th9 = Process(target=work, args=(9, 4000000001, 4500000000, result))
    th10 = Process(target=work, args=(10, 4500000001, 5000000000, result))
    th11 = Process(target=work, args=(11, 5000000001, 5500000000, result))
    th12 = Process(target=work, args=(12, 5500000001, 6000000000, result))
    th13 = Process(target=work, args=(13, 6000000001, 6500000000, result))
    th14 = Process(target=work, args=(14, 6500000001, 7000000000, result))
    th15 = Process(target=work, args=(15, 7000000001, 7500000000, result))
    th16 = Process(target=work, args=(16, 7500000001, 8000000000, result))
    th17 = Process(target=work, args=(17, 8000000001, 8500000000, result))
    th18 = Process(target=work, args=(18, 8500000001, 9000000000, result))
    th19 = Process(target=work, args=(19, 9000000001, 9500000000, result))
    th20 = Process(target=work, args=(20, 9500000001, 10000000000, result))
    th21 = Process(target=work, args=(21, 10000000001, 10500000000, result))
    th22 = Process(target=work, args=(22, 10500000001, 11000000000, result))
    th23 = Process(target=work, args=(23, 11000000001, 11500000000, result))
    th24 = Process(target=work, args=(24, 11500000001, 12000000000, result))
    th25 = Process(target=work, args=(25, 12000000001, 12500000000, result))
    th26 = Process(target=work, args=(26, 12500000001, 13000000000, result))
    th27 = Process(target=work, args=(27, 13000000001, 13500000000, result))
    th28 = Process(target=work, args=(28, 13500000001, 14000000000, result))
    th29 = Process(target=work, args=(29, 14000000001, 14500000000, result))
    th30 = Process(target=work, args=(30, 14500000001, 15000000000, result))

    th1.start()
    th2.start()
    th3.start()
    th4.start()
    th5.start()
    th6.start()
    th7.start()
    th8.start()
    th9.start()
    th10.start()
    th11.start()
    th12.start()
    th13.start()
    th14.start()
    th15.start()
    th16.start()
    th17.start()
    th18.start()
    th19.start()
    th20.start()
    th21.start()
    th22.start()
    th23.start()
    th24.start()
    th25.start()
    th26.start()
    th27.start()
    th28.start()
    th29.start()
    th30.start()

    th1.join()
    th2.join()
    th3.join()
    th4.join()
    th5.join()
    th6.join()
    th7.join()
    th8.join()
    th9.join()
    th10.join()
    th11.join()
    th12.join()
    th13.join()
    th14.join()
    th15.join()
    th16.join()
    th17.join()
    th18.join()
    th19.join()
    th20.join()
    th21.join()
    th22.join()
    th23.join()
    th24.join()
    th25.join()
    th26.join()
    th27.join()
    th28.join()
    th29.join()
    th30.join()

    result.put('STOP')
    total = 0
    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
        else:
            total += tmp
    print(f"Result: {total}")
    print("--- %s seconds ---" % (time.time() - start_time))
