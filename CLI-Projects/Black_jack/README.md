# Blackjack Game (Python)

A command-line based Blackjack game built using Python.  
The player competes against the computer and tries to get a score as close to **21** as possible without going over.

##  About The Game

Blackjack is a card game where the goal is to beat the dealer (computer) by having a higher score than them, while keeping your total at **21 or below**.

---

##  Features

- Player vs Computer gameplay
- Random card dealing
- Blackjack detection
- Smart Ace handling
- Computer dealer logic
- Win, lose, and draw detection

---

##  Blackjack Rules

### Card Values

- Number cards (2-10):
  - Their face value counts as their score
  - Here in this project Cards stay the same means they are not removed when drawned for simplicity.

---

##  Winning Conditions

You win if:

- Your score is higher than the computer's score
- The computer goes over 21 (bust)
- You get Blackjack (21)

You lose if:

- Your score goes above 21
- Computer has a higher score
- Computer gets Blackjack

A draw happens if:

- Both player and computer have the same score

---

## Computer Rules

The computer acts as the dealer.

The computer will:

- Keep drawing cards while its score is below 17
- Stop drawing when its score reaches 17 or higher

