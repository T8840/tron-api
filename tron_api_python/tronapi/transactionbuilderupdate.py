from tronapi.transactionbuilder import TransactionBuilder
class CustomTransactionBuilder(TransactionBuilder):
    def check_permissions(self, permissions, _type):
        if permissions is not None:
            if permissions['type'] != _type or \
                    not permissions['permission_name'] or \
                    permissions['threshold'] < 1 or not permissions['keys']:
                return False
        return True