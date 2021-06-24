import camelot
import warnings

warnings.simplefilter("ignore", UserWarning)


def save_clean_tables_with_page(file):
    """
    extracts all tables of one pdf and removes unnecessary symbols
    Returns dict of pages as keys and dict of tables as values
   """

    tables = camelot.read_pdf(file, pages='1-end', strip_text='\n')
    tables_dict = {}

    for i in range(len(tables)):
        # just keep tables with accuracy over 90
        if tables[i].parsing_report['accuracy'] > 90:
            page = tables[i].parsing_report['page']

            # remove unnecessary information in cells
            df = tables[i].df.replace(to_replace='\s?\(.{1,4}\)\s?', value='', regex=True)

            first_row = []
            first_column = []

            # save elements of first row (header)
            count = 0
            for i in df[0:1].values:
                first_row.append(i)
            first_row = first_row[0]

            for i in first_row:
                if i == '':
                    count += 1

            if len(first_row) == count:
                del first_row
            else:
                # header of first column ='key' if no header existent
                if first_row[0] == '':
                    first_row[0] = 'key'

                # save elements of first column
                for j in df[0].values:
                    first_column.append(j)

                # rename header of column to elements of first row of list first_row
                df.columns = first_row
                # rename row indices to elemtns of first column of list first_column
                df.index = first_column

                # remove first row as it became header row
                df_clean = df.drop(first_column[0])

                # df to dict
                result_dict = df_clean.to_dict('records')

                if page in tables_dict:
                    tables_dict[page].append(result_dict)
                else:
                    tables_dict[page] = [result_dict]

    return tables_dict
