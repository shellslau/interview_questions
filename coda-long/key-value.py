class ValueStore:
    def __init__(self):
        self.keyValue = {}
        self.counts = {}
        self.currentTransaction = None

    def set(self, key, value):
        if (key in self.keyValue):
            self.counts[self.keyValue[key]] -= 1

        self.keyValue[key] = value

        if (value in self.counts.keys()):
            self.counts[value] += 1
        else:
            self.counts[value] = 1

    def delete(self, key):
        value = self.keyValue[key]
        self.keyValue.pop(key, None)

        if (value in self.counts.keys() and self.counts[value] <= 1):
            self.counts.pop(value, None)
        else:
            self.counts[value] -= 1

    def get(self, key):
        if (key in self.keyValue.keys()):
            return self.keyValue[key]
        else:
            return f'{key} not set'

    def count(self, value):
        if (value in self.counts.keys()):
            return self.counts[value]
        else:
            return 0

    def begin(self):
        self.currentTransaction = Transaction(self.counts, self.keyValue, self.currentTransaction)

    def commit(self):
        if (not self.currentTransaction):
            print("No Transaction")
            return

        self.currentTransaction = self.currentTransaction.get_old_transaction()

    def rollback(self):
        if (not self.currentTransaction):
            print("No Transaction")
            return

        self.keyValue = self.currentTransaction.get_old_key_value()
        self.counts = self.currentTransaction.get_old_counts()
        self.currentTransaction = self.currentTransaction.get_old_transaction()


class Transaction:
    def __init__(self, counts, keyValue, parentTransaction):
        self.counts = counts.copy()
        self.key_value = keyValue.copy()
        self.parentTransaction = parentTransaction

    def get_old_counts(self):
        return self.counts

    def get_old_key_value(self):
        return self.key_value

    def get_old_transaction(self):
        return self.parentTransaction

def __main__():
    valueStore = ValueStore()

    while(True):
        command = input()
        args = command.split()

        if(args[0] == "SET"):
            valueStore.set(args[1], args[2])
        if(args[0] == "DELETE"):
            args = command.split()
            valueStore.delete(args[1])
        if(args[0] == "GET"):
            print(valueStore.get(args[1]))
        if(args[0] == "COUNT"):
            print(valueStore.count(args[1]))
        if(args[0] == "BEGIN"):
            valueStore.begin()
        if(args[0] == "COMMIT"):
            valueStore.commit()
        if(args[0] == "ROLLBACK"):
            valueStore.rollback()



# valueStore =  ValueStore()
# valueStore.set("A", "1")
# valueStore.set("B", "1")
# valueStore.set("C", "2")
# valueStore.set("A", "8")
# valueStore.set("D", "2")

# valueStore.begin()
# valueStore.set("X", "h")
# valueStore.set("A", "h")
# valueStore.commit()

# valueStore.begin()
# valueStore.set("X", "y")
# valueStore.rollback()


# print(valueStore.get("A"))
# print(valueStore.get("B"))
# print(valueStore.get("C"))
# print(valueStore.get("X"))
# print(valueStore.count("A"))
# print(valueStore.count("1"))
# print(valueStore.count("2"))

if __name__ == __main__():
    main()
