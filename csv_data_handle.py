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

# with open('external_link_test.csv', 'a+', newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['id', 'link'])
#     for iteration, link in enumerate(links):
#         writer.writerow([iteration + 1, link])

writer = CSVDataHandle('test1')
writer.add_tags(['id', 'abcd', 'defg'])
