with open('external_link_test.csv', 'a+', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['id', 'link'])
    for iteration, link in enumerate(links):
        writer.writerow([iteration + 1, link])