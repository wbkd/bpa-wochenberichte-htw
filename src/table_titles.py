from operator import itemgetter

"""Script to extract all table headers of one pdf, using font styles and sizes to identify headers.

Most parts of the code gratefully taken from  https://ichi.pro/de/extrahieren-von-uberschriften-und-absatzen-aus-pdf
-mit-pymupdf-113724360868967 

Headers that don't belong to tables can be deleted.
Headers are being saved in a dict with page numbers as keys and the actual headers as values.

The right element tag for the pdfs is h3.

Param doc: PDF document to iterate through of type <class 'fitz.fitz.Document'>

Returns all existing combinations of fonts and their font-sizes in spans of one pdf, sorted by occurrence.
"""


def fonts(doc):
    styles = {}
    font_counts = {}

    for page in doc:
        blocks = page.getText("dict")["blocks"]
        for b in blocks:  # iterate through the text blocks
            if b['type'] == 0:  # this block contains text
                for l in b["lines"]:  # iterate through the text lines
                    for s in l["spans"]:  # iterate through the text spans
                        identifier = "{0}".format(s['size'])
                        styles[identifier] = {'size': s['size'], 'font': s['font']}

                        font_counts[identifier] = font_counts.get(identifier, 0) + 1  # count use of font

    font_counts = sorted(font_counts.items(), key=itemgetter(1), reverse=True)

    return font_counts, styles


def font_tags(font_counts, styles):
    """Returns dictionary with font sizes as keys and tags as value.
    :param font_counts: (font_size, count) for all fonts occuring in document
    :type font_counts: list
    :param styles: all styles found in the document
    :type styles: dict
    :rtype: dict
    :return: all element tags based on font-sizes
    """
    p_style = styles[font_counts[0][0]]  # get style for most used font by count (paragraph)
    p_size = p_style['size']  # get the paragraph's size

    # sorting the font sizes high to low, so that we can append the right integer to each tag
    font_sizes = []
    for (font_size, count) in font_counts:
        font_sizes.append(float(font_size))
    font_sizes.sort(reverse=True)

    # aggregating the tags for each font size
    idx = 0
    size_tag = {}
    for size in font_sizes:
        idx += 1
        if size == p_size:
            idx = 0
            size_tag[size] = '<p>'
        if size > p_size:
            size_tag[size] = '<h{0}>'.format(idx)
        elif size < p_size:
            size_tag[size] = '<s{0}>'.format(idx)
    # if h3 not exist then overwrite h2 to h3
    if not '<h3>' in size_tag.values():
        for key, value in size_tag.items():
            if '<h2>' == value:
                size_tag[key] = '<h3>'

    return size_tag


def headers_para(doc, size_tag):
    """Scrapes headers & paragraphs from PDF and return texts with element tags.
    :param doc: PDF document to iterate through
    :type doc: <class 'fitz.fitz.Document'>
    :param size_tag: textual element tags for each size
    :type size_tag: dict
    :rtype: list
    :return: texts with pre-prended element tags
    """
    header_dict = {}
    page_number = 0
    previous_string = {}
    first = True

    for page in doc:
        page_number += 1
        blocks = page.getText("dict")["blocks"]

        for infos in blocks:
            if infos['type'] == 0:
                for line in infos["lines"]:
                    for s in line["spans"]:
                        if s['text'].strip():
                            if first:
                                previous_string = s
                                first = False
                            else:
                                if size_tag[s['size']] == '<h3>' and size_tag[previous_string['size']] == '<h3>':

                                    # If current and previous span is h3: combine them
                                    block_string = previous_string['text'] + s['text'].strip()
                                    test = [block_string.strip()]

                                    if page_number in header_dict:  # if key already exists
                                        if type(header_dict[page_number]) == list:
                                            header_dict[page_number].append(
                                                block_string.strip())  # add header as value
                                    else:
                                        # add page number as key, header as value
                                        # header_para[page_number] = block_string
                                        header_dict[page_number] = test
                                    value_list = header_dict[page_number]

                                    if type(value_list) == list and len(value_list) > 1:
                                        del value_list[-2]  # delete incomplete header

                                # For headers of one line only:
                                elif size_tag[s['size']] == '<h3>':  #
                                    if page_number in header_dict:
                                        if type(header_dict[page_number]) == list:
                                            header_dict[page_number].append(s['text'].strip())
                                    else:
                                        header_dict[page_number] = [s['text'].strip()]

                                previous_string = s  # set previous_string to current span 
    return header_dict


def delete_headers(headers, headers_to_be_deleted):
    """delete those that don't belong to tables (headers_to_be_deleted set in content_one_pdf.py)
    """
    keys_to_be_deleted = []

    for elem in headers_to_be_deleted:
        for key, value in headers.items():  # iterate through every page with extracted headers
            for i, header in enumerate(value):  # iterate through headers on one page
                if elem in header:
                    if len(value) == 1:  # list consists of only one header: save key to delete later
                        keys_to_be_deleted.append(key)
                    else:  # otherwise delete only the one header value
                        del value[i]
                        i -= 1

    for key in keys_to_be_deleted:
        headers.pop(key, None)

    return headers
