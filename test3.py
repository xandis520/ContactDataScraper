def add_urls(urls):
    values = ''
    n = len(urls) - 1
    for index, url in enumerate(urls):
        values += url
        if index != n:
            values += ', '
    return values

print(add_urls(['www.google.pl', 'www.wp.pl', 'amazon.com']))