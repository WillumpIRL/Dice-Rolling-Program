import random

def header():
    print('=' * 60) 
    print('||' + heading_text.center(56) + '||') 
    print('=' * 60)

total = None
roll_array = []
turn = 1
user_input = None
heading_text = '! Dice Roller 1984 !'
header()
    
while user_input != 'x':
    valid = True
    exploding = False
    user_input = input('Enter Your Roll (or "h" for help, "x" to close): ').lower()
    if user_input == 'h':
        heading_text = 'HELP'
        header()
        helptext = '''Enter roll in the format "(quantity)d(sides)".
For example the entry 10d12 would roll ten-twelve sided dice.

With a ! at the end (4d6!), for "exploding dice".
Dice that roll max number are re-rolled and added.

'''
        print(helptext)
        continue
    
    if user_input == 'x':
        heading_text = 'Goodbye :('
        header()
        break

    if user_input.count('!') == True:
            user_input = user_input.replace('!', '')
            exploding = True
            
    parts = user_input.split('d')
    dice_rolls = parts[0]
    dice_sides = parts[1]
    if (len(parts) != 2) or (parts[0].isdigit() == False or parts[1].isdigit() == False) or (int(dice_rolls) < 1 or int(dice_sides) < 2):
        valid = False
        print('Invalid Input')
        continue

    if valid == True:
        roll_array = []
        extratext=""
        dice_rolls = int(parts[0])
        dice_sides = int(parts[1])
        
        if exploding == True:
            extratext = 'Exploding Dice'
        print('\nNow Rolling', user_input, extratext)
        total_turns = dice_rolls

        while dice_rolls != 0:
            rollvalue = random.randint(1, dice_sides)
            total = rollvalue
            print('\nRoll', turn, 'of', total_turns, '.','Rolled a', str(rollvalue) + '!')
            
            while (exploding and rollvalue == dice_sides):
               print('BOOM!')
               rollvalue = random.randint(1, dice_sides)
               total = total + rollvalue
               print('Rolled a', str(rollvalue) + ', exploding total of ', str(total) +'!')

            roll_array.append(total)
            dice_rolls = dice_rolls - 1
            turn = turn + 1
        turn = 1
        
        heading_text = 'STATS'
        header()

        print('Rolls: ', roll_array)
        print('Total: ', sum(roll_array))
        print('Average: ', sum(roll_array) / len(roll_array))
        if roll_array.count(min(roll_array)) == 1:
            occurrence = 'occurrence'
        else:
            occurrence = 'occurrences'
        if roll_array.count(max(roll_array)) == 1:
            occurrence = 'occurrence'
        else:
            occurrence = 'occurrences'
        print('Minimum: ', min(roll_array), '(' + str(roll_array.count(min(roll_array))), str(occurrence) + ')')
        print('Maximum: ', max(roll_array), '(' + str(roll_array.count(max(roll_array))), str(occurrence) + ')')
        heading_text = '! Dice Roller 1984 !'
        header()
    
        
        
