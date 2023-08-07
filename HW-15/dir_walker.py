# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import argparse
import logging
from collections import namedtuple
from pathlib import Path

ObjectName = namedtuple('ObjectName', 'name ext is_dir parent', defaults=['', '', True, ''])
FORMAT = "{asctime} - {levelname:<5}: {msg}"

logging.basicConfig(filename='./HW-15/log/log.txt',
                    filemode='w',
                    encoding='utf-8',
                    format=FORMAT,
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger()


def parse_args():
    parser = argparse.ArgumentParser(description="Информация о содержимом папки")
    parser.add_argument('-p',  metavar='path', type=str, nargs='*', default='.', help='Введите путь к папке')
    args = parser.parse_args()
    return args.p


def dir_info(path: str = None):
    if not path:
        logger.info(f'Путь по умолчанию {Path(path)}')
    return directory_walk(Path().cwd() if path is None else Path(path))


def directory_walk(file: Path):
    lst_name = []
    try:
        if file.is_file():
            obj_name = Path(file.name).stem
            obj_ext = Path(file.name).suffix
            obj_dir = False
            lst_name.append(ObjectName(obj_name, obj_ext, obj_dir, file.parent.name))
        else:
            for item in file.iterdir():
                obj = directory_walk(item)
                lst_name.append(ObjectName(obj))
                logger.info(f'{obj}')

    except Exception as exc:
        print(f'\033[31mERROR: {exc.__class__.__name__}: {exc}\033[0m')
        logger.info(msg=f'{exc.__class__.__name__}: {exc}')

    return lst_name


def main():
    for pars_item in parse_args():
        for item in (dir_info(pars_item)):
            print(repr(item))


if __name__ == '__main__':
    main()