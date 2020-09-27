from google_search import GoogleSearch
import csv


def save_pages(pages, file_name):
    with open(file_name, 'a+', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for id, page in enumerate(pages):
            writer.writerow([id+1, page])


def save_google_pg(pages, file_name):
    with open(file_name, 'a+', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in pages.items():
            writer.writerow([key, value])


def get_all_pages(phrase='', parser='lxml', how_many_pages=5):
    page = GoogleSearch(phrase)
    soup = page.get_soup(parser=parser)

    next_pages = page.get_next_pages(soup)

    external_links_list = []
    external_links = page.get_external_links(soup)
    try:
        for link in external_links:
            if link not in external_links_list:
                external_links_list.append(link)
    except:
        print('Some error')

    external_links = []

    for page_number in range(2, how_many_pages):
        # Pętla wyszukuje linki do kolejnych stron w wyszukiwarce i dopisuje je do słownika wyjściowego
        try:
            soup = page.get_soup(url=next_pages[f'Page {page_number}'], parser=parser)
            external_links = page.get_external_links(soup)
            try:
                for link in external_links:
                    if link not in external_links_list:
                        external_links_list.append(link)
            except:
                print('Some error')

            next_pages_iter = page.get_next_pages(soup)
            next_pages.update(next_pages_iter)
        except KeyError:
            print(f"Page {page_number} doesn't exist in google search.")
            print(f"Finished program on {page_number-1} pages.")
            break

    # for keys, values in next_pages.items():
    #     print(keys+':', values)

    # for index, link in enumerate(external_links_list):
    #     print(str(index+1)+':', link)

    # 1. Funkcja przeszukuje pierwszą podaną stronę i odnajduje wszystkie linki do kolejnych stron. (zapisuje linki w bazie danych lub pliku)
    # 2. Następnie uruchamia funkcję get_external_links i zapisuje linki w bazie danych
    # 3. Następnie wchodzi w kolejny link w zwróconym słowniku i znowu odnajduje wszystkie linki do kolejnych stron
    # 4. (nie dodaje tych już znalezionych wcześniej)
    # 5. Skrypt ponownie uruchamia funkcję get_external_links i dopisuje do linków w bazie danych
    # 6. (Skrypt sprawdza, czy linki nie istnieją już w bazie danych oraz, czy nie sę na black_liscie)
    # 7. Skrypt wraca do punktu 3. do momentu, aż nie znajdzie nowych linków do kolejnych stron google.

    # Skrypt kończy działać, kiedy nie znajdzie już żadnych nowych linków
    # Zwraca pełną listę linków zapisaną w pliku (tak, aby tylko część linków była zapisana w pamięci podręcznej)
    links = {
        'internal': next_pages,
        'external': external_links_list,
    }
    return links

def find_data_in_url():
    # Skrypt przeszukuje stronę internetową w poszukiwaniu danych o tej stronie
    pass

def find_data_in_krs():
    # Skrypt przeszukuje bazę danych krs na podstawie danych zebranych ze strony internetowej
    pass
