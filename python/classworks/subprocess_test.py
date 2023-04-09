import subprocess

cmd = "zenity --password --username"
cmd_list = ["zenity", "--password", "--username"]
p = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
while p.poll() is None:
    out = p.stdout.readline()
    print(out)

import fileseq
print(dir(fileseq))
path_dir = "/home/rapa/project/avata/shot/far/0010/plate/v001"
sequences = fileseq.findSequencesOnDisk(path_dir)
print(sequences)

for i in sequences:
    print(i.frameRange())

import cv2
import numpy
for dirr in dir(cv2):
    print(dirr)
for dirr in dir(numpy):
    print(dirr)






def aaa_decorator(func):
    def wrapper():
        print("func start")
        func()
        print("func end")
    return wrapper

@aaa_decorator
def aaa():
    print("aaa")

aaa()
aaabb = aaa_decorator(aaa)
aaabb()

def sum_deco(func):
    def wrapper(*args):
        print("func start")
        result = func(*args)
        print("func end")
        return result
    return wrapper


@sum_deco
def sum(a, b):
    return a + b

print(sum(1, 2))


out = sum(1, 2)
print(out)
print(sum(1, 2))
