import argparse
import os.path
from collections import defaultdict


def inspect_folder(folder):
    if not os.path.isdir(folder):
        return None
    filepaths = defaultdict(list)
    for root, dirs, files in os.walk(folder):
        for filename in files:
            fullpath = os.path.join(root, filename)
            filesize = os.path.getsize(fullpath)
            filepaths[(filename, filesize)].append(fullpath)
    return filepaths


def search_duplicates(filepaths):
    return filter(lambda paths: len(paths) > 1, filepaths.values())


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description="Поиск дубликатов в папке и её подпапках")
    argparser.add_argument('folder', help='путь к папке')
    args = argparser.parse_args()
    folder_content = inspect_folder(args.folder)
    if folder_content is None:
        print("Не удалось прочитать папку")
    else:
        duplicates = search_duplicates(folder_content)
        for set_of_duplicates in duplicates:
            print('Дубликаты: {}'.format(', '.join(set_of_duplicates)))
