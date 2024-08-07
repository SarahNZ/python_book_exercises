# Print all the cards in a deck using a nested for loop

'''
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [ '2', '3', '4', '5', '6', '7', '8', '9', '10',
         'Jack', 'Queen', 'King', 'Ace']
deck = []
for suit in suits:
    for rank in ranks:
        card = f'{rank} of {suit}'
        deck.append(card)

print(deck)
'''

# Print all the cards in a deck using a list comprehension and 2 for statements

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 
    'Jack', 'Queen', 'King', 'Ace'
]

deck = [ f'{rank} of {suit}'
        for suit in suits
        for rank in ranks]

print(deck)


