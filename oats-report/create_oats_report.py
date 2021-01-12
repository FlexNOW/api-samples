#!/usr/bin/env python3
 
from api import Api
from writers import write_csv_file, write_console
from formatters import format_oats
from configuration import load_config, get_api_config, parse_arguments
import pytz

def generate_report():
    broker_config = load_config("broker.ini")
    api_config = get_api_config()
    api = Api(api_config)
    date = parse_arguments().date

    if date:
        street_orders = api.get_street_orders(date)
    else:
        street_orders = api.get_street_orders()

    eastern_timezone = pytz.timezone('US/Eastern')

    for street_order in street_orders:
        parent_order = api.get_parent_order(street_order.parent_id)
        formatted_entry = format_oats(street_order, parent_order, broker_config, eastern_timezone)
        
        yield formatted_entry


if __name__ == "__main__":
    report = generate_report()
    write_csv_file(report, "oats_report.csv")
    # write_console(report)
