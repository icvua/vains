import os
import re
import sys


def search_loc():
    path = sys.argv[1]
    ow = sys.argv[2]
    nw = sys.argv[3]
    return path, ow, nw


def search_files(path, ow, nw):
    full_path = []
    for (root, _, files) in os.walk(path):
        for file in files:
            joined = (os.path.join(root, file))
            sch = re.search(ow, joined)
            if sch is None:
                full_path.append(joined)
            else:
                continue
    return path, full_path, ow, nw


def change_filename(path, full_path, ow, nw):
    for file in full_path:
        newpath = re.sub(ow, nw, file)
        dname = os.path.dirname(file)
        fname = os.path.basename(newpath)
        os.rename(file, os.path.join(dname, fname))
    return path, ow, nw


def change_dirname(path, ow, nw):
    for (root, dirs, _) in os.walk(path):
        for dir_name in dirs:
            if dir_name.endswith(ow) == True:
                fulldir = os.path.join(root, dir_name)
                newname = re.sub(ow, nw, fulldir)
                os.rename(fulldir, newname)
            else:
                pass


def main():
    path, ow, nw = search_loc()
    path, full_path, ow, nw = search_files(path, ow, nw)
    path, ow, nw = change_filename(path, full_path, ow, nw)
    change_dirname(path, ow, nw)


if __name__ == "__main__":
    main()
