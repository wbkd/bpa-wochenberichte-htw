# extracts only relevant words from frontpage, returns one string
# param doc: PDF document to iterate through of type <class 'fitz.fitz.Document'>

def get_clean_frontpage_text(doc):
    page = doc.loadPage(0)
    text = page.getText('text')  # extract text from pdf
    clean_text = text.split()  # removes formatting info etc and returns list of strings
    remove_unwanted_words(clean_text)
    index = clean_text.index("Wähleranteile:")
    relevant_words = clean_text[index:]  # only keep words beginning from 'Wähleranteile'
    joined_words = ' '.join(relevant_words)  # join all relevant words back together
    return joined_words


# removes unwanted words from relevant words, like "Steffen Seibert"
def remove_unwanted_words(wordlist, unwanted_words=["Steffen", "Seibert"]):
    for unwanted_word in unwanted_words:
        if unwanted_word in wordlist:
            wordlist.remove(unwanted_word)
    return wordlist


# takes (hard coded) key words and returns list of key + their start- and end indices
def get_indices(text, keys, end_word):  # choose end_word freely, for example 'Ende'
    indices = []

    for key in keys:
        if key in text:
            start_index = text.find(key)
            end_index = text.find(key) + len(key)
            temp_list = [key, start_index, end_index]
            indices.append(temp_list)
    end_list = [end_word, len(text)]
    indices.append(end_list)
    return indices


# takes clean text (only relevant words as string) and returns dict with
# topic as key and content as value
def get_frontpage_content(text, keys_with_indices):
    title_page = {}
    values = []
    counter = 0
    endword = keys_with_indices[-1][0]

    for key in keys_with_indices:
        if keys_with_indices[counter][0] in text:
            key = keys_with_indices[counter][0].replace(":", "")
            start_index = keys_with_indices[counter][2] + 1
            if keys_with_indices[counter + 1][0] == endword:
                end_index = keys_with_indices[counter + 1][1]
            else:
                end_index = (keys_with_indices[counter + 1][1])
            for item in text[start_index:end_index]:
                values.append(item)
                string_values = ''.join(values)

            title_page[key] = string_values.rstrip()
            values.clear()
            counter += 1

    return title_page
