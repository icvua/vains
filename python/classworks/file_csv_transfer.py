import csv
import os
import re
import sys


def path_select():
    pth = sys.argv[1]
    return pth
    # argv로 인자 받기, class에선 이 방법을 사용할 수 없다


def search_files(pth):
    sep_path = []
    path_group = {}
    for (root_dirs, _, file_dirs) in os.walk(pth):
        for fil in file_dirs:
            # file_dirs는 root_dirs 안에 있는 모든 파일들, fil은 그 개별의 파일이다
            full_path = os.path.join(root_dirs, fil)
            # root_dirs와 fil을 합치면 fil의 절대 경로가 나온다
            if root_dirs not in path_group:
                path_group[root_dirs] = []
                sep_path.append(root_dirs)
                # root_dir이 앞에서 선언한 path_group 딕셔너리에 없다면 root_dir을 딕셔너리 key 값으로 생성한다
                # 모든 파일을 체크하지만 root_dir이 같다면 딕셔너리에 추가 되지 않는다
                # sep_path에 파일 경로를 따로 저장한다
            path_group[root_dirs].append(full_path)
            # path_group[root_dirs]의 value 값으로 full_path를 넣는다
            # 바로 직전에 root_dirs를 생성하지 않았어도 이미 이전에 생성했던 같은 경로의 key가 있으니 그 안에 full_path를 넣으면 된다
    return path_group, sep_path


def write_files(path_group, sep_path):
    csv_path = os.path.expanduser('~/final_test.csv')
    # csv 파일이 저장될 경로 설정, os의 홈 폴더에 생성하게 한다
    with open(csv_path, 'w') as f:
        i = 0
        writer = csv.writer(f)
        writer.writerow(
            ["#", "Project Name", "Sequence Name", "Shot Name", "Version", "Start Frame", "Final Frame", "Total Frames",
             "Path"])
        for pth in sep_path:
            i += 1
            # i는 인덱싱을 하기 위한 숫자다
            sep = pth.split(os.sep)
            # 각 파일이 들어있는 경로인 key를 리스트로 분리해준다
            frame_grp = []
            for n in path_group[pth]:
                frame_num = re.search('[0-9]{4}[.]', n)
                frame_num = n[frame_num.span()[0]:frame_num.span()[1] - 1]
                frame_grp.append(frame_num)
            frame_grp = sorted(frame_grp)
            first_frame = frame_grp[0]
            final_frame = frame_grp[-1]
            # 각 key 값의 value 리스트 마다 프레임 넘버를 뽑아 새로운 리스트에 넣어주고, 그 리스트를 정렬해 스타트/엔드 프레임을 찾는다
            fileseq = path_group[pth][0]
            # value값은 리스트 안에 여러개 있지만, 그 값은 프레임 넘버 빼고 전부 동일하니까 아무거나 가져와도 된다
            numm = re.search('[0-9]{4}[.]', fileseq)
            numm = fileseq[numm.span()[0]:numm.span()[1] - 1]
            fileseq = fileseq.replace(numm, '####')
            pathname = pth + fileseq
            # 가져온 value 값에서 프레임 넘버를 뽑아서 ####로 변경해준다, 그 뒤 key값과 합쳐서 풀 패스 경로를 만든다
            writer.writerow([i, sep[4], sep[6], sep[7], sep[9], first_frame, final_frame, len(frame_grp), pathname])


def main():
    pth = path_select()
    path_group, sep_path = search_files(pth)
    write_files(path_group, sep_path)


if __name__ == "__main__":
    main()


def search_files_old(pth):
    sep_path = []
    for (rots, _, fils) in os.walk(pth):
        for fil in fils:
            full_path = os.path.join(rots, fil)
            exact_path = full_path
            full_path = full_path[len(pth):-len(fil) - 1]
            numm = re.search('[0-9]{4}[.]', fil)
            full_path = full_path + os.sep + fil[numm.span()[0]:numm.span()[1] - 1]
            mid_path = full_path.split(os.sep)
            mid_path.append(exact_path)

            sep_path.append(mid_path)
    print(sep_path)
    return sep_path
