def parent_function(person, coins):
    def person_function():
        nonlocal coins
        coins -= 1
        if coins >= 2:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    return person_function


tommy = parent_function("Tommy", 4)
jenny = parent_function("Jenny", 2)

tommy()
jenny()
tommy()
