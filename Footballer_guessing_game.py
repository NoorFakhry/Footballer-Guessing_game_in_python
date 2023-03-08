import random
# List of famous footballers
footballers = ['Leo Messi', 'Cristiano Ronaldo', 'Neymar Jr', 'Mohamed Salah', 
           'Kylian Mbappe', 'Robert Lewandowski', 'Sergio Ramos', 'Kevin De Bruyne',
           'Virgil van Dijk', 'Manuel Neuer', 'Paul Pogba', 'Harry Kane',
           'Antoine Griezmann', 'Erling Haaland', 'Raheem Sterling', 
           'Luka Modric', 'Jan Oblak', 'Pedri Gonzales', 'Riyad Mahrez']

def greeting():
    print('Hello and welcome to the footballer guessing game\n\n')
    print('We picked a Footballer and you have to guess it right inorder to win the game\nAnd be careful you only have 12 chances to guess your favorite footballer\n\n')

def generateRandomPlayer(footballers):
    player = random.choice(footballers)
    player = player.lower()
    return player

def giveHint(player):
    commonMsg = 'He plays for '
    if player == 'leo messi': 
        print(f'{commonMsg}PSG')
    elif player == 'cristiano ronaldo': 
        print(f'{commonMsg}Al Nasr')
    elif player == 'neymar jr': 
        print(f'{commonMsg}PSG')
    elif player == 'mohamed salah': 
        print(f'{commonMsg}Liverpool')
    elif player == 'kylian mbappe': 
        print(f'{commonMsg}PSG')
    elif player == 'robert lewandowski': 
        print(f'{commonMsg}Barcelona')
    elif player == 'sergio ramos': 
        print(f'{commonMsg}PSG')
    elif player == 'kevin de bruyne': 
        print(f'{commonMsg}City')
    elif player == 'virgil van dijk': 
        print(f'{commonMsg}Liverpool')
    elif player == 'manuel neuer': 
        print(f'{commonMsg}Bayern Munich')
    elif player == 'paul pogba': 
        print(f'{commonMsg}Juventus')
    elif player == 'harry kane': 
        print(f'{commonMsg}Totenham')
    elif player == 'antoine griezmann': 
        print(f'{commonMsg}Atletico Madrid')
    elif player == 'erling haaland': 
        print(f'{commonMsg}Man City')
    elif player == 'raheem sterling': 
        print(f'{commonMsg}Chelsea')
    elif player == 'luka modric': 
        print(f'{commonMsg}Real Madrid')
    elif player == 'jan oblak': 
        print(f'{commonMsg}Atletico Madrid')
    elif player == 'pedri gonzales': 
        print(f'{commonMsg}Barcelona')
    elif player == 'riyad mahrez': 
        print(f'{commonMsg}Man City')

def checkState(player, state):
    won = True
    for char in player:
        if char in state['guesses'] or char == ' ':
            print(char, end=' ')
        else:
            print('_', end=' ')
            won = False
    print('\n\n')
    if won: state['status'] = 'won'

def takeGuessAndUpdateTurns(player, state):
    guess = input('guess a character:')
    guess = guess.lower()

    if guess not in player and guess not in state['guesses']:
        print('Wrong guess')
        state['turns'] -= 1
        state['guesses'] += guess
        if state['turns'] > 0:
            print(f'you have {state["turns"]} Guesses left')
    elif guess in state['guesses'] and guess not in player:
        print('You already guessed that and it was a wrong guess')
        print(f'You still have {state["turns"]} Guesses left')
    elif guess not in state['guesses'] and guess in player:
        print('Right Guess, Good job')
        state['guesses'] += guess
    else:
        print('You already guessed it and it wa a right guess, so this guess will be considered a wrong guess')
        state['turns'] -= 1
        if state['turns'] > 0:
            print(f'you have {state["turns"]} Guesses left')
    if state['turns'] == 0: state['status'] = 'lost'

def guessFootballerGame(footballers):
    state = {
        'status': 'playing',
        'guesses': '',
        'turns': 12
    }

    player = generateRandomPlayer(footballers)
    greeting()
    giveHint(player)

    while state['status'] == 'playing':
        checkState(player, state)
        if state['status'] == 'won':
            print('\ncongratulations, you guessed the footballer!')
            return
        takeGuessAndUpdateTurns(player, state)
        if state['status'] == 'lost':
            print('Soryy, you ran out of turns, The footballer was', player.title())
            return
    
guessFootballerGame(footballers)