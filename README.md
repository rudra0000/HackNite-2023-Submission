# HackNite-2023-Submission
## **ALIEN ATTACK**
### THE PAST CAN BE REWRITTEN
So, this is a 2D space shooting game made using pygame library.
We have taken our icons for spaceship and enemies from **Flaticon** website and audio clips from **Naa Song Lyrics** website.
The game is based upon an alien attack on Earth and so the objective of the game is to destroy as many enemy ships as
possible **by shooting them down with missiles**.

The score of the player is calculated on the basis of number of kills made by the player ship.The game has various level and as the game progresses 
the level increases and so does the difficulty of the game. The level gets automatically increased as the current wave gets destroyed or passes through.

On the top-left side of the screen, the **health bar** and the **No of Kills** by the player ship is displayed and on the bottom-right corner, the current level of the game is diplayed. There are 3 types of enemies:  
1. Red enemy
2. Green enemy
3. Blue enemy

The Blue enemy has 3 units of health, the Red has 2 units and the Green has 1 unit of health whereas the player ship has 15 units of health.

In each level, there is a **space portal** which appears along with the enemy ships. If the player ship manages to hit the portal, 
then the ship will be taken to the Past so its health will become full as it was in the beginning of the game.Then the ship will return back to the current time, and again fight enemies to defend its planet. 

The player loses the game as soon as the life of the player ship hits 0.

### HOW TO RUN

The programme is simple to run. Simply download the code and run it with the command * ***pyhon3 space_invaders.py*** *. A pop-up screen will immediately be displayed on the screen. 

### HOW TO PLAY

Press the enter key to start the game. As soon as the game starts, the enemy ships will start appearing and will
begin to shoot. The player ship can 
be moved by  using **W S D A** keys for **UP DOWN RIGHT LEFT** movement respectively.
The player ship can fire missiles when **SPACE** key is pressed.

The player ship can defend itself from enemy missiles by counter shooting missiles at them and destroying them before they reach the player ship.
And to travel back in time and regain its full health, the player ship simply needs to touch the SPACE PORTAL. 
