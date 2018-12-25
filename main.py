import engine


def newline(num=2):
    for _ in range(num):
        print("")


game = engine.Game()
game.initializing()

while game.get_round() < 5:
    newline()
    newline()
    print("=====", "Round", game.get_round(), "=====")

    for i in game.round_cycle():
        newline()
        print("===", "Player", i, "===")
        print("Change cards with other")
        print(game.get_player(i).get_cards())
        target = int(input("Target Player (-1 for None): "))

        if target != -1:
            print(game.get_player(i).get_cards())
            mine = list(map(int, input("Change your?: ").split()))
            your = list(map(int, input("Change target?: ").split()))

            game.get_player(i).change_player_cards(target, mine, your)

        print("Change cards with playground")
        print(game.get_player(i).get_cards())
        mine = list(map(int, input("Change your?: ").split()))
        print(game.get_playground())
        your = list(map(int, input("Change playground?: ").split()))

        game.get_player(i).change_playground_cards(mine, your)

    for i in game.round_cycle()[::-1]:
        if not game.get_player(i).has_joker():
            continue
        newline()
        print("===", "Player", i, "===")

    newline()
    for i in range(5):
        print("Player", i, ":", game.get_player(i).get_cards())

    game.finish_round()
    input()

for i, score in enumerate(game.finish_game()):
    print("Player", i, ":", score)
