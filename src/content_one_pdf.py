from src.frontpage import get_indices, get_clean_frontpage_text, get_frontpage_content
from src.table_titles import fonts, font_tags, headers_para, delete_headers
from src.tables_one_pdf import save_clean_tables_with_page
from src.combine_headers_tables import combine_tables_with_headers
from src.timestamp import set_timestamp
from src.clean_title import clean_title
import fitz
import json

path_to_pdfs = "../rawdata/"
keys_frontpage = ["Wähleranteile:", "Kanzlerpräferenz:", "Politische Aufgaben:", "Wirtschaft:",
                  "Allgemeine Lebenslage:", "Eigene finanzielle Lage:", "Themen der Bundesregierung:",
                  "Themen Bundesregierung:", "Weltpolitische Lage:", "Flüchtlinge:", "Diesel:", "Wichtigstes Thema:",
                  "Wichtigste Themen:", "Anlage:", "Anlagen:"]
headers_to_be_deleted = ['Frau Bundeskanzlerin', 'Wähleranteile im Vergleich', ''
                                                                               'Beurteilung der Arbeit der Bundesregierung in "sehr wichtigen" politischen Aufgabenbereichen',
                         'Die wichtigsten Themen', 'wichtigsten Themen des ersten Halbjahres',
                         'wichtigsten Themen im ersten Halbjahr']


def extract_content_from_one_pdf(path_to_pdf, path_to_destination):
    """
    get one json with relevant content of one PDF, combining all methods needed therefore

    Necessary steps:

     1. load pdf
     2. add timestamp
     3. extract frontpage
     4. extract headers
     5. extract tables
     6. combine headers and tables and collect errors
     7. change pdf name for saving
     8. save as json
   """

    content = {}

    # 1.
    doc = fitz.open(path_to_pdf)

    # 2.
    timestamp = set_timestamp(path_to_pdf)
    content['date'] = timestamp

    # 3.
    frontpage_text = get_clean_frontpage_text(doc)
    indices = get_indices(frontpage_text, keys_frontpage, 'Ende')
    frontpage_content = get_frontpage_content(frontpage_text, indices)  # --> returns dict with 'headers' as keys
    content['frontpage'] = frontpage_content

    # 4.
    font_counts, styles = fonts(doc)
    size_tag = font_tags(font_counts, styles)
    headers = headers_para(doc, size_tag)
    clean_headers = delete_headers(headers, headers_to_be_deleted)

    # 5.
    tables = save_clean_tables_with_page(path_to_pdf)

    # 6.
    combined_headers_tables, errors = combine_tables_with_headers(tables, clean_headers)
    content['tables'] = combined_headers_tables
    content['errors'] = errors

    # 7.
    title = clean_title(path_to_pdf)

    # 8.
    with open(path_to_destination + '{}.json'.format(title), 'w') as json_file:
        json.dump(content, json_file, ensure_ascii=False)

    return content, title


if __name__ == "__main__":
    example_path = '../rawdata/WB 2017 51 KW.pdf'

    content_dict, pdf_title = extract_content_from_one_pdf(example_path, '../jsons/')

    print(content_dict.keys(), pdf_title)
    print("content = ", content_dict)
