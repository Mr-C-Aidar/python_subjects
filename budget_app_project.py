class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for entry in self.ledger:
            total += entry["amount"]
        return total

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title_len = 30
        name_len = len(self.name)
        stars_left = (title_len - name_len) // 2
        stars_right = title_len - stars_left - name_len
        title = "*" * stars_left + self.name + "*" * stars_right + "\n"

        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]
            amount = f"{entry['amount']:.2f}"
            # Ограничиваем длину amount до 7 символов, справа выравниваем
            amount = amount[:7]
            items += desc.ljust(23) + amount.rjust(7) + "\n"

        total = self.get_balance()
        total_line = f"Total: {total:.2f}"

        return title + items + total_line


def create_spend_chart(categories):
    spent_amounts = []
    total_spent = 0
    for cat in categories:
        spent = 0
        for entry in cat.ledger:
            if entry["amount"] < 0:
                spent += -entry["amount"]
        spent_amounts.append(spent)
        total_spent += spent

    spent_percentages = [int((spent / total_spent) * 100) // 10 * 10 for spent in spent_amounts]

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        line = str(i).rjust(3) + "|"
        for percent in spent_percentages:
            if percent >= i:
                line += " o "
            else:
                line += "   "
        line += " "
        chart += line + "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        line = "     "
        for cat in categories:
            if i < len(cat.name):
                line += cat.name[i] + "  "
            else:
                line += "   "
        chart += line + "\n"

    if chart.endswith('\n'):
        return chart[:-1]
    return chart