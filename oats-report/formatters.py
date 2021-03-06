import sys

def format_oats(street_order, parent_order, config):
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
        parent_order.load_time,
        parent_order.client_order_id,
        broker_mpid,
        street_order.id,
        street_order.symbol,
        street_order.load_time,
        street_order.size,
        "E",
        "",
        "",
        broker_destination_code,
        street_order.price_type,
        "",
        "",
        "",
        "",
        "",
        ""
    ]