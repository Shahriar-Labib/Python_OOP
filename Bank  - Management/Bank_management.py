import random
class User:
    def __init__(self) -> None:
        self.accounts = {}
        self.transactions = {}
        self.loan_check = {}
        self.bank_balance = 20000000000
        self.bank_loans = 0

    def create_account(self,name,email,address,account_type):
        try:
            account_number = int(random.randint(100, 999999) + len(address))
            self.accounts[account_number] = {
                'Name' : name,
                'Email' : email,
                'Address' : address,
                'Account_Type' : account_type,
                'Balance' : 0,
                'loan_taken' : 0
            }
            self.loan_check[account_number] = {
                'enable_loan' : 'on'
            }

            self.transactions[account_number] = []
            
            return account_number
        
        except ValueError:
            print("Invalid input")
    
    def deposit(self,account_number,amount):
        try:
            if account_number in self.accounts:
                if amount > 0:
                    print(f"TK {amount} deposit successfully")
                    self.accounts[account_number]['Balance'] += amount
                    self.bank_balance += amount
                    self.transactions[account_number].append(f'TK {amount} Deposited')
                else:
                    print("Amount must be positive")
            else:
                print("Accounts doesn't exist")

        except ValueError:
            print("Invalid input")

    def withdrawl(self,account_number,amount):
        try:
            if account_number in self.accounts:
                if amount <= self.accounts[account_number]['Balance']:
                    if amount > 0:
                        print(f"TK {amount} withdraw successfully")
                        self.transactions[account_number].append(f'TK {amount} Withdraw')
                        self.accounts[account_number]['Balance'] -= amount
                        self.bank_balance -= amount
                    else:
                        print("Amount must be positive")
                else:
                    if self.accounts[account_number]['Balance'] <= 0:
                        print("You have no money in the bank")
                    else:
                        print("Withdrawal amount exceeded")
                
            else:
                print("Account doesn't exist")

        except ValueError:
            print("Invalid input")


    def check_balance(self,account_number):
        b = self.accounts[account_number]['Balance']
        print(f"Total Balance is {b}")

    def transactions_history(self,account_number):
        try:
            if len(self.transactions[account_number]) == 0:
                print("NO Transactions")
            else:
                print(f"Transaction History of Account no: {account_number}")
                for i in self.transactions[account_number]:
                    print(i)
            
        except ValueError:
            print("Invalid input")

    def take_loan(self,account_number,amount):
        try:
            if self.loan_check[account_number]['enable_loan'] == 'on' and amount <= self.bank_balance:
                print(f"Loan of Tk {amount} taken successfully")
                self.accounts[account_number]['Balance'] += amount
                self.accounts[account_number]['loan_taken'] += 1
                self.transactions[account_number].append(f'TK {amount} taken loan')
                self.bank_loans += amount
                self.bank_balance -= amount
                if self.accounts[account_number]['loan_taken'] >= 2:
                    self.loan_check[account_number]['enable_loan'] = 'off'
            else:
                if self.loan_check[account_number]['enable_loan'] == 'off':
                    print("Can't take more loans")
                else:
                    print("Bank doesn't have this amount of money")

        except ValueError:
            print("Invalid input")


    def transfer_amount(self,account_number_sender,account_number_to_send,amount):
        try:
            if account_number_to_send in self.accounts and account_number_sender in self.accounts:
                if amount <= self.accounts[account_number_sender]['Balance']:
                    print(f"Tk {amount} is send to Account no : {account_number_to_send} successfully")
                    self.accounts[account_number_sender]['Balance'] -= amount
                    self.accounts[account_number_to_send]['Balance'] += amount
                    self.transactions[account_number_sender].append(f"TK {amount} sent to Account no: {account_number_to_send}")
                    self.transactions[account_number_to_send].append(f"TK {amount} taken from Account no: {account_number_sender}")
                else:
                    if self.accounts[account_number_sender]['Balance'] <= 0:
                        print("You have no money left in the bank")
                    else:
                        print("Insufficient Balance")

            else:
                print("Account doesn't exist")

        except ValueError:
            print("Invalid input")


