
'''
def black_list_remove(link):
    black_list = [
        'https://pl.wikipedia.org',
        'https://www.google.pl',
        'https://www.yahoo.com'
    ]
    if link not in black_list:
        return link
    else:
        return None


if __name__ == "__main__":
    external_links_list = []
    phrase = 'biura+architektoniczne+warszawa'
    webpage = google_web_page(phrase)
    bsObj = BeautifulSoup(webpage, 'lxml')
    if webpage != None:
        links = get_external_links(bs_obj=bsObj)
        for link in links:
            if black_list_remove(link) != None:
                external_links_list.append(link)

    print(external_links_list)

    # SEKCJA: Pobieranie kolejnej strony z google
    get_next_page(bs_obj=bsObj)

    # dodanie linków do bazy danych mysql (tworzy bazę danych na podstawie wpisanej kategorii np. biura architektoniczne łódź = biura_architektoniczne_lodz)
    # kolumny = (id, data_pierwszego dodania, ostatnia aktualizacja, nazwa firmy, strona internetowa, przeszukana strona - Tak lub Nie, mail, nr telefonu, fax, Ulica, Miejscowość, Kod pocztowy, KRS, NIP, REGON, Kapitał zakładowy, Forma prawna, Data Rejestracji, Ostatnia zmiana w KRS, Reprezentacja, Sposób reprezentacji, Sąd, Sygnatura, Podstawowa działalność, Wspólnicy, Zarząd, Prokura, Właściciel)
    # stworzenie bazy danych black listy (wikipedia, google, amazon, allegro , wp, onet itp.)
    # pobranie linku z bazy 
'''
