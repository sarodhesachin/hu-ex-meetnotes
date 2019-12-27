import re

from common import constants as CONSTANTS
from lib.csv_reader import CSV_Reader


class MeetNotes(object):

    def __init__(self):
        self.csv = CSV_Reader(CONSTANTS.MEET_NOTES_CSV_FILE_PATH)

    def get_most_active_pages(self):
        pass

    def get_most_active_user(self):
        pass

    def get_most_viewed_pages(self):

        for record in self.csv.csv_generator():
            # print(re.findall(r'(/+[+]?[a-z]+)+', record['location']))
            record = record['location'].split('?')[0]
            print(record)
            print(re.findall(r'', record))

        # values = self.csv.get_columns('location')
        # unique_values = {'/', }
        # for value in values:
        #     temp = re.findall(r'/[+]?[a-z]*/?', value)
        #     if len(temp) > 0:
        #         unique_values.add(temp[0])
        #
        # # unique_values = {re.findall(r'/', value) for value in values}
        # print(values[81])
        # print(re.findall(r'/[+]?[a-z]*/?', values[81]))
        # print(unique_values)
        # for row in self.csv.csv_generator1():
        #     print(row)


if __name__ == "__main__":
    print("Running meet notes")
    m = MeetNotes()
    m.get_most_viewed_pages()
