import os
import shutil

path = '/home/rapa/test/'
lenn = len(path)

wrong_files = []
mid_path = []
old_path = []
new_path = []

for (root, dirs, files) in os.walk(path):
    # print("root : " + root)
    # path_split = root.split(os.sep)
    # print(path_split)
    for file in files:
        full_path = os.path.join(root, file)
        sliced_path = full_path[lenn:]
        path_split = sliced_path.split(os.sep)
        # print(path_split)
        path_split_2 = path_split[-1].split('_')
        # print(path_split_2)
        if path_split[0:-2] == path_split_2[0:-2]:
            print(path_split[-1], ' Path is correct')
        else:
            old_path.append(full_path)
            wrong_files.append(path_split[-1])
            print(path_split[-1], ' Path is wrong')

# for i in wrong_files:
#     print(i)
# 파일 경로에서 유추하여 정확한 경로 만들기

# 실제 파일 이동하기
# os.system('mv %s %s' % (원래 경로, 이동할 경로))


for wf in wrong_files:
    path2 = path + wf.replace('_', os.sep)
    mid_path.append(path2)
    # print(new_path)
    for i in mid_path:
        a = i[0:-9]
        try:
            os.makedirs(a)
        except:
            pass
    new_path.append(a + os.sep + wf)
pathlen = len(old_path)

if len(wrong_files) == 0:
    print("\nAll paths are correct\n")
    exit()
else:
    print('\n', wrong_files, '\n' 'These files are in wrong path\n')

whether = input("Execute? ")
if whether == 'y' or 'Y':
    pass
else:
    exit()

for n in range(0, pathlen):
    shutil.move(old_path[n], new_path[n])
# print(new_path)
# print(old_path)


# for i in range(0-4):
#     if path_split[i] == path_split_2[i]:
#         print('correct')
#     else:
#         print('nope')
