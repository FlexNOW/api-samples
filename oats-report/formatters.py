import sys
import datetime
import pytz

def format_from_iso_time(iso_timestamp, timezone):
    try:
        dt = datetime.datetime.fromisoformat(iso_timestamp.replace('Z', '')).replace(tzinfo=pytz.UTC)
        return dt.astimezone(timezone).strftime('%Y%m%d%H%M%S%f')[:-3]
    except:
        return None

def format_from_street_order_time(timestamp, timezone):
    try:
        dt = datetime.datetime.strptime(timestamp.replace('Z', ''), "%Y-%m-%dT%H:%M:%S.%f").replace(tzinfo=pytz.UTC)
        return dt.astimezone(timezone).strftime('%Y%m%d%H%M%S%f')[:-3]
    except:
        return None

def format_oats(street_order, parent_order, config, timezone=pytz.timezone('UTC')):
    """
    Returns an OATS formatted report for a specified street/parent order.
    
    config should be a list of objects in the format:
    [
        "Broker1": {"mpid": "BRKO", "destination_code": "D"},
        "Broker2": {"mpid": "BRKT", "destination_code": "M"}
    ]
    with the appropriate MPID and destination codes per broker.
    """
    try:
        broker_mpid = config[street_order.destination]["mpid"]
        broker_destination_code = config[street_order.destination]["destination_code"]
    except KeyError:
        print(f"Destination {street_order.destination} must have mpid and destination_code configured")
        sys.exit(1)

    return [
        "#OE#",
        "RT",
        "N",
        "",
        "",
        "",
        "BROC",
        format_from_iso_time(parent_order.load_time, timezone),
        parent_order.compliance_id,
        broker_mpid,
        street_order.id,
        street_order.symbol,
        format_from_street_order_time(street_order.load_time, timezone),
        int(street_order.size),
        "E",
        "",
        "",
        broker_destination_code,
        street_order.price_type,
        street_order.route_price,
        "",
        "",
        "",
        "",
        ""
    ]