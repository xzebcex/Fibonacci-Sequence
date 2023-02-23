import sys

'''The Fibonacci sequence begins with 0 and 1, and the next number
is the sum of the previous two numbers. The sequence continues forever:
   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233...... '''

print('Fibonacci Sequence')

while True:  # Main loop.
    while True:  # Keep asking until the user enters valid input.
        print('Enter the Nth Fibonacci number you wish to')
        response = input(
            'calculate (such as 5, 50, 100, 9999), or \'Q\' to quit: ').upper()

        if response == 'Q':
            print('Thanks for playing')
            sys.exit()

        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break  # Exit the loop when the user enters a valid number.

        print('Please enter a number greater than \'0\', or press \'Q\' to quit \n')

    # Handle the special cases if the user entered 1 or 2.
    if nth == 1:
        print('0')
        print('\nThe #1 Fibonacci number is 0.')
    elif nth == 2:
        print('\n0, 1')
        print('The #2 Fibonacci number is 1.')

    # Display a warning if the user entered a large number.
    if nth >= 10000:
        print('"WARNING:" This will take a while to display take a short break.\nIf you want to quit this program before it\'s done, press ctrl-c.')
        input('Press Enter to begin...')

    # Calculate the Nth Fibonacci number.
    second_to_last_number = 0
    last_number = 1
    fibonacci_numbers_calculated = 2
    print('0, 1', end='')  # Display the first two Fibonacci numbers.

    # Display all the later numbers of the Fibonacci sequence.
    while True:
        next_number = second_to_last_number + last_number

        fibonacci_numbers_calculated += 1

        # Display the next number in the sequence.
        print(', ', next_number, sep='', end='')

        # Checks if we've found the Nth number the user asked for.
        if fibonacci_numbers_calculated == nth:
            print('\nThe #', fibonacci_numbers_calculated,
                  'Fibonacci number is', next_number)
            break

        # Shift the last two numbers.
        second_to_last_number = last_number
        last_number = next_number
