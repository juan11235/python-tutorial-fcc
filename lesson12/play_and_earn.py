def play_game(person, coins):
    def play():
        nonlocal coins
        coins -= 1
        return play_status()

    def earn(add):
        nonlocal coins
        coins += add
        return play_status()

    def play_status():
        if coins >= 2:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out fo coins.")

    return {"play": play, "earn": earn}


tommy = play_game("Tommy", 5)
jenny = play_game("Jenny", 2)
tommy["play"]()
jenny["play"]()
tommy["play"]()
tommy["earn"](10)
tommy["play"]()
