import os.path
import sys
from collections import defaultdict
from itertools import combinations


def inspect_folder(folder):
    if not os.path.isdir(folder):
        return None
    filepaths = defaultdict(list)
    for root, dirs, files in os.walk(folder):
        for filename in files:
            fullpath = os.path.join(root, filename)
            filepaths[filename].append(fullpath)
    return {name: paths for name, paths in filepaths.items() if len(paths) > 1}


def are_files_duplicates(file_path1, file_path_2):
    if os.path.getsize(file_path1) == os.path.getsize(file_path_2):
        return True


def search_duplicates(filepaths):
    duplicates = []
    for path_list in filepaths.values():
        duplicates += [pair for pair in combinations(path_list, 2) if are_files_duplicates(*pair)]
    return duplicates


if __name__ == '__main__':
    folder_content = inspect_folder(sys.argv[1])
    if folder_content is None:
        print("Не удалось прочитать папку")
    else:
        duplicates = search_duplicates(folder_content)
        for pair in duplicates:
            print('Дубликаты: {} и {}'.format(pair[0], pair[1]))
