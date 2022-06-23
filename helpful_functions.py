def to_date_str(date_arr, sep="/"):
    '''
    Input: array like [year, month]; separator
    Output: string like {year}{sep}{month}
    '''
    year = str(date_arr[0])
    month = ('0' + str(date_arr[1]))[-2:]
    return year + sep + month

def add_month(date_str, sep="/"):
    '''
    Return next month in format year-month.

    Input: string like {year}{sep}{month}
    Output: string like {year}{sep}{manth+1}
    '''
    date_arr = [int(i) for i in date_str.split(sep)]
    if date_arr[1] != 12:
        date_arr[1] += 1
    else:
        date_arr[1] = 1
        date_arr[0] += 1
    return to_date_str(date_arr, sep=sep)

def generate_months_in_period(start_month=4, start_year=2019, end_month=6, end_year=2022, sep="/"):
    '''
    Returns list of all monthes in period between start year-month and end year-month.
    '''
    cur_date_str = to_date_str([start_year, start_month], sep=sep)
    end_date_str = to_date_str([end_year, end_month], sep=sep)
    dates_str_list = list()
    if cur_date_str == end_date_str:
        dates_str_list = [cur_date_str]
    else:
        while True:
            dates_str_list.append(cur_date_str)
            cur_date_str = add_month(cur_date_str, sep=sep)
            if cur_date_str == end_date_str:
                dates_str_list.append(cur_date_str)
                break
    return dates_str_list