from src.content_one_pdf import extract_content_from_one_pdf
import glob
import json


def content_all_pdfs(path_to_source_directory, path_to_target_directory):
    """
    extracts content of all pdfs stored in path_to_source_directory, saving one json file per pdf and additionally
    one file with aggregated error messages at path_to_target
    param path_to_source_directory: path to directory to all pdfs
    param path_to_target: path to target directory
   """

    all_contents = []
    all_errors = {}

    all_full_paths = glob.glob(path_to_source_directory + '*.pdf')

    for path in all_full_paths:
        print(path)

        content_single_pdf, title = extract_content_from_one_pdf(path, path_to_target_directory)
        all_contents.append(content_single_pdf)

        if len(content_single_pdf['errors']) is not 0:
            all_errors[title] = content_single_pdf['errors']
            print('errors: ', content_single_pdf['errors'])

    with open(path_to_target_directory + 'errors/errors.json', 'w') as json_file:
        json.dump(all_errors, json_file, ensure_ascii=False)

    return all_contents, all_errors


if __name__ == "__main__":
    path_to_pdf = "../rawdata/"

    contents, errors = content_all_pdfs(path_to_pdf, '../jsons/')
    # print(errors)