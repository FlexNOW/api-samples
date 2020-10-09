import json
import requests
from datetime import datetime
from orders import StreetOrder, ParentOrder
from execs import StreetOrderExec

class Api:
    def __init__(self, config):
        base_url = config.get("base_url")
        client_id = config.get("client_id")
        secret_token = config.get("secret_token")
        self.base_url = base_url
        self.access_token = self.get_access_token(client_id, secret_token)


    def generate_headers_with_auth(self):
        """Generates HTTP headers with authorization for API requests."""
        return {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.access_token
        }


    def generate_headers(self):
        """Generates HTTP headers for API requests."""
        return {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        

    def get_access_token(self, client_id, secret_token):
        """Authenticates with the API and returns an access token."""
        url = f"{self.base_url}/auth/client-token"
        data = {
            "clientId": client_id,
            "clientSecret": secret_token
        }
        response = requests.request(
            "POST", url, headers=self.generate_headers(), json=data)

        return json.loads(response.text).get("accessToken")


    def get_street_orders(self, date=datetime.today().strftime('%Y-%m-%d')):
        """Returns a list of StreetOrders for the specified date"""
        url = f"{self.base_url}/street-orders/summary?Date={date}"
        response = requests.request(
            "GET", url, headers=self.generate_headers_with_auth())

        for order in json.loads(response.text):
            yield StreetOrder(order)

    def get_parent_order(self, order_id):
        """Returns a ParentOrder with the specified order ID."""
        if order_id is None:
            return ParentOrder({})

        url = f"{self.base_url}/parent-orders/{order_id}/details"
        response = requests.request(
            "GET", url, headers=self.generate_headers_with_auth())

        return ParentOrder(json.loads(response.text))

    def get_street_order_execs(self, order_id):
        """Returns a list of StreetOrderExecs for the specified order ID"""
        url = f"{self.base_url}/street-orders/{order_id}/executions"
        response = requests.request(
            "GET", url, headers=self.generate_headers_with_auth())

        for execution in json.loads(response.text):
            yield StreetOrderExec(execution)
