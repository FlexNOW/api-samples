import csv
import sys

def write_csv_file(source, filename):
    """Writes each item in source list to specified file in csv format."""
    with open(filename, 'w', newline='') as csv_file: 
        file_writer = csv.writer(csv_file)

        for item in source:
            file_writer.writerow(item)


def write_console(source):
    """Writes each item in source list to the console in csv format."""
    console_writer = csv.writer(sys.stdout)

    for item in source:
        console_writer.writerow(item)