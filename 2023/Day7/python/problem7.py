import copy


class Card:
    def __init__(self, hand: str, bid: int) -> None:
        self._hand = hand
        self._bid = bid
        self.hand_types = {
            "high_card": 0,
            "one_pair": 1,
            "two_pair": 2,
            "three_of_a_kind": 3,
            "full_house": 4,
            "four_of_a_kind": 5,
            "five_of_a_kind": 6,
        }
        self.card_levels = {
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
        self._hand_type = self.get_my_hand_type()

    @property
    def hand(self):
        return self._hand

    @property
    def bid(self):
        return self._bid

    @property
    def hand_type(self):
        return self._hand_type

    def get_my_hand_type(self) -> int:
        deep_copy = copy.deepcopy(self.hand)
        pair_found = False
        for c in self.hand:
            if self.hand.count(c) == 5:
                return self.hand_types["five_of_a_kind"]

            if self.hand.count(c) == 4:
                return self.hand_types["four_of_a_kind"]

            if deep_copy.count(c) == 3:
                if pair_found:
                    return self.hand_types["full_house"]

                deep_copy = deep_copy.replace(c, "")

                if deep_copy.count(deep_copy[0]) == 2:
                    return self.hand_types["full_house"]
                else:
                    return self.hand_types["three_of_a_kind"]

            if deep_copy.count(c) == 2:
                pair_found = True
                deep_copy = deep_copy.replace(c, "")

        if len(deep_copy) == 1:
            return self.hand_types["two_pair"]

        if len(deep_copy) == 3:
            return self.hand_types["one_pair"]

        return self.hand_types["high_card"]

    def wins_against_hand(self, other_hand) -> bool:
        if self.hand_type > other_hand.hand_type:
            return True
        elif self.hand_type < other_hand.hand_type:
            return False
        else:
            for i in range(len(self.hand)):
                if (
                    self.card_levels[self.hand[i]]
                    > self.card_levels[other_hand.hand[i]]
                ):
                    return True
                elif (
                    self.card_levels[self.hand[i]]
                    < self.card_levels[other_hand.hand[i]]
                ):
                    return False


class Card2(Card):
    def __init__(self, hand: str, bid: int) -> None:
        super().__init__(hand, bid)
        self.card_levels = {
            "A": 12,
            "K": 11,
            "Q": 10,
            "T": 9,
            "9": 8,
            "8": 7,
            "7": 6,
            "6": 5,
            "5": 4,
            "4": 3,
            "3": 2,
            "2": 1,
            "J": 0,
        }

    def get_j_replacement(self) -> str:
        deep_copy = copy.deepcopy(self.hand).replace("J", "")
        for c in deep_copy:
            if deep_copy.count(c) == 4:
                return c
            if deep_copy.count(c) == 3:
                return c
            if deep_copy.count(c) == 2:
                return c

        deep_copy = copy.deepcopy(self.hand).replace("J", "")
        strongest_char = "J"
        for c in deep_copy:
            if self.card_levels[c] > self.card_levels[strongest_char]:
                strongest_char = c

        return strongest_char

    def get_my_hand_type(self) -> int:
        j_replacement = self.get_j_replacement()
        deep_copy = copy.deepcopy(self.hand)
        deep_copy = deep_copy.replace("J", j_replacement)
        pair_found = False
        for c in deep_copy:
            if deep_copy.count(c) == 5:
                return self.hand_types["five_of_a_kind"]

            if deep_copy.count(c) == 4:
                return self.hand_types["four_of_a_kind"]

            if deep_copy.count(c) == 3:
                if pair_found:
                    return self.hand_types["full_house"]

                deep_copy = deep_copy.replace(c, "")

                if deep_copy.count(deep_copy[0]) == 2:
                    return self.hand_types["full_house"]
                else:
                    return self.hand_types["three_of_a_kind"]

            if deep_copy.count(c) == 2:
                pair_found = True
                deep_copy = deep_copy.replace(c, "")

        if len(deep_copy) == 1:
            return self.hand_types["two_pair"]

        if len(deep_copy) == 3:
            return self.hand_types["one_pair"]

        return self.hand_types["high_card"]


def quick_sort(cards: list) -> list:
    if len(cards) <= 1:
        return cards
    else:
        pivot = cards[0]
        left = [x for x in cards[1:] if pivot.wins_against_hand(x)]
        right = [x for x in cards[1:] if not pivot.wins_against_hand(x)]

        return quick_sort(left) + [pivot] + quick_sort(right)


def part_2():
    # file_name = "testData.txt"
    file_name = "fulldata.txt"

    with open(f"/Users/elara/AoC/2023/Day7/python/{file_name}", "r") as data_file:
        data = data_file.read().splitlines()

    all_cards = []
    for line in data:
        hand = line.split()[0]
        bid = int(line.split()[1])
        all_cards.append(Card2(hand, bid))

    all_cards = quick_sort(all_cards)

    total_winnings = 0
    for i in range(len(all_cards)):
        total_winnings += (i + 1) * all_cards[i].bid

    print(total_winnings)


def part_1():
    # file_name = "testData.txt"
    file_name = "fulldata.txt"

    with open(f"/Users/elara/AoC/2023/Day7/python/{file_name}", "r") as data_file:
        data = data_file.read().splitlines()

    all_cards = []
    for line in data:
        hand = line.split()[0]
        bid = int(line.split()[1])
        all_cards.append(Card(hand, bid))

    all_cards = quick_sort(all_cards)

    total_winnings = 0
    for i in range(len(all_cards)):
        total_winnings += (i + 1) * all_cards[i].bid

    print(total_winnings)


if __name__ == "__main__":
    part_1()
    part_2()
