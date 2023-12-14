from hw_15_sims.bank.bank_account import BankAccount


class Human:
    created_passport_nums = set()

    def __init__(self, name, passport_num):
        if passport_num in self.created_passport_nums:
            raise ValueError('This passport already exists')

        self.name = name
        self.passport_num = passport_num
        bank_acc = BankAccount(self.passport_num)
        self.__bank_account = bank_acc
        self.company = None

    def work(self):
        if not self.company:
            print('Go find you job..')
            return

        salary = self.company.increase_money()
        self.__bank_account.increase_money(salary)

    def __str__(self):
        return f'{self.name} {self.passport_num}'
