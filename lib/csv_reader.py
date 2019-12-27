import csv


class CSV_Reader(object):
    
    def __init__(self, file_path):
        self.file_path = file_path

        with open(self.file_path, 'r') as csv_file:
            header = next(csv.reader(csv_file))[0]
            self.headers = header.split('\t')

    # def csv_generator(self):
    #     with open(self.file_path, 'r') as csv_file:
    #         reader = csv.reader(csv_file)
    #         for row in reader:
    #             yield row

    def csv_generator(self):
        with open(self.file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                key = next(iter(row))
                value = row.get(key, '')

                key = key.split('\t')
                value = value.split('\t')
                yield dict(zip(key, value))

    def get_columns(self, column):
        col_position = self.headers.index(column)
        items = list()
        for row in self.csv_generator():
            row_content = row[0].split('\t')
            if len(row_content) > col_position:
                items.append(row_content[col_position])

        # Returning all items except header
        return items[1:]
