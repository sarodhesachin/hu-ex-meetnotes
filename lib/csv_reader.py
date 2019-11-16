import csv


class CSV_Reader(object):
    
    def __init__(self, file_path):
        self.file_path = file_path

        with open(self.file_path, 'r') as csv_file:
            self.headers = next(csv.reader(csv_file))

    def csv_generator(self):
        with open(self.file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                yield row
