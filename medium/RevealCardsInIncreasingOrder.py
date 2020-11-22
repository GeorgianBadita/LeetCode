# https://leetcode.com/problems/reveal-cards-in-increasing-order/

from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = sorted(deck)
        new_deck = []
        for i in range(len(deck)):
            current_card = deck[len(deck) - i - 1]
            if not new_deck:
                new_deck.append(current_card)
                continue
            new_deck.insert(0, new_deck[-1])
            del new_deck[-1]
            new_deck.insert(0, current_card)
        return new_deck