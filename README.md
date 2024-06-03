# Game of Life Application

Welcome to this very simple, yet interesting enough (to me) Game of Life Application repository. This project showcases two implementations of Conway's Game of Life: a basic and an optimized version. Each version is designed to illustrate different aspects of implementing and optimizing the Game of Life algorithm.

![Game of Life Screenshot](img/screenshot.png)


## Table of Contents
- [Introduction](#introduction)
- [Basic Implementation](#basic-implementation)
- [Optimized Implementation](#optimized-implementation)
- [How to Run](#how-to-run)

## Introduction

Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, with no further input from human players. The game consists of a grid of cells, each of which can be in one of two states: alive or dead. The state of the grid evolves over discrete time steps according to a set of simple rules.

## Basic Implementation

The **basic.py** script provides a straightforward implementation of the Game of Life, complete with visual enhancements for better cell state distinction. This version is ideal for educational purposes, demonstrating the fundamental principles and visual aesthetics of the Game of Life.

### Features
- Simple rules implementation
- Visual enhancements with custom colormap
- Age tracking for fading effects

```python
# To view the full code, see the basic.py file in this repository.
```


## Optimized Implementation
The **optimized.py** script introduces several optimizations for improved performance, including the use of the Numba library to accelerate the update logic. This version is designed to handle larger grids and more complex simulations efficiently.

### Features
Optimized cell state updates using Numba
Enhanced visual representation with a detailed colormap
Improved performance for larger grids

```python
# To view the full code, see the optimized.py file in this repository.
```

## How to Run
To run this code, you'll need to have Python installed on your machine along with the necessary libraries. The recommended way to install these dependencies is to use pip.

### Prerequisites
- Python 3.x
- NumPy
- Matplotlib
- Numba (for the optimized version)

## Installation
1. Clone this repository:

```sh
git clone https://github.com/pedroheck/game-of-life-optimization.git
cd game-of-life
```
2. Install the required Python packages:

```sh
pip install numpy matplotlib numba
```

## Running
To run the basic implementation of the Game of Life:
```python
python basic.py
```
To run the optimized implementation of the Game of Life:
```python
python optimized.py
```


