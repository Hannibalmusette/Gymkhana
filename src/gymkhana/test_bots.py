from gymkhana import main


def test():
    bot_1 = 0
    bot_2 = 0
    games = 0
    while games < 100:
        game = main.main()
        if game == "Louise":
            bot_1 += 1
        elif game == "Abdellah":
            bot_2 += 1
        elif game == "NO ONE":
            print("match nul")
        games += 1
    print("player 1 : ", bot_1)
    print("player 2 : ", bot_2)
