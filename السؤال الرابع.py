# تعريف كلاس BankAccount مع الخصائص والطرق المطلوبة
class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number # رقم الحساب
        self.account_holder = account_holder # اسم صاحب الحساب
        self.balance = 0.0 # رصيد الحساب، يبدأ بصفر

    def deposit(self, amount):
        # طريقة إيداع المبلغ في الحساب
        self.balance += amount

    def withdraw(self, amount):
        # طريقة سحب المبلغ من الحساب
        self.balance -= amount

    def get_balance(self):
        # طريقة للحصول على رصيد الحساب الحالي
        return self.balance

# إنشاء كائن من كلاس BankAccount
account = BankAccount("1071", "علي زيني")

# إيداع مبلغ 1000 دولار
account.deposit(1000)
print("الرصيد الحالي:", account.get_balance()) # 1000.0

# سحب مبلغ 500 دولار
account.withdraw(500)
print("الرصيد الحالي:", account.get_balance()) # 500.0
print("ًصاحب الحساب:", account.account_holder)
# تعريف كلاس SavingsAccount التي ترث من كلاس BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate # معدل الفائدة

    def apply_interest(self):
        # طريقة لتطبيق الفائدة على رصيد الحساب
        self.balance += self.balance * self.interest_rate

    def __str__(self):
        # تعريف طريقة print() المخصصة
        return f"الرصيد الحالي: {self.get_balance():.2f} دولار، معدل الفائدة: {self.interest_rate:.2%}"

# إنشاء كائن من كلاس SavingsAccount
saccount = SavingsAccount("11010", "علي زيني", 0.05)

# تطبيق الفائدة على رصيد الحساب
saccount.apply_interest()
print(saccount) # الرصيد الحالي: 0.00 دولار، معدل الفائدة: 5.00%