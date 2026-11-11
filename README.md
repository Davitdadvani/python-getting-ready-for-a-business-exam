# Python: Getting Ready for a Business Exam

A small command-line Python project that combines a game with exam revision.

## How it works
1. **Slot machine:** place a bet from a starting balance of $100 and spin three symbols. Your net loss sets the difficulty (EASY, MEDIUM or HARD).
2. **Math warm-up:** five arithmetic questions whose number range depends on that difficulty.
3. **Business quiz:** 60 shuffled multiple-choice questions on introductory business topics (competition, economics, value chains, unemployment, corporate structures and more) with a 30-minute timer and a final grade.
4. **Weather check:** a small if/else example that suggests an activity based on the temperature.

## How to run
```bash
python main.py
```
Requires Python 3 and no extra packages.

## Concepts practiced
- Functions, loops and conditionals
- User input validation (`try/except`, `isdigit`)
- Weighted random choice (`random.choices`)
- Threading for a countdown timer
- Lists and `zip` for question/answer data

## Possible improvements
- Move the quiz questions into a separate data file (e.g. JSON)
- Print the final quiz result as a review of wrong answers
- Add unit tests for the payout logic
