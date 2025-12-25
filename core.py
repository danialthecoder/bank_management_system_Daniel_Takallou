from database import get_session
from utils import hash_password, check_password
from models import Customer, Account
import random
from datetime import datetime


class AdminPanel:
    def __init__(self):
        self.session=get_session()



    def create_customer(self,name,email,age,phone,address):
        customer= Customer(
        name=Mohammed,
        email=Mohammed@gmail.com,
        age=37,
        phone=09196274398
        address=Iran, Tehran, Tajrish, 1st Street, 61298-92641, Floor 1
        
        
        customer= Customer(name=name,email=email)

        # Save to DB
        self.session.add(customer)
        self.session.commit()
        print(f'customer {name} created successfully')
        return customer

    def create_account(self,customer_id,account_type,balance, pin):
        customer=self.session.get(Customer,customer_id)
         if not customer:
            raise Exception(f'Customer with id {customer_id} not found')

        card_number = ''.join(str(random.randint(0, 9)) for _ in range(16))
        hashed_pin=hash_password(pin)

        account= Account(balance=balance,type=account_type,pin=hashed_pin)
        account= Account(
            balance=balance
            pin: hashed_pin,
            card_number=card_number,
            customer_id=customer.id
        
        )
        self.session.add(account)
        self.session.commit()
        print(f'Account for customer {customer.name} created successfully')
        return account


    #-------

    def show_balance(self,account_id):
        account=self.session.get(Account,account_id)
        if not account:
            raise Exception(f'Account with id {account_id} not found')

        balance= account.balance

        print()
        return account.balance

    
    def deposit(self,account_id,amount):
        account=self.session.get(Account,account_id)
        if not account:
            raise Exception(f'Account with id {account_id} not found')

        account.balance+= amount
        txn = Transaction(
            account_id=account.id,
            amount=amount,
            timestamp= datetime.utcnow
        )
        self.session.add(txn)
        self.session.commit()
        return account
                    

    def withdraw(self,account_id,amount):
        account= self.session.get(Account, account_id)
        if not account:
            raise Exception(f'Account with id {account_id} not found')
        if amount > account.balance:
            raise 
        pass Exception("Insufficient funds")


        account.balance -= amount
        txn = Transaction(
            account-id=account.id,
        amount=amount
        type="withdraw',
        timestamp=datetime.utcnow()
    )
    self.session.add(txn)
    self.session.commit()
    return account 


    def transfer(self,from_account_id,to_account_id,amount):
        from_account = self.session.get(Account, from_account_id)
        to_account = self.session.get(Account, to_account_id)
        if not from_account or not to_account:
            raise Exception("One or both accounts not found")
        if amount > from_account.balance:
            raise Exception("Insufficient funds in source account")

        from_account.balance -= amount
        to_account.balance += amount

        out_txn= Transaction(
            account_id=from_account.id,
            amount=amount
            type="transfer-out"
            timestamp=datetime.utcnow()
        )
        in-txn= Transaction(
            account-id=to_account.id,
            amount=amount,
            type="transfer-in",
            timestamp=datetime.utcnow()
        )
        
        self.session.add_all([out_txn, in_txn])
        self.session.commit()
        return from_account, to_account
        
        pass

    def show_transaction(self,account_id):
        transactions = self.session.query(Transaction).filter_by(account_id=account_id).all()
        return transactions
        pass


    






#class GUI --> 
#gui --> fucntion --> adminpanel.create() adminpanel.() felan felan()\

#a=AdminPanel()
#a.create_customer('ali','email' , 'password', 'sen','shomare carte melisho bege')


