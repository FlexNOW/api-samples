class StreetOrderExec:
    def __init__(self, exec_info):
        self.id = exec_info.get("id")
        self.size = exec_info.get("size")
        self.price = exec_info.get("price")
        self.last_market = exec_info.get("lastMarket")
        self.transaction_time = exec_info.get("transactionTime")
        self.type = exec_info.get("executionType")