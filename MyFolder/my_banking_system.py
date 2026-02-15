from time import sleep
storage_list_info = []

def create_account():
    from random import randint
    prefix_number = randint(111, 999)
    number = randint(1111111111, 8888888888)
    title = input('\nEnter your title (Mr, Mrs, Miss): ').title()
    first_name = input('Enter first name: ').capitalize()
    last_name = input('Enter last name: ').capitalize()
    other_name = input('Enter other name: ').capitalize()
    prefix = (f'{first_name[0]}{last_name[0]}{other_name[0]}')
    user_name = (f'{prefix}{prefix_number}')
    account_number = str(number)
    
    storage_info = {
        'First_Name':first_name,
        'Last_Name':last_name,
        'Other_Name':other_name,
        'User_Name':user_name,
        'Account_Number':account_number,
        'Account_Balance':0.00
    }
    
    storage_list_info.append(storage_info)
    
    print(f'\n{title} {last_name}, your account as been created sucessfully. \nHere are your details: \n\n{storage_info}')
    sleep(1.5)
    
    
def user_authentication():
    user = True
    while user:
        name = (input('\nEnter your User_Name: '))
        pass_code = (input('Enter your Account_Number: '))
        if name == 'Admin' and pass_code == 'Admin123':
            print('\nLogin successful. \nWelcome Admin.. \n')
            sleep(.3)
            print(storage_list_info)
            sleep(3.5)
            return 'admin'
        
        user_data = next((u for u in storage_list_info if u['User_Name'] == name and u['Account_Number'] == pass_code), None    )
        if user_data:
            sleep(.3)
            print(f'\nLogin successful. \nWelcome {name} \n')
            return user_data
        
        sleep(.3)   
        print(f'\n{name} and {pass_code} does not exist. \n ')
        question = (input('Do you want to try again (yes or no): ')).lower()
        if question == 'yes':
            continue
        elif question == 'no':
            print('Thank you for using MyBanking.')
            user = False
            break
        else:
            print('Invalid Input, Try again')
            continue
        sleep(1.5)   
             
def deposit(storage_info):
   while True:
        amount = float(input('\nHow much do you want to deposit?: '))
        storage_info['Account_Balance'] += amount
        sleep(.3)
        print(f'\nCredit Alert \n{amount} has been credited to your account. \nAccount Balance : {storage_info["Account_Balance"]}\n')
        question = input('Do you want to perform another transaction?: (yes or no): ')
        if question == 'yes':
            sleep(.5)   
            continue
        elif question == 'no':
            return None
        else:
            sleep(.5)
            print('Invalid input')
            continue
        
    
def withdraw(storage_info):
    while True:
        amount = float(input('\nHow much do you want to withdraw?: '))
        if storage_info['Account_Balance'] > amount:
            storage_info['Account_Balance'] -= amount
            sleep(.3)
            print(f'\nDebit Alert : \n{amount} has been debited from your account.  \nAccount Balance: {storage_info["Account_Balance"]}\n')
            sleep(.5)
            question = input('Do you want to perform another transaction?: (yes or no): ')
            if question == 'yes':
                sleep(.5)   
                continue
            elif question == 'no':
                sleep(1.5)
                return None
            else:
                sleep(.5)
                print('Invalid input')
                continue
        else:
            sleep(.3)
            print('Not sufficient funds. \n')
            sleep(1.5)
            return False
                    
        

def balance_check(storage_info):
    # for storage_info in storage_list_info:
    sleep(.2)
    print(f'\nAccount Balance: {storage_info["Account_Balance"]}')
    sleep(1.5)
                 


def loan_request(storage_info):
    while True:
        amount = float(input('\nHow much loan do you want to take?: '))
        if storage_info['Account_Balance'] > 2000:
            sleep(.3)
            print('Access Granted')
            sleep(.5)
            question = input('How soon do you plan on returning the loan (soon or not_soon)?: ').lower()
            if question == 'soon':
                count = .5
                sleep(.2)
                print(f'You are to pay back an intrest of  {amount * count} \nA total of {(amount * count) + (amount)}/n')
                sleep(1.5)
                return None
                
            elif question == 'not_soon':   
                count = .8
                sleep(.2)
                print(f'You are to pay back an intrest of  {amount * count} \nA total of {(amount * count) + (amount)} \n')
                sleep(1.5)
                return None
            
            else:
                sleep(.2)
                print('Invalid input/n')
                continue
                
        else:
            sleep(.5)
            print('Access Denied..Try again when you hold funds /n')
            sleep(1.5)
            return False

def my_bank():
      
    while True:        
        print('\nWelcome to MyBanking!! \n\n1, Create Account. \n2, Login  \n3, Exist. \n')
        sleep(1.5)
        option = input('Enter option (1-3): ')
        if option == '1':  
            sleep(1.5)      
            create_account()
        elif option == '2':
            
            sleep(1.5)         
            user_name = user_authentication()  
            if user_name and user_name != 'admin':
                while user_name:
                        
                        print('What would you like to do: \n1, Deposit.\n2, Withdraw. \n3, Check Balance. \n4, Loan Request. \n5, Exist. \n')
                        sleep(1.5)
                        sub_option = input('Enter option (1-5): ')                
                        if sub_option == '1':
                            sleep(1)
                            deposit(user_name)
                        elif sub_option == '2':
                            sleep(1)
                            withdraw(user_name)
                        elif sub_option == '3':
                            sleep(1)
                            balance_check(user_name )
                        elif sub_option == '4':
                            sleep(1)
                            loan_request(user_name)
                        elif sub_option == '5':
                            break
                        else:
                            sleep(.8)
                            print('Option does not exist, Try again.')
                    
        
        elif option == '3':
            break
        
        else:
            sleep(.8)
            print('Option does not exist, Try again.')
        
        
my_bank()