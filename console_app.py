import simulator

hand, deck = simulator.initialize()
while True:
    command = input("> ")
    if command[0:4] == "draw":
        hand.draw(int(command[5:]))
    elif command[0:8] == "readhand":
        hand.read()
    elif command[0:8] == "listhand":
        hand.list()
    elif command[0:8] == "readcard":
        hand.cards[int(command[9:]) - 1].read()
    elif command[0:4] == "play":
        print("Played "+hand.cards[int(command[5:]) - 1].name)
        hand.cards.remove(hand.cards[int(command[5:]) - 1])
    elif command[0:4] == "exit":
        break;
    else:
        print("Error - command not recognized.")
