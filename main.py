import random


def user_current_score(user):
    user_total_score = sum(user)
    return user_total_score


def check_score(user, computer):
    user_score = sum(user)
    computer_score = sum(computer)
    return [user_score, computer_score]


deck_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
want_to_play_game = input("If you want to play the game 'y' or 'n' ? ")
game_on = bool
if want_to_play_game == "y":  # if user want to play
    game_on = True
    # blackjack logo should appear
elif want_to_play_game == "n":  # if user doesn't want to play
    game_on = False
else:
    print("please enter valid input")
while game_on:
    # 2 cards for user and computer should be allotted
    for x in range(2):
        user_cards.append(random.choice(deck_of_cards))
        computer_cards.append(random.choice(deck_of_cards))
    # and 2 cards of user with the total score should be displayed
    print(f"Your cards: {user_cards}, current score: {user_current_score(user_cards)}")
    # computer first card should be shown also to user
    print(f"Computer's first card: {computer_cards[0]}")
    # ,and we have to ask the user that if he wants to draw a card or not
    draw_card = input("Type 'y' to get another card, type 'n' to PASS : ")
    # if yes we have assign another random cards to both the user and computer and check for the score
    if draw_card == "y":
        card_on = True
        while card_on:
            user_cards.append(random.choice(deck_of_cards))
            user_cards.append(random.choice(deck_of_cards))
            if user_current_score(user_cards) > 21:
                print(f"Your cards: {user_cards}, current score: {user_current_score(user_cards)}")
                print(f"Computer's final hand: {computer_cards[0]}, final score: {computer_cards[0]}")
                print("You went over. You lose 😭")
                game_on = False
    elif draw_card == "n":
        print(f"Your final hand: {user_cards}, final score: {user_current_score(user_cards)}")
