# Technical Spec


I implemented my application using the MVC design pattern.
- Model - TicTacToe class
- View - TicTacToeUI class
- Controller - TicTacToeCtrl class

## Classes 
- TicTacToe - This class is the model. It represents a Tic Tac Toe game where the opponent is the computer and 
              it contains all the logic and functionalities to simulate a Tic Tac Toe game. 
              
- GameBoard - This class represents a Tic Tac Toe game board using a 2D array and contains the functionalities 
              that allows players to add their marker to the board. This class is used to create the game board
              in the TicTacToe class.
              
- Player - This class represents a Tic Tac Toe game player. This class is used to create the players
           in the TicTacToe class.
           
- TicTacToeUI - This class implements the view or the UI component of the application such as creating the window 
                and adding the widgets and layouts.

- TicTacToeCtrl - This class is the Controller. It implements the communications between the view and the model.
