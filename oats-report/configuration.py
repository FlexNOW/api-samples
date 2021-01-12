import configparser
import os
import sys
import datetime
import argparse

def load_config(filename):
    """Reads in .INI style configuration file."""
    config_file_name = filename
    config = configparser.ConfigParser()
    config.read(config_file_name)

    return config
    
def get_api_config():
    """
    Reads in API configuration.

    FLEXNOW_API_CLIENT_ID -- FlexNOW-provided client id
    FLEXNOW_API_SECRET_TOKEN -- FlexNOW-provided secret token
    FLEXNOW_API_BASE_URL -- Base URL of the api
        (default https://flexnow-uat.eu.flextrade.com/api/v3)
    """

    try:
        base_url = os.environ['FLEXNOW_API_BASE_URL']
    except KeyError:
        base_url = "https://flexnow-uat.eu.flextrade.com/api/v3"

    try:
        client_id = os.environ['FLEXNOW_API_CLIENT_ID']
        secret_token = os.environ['FLEXNOW_API_SECRET_TOKEN']
    except KeyError as e:
        print(f"Environment {e} must be set")
        sys.exit(1)

    return {
        "base_url": base_url,
        "client_id": client_id,
        "secret_token": secret_token
    }

def parse_arguments():
    """
    Parses command line arguments
    """

    parser = argparse.ArgumentParser(description='Process command line arguments.')
    parser.add_argument('--date', type=valid_date, help='the UTC date to run the report for in yyyy-MM-dd format')
    args = parser.parse_args()

    return args

def valid_date(s):
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)
