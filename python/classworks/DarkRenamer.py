import json
import os
import sys


class ReName:
    def __init__(self):
        syst = sys.argv[1]
        self.full_path = syst
        path = input("경로를 입력해 주세요 : ")
        if os.path.exists(path):
            self.path = path
            self.files = os.listdir(path)
            self.change_name()
        else:
            self.error()

    def find_path(self, path):
        for idx, file in enumerate(self.files):
            self.full_path.append(path + os.sep + file)

    def change_name(self):
        will_delete_list = []
        execute_list = {}
        print(self.files)
        old_str = input("바꾸고 싶은 문자열을 입력하세요 : ")
        for old_file in self.files:
            if old_str in old_file:
                will_delete_list.append(old_file)
            else:
                pass
        print(will_delete_list)
        new_str = input("새 문자열을 입력하세요 : ")
        for new_file in will_delete_list:
            execute_list[new_file] = new_file.replace(old_str, new_str)
        print(execute_list)
        self.execute(execute_list)

    def execute(self, execute_list):
        whether = input("Press Y to execute : ")
        if whether in ['y', 'Y']:
            pass
        else:
            self.__init__()
        for old_name, new_name in execute_list.items():
            old_full_path = self.path + os.sep + old_name
            new_full_path = self.path + os.sep + new_name
            os.rename(old_full_path, new_full_path)
        whether = input("Press Y to make log files : ")
        if whether in ['y', 'Y']:
            self.make_log_file(execute_list)
        else:
            print("감사합니다")

    def make_log_file(self, execute_list):
        output_json = {'path': self.path, 'executed files': execute_list}
        file_name = input("Save as : ")
        file_path = os.path.expanduser(f'~/{file_name}.json')
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(output_json, file)

    def error(self):
        print("잘못된 입력입니다.")
        self.__init__()


def main():
    me = ReName()


if __name__ == "__main__":
    main()