class Admin:
    def __init__(self,user) -> None:
        self.user = user

    def create_an_account(self,name,email,address,account_type):
        try:
            return self.user.create_account(name,email,address,account_type)
        except ValueError:
            print("Invalid input")

    def delete_an_account(self,account_number):
        try:
            if account_number in self.user.accounts:
                del self.user.accounts[account_number]
                del self.user.transactions[account_number]
                del self.user.loan_check[account_number]
                print(f"Account no {account_number} deleted successfully")

            else:
                print("Account doesn't exist")

        except ValueError:
            print("Invalid input")

    def view_user_accounts(self):
        if len(self.user.accounts) > 0:
            for (x,y) in self.user.accounts.items():
                print(f"Details of Account No: {x}")
                print(y,'\n')

        else:
            print("No user accounts")


    def total_bank_balance(self):
        money = self.user.bank_balance  
        print(f"Total available balance of the bank is {money} TK")

    def total_loan_amount(self):
        loan_money = self.user.bank_loans
        print(f"Total loan amounts of the bank is {loan_money} TK")

    def loan_features(self,account_number,types):
        try:
            if account_number in self.user.accounts:
                if types == 'on':
                    self.user.loan_check[account_number]['enable_loan'] = 'on'
                    self.user.accounts[account_number]['loan_taken'] = 0
                    print(f"Loan feature for Account no: {account_number} is On")
                elif types == 'off':
                    self.user.loan_check[account_number]['enable_loan'] = 'off'
                    self.user.accounts[account_number]['loan_taken'] = 2
                    print(f"Loan feature for Account no: {account_number} is Off")

                else:
                    print("Invalid input")

            else:
                print("Account doesn't exist")
        
        except ValueError:
            print("Invalid input")

s = User()
x = Admin(s)
acc_number = x.create_an_account('shahriar','labibshahriar@gmail.com','badda','Savings')
acc2_number = x.create_an_account('shoily','snighdashoily@gmail.com','badda','Current')

admin_password = 1234
admin_name = 'admin'

while(True):
    print('----------------------Welcome to bank----------------------')
    print("1.Admin")
    print("2.User")
    print("3.Exit")
    n = int(input("Enter your choice: "))
    if n == 3:
        break
    elif n == 1:
        check_name = input('Enter your name: ')
        check_password = int(input("Enter your password: "))
        if check_name == admin_name and check_password == admin_password:
            print("------ Welcome to Admin Panel ------")
            print("1. Make an Account") 
            print("2. Delete an Account")
            print("3. View every user accounts")
            print("4. Check bank's total available balance")
            print("5. Check bank's total loan amounts")
            print("6. Change feature of loan for an account")
            print("7. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 7:
                break
            elif choice == 1:
                name = input("Enter name: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                account_type = input("Enter account_type: ")
                x.create_an_account(name,email,address,account_type)
            elif choice == 2:
                account_number = int(input("Enter account number to delete: "))
                x.delete_an_account(account_number)

            elif choice == 3:
                x.view_user_accounts()

            elif choice == 4:
                x.total_bank_balance()

            elif choice == 5:
                x.total_loan_amount()

            elif choice == 6:
                account_number = int(input("Enter account number: ")) 
                types = input("Enter the type: ")
                x.loan_features(account_number,types)

        else:
            print("Doesn't match with admin")
        
    elif n == 2:
        print("------ Welcome to User Panel ------")
        print("1. Make an account")
        print("2. Money Deposit")
        print("3. Money Withdraw")
        print("4. Check available balance")
        print("5. Check transaction history")
        print("6. Transfer Money")
        print("7. Take loan")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 8:
            break
         
        elif choice == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account_type: ")
            s.create_account(name,email,address,account_type)

        elif choice == 2:
            account_number = int(input("Enter the account number: "))
            amount = int(input("Enter the amount to deposit: "))
            s.deposit(account_number,amount)

        elif choice == 3:
            account_number = int(input("Enter the account number: "))
            amount = int(input("Enter the amount of withdraw: "))
            s.withdrawl(account_number,amount)

        elif choice == 4:
            account_number = int(input("Enter the account number: "))
            s.check_balance(account_number)

        elif choice == 5:
            account_number = int(input("Enter the account number: "))
            s.transactions_history(account_number)

        elif choice == 6:
            account_number_sender = int(input("Enter the sender account number: "))
            account_number_to_send = int(input("Enter the account number to send the money: "))
            amount = int(input("Enter the amount to send: "))
            s.transfer_amount(account_number_sender,account_number_to_send,amount)

        elif choice == 7:
            account_number = int(input("Enter the account number: "))
            amount = int(input("Enter the amount: "))
            s.take_loan(account_number,amount)
        



        

        

            
            

    
    






        
    