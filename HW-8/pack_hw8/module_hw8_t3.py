import os
import json
import csv
import pickle
from pathlib import Path


def get_dir_size(drc):
    total_size = 0
    for path, dirs, files in os.walk(drc):
        for file in files:
            total_size += os.path.getsize(os.path.join(path, file))
    return total_size


def save_dir_info(path_):

    p = Path(path_)
    description = []
    for path, dirs, files in os.walk(p):

        for d in dirs:
            description.append({'obj': d, 'parent': os.path.basename(path), 'obj_type': 'directory',
                         'size': get_dir_size(os.path.join(path, d))})
        for file in files:
            description.append({'obj': file, 'parent': os.path.basename(path), 'obj_type': 'file',
                         'size': os.path.getsize(os.path.join(path, file))})

    if not os.path.exists('Catalog'):
        os.makedirs('Catalog')

    with(
        open('Catalog/data.json', 'w', encoding='utf-8') as j,
        open('Catalog/data.csv', 'w', newline='', encoding='utf-8') as c,
        open('Catalog/data.pickle', 'wb') as p
    ):
        json.dump(description, j)

        csv_write = csv.DictWriter(c, fieldnames=['obj', 'parent', 'obj_type', 'size'])
        csv_write.writeheader()
        csv_write.writerows(description)
        pickle.dump(description, p)