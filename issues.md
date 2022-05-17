1. I tried to place the "New Game" button right below and close to the scoreboard, however
it didn't work. I tried using the .setSpacing(), .move() , .setGeometry methods but none of them worked.
Therefore, I just aligned it in the center and kept it the way it was.
2. Kept getting "ValueError: list.remove(x): x not in list" when the player won or lost a game.
The error was caused because the unmarkedPositions array is empty at the end of the game 
since all marked positions are removed from it, but when new game starts, the array accesses that array again.
Therefore, the bug was fixed by reinitializing the unmarkedPositions when a game ends. This was done in the 
clearBoard() of the class TicTacToe.
3. Player was able to tap on an already marked square and give up their turn, which they shouldn't be able to do.
At first I tried to fix this by disabling each button after it was marked by a player. However, 
this made the button faded and have a grey tint, so I enabled the buttons again. I was able to fix the bug by 
adding a check to see if a button/square is already marked and if so returning from the signal function 
that is called when the player clicks on that button. Therefore, the computer never gets its turn until player clicks
on another button/square that is unmarked.
4. Scoreboard didn't reset when "New Game" buton clicked. Fixed by resetting the keyboard in the signal function for the
button.
5. Nothing happens when there is a draw between the players. There should be a popup message that tells user that there 
a draw like when user wins or loses, but it seems that code is never executed. Update: Bug fixed. I fixed it by
updating the checkIfGameOver() of the TicTacToeCtrl class. I added code that checks if all positions in the gamebord
is marked. If it is and it had none of the vertical, horizontal, diagnol patterns, then there is a draw and game is 
over so it returns True which makes the TicTacToeCtrl display the "Draw" popup message .
6. There is one instance where the game says the player won when there is a draw. This only happens when the board is 
marked in one particular pattern. Need to fix.
