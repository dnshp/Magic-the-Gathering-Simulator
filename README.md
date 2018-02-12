# Magic: the Gathering Simulator

This is a text-based (hopefully soon to include graphics) simulator of Magic: the Gathering. It's still in progress and pretty simplistic - currently, you can instantiate a deck and "goldfish" with it, but you can't interact with other players and game mechanics are not enforced.

## Using the simulator

**simulator.py** contains the functions that import the card database from a JSON archive (thanks to *mtgjson.com*), as well as the class definitions for card, deck, and hand. You shouldn't need to use this file directly - it lays the groundwork for other files to use.

**console_app.py** is the file that the user interacts with directly. After a deck is created (currently, Shahar Shenhar's Worlds-winning Modern Jeskai Control list is hardcoded in), this file opens an interactive console interface with the following commands available:

* ```draw x```: draws x cards from the deck and prints their names
* ```readhand```: prints the full text of each card in hand
* ```listhand```: prints the name of each card in hand
* ```readcard x```: prints the full text of the xth card in hand
* ```play x```: plays the xth card in hand, adding it to the battlefield if it's a permanent and moving it to the graveyard if not.
* ```viewboard```: shows the current state of the player's board.
* ```exit```: exits the simulator
* ```mulligan```: shuffles the player's hand back into the deck and draws that many minus 1 cards.
* ```life```: displays the player's life total.
* ```setlife x```: sets the player's life total to ```x```.
* ```changelife x```: adds ```x``` to the player's life total.
* ```tap [land/nonland] x```: taps the xth land or nonland permanent in play.
* ```untap*```: untaps all permanents.
* ```untap [land/nonland] x```: untaps the xth land or nonland permanent in play.
* ```destroy [land/nonland] x```: moves the xth land or nonland permanent in play to the graveyard.
* ```viewgraveyard```: lists all cards in the player's graveyard.
* ```shuffle```: shuffles the player's library.
* ```viewlibrary```: lists all cards in the player's library.
* ```librarytohand x```: moves the xth card in the player's library to their hand.
* ```librarytoplay x``` moves the xth card in the player's library to the battlefield.