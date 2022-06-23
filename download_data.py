import urllib.request
import time
import helpful_functions
from os import path

# fill next few rows with actual info
# by defalut, will be downloaded for Oslo, all existing data (since 2019-04 till 2022-06) into folder ./data.
city_name = 'oslo'        # можливі варіанти: olso, bergen, trondheim

start_month = 4           # 1 - 12
start_year = 2019         # 2019 - 2022

end_month = 6             # 1 - 12
end_year = 2022           # 2019 - 2022

destination_folder = './data'
# end filling

def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)    
    file = open(filename, 'wb')
    file.write(response.read())
    file.close()

# generate all possible month-year combinations within the selected period
dates_str_list = helpful_functions.generate_months_in_period(
    start_month=start_month, 
    start_year=start_year, 
    end_month=end_month, 
    end_year=end_year, 
    sep="/")

# download files
start = time.time()
if path.exists(destination_folder):
    for date in dates_str_list:
        download_url = f"https://data.urbansharing.com/{city_name}bysykkel.no/trips/v1/{date}.csv"
        filename = f"{city_name}_{date.replace('/', '_')}.csv"
        print("in progres: ", filename[:-4])
        destination_full_path = '/'.join([destination_folder, filename])
        download_file(download_url, destination_full_path)
else:
    print("Destination folder not found")
end = time.time()
print('Time: ', end - start, ' s')