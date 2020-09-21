# Write your code here
class CoffeeMachine:
    state = ''
    water = 400
    milk = 540
    coffee_beans = 120
    cups = 9
    money = 550

    def user_action(self):
        action = ''
        while action != "exit":
            action = input('Write action (buy, fill, take, remaining, exit):\n')
            if action == 'buy':
                    coffee_type = input('What do you want to buy 1 - espresso, 2 - latte, 3 - cappuccino:\n')
                    if coffee_type == '1':
                        if CoffeeMachine.water < 250:
                            print('Sorry not enough water')
                        elif CoffeeMachine.coffee_beans < 16:
                            print('Sorry not enough coffee beans')
                        elif CoffeeMachine.cups < 1:
                            print('Sorry not enough cups')
                        else:
                            print('I have enough resources, making you a coffee!')
                            CoffeeMachine.water -= 250
                            CoffeeMachine.coffee_beans -= 16
                            CoffeeMachine.money += 4
                            CoffeeMachine.cups -= 1
                    elif coffee_type == '2':
                        if CoffeeMachine.water < 350:
                            print('Sorry not enough water')
                        elif CoffeeMachine.milk < 75:
                            print('Sorry not enough milk')
                        elif CoffeeMachine.coffee_beans < 20:
                            print('Sorry not enough coffee beans')
                        elif CoffeeMachine.cups < 1:
                            print('Sorry not enough cups')
                        else:
                            print('I have enough resources, making you a coffee!')
                            CoffeeMachine.water -= 350
                            CoffeeMachine.milk -= 75
                            CoffeeMachine.coffee_beans -= 20
                            CoffeeMachine.money += 7
                            CoffeeMachine.cups -= 1
                    elif coffee_type == '3':
                        if CoffeeMachine.water < 200:
                            print('Sorry not enough water')
                        elif CoffeeMachine.milk < 100:
                            print('Sorry not enough milk')
                        elif CoffeeMachine.coffee_beans < 12:
                            print('Sorry not enough coffee beans')
                        elif CoffeeMachine.cups < 1:
                            print('Sorry not enough cups')
                        else:
                            print('I have enough resources, making you a coffee!')
                            CoffeeMachine.water -= 200
                            CoffeeMachine.milk -= 100
                            CoffeeMachine.coffee_beans -= 12
                            CoffeeMachine.money += 6
                            CoffeeMachine.cups -= 1
                    elif coffee_type == 'back':
                        continue
            elif action == 'fill':
                    water_add = int(input('Write how many ml of water do you want to add:\n'))
                    milk_add = int(input('Write how many ml of milk do you want to add:\n'))
                    coffee_add = int(input('Write how many grams of coffee beans do you want to add:\n'))
                    cups_add = int(input('Write how many disposable cups of coffee dp you want to add:\n'))
                    CoffeeMachine.water += water_add
                    CoffeeMachine.milk += milk_add
                    CoffeeMachine.coffee_beans += coffee_add
                    CoffeeMachine.cups += cups_add
            elif action == 'take':
                    money_taken = CoffeeMachine.money
                    CoffeeMachine.money -= CoffeeMachine.money
                    print('I gave you', money_taken)
            elif action == 'remaining':
                print('The coffee machine has:\n', CoffeeMachine.water, 'of water\n', CoffeeMachine.milk, 'of milk\n', CoffeeMachine.coffee_beans, 'of coffee beans\n',
                      CoffeeMachine.cups, 'of disposable cups\n', CoffeeMachine.money, 'of money')
            else:
                print('Please provide one of valid options (buy, fill, take)')


coffeeM = CoffeeMachine()
coffeeM.user_action()





