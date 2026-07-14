# Cube Solver
## A Level Computer Science NEA
This was my project for my Computer Science A level NEA (Non Exam Assesment).
It is a Rubik's Cube solver with functionality for both the 2x2 and 3x3 cubes. 
The program uses pygame and numpy to store and display 3D models of the cubes with turning animations.

The program is designed to be accessible and fast, so while the algorithm used for solving the 2x2 cube produces an optimal solve, 
the algorithm used for the 3x3 cube is a heuristic solve, favouring minimal computation time and memory usage.

### 2x2 Cube
For the 2x2 cube, a meet in the middle approach to brute force searching is used where two starting nodes are explored at the same time
(initial and solved states) and searches branch out from both, until a common state is reached by both.
Lookup tables are used to store the states explored after each iteration. The maximum number of iterations the algorithm searches is 6 from each starting node, 
as the maximum number of moves to solve any state on a 2x2 cube (god's number) is 11.  



### 3x3 Cube
The 3x3 cube cannot use the same brute force approach, as the maximum number of moves to solve any state on the 3x3 cube is 20,
and the computation time would be far too long to search to that depth, even with a meet in the middle approach.
Instead the program implements a move reduction approach, heavily inspired by [Thistlethwaite's algorithm](https://www.jaapsch.net/puzzles/thistle.htm), 
which splits the solving process into 4 phases, reducing the selection of moves needed to solve the cube in each phase using a combination of searching algorithms and lookup tables. 
This approach takes significantly less computation time.



### Performing Moves on the Cube
Moves can be performed on both cubes by pressing the buttons on the side of the screen, each button corresponding to a face movement.
Keyboard input can also be used to perform moves by using the R, L, F, B, U and D keys.
Holding the shift key while pressing these keys will perform the respective anticlockwise face movements.

### Editing the Cube
The cube can be edited on the edit screen, and a cursor will appear on the top left facelet of the current face.
By pressing the R, O, G, B, W and Y keys the facelet selected by the cursor will be changed to the respective colour.
The cursor will then move on to the next facelet and will continue to do so, moving the cube as required, until all facelets have been accessed and coloured.




## Dependencies
- numpy
- pygame

If not detected, the program should try and automatically install both modules, however if this doesn't work, 
they can be installed via pip.
