#Three flavours in the coffee machine = Espresso, Latte and Cappuccino.
flavours = {
    'espresso':{
        'price': 1.50,
        'ingredients': {
            'water': 50,
            'coffee': 18
        }
    },
    'latte':{
        'price': 2.50,
        'ingredients': {
            'water': 200,
            'coffee': 24,
            'milk': 150
        }
    },
    'cappuccino':{
        'price': 3.00,
        'ingredients': {
            'water': 250,
            'coffee': 24,
            'milk': 100
        }
    }
}


#These are the coins accepted by the machine for purchase.
coins = {
    'penny': 0.01,
    'dime': 0.10,
    'nickel': 0.05,
    'quarter': 0.25
}


#This indicates the resources left in the coffee machine.
resources = {
    'water': 300,
    'coffee': 100,
    'milk': 200,
    'money': 0
}

def check_resources(coffee_selection):
    if((flavours[coffee_selection]['ingredients']['water'] > resources['water'] or 
       flavours[coffee_selection]['ingredients']['coffee'] > resources['coffee'] or 
       flavours[coffee_selection]['ingredients']['milk'] > resources['milk'])):
        return False
    else:
        return True
    
    
def update_resources(coffee_selection):
    resources['water'] -= flavours[coffee_selection]['ingredients']['water']
    resources['milk'] -= flavours[coffee_selection]['ingredients']['milk']
    resources['coffee'] -= flavours[coffee_selection]['ingredients']['coffee']
    resources['money'] += flavours[coffee_selection]['price']


def payment(coffee_selection):
    quarters_num = input('How many quarters: ')
    dimes_num = input('How many dimes: ')
    nickles_num = input('How many nickles: ')
    pennies_num = input('How many pennies: ')

    total_money = coins['quarter']*float(quarters_num) + coins['dime']*float(dimes_num) + coins['nickel']*float(nickles_num) + coins['penny']*float(pennies_num)

    if(total_money < flavours[coffee_selection]['price']):
        print('Insufficient payment!')
        return False
    else:
        remainder = total_money - flavours[coffee_selection]['price']
        print('Your remainder is {}'.format(remainder))
        return True


def purchase_coffee(coffee_selection):
    if(check_resources(coffee_selection)):
        if(payment(coffee_selection)):
            update_resources(coffee_selection)
            print('Enjoy your {}, thank you for using CoffeeMachine!'.format(coffee_selection))
    else:
        print('Resource insufficient!')


def report_resource():
    print('Water: {}ml\nMilk: {}ml\nCoffee: {}g\nMoney: ${}'.format(resources['water'], resources['milk'], resources['coffee'], resources['money']))


while(True):
    user_input = input('What would you like? (espresso/latte/cappuccino): ')

    # '==' operator compares the value while 'is' operator will compare whether they are the exact same object.
    if(user_input == 'espresso'):
        purchase_coffee(user_input)
    elif(user_input == 'latte'):
        purchase_coffee(user_input)
    elif(user_input == 'cappuccino'):
        purchase_coffee(user_input)
    elif(user_input == 'report'):
        report_resource()
    elif(user_input == 'exit'):
        break
    else:
        print('Input unrecognized, please try again!')


print('Coffee machine shutting down...')