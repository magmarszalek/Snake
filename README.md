### Snake Game - README

---

#### Overview
**Snake Game** is a classic arcade game where the player controls a snake that grows longer by eating food. The goal is to collect as much food as possible while avoiding collisions with the edges of the game area and the snake's own body.

This implementation of Snake is built using **Pygame**, offering enhanced visuals, a timed challenge, and interactive gameplay elements.

---

### Table of Contents
1. [Features](#features)
2. [Getting Started](#getting-started)
3. [Game Mechanics](#game-mechanics)
4. [Controls](#controls)
5. [How to Play](#how-to-play)
6. [Credits](#credits)

---

### Features
- Dynamic snake movement with smooth animations.
- Collect regular and golden apples for points and bonuses.
- Interactive scoreboard to track player names and scores.
- Timer-based gameplay for an added challenge.
- Customizable visuals and assets using Pygame.

---

### Getting Started

#### Prerequisites
Ensure you have Python installed with `pygame`. You can install Pygame using:

```bash
pip install pygame
```

#### Installation
1. Clone the repository or download the `.zip`:
   ```bash
   git clone https://github.com/your-repo/snake-game.git
   cd snake-game
   ```
2. Place all assets (images, fonts) in the `images` and `fonts` directories.

#### Run the Game
Execute the game by running:
```bash
python menu.py
```

---

### Game Mechanics

#### Objective
- Collect **apples** and **golden apples** to score points and extend the timer.
- Avoid colliding with the edges of the game area or the snake's body.

#### Scoring System
- **Apple**: Adds `50 points`.
- **Golden Apple**: Adds `100 points` and extends the timer by `15 seconds`.

---

### Controls
- **Arrow Keys**:
  - `↑` - Move Up
  - `↓` - Move Down
  - `←` - Move Left
  - `→` - Move Right

---

### How to Play
1. Start the game from the **main menu**.
2. Navigate the snake using the arrow keys.
3. Collect apples and golden apples for points.
4. Avoid crashing into walls or the snake's body.
5. Check your score and save it to the leaderboard when the game ends.

---

### Credits
Developed by Magdalena Marszałek using **Pygame**.

#### Assets
- **Fonts**: Custom font included in `fonts` directory.
- **Images**: All images used for the snake, apples, and background are in the `images` directory.

---
