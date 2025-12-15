from database import get_session
from utils import hash_password, check_password
from models import Customer, Account



class AdminPanel:
    def __init__(self):
        self.session=get_session()



    def create_customer(self,name,email,age,phone,address):
        #row tooye database besazam
        
        #^^^
        #kare shomast *** age, phone, address tooye models.py inja ham bezarid *******
        customer= Customer(name=name,email=email)

        #ta alan classesho sakhti tooye python
        #zakhire bshe?? tooey db
        self.session.add(customer)
        self.session.commit()
        print(f'customer {name} created successfully')
        return customer

    def create_account(self,customer_id,account_type,balance, pin):
        customer=self.session.get(Customer,customer_id)
        #row ro bekesham biron

        if not customer:
            #^^^
            raise Exception(f'Customer with id {customer_id} not found')

        #^^^
        #card number shoam ezafe kon?????
        #numpy ---> gpt beporsid ???
        #card_number=328273817

        hashed_pin=hash_password(pin)

        account= Account(balance=balance,type=account_type,pin=hashed_pin)
        self.session.add(account)
        self.session.commit()

        return account


    #-------

    def show_balance(self,account_id):
        account=self.session.get(Account,account_id)
        if not account:
            #^^
            raise Exception(f'Account with id {account_id} not found')

        balance= account.balance

        #^^ print
        return balance

    
    def deposit(self,account_id,amount):
        account=self.session.get(Account,account_id)
        if not account:
            #^^
            raise Exception(f'Account with id {account_id} not found')

        account.balance=account.balance + amount
        self.session.commit()
        return account

    def withdraw(self,account_id,amount):
        #^^^^^^^^
        '''
        hatman check kone amount <balance
        '''
        pass


    def transfer(self,from_account_id,to_account_id,amount):
        '''
        account from --> pull balance+ --> farde dg
        '''

        pass

    def show_transaction(self,account_id):
        '''
        tarakonesh haro neshoon bede

        ** Models.py --> Class transaction --> id ,amount, type=deposit ya witdhraw, tim,
        dposit() withdraw() --> ye radis tooye clas transaction
        

        '''
        pass


    






#class GUI --> 
#gui --> fucntion --> adminpanel.create() adminpanel.() felan felan()\

#a=AdminPanel()
#a.create_customer('ali','email' , 'password', 'sen','shomare carte melisho bege')


