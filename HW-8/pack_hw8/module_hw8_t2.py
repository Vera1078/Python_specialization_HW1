import csv
import pickle


def read_csv(csv_file):
    with open(csv_file, 'r', newline='', encoding='utf-8') as f1:
        csv_read = list(csv.reader(f1))
        headers = csv_read.pop(0)
        lst = []
        for row in csv_read:
            dct = {}
            for i, cell in enumerate(row):
                dct[headers[i]] = cell
            lst.append(dct)
        pickle_res = pickle.dumps(lst)
        print(pickle_res)