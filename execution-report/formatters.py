class execution_report_formatter:
    def generate_header(self):
        return [
            "parent_load_time",
            "parent_client_order_id",
            "parent_notes",
            "street_id",
            "street_symbol",
            "street_load_time",
            "street_size",
            "exec_type",
            "exec_id",
            "exec_size",
            "exec_price",
            "exec_last_market",
            "exec_transaction_time"
        ]

    def format(self, street_order, parent_order, execution):
        """
        Returns an execution report for a specified street order/parent order/street exec.
        """

        return [
            parent_order.load_time,
            parent_order.client_order_id,
            parent_order.notes,
            street_order.id,
            street_order.symbol,
            street_order.load_time,
            street_order.size,
            execution.type,
            execution.id,
            execution.size,
            execution.price,
            execution.last_market,
            execution.transaction_time
        ]