from google_search import GoogleSearch
import csv
from traverse_page import *


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


def get_all_pages(phrase='', parser='lxml', user_agent='desktop', how_many_pages=5):
    #######################################################################
    # INITIAL SEARCHING INTERNAL AND EXTERNAL PAGE URLS
    #######################################################################
    # GETTING SOUP OF FIRST PAGE
    page = GoogleSearch(phrase)
    soup = page.get_soup(parser=parser, user_agent=user_agent)

    # INITIAL SEARCHING OF NEXT GOOGLE PAGES
    next_pages = page.get_next_pages(soup)

    # GETTING EXTERNAL LINKS OF FIRST GOOGLE PAGE
    external_links_list = []
    external_links = page.get_external_links(soup)
    try:
        for link in external_links:
            if link not in external_links_list:
                external_links_list.append(link)
    except:
        print('Some error')

    #######################################################################
    # SEARCHING EXTERNAL AND INTERNAL LINKS IN "FOR" LOOP
    #######################################################################
    for page_number in range(2, how_many_pages):
        try:
            #######################################################################
            # SEARCHING EXTERNAL LINKS IN GOOGLE PAGE
            #######################################################################
            soup = page.get_soup(url=next_pages[f'Page {page_number}'], parser=parser)
            external_links = page.get_external_links(soup)
            try:
                for link in external_links:
                    if link not in external_links_list:
                        external_links_list.append(link)
            except:
                print('Error')

            #######################################################################
            # SEARCHING INTERNAL (NEXT PAGES) LINKS IN GOOGLE PAGE
            #######################################################################
            if page_number >= 10:
                next_pages_iter = page.get_next_pages(soup)
                next_pages.update(next_pages_iter)
        except KeyError:
            print(f"Page {page_number} doesn't exist in google search.")
            print(f"Finished program on {page_number-1} pages.")
            break

    #######################################################################
    # SAVING FOUND LINKS IN DICTIONARY
    #######################################################################
    links = {
        'internal': next_pages,
        'external': external_links_list,
    }
    return links


def traverse_pages(file_name, settings, parser='html.parser', user_agent='desktop'):
    #######################################################################
    # CREATING AND WRITING FIRST ROW OF CONTACT DATA FILE
    #######################################################################
    file_name_contact = file_name[:-18] + 'contact_data.csv'
    with open(file_name_contact, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['id', 'page_url', 'phone', 'email', 'nip'])

    #######################################################################
    # TRAVERSING PAGES FROM FILE
    #######################################################################

    # OPEN FILE WITH PAGES URLS
    with open(file_name, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)

        #######################################################################
        # ITERATING THROUGH PAGES URLS
        #######################################################################
        for row in reader:
            try:
                #######################################################################
                # GETTING INTERNAL CONTACT URLS
                #######################################################################

                # GETTING INTERNAL URLS
                print(f'GETTING INTERNAL CONTACT LINKS OF PAGE: {row[1]}')
                page = CompanyDataSearch(url=row[1], parser=parser, user_agent=user_agent)
                internal_links = page.get_internal_links()

                # GETTING CONTACT PAGES URLS
                contact_pages = []
                contact_pages = get_contact_pages(internal_links)

                # CHECKING HOW MANY CONTACT URLS WAS FOUND
                if len(contact_pages) != 0:
                    print(contact_pages)
                    print(f'PROGRAM FOUND {len(contact_pages)} CONTACT PAGES')
                else:
                    print('PROGRAM COULD NOT FIND INTERNAL CONTACT PAGES')

                # ADDING MAIN PAGE URL TO CONTACT URLS
                contact_pages.append(row[1])
            except:
                print(f'PAGE {row[1]} COULD NOT BE SCRAPPED')

            #######################################################################
            # SEARCHING FOR CONTACT DATA IN CONTACT PAGES URLS
            #######################################################################
            print('SEARCHING FOR CONTACT DATA')
            contact_data = {
            "phone": None,
            "email": None,
            "street": None,
            "street_number": None,
            "apartment": None,
            "city": None,
            "postal_code": None,
            "nip": None,
            "regon": None
            }

            # ITERATING THROUGH CONTACT PAGES URLS
            for id, page_url in enumerate(contact_pages):
                # SEARCHING CONTACT DATA IN PAGE URL
                page = ContactData(url=page_url, parser=parser, user_agent=user_agent)
                contact_data_iter = page.get_contact_data(settings=settings['contact_data'])
                contact_data.update(contact_data_iter)
            print('CONTACT DATA:')
            print(contact_data)

            # INSERTING FOUND CONTACT DATA TO ROW
            row = [row[0], row[1], contact_data['phone'], contact_data['email'], contact_data['nip']]

            # SAVING ROW IN FILE
            with open(file_name_contact, 'a+', newline='') as csv_contact_file:
                writer = csv.writer(csv_contact_file)
                writer.writerow(row)


#######################################################################
# SEARCH DATA IN KRS DATABASE
#######################################################################
def find_data_in_krs():
    pass
