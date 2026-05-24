# Bulls and Cows Solver 🐂🐄

Python project for solving the classic **Bulls and Cows** game.

The project includes:
- Generating all possible unique-digit codes
- Calculating Bulls and Cows feedback
- Dynamically filtering possible candidates
- Implementing multiple guessing strategies
- Using a Knuth-based strategy for optimal guessing
- Writing test functions for algorithm validation

---

# Features

- Unique digit code generation
- Bulls and Cows evaluation
- Dynamic candidate filtering
- Multiple solving strategies:
  - First candidate
  - Random candidate
  - Knuth strategy
- Automatic code solving
- Built-in testing functions

---

# Bulls and Cows Logic

- **Bull** → Correct digit in the correct position
- **Cow** → Correct digit in the wrong position

Example:

```txt
Secret: 435
Guess : 234
Result: (1 Bull, 1 Cow)
```

---

# Strategies

## First Strategy
Always selects the first available candidate.

## Random Strategy
Selects a random valid candidate.

## Knuth Strategy
Chooses the guess that minimizes the worst-case remaining candidate set.

---

# Technologies

- Python
- Lists & Dictionaries
- Algorithms
- Search Optimization
- Dynamic Filtering

---

# How to Run

```bash
python project.py
```

Input order:
1. Vocabulary
2. Number of digits
3. Strategy
4. Secret code

Example:

```txt
0123456789
4
knuth
1234
```

---

# Testing

The project includes dedicated test functions for:
- Code generation
- Evaluation logic
- Candidate filtering
- Secret validation
- Guess selection
- Knuth strategy

---

# Credits

Created by: Noa Allouche
