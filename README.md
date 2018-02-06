# Magic: the Gathering Simulator

This is a text-based (hopefully soon to include graphics) simulator of Magic: the Gathering. It's still in progress and pretty simplistic - currently, you can instantiate a deck and "goldfish" with it, but you can't interact with other players and game mechanics are not enforced.

## Using the simulator

**simulator.py** contains the functions that import the card database from a JSON archive (thanks to *mtgjson.com*), as well as the class definitions for card, deck, and hand. You shouldn't need to use this file directly - it lays the groundwork for other files to use.

**console_app.py** is the file that the user interacts with directly. After a deck is created (currently, Shahar Shenhar's Worlds-winning Modern Jeskai Control list is hardcoded in), this file opens an interactive console interface with the following commands available:

* ```draw x```: draws x cards from the deck and prints their names
* ```readhand```: prints the full text of each card in hand
* ```listhand```: prints the name of each card in hand
* ```readcard x```: prints the full text of the xth card in hand
* ```play```: removes the card from hand (will eventually add the card to the battlefield, but battlefield functionality has not been implemented yet)
* ```exit```: exits the simulator
