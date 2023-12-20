class ATM:

    def __init__(self):
        self.book = [0, 0, 0, 0, 0]
        self.index = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, bank_note in enumerate(banknotesCount):
            self.book[i] += bank_note

    def withdraw(self, amount: int) -> List[int]:
        ans = [0, 0, 0, 0, 0]
        for i in range(4, -1, -1):
            ans[i] = min(self.book[i], amount // self.index[i])
            amount -= ans[i] * self.index[i]
        
        if amount == 0:
            self.book = [a - b for a, b in zip(self.book, ans)]

        return [-1] if amount else ans



# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)