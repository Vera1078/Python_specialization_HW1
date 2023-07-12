import csv
import pickle


def pickle_to_csv(pickle_file):
    with(
        open(pickle_file, 'rb') as pickle_file,
        open('csv_file.csv', 'w', newline='', encoding='utf-8') as csv_f,
    ):
        data = pickle.load(pickle_file)
        headers = []
        for dct in data:
            for header in dct.keys():
                if header not in headers:
                    headers.append(header)
        csv_write = csv.DictWriter(csv_f, fieldnames=headers)
        csv_write.writeheader()
        for dct in data:
            csv_write.writerow(dct)