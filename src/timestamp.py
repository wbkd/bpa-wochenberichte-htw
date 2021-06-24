# Unix Timestamp nach UTC Greenwich
import re
import datetime


def set_timestamp(original_title):
    # error=[]
    zahlen = re.findall('([0-9]+)', original_title)

    # last two numbers from list
    jahr = zahlen[-2]
    woche = zahlen[-1]

    datum = jahr + '-' + woche
    '''print('Datum: ',datum, 'Woche: ',woche)
    # check whether weeknumber is binary or not - it makes a difference whether the week starts on monday or tuesday
    if int(woche) < 10:
        r = datetime.datetime.strptime(datum + '-2', '%G-%V-%u')
    else:
        r = datetime.datetime.strptime(datum + '-1', '%G-%V-%u')'''

    r = datetime.datetime.strptime(datum + '-1', '%G-%V-%u')  # %u-weeknumber beginnt bei So
    timestamp = int(datetime.datetime(r.year, r.month, r.day).strftime('%s'))

    # day = time.strftime('%A', time.localtime(timestamp))
    '''if day!='Monday':
        error_message='Unix Timestamp is not Monday, but '+day
        error.append(error_message)
    '''
    # print('weekday: ', day)

    return timestamp  # , error
