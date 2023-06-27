# 9.15.5 csv Module
# https://docs.python.org/3/library/csv.html

import csv

# Read a CSV file into a list of tuples
def read_csv_data(filename):
    with open(filename, newline='') as file:
        rows = csv.reader(file)
        # First line is often a header. This reads it
        headers = next(rows)
        print(headers)
        # Now read the rest of the data
        for row in rows:
            # Do something with row
            print(row)


# Write Python data to a CSV file
def write_csv_data(filename, headers, rows):
    with open(filename, 'w', newline='') as file:
        out = csv.writer(file)
        out.writerow(headers)
        out.writerows(rows)

def close_enough(lat, lon):
    if lat >= 40.0 and lat <= 45.0:
        if lon >= 20.0 and lon <= 25.0:
            return True
    return False

# https://github.com/albertyw/avenews/blob/master/old/data/average-latitude-longitude-countries.csv
def find_nearby(filename):
    with open(filename, newline='') as file:
        # DictReader interprets the first line of a CSV file as headers
        # and returns each row as a dictionary instead of a tuple
        rows = csv.DictReader(file)
        for row in rows:
            lat = float(row['Latitude'])
            lon = float(row['Longitude'])
            if close_enough(lat, lon):
                country = row['Country']
                country_code = row['Country Code']
                print(f"{country} [{country_code}] ({lat}, {lon})")

if __name__ == "__main__":
    read_csv_data('data/portfolio.csv')
    print()
    find_nearby('data/countries.csv')