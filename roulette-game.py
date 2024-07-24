import random

roulette_wheel = {
    0: 'green', 1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black', 7: 'red', 8: 'black', 9: 'red',
    10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red', 15: 'black', 16: 'red', 17: 'black', 18: 'red',
    19: 'red', 20: 'black', 21: 'red', 22: 'black', 23: 'red', 24: 'black', 25: 'red', 26: 'black', 27: 'red',
    28: 'black', 29: 'black', 30: 'red', 31: 'black', 32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'
}

def spin_wheel():
    return random.choice(list(roulette_wheel.keys()))

def place_bet():
    bet_type = input(
        "Place your bet on 'number', 'color', 'parity' (odd/even), '1st 12', '2nd 12', '3rd 12', 'split', 'street', 'corner', or '6-line': "
    ).strip().lower()
    if bet_type == 'number':
        bet_value = int(input("Enter the number (0-36) you want to bet on: "))
        if bet_value < 0 or bet_value > 36:
            print("Invalid number. Please choose a number between 0 and 36.")
            return None, None
    elif bet_type == 'color':
        bet_value = input("Enter the color (red/black): ").strip().lower()
        if bet_value not in ['red', 'black']:
            print("Invalid color. Please choose 'red' or 'black'.")
            return None, None
    elif bet_type == 'parity':
        bet_value = input("Enter 'odd' or 'even': ").strip().lower()
        if bet_value not in ['odd', 'even']:
            print("Invalid parity. Please choose 'odd' or 'even'.")
            return None, None
    elif bet_type in ['1st 12', '2nd 12', '3rd 12']:
        bet_value = bet_type
    elif bet_type == 'split':
        bet_value = [int(x) for x in input("Enter two numbers separated by a space: ").split()]
        if len(bet_value) != 2 or any(x < 0 or x > 36 for x in bet_value):
            print("Invalid split bet. Please choose two numbers between 0 and 36.")
            return None, None
    elif bet_type == 'street':
        bet_value = [int(x) for x in input("Enter three numbers separated by a space: ").split()]
        if len(bet_value) != 3 or any(x < 0 or x > 36 for x in bet_value):
            print("Invalid street bet. Please choose three numbers between 0 and 36.")
            return None, None
    elif bet_type == 'corner':
        bet_value = [int(x) for x in input("Enter four numbers separated by a space: ").split()]
        if len(bet_value) != 4 or any(x < 0 or x > 36 for x in bet_value):
            print("Invalid corner bet. Please choose four numbers between 0 and 36.")
            return None, None
    elif bet_type == '6-line':
        bet_value = [int(x) for x in input("Enter six numbers separated by a space: ").split()]
        if len(bet_value) != 6 or any(x < 0 or x > 36 for x in bet_value):
            print("Invalid 6-line bet. Please choose six numbers between 0 and 36.")
            return None, None
    else:
        print("Invalid bet type.")
        return None, None
    return bet_type, bet_value

def check_result(spin_result, bet_type, bet_value):
    if bet_type == 'number':
        return spin_result == bet_value
    elif bet_type == 'color':
        return roulette_wheel[spin_result] == bet_value
    elif bet_type == 'parity':
        if bet_value == 'odd':
            return spin_result != 0 and spin_result % 2 != 0
        elif bet_value == 'even':
            return spin_result != 0 and spin_result % 2 == 0
    elif bet_type == '1st 12':
        return 1 <= spin_result <= 12
    elif bet_type == '2nd 12':
        return 13 <= spin_result <= 24
    elif bet_type == '3rd 12':
        return 25 <= spin_result <= 36
    elif bet_type == 'split':
        return spin_result in bet_value
    elif bet_type == 'street':
        return spin_result in bet_value
    elif bet_type == 'corner':
        return spin_result in bet_value
    elif bet_type == '6-line':
        return spin_result in bet_value
    return False

def get_payout_multiplier(bet_type):
    if bet_type == 'number':
        return 35
    elif bet_type in ['split']:
        return 17
    elif bet_type in ['street']:
        return 11
    elif bet_type in ['corner']:
        return 8
    elif bet_type in ['6-line']:
        return 5
    elif bet_type in ['color', 'parity']
        return 1
    elif bet_type in ['1st 12', '2nd 12', '3rd 12']:
        return 2
    return 0

def play_roulette():
    balance = 1000
    initial_balance = balance
    while balance > 0:
        print(f"\nYour current balance is: ${balance:.2f}")
        try:
            bet_amount = round(float(input("Enter your bet amount: ")), 2)
        except ValueError:
            print("Invalid bet amount. Please enter a valid number.")
            continue
        if bet_amount > balance:
            print("Insufficient balance.")
            continue

        bet_type, bet_value = place_bet()
        if bet_type is None:
            continue

        spin_result = spin_wheel()
        print(f"The wheel spun and the ball landed on {spin_result} ({roulette_wheel[spin_result]})")

        if check_result(spin_result, bet_type, bet_value):
            payout_multiplier = get_payout_multiplier(bet_type)
            balance += bet_amount * payout_multiplier
            print("You won!")
        else:
            balance -= bet_amount
            print("You lost!")

        if input(f'Your balance is ${balance:.2f}. Do you want to play again? (yes/no): ').strip().lower() == 'no':
            break

    print("Game over. Your final balance is:", balance)
    total_return = ((balance - initial_balance) / initial_balance) * 100
    print(f"Your total return is: {total_return:.2f}%.")

play_roulette()
