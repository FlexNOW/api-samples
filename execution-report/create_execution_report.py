#!/usr/bin/env python3
 
from api import Api
from writers import write_csv_file, write_console
from formatters import execution_report_formatter
from configuration import load_config, get_api_config

def generate_report(include_headers=True):
    api_config = get_api_config()
    api = Api(api_config)
    formatter = execution_report_formatter()

    if include_headers:
        yield formatter.generate_header()
        
    street_orders = api.get_street_orders("2020-09-14")
    
    for street_order in street_orders:
        parent_order = api.get_parent_order(street_order.parent_id)
        street_executions = api.get_street_order_execs(street_order.id)
        for street_execution in street_executions:
            formatted_entry = formatter.format(street_order, parent_order, street_execution)
            yield formatted_entry


if __name__ == "__main__":
    report = generate_report()
    #write_csv_file(report, "oats_report.csv")
    write_console(report)
