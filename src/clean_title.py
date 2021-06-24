import glob
import re

path_to_pdfs = "../rawdata/"


def load_all_titles(path_to_pdfs):
    pdf_titles = glob.glob('../rawdata/*.pdf')
    return pdf_titles


all_titles = load_all_titles(path_to_pdfs)


def clean_title(original_title):
    pattern = re.compile(r'[WwBb]{2}[\s-]\d{4}[\s-]\d{1,2}[\s-][KkWw]{2}')
    match = re.search(pattern, original_title)
    title = match.group(0)
    final_title = title.replace(" ", "_")
    return final_title


titles = []
for title in all_titles:
    cleaned_title = clean_title(title)
    titles.append(cleaned_title)
