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

HAND_SCORES = {
    "Five of a kind": 6,
    "Four of a kind": 5,
    "Full house": 4,
    "Three of a kind": 3,
    "Two pair": 2,
    "One pair": 1,
    "High card": 0,
}


def calulate_score(hand, values=CARD_VALUES):
    counter = Counter(hand)
    if len(counter) == 1:
        return HAND_SCORES["Five of a kind"], *map(lambda card: values[card], hand)
    if len(counter) == 2:
        if counter.most_common(1)[0][1] == 4:
            return HAND_SCORES["Four of a kind"], *map(lambda card: values[card], hand)
        return HAND_SCORES["Full house"], *map(lambda card: values[card], hand)
    if len(counter) == 3:
        if counter.most_common(1)[0][1] == 3:
            return HAND_SCORES["Three of a kind"], *map(lambda card: values[card], hand)
        return HAND_SCORES["Two pair"], *map(lambda card: values[card], hand)
    if len(counter) == 4:
        return HAND_SCORES["One pair"], *map(lambda card: values[card], hand)
    if len(counter) == 5:
        return HAND_SCORES["High card"], *map(lambda card: values[card], hand)


def calculate_score_with_joker(hand, values=CARD_VALUES_WITH_JOKER):
    if "J" not in hand:
        return calulate_score(hand, values)

    counter = Counter(hand)
    number_of_jokers = counter["J"]
    counter.pop("J")

    if len(counter) <= 1:
        return HAND_SCORES["Five of a kind"], *map(lambda card: values[card], hand)
    if len(counter) == 2:
        if counter.most_common(1)[0][1] + number_of_jokers == 4:
            return HAND_SCORES["Four of a kind"], *map(lambda card: values[card], hand)
        return HAND_SCORES["Full house"], *map(lambda card: values[card], hand)

    if len(counter) == 3:
        if counter.most_common(1)[0][1] + number_of_jokers == 3:
            return HAND_SCORES["Three of a kind"], *map(lambda card: values[card], hand)
        return HAND_SCORES["Two pair"], *map(lambda card: values[card], hand)

    if len(counter) == 4:
        return HAND_SCORES["One pair"], *map(lambda card: values[card], hand)


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
