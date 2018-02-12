import simulator

player = simulator.initialize()
while True:
    command = input("> ")
    if command[0:4] == "draw":
        try:
            quantity = int(command[5:])
            player.draw(int(command[5:]))
        except:
            player.draw(1)
    elif command[0:8] == "readhand":
        player.hand.read()
    elif command[0:8] == "listhand":
        player.hand.list()
    elif command[0:8] == "readcard":
        try:
            player.hand.cards[int(command[9:]) - 1].read()
        except:
            print("Invalid argument - specify which card you want to read by using its number in \'listhand\'.")
    elif command[0:4] == "play":
        try:
            card = player.hand.remove_from_hand(int(command[5:]) - 1)
            if "Instant" in card.types or "Sorcery" in card.types:
                player.graveyard.add_to_graveyard(card)
            else:
                player.board.add_card(card, 0)
            print("Played " + card.name + ".")
        except:
            print("Invalid argument - specify which card you want to play by using its number in \'listhand\'.")
    elif command[0:9] == "viewboard":
        player.board.view()
    elif command[0:4] == "exit":
        break
    elif command[0:8] == "mulligan":
        player.mulligan()
    elif command[0:4] == "life":
        player.display_life()
    elif command[0:7] == "setlife":
        try:
            new_life = int(command[8:])
            player.set_life(new_life)
        except:
            print("Invalid argument: new life total must be an integer.")
    elif command[0:10] == "changelife":
        try:
            change = int(command[11:])
            player.change_life(change)
        except:
            print("Invalid argument: change in life total must be an integer.")
    elif command[0:3] == "tap":
        try:
            if command[4:8] == "land":
                index = int(command[9:]) - 1
                if player.board.lstates[index] == 0:
                    player.board.lstates[index] = 1
                    print("Tapped " + player.board.lands[index].name + ".")
                else:
                    print(player.board.lands[index].name + " already tapped.")
            elif command[4:11] == "nonland":
                index = int(command[12:]) - 1
                if player.board.nstates[index] == 0:
                    player.board.nstates[index] = 1
                    print("Tapped " + player.board.nonlands[index].name + ".")
                else:
                    print(player.board.nonlands[index].name + " already tapped.")
            else:
                print("Invalid argument: specify \'land\' or \'nonland\' followed by a number in range.")
        except:
            print("Invalid argument: specify \'land\' or \'nonland\' followed by a number in range.")
    elif command[0:5] == "untap":
        try:
            if command[5] == "*":
                player.board.untap_all()
            elif command[6:10] == "land":
                index = int(command[11:]) - 1
                if player.board.lstates[index] == 1:
                    player.board.lstates[index] = 0
                    print("Untapped " + player.board.lands[index].name + ".")
                else:
                    print(player.board.lands[index].name + " already untapped.")
            elif command[6:13] == "nonland":
                index = int(command[14:]) - 1
                if player.board.nstates[index] == 1:
                    player.board.nstates[index] = 0
                    print("Untapped " + player.board.nonlands[index].name + ".")
                else:
                    print(player.board.nonlands[index].name + " already untapped.")
            else:
                print("Invalid argument: specify \'land\' or \'nonland\' followed by a number in range.")
            print("hi")
        except:
            print("Invalid argument: specify \'land\' or \'nonland\' followed by a number in range.")
    elif command[0:7] == "destroy":
        try:
            if command[8:12] == "land":
                index = int(command[13:]) - 1
                card = player.board.remove_land(index)
                player.graveyard.add_to_graveyard(card)
                print("Moved " + str(card.name) + " to the graveyard.")
            elif command[8:15] == "nonland":
                index = int(command[16:]) - 1
                player.graveyard.add_to_graveyard(player.board.remove_nonland(index))
                player.graveyard.add_to_graveyard(card)
                print("Moved " + card.name + " to the graveyard.")
            else:
                print("Invalid argument: specify \'land\' or \'nonland\' followed by a number in range.")
        except:
            print("Invalid argument: specify \'land\' or \'nonland\' followed by a number in range.")
    elif command[0:13] == "viewgraveyard":
        player.graveyard.view()
    elif command[0:7] == "shuffle":
        player.deck.shuffle()
        print("Shuffled deck.")
    elif command[0:11] == "viewlibrary":
        player.deck.view()
    elif command[0:13] == "librarytohand":
        try:
            index = int(command[14:]) - 1
            card = player.deck.remove_from_deck(index)
            player.hand.add_to_hand(card)
            print("Moved " + card.name + " from your library to your hand.")
        except:
            print("Invalid argument: specify an integer index in range.")
    elif command[0:13] == "librarytoplay":
        try:
            index = int(command[14:]) - 1
            card = player.deck.remove_from_deck(index)
            player.board.add_card(card, 0)
            print("Moved " + card.name + " from your library to play.")
        except:
            print("Invalid argument: specify an integer index in range.")
    else:
        print("Error - command not recognized.")
