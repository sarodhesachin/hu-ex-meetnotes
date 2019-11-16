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
        pass


if __name__ == "__main__":
    print("Running meet notes")
    m = MeetNotes()

    for row in m.csv.csv_generator():
        print(row)
