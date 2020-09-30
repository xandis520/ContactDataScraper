import csv


class CSVDataHandle:
    def __init__(self, filename):
        if filename.endswith('.csv'):
            self.filename = filename
        else:
            self.filename = filename + '.csv'

    def add_tags(self, tags):
        with open(f'{self.filename}', 'a+', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(tags)
