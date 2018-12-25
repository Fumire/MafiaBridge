import random
import variable


class Player:
    def __init__(self):
        self._name = "Name"
        self._cards = [None, None]
        self._score = 0
        self._game = None

    def set_game(self, game):
        self._game = game

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_cards(self, one, two):
        self._cards = [one, two]

    def set_card(self, where, what):
        self._cards[where] = what

    def get_cards(self):
        return self._cards

    def has_joker(self):
        return self.has_jobs("Joker")

    def use_joker(self, target):
        assert self.has_joker()
        assert len(self.has_joker()) == len(target)
        for t in target:
            self.set_card(self.get_cards().index("Joker"), t)

    def change_player_card(self, target, mine, your):
        my_card = self.get_cards()[mine]
        your_card = target.get_cards()[your]

        self.set_card(mine, your_card)
        target.set_card(your, my_card)

    def change_player_cards(self, target, mine, your):
        if not mine and not your:
            return
        assert len(mine) == len(your)
        for i, j in zip(mine, your):
            self.change_player_card(self._game.get_player(target), i, j)

    def change_playground_card(self, mine, target):
        my_card = self.get_cards()[mine]
        playerground_card = self._game.get_playground()

        my_card, playerground_card[target] = playerground_card[target], my_card
        self.set_card(mine, my_card)
        self._game.set_playground(playerground_card)

    def change_playground_cards(self, mine, target):
        assert mine
        assert len(mine) == len(target)
        for i, j in zip(mine, target):
            self.change_playground_card(i, j)

    def has_jobs(self, job):
        return self.get_cards().count(job)

    def add_score(self, num):
        self._score += num

    def get_score(self):
        return self._score


class Game:
    def __init__(self):
        self._round = 0
        self._players = [Player() for _ in range(5)]
        self._playground = list()

    def initializing(self):
        self.set_player_name()
        self.set_cards()
        for i in range(5):
            self._players[i].set_game(self)

    def set_player_name(self):
        for i, name in enumerate(variable.choose_name(number=5)):
            self._players[i].set_name(name)

    def get_player_name(self):
        return [self._players[i].get_name() for i in range(5)]

    def set_cards(self):
        self._playground = variable.choose_job(number=16)
        self._playground, tmp = self._playground[:8], self._playground[8:]
        tmp.extend(["Joker", "Joker"])
        random.shuffle(tmp)
        for i in range(5):
            self._players[i].set_cards(tmp[i * 2], tmp[i * 2 + 1])

    def get_player_cards(self):
        return [self._players[i].get_cards() for i in range(5)]

    def get_playground(self):
        return self._playground

    def set_playground(self, playground):
        assert len(playground) == 8
        self._playground = playground

    def finish_round(self):
        if "Mafia" not in self.get_playground():
            for i in range(5):
                self._players[i].add_score(self._players[i].has_jobs("Civilian") * (1 if self.get_playground().count("Civilian") < 4 else self.get_playground().count("Civilian") - 3))
        elif self.get_playground().count("Mafia") > self.get_playground().count("Police"):
            for i in range(5):
                self._players[i].add_score(self._players[i].has_jobs("Mafia") * 3)
        elif self.get_playground().count("Mafia") <= self.get_playground().count("Police"):
            for i in range(5):
                self._players[i].add_score(self._players[i].has_jobs("Civilian") * (1 if self.get_playground().count("Civilian") < 4 else self.get_playground().count("Civilian") - 3))
                self._players[i].add_score(self._players[i].has_jobs("Police") * 2)

        self._round += 1
        self.set_cards()

    def get_round(self):
        return self._round

    def finish_game(self):
        return [self._players[i].get_score() for i in range(5)]

    def round_cycle(self):
        return [(i + self.get_round()) % 5 for i in range(5)]

    def get_player(self, i):
        return self._players[i]


if __name__ == "__main__":
    game = Game()
    game.initializing()
    print(game.get_player_name())
    print(game.get_player_cards())
    game.finish_round()
    print(game.finish_game())
