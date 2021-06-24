# param tables: dict with page numbers as keys and tables as values
# param headers: dict with page numbers as keys and headers as values
# combines them via page numbers
# returns dict with headers as keys and tables as values
def combine_tables_with_headers(tables, headers):
    result = {}
    errors = []

    for key, value in headers.items():

        if key in tables:

            # key exists in both and values are of same length --> no errors, header value becomes key, #
            # table value the value
            if len(value) == len(tables[key]):
                for i in range(len(value)):
                    result[value[i]] = tables[key][i]
                    i += 1

            # key exists in both, but lengths of values differ --> error message with affected page number an headers
            else:
                if len(value) > len(tables[key]):
                    error_message = "page {} : too many headers. Affected headers: {}".format(key, value)
                    errors.append(error_message)
                else:
                    error_message = "page {} : too many tables. Affected headers: {}".format(key, value)
                    errors.append(error_message)

        # headers has keys that don't exist in tables --> error message with affected page number an headers
        else:
            error_message = "no tables for headers on page {}. Affected headers: {}".format(key, value)
            errors.append(error_message)

    # tables has keys that don't exist in haeders --> error message with affected page number
    too_many_tables_error = ["no headers for tables on page {}".format(table_key) for table_key in tables if table_key
                             not in headers]
    errors += too_many_tables_error

    return result, errors
