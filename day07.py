from utils import read_file, split_lines
import re
from collections import Counter

CARD_VALUES = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0,
}

CARD_VALUES_WITH_JOKER = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "J": 0,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}


def calulate_score(hand, values=CARD_VALUES):
    counter = Counter(hand)
    if len(counter) == 1:
        # Five of a kind
        return 6, *map(lambda card: values[card], hand)
    if len(counter) == 2:
        # Four of a kind
        if counter.most_common(1)[0][1] == 4:
            return 5, *map(lambda card: values[card], hand)
        # Full house
        return 4, *map(lambda card: values[card], hand)
        #
    if len(counter) == 3:
        # Three of a kind
        if counter.most_common(1)[0][1] == 3:
            return 3, *map(lambda card: values[card], hand)
        # Two pair
        return 2, *map(lambda card: values[card], hand)
    if len(counter) == 4:
        # One pair
        return 1, *map(lambda card: values[card], hand)
    if len(counter) == 5:
        # High card
        return 0, *map(lambda card: values[card], hand)


def calculate_score_with_joker(hand):
    if "J" not in hand:
        return calulate_score(hand, CARD_VALUES_WITH_JOKER)

    counter = Counter(hand)
    number_of_jokers = counter["J"]
    counter.pop("J")

    if len(counter) <= 1:
        # Five of a kind
        return 6, *map(lambda card: CARD_VALUES_WITH_JOKER[card], hand)
    if len(counter) == 2:
        # Four of a kind
        if counter.most_common(1)[0][1] + number_of_jokers == 4:
            return 5, *map(lambda card: CARD_VALUES_WITH_JOKER[card], hand)
        # Full house
        return 4, *map(lambda card: CARD_VALUES_WITH_JOKER[card], hand)

    if len(counter) == 3:
        # Three of a kind
        if counter.most_common(1)[0][1] + number_of_jokers == 3:
            return 3, *map(lambda card: CARD_VALUES_WITH_JOKER[card], hand)
        # Two pair
        return 2, *map(lambda card: CARD_VALUES_WITH_JOKER[card], hand)

    if len(counter) == 4:
        # One pair
        return 1, *map(lambda card: CARD_VALUES_WITH_JOKER[card], hand)


if __name__ == "__main__":
    file_input = read_file("inputs/day07.txt")
    lines = split_lines(file_input)

    answer_1, answer_2 = 0, 0
    hands_to_bet = {}
    print("Part 1")

    for hand, bet in map(lambda line: line.split(" "), lines):
        hands_to_bet[hand] = int(bet)

    sorted_hands = sorted(hands_to_bet.items(), key=lambda x: calulate_score(x[0]))
    for i, (hand, bet) in enumerate(sorted_hands):
        answer_1 += bet * (i + 1)

    print(answer_1)

    print("Part 2")
    sorted_hands_2 = sorted(
        hands_to_bet.items(), key=lambda x: calculate_score_with_joker(x[0])
    )
    for i, (hand, bet) in enumerate(sorted_hands_2):
        answer_2 += bet * (i + 1)

    print(answer_2)
