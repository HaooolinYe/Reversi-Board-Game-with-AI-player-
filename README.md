# Reversi-Board-Game-with-AI-player
A <a href="https://en.wikipedia.org/wiki/Reversi">Reversi Board Game</a> written in Python.  Download the python files and Play against the Computer player lives in ui.py!

<a href="https://en.wikipedia.org/wiki/Reversi">
<img src="https://user-images.githubusercontent.com/90864900/152212286-b8ad7052-14d2-467c-a3a7-ebba9b11ae4d.png" width="400" height="250">
</a>

### Build with
* Python
* tkinter library

## Getting Started
### Prerequisites
Of course, make sure you have Python installed on your laptop/computer.
#### For Windows User
If you are a beginner to <a href ="https://www.python.org/">Python</a>, then I recommend you using<a href="https://thonny.org/">Thonny</a> to run this program.

Use command
```
python --version
```
in terminal to varify whether python can be recognized on your computer's Path. This command works on all MAC/PC/LINUX.

### Installation
Download all three python files: <a href="https://github.com/HaooolinYe/Reversi-Board-Game-with-AI-player-/blob/main/board.py">board.py</a>, <a href="https://github.com/HaooolinYe/Reversi-Board-Game-with-AI-player-/blob/main/game.py">game.py</a> and <a href="https://github.com/HaooolinYe/Reversi-Board-Game-with-AI-player-/blob/main/ui.py">ui.py</a>.

## Play Time!
Run the python file  <a href="https://github.com/HaooolinYe/Reversi-Board-Game-with-AI-player-/blob/main/ui.py">ui.py</a> which can be treated as the main file of this project. This will open a window looks like the following:
<img src="https://user-images.githubusercontent.com/90864900/152217872-7718815e-2c96-4815-b306-9ed270fd849d.png" width="300" height="300">

It is set to default that you(<strong>Black</strong>) are playing against the AI computer(<strong>White</strong>). You can left click the blocks to choose a move. Only legal move can be chosen. 
Example of legal moves:

<img src="https://user-images.githubusercontent.com/90864900/152218373-2071ef18-ba1f-4a7a-a3e1-650f569a3ee3.png" width="300" height="300">

### Rules
If you are wondering about the rules o reversi, here is the <a href="https://en.wikipedia.org/wiki/Reversi">link</a> to the wiki page!

## AI Player
This AI can beat beginners to Reversi quitely easily, but don't worry, it's just a reactive AI. That being said, it won't get better game after game, and it's you who are getting better by playing against it!
### Source code
The source code of this AI is in the <a href="https://github.com/HaooolinYe/Reversi-Board-Game-with-AI-player-/blob/main/game.py">game</a> python file. The method of it's choosing move algorithm is simply called <strong>_choose_move</strong>. Feel free to check it out and give some advice!
