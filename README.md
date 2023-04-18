# Please go to master branch to download fully working game
To launch, type 'python main.py' in command prompt or terminal.
Buttons in character selection part may not seem to work (probably the for loop's fault), but they do - try a few times.
(Recommended clicking directly into center of the button)
# Gameplay
After choosing 3 characters ('pick' button sygnalizes it by turning red), player fight with enemy team in set order.
Within the battle characters can deal damage, change stats or heal themselves.
Game ends when whole team (player's or computer's) is defeated.
# About Classes
## Class Character 
### Function set_abilities
Reads .txt files and creates 2-dimensional list called abilities[], which contains attributes of character abilities.
Each character has 4 abilities, and list is later later used to set right effect on them or their target.
### Functions stats_blit_ and select_list
Functions that display bunch of information about characters on screen
### Function use_potion
Player gain 3 potions, each restores 10 HP. When one potion is used, total number decreases. Includes prevention from negative number of them :)
## Class HealthBar 
### Functions drawRects and updateBar
Draws rectangles in declared position on screen and updates them if character's HP change
## Classes Button and ToggleButton - inheritance
Child class has additional flag toggled, which allows hovering color to stay when button is clicked
