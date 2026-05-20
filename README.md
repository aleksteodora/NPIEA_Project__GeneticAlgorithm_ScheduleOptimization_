![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Genetic Algorithm](https://img.shields.io/badge/Genetic%20Algorithm-purple)

# Schedule Optimization — Genetic Algorithm

This project implements a **genetic algorithm** to generate an optimized university timetable for a given set of events and classrooms — the same class of algorithms used in robotics, logistics, and financial optimization.

---

## Problem

Given a set of events (name, duration) and available classrooms, the goal is to generate a valid, optimized timetable that satisfies the following constraints:

- Classes are held **Monday–Friday, between 7:00 and 19:00**
- A **minimum 15-minute break** is required between two events in the same classroom
- No overlapping events in the same classroom
- The schedule should be as **compact as possible** — late starts and early finishes are rewarded

---

## Algorithm Overview

| Step | Description |
|---|---|
| **Encoding** | Each individual represents one complete, valid timetable |
| **Selection** | Rank-based roulette selection — better individuals have higher probability |
| **Crossover** | Combines events from both parents while preserving schedule validity |
| **Mutation** | Randomly changes the day, time, or classroom of an event |
| **New generation** | Best individuals from old population combined with best offspring |

The fitness function penalizes early arrivals and late departures — the more compact the schedule, the higher the score.

---

## Project Structure

```
GA_Timetable/
├── data/
│   ├── data_timetable.txt      # Input data
│   ├── final_schedule.txt      # Output — schedule by day
│   └── room_occupancy.txt      # Output — schedule by classroom
├── individual.py               # Individual (single timetable)
├── population.py               # Population management and evaluation
├── selection.py                # Roulette selection
├── crossover.py                # Crossover operator
├── mutation.py                 # Mutation operator
├── replacement.py              # New generation selection
├── optimality_criterion.py     # Fitness function
├── load_data.py                # Data loading
├── utils.py                    # Validation helpers
└── main.py                     # Entry point
```
---

## Results

After execution, two output files are generated in the `data/` folder:

- **`final_schedule.txt`** — timetable organized by day
- **`room_occupancy.txt`** — timetable organized by classroom (useful for visually verifying there are no conflicts)

The algorithm runs for **700 generations** and consistently improves the schedule quality over time.
The following parameters can be configured in `main.py`:

| Parameter | Default | Description |
|---|---|---|
| `POPULATION_SIZE` | 100 | Number of timetables evaluated per generation |
| `GENERATIONS` | 700 | Number of iterations the algorithm runs |
| `MUTATION_RATE` | 0.05 | Probability of mutating an event (5%) |
| `ELITE_SIZE` | 5 | Top individuals automatically carried to next generation |
| `NUM_PARENTS` | 20 | Number of individuals selected for crossover |

### Progress over generations
![Algorithm progress](docs/progress)
