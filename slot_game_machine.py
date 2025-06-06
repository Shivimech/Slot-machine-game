import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        current_symbols = all_symbols[:]
        column = []
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            print(column[row], end="|" if i != len(columns) - 1 else "")
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print(f"Enter a number between 1 and {MAX_LINES}.")
        else:
            print("Please enter a valid number.")

def get_bet():
    while True:
        amount = input(f"What would you like to bet on each line? (${MIN_BET}-${MAX_BET}): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Bet must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid number.")

def main():
    balance = deposit()

    while True:
        print(f"\nCurrent balance: ${balance}")
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is ${balance}.")
            continue

        balance -= total_bet
        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print("\n--- SLOT MACHINE ---")
        print_slot_machine(slots)

        winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
        balance += winnings
        print(f"\nYou won ${winnings}.")
        if winning_lines:
            print("Winning lines:", *winning_lines)
        else:
            print("No winning lines this time.")

        print(f"Updated balance: ${balance}")

        if balance <= 0:
            print("You ran out of money. Game over!")
            break

        play_again = input("Press Enter to play again (or type 'q' to quit): ").lower()
        if play_again == 'q':
            break

    print(f"\nYou left with ${balance}. Thanks for playing!")

main()
