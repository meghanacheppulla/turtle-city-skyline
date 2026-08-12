# Turtle City Skyline

## Overview

Turtle City Skyline is a Python Turtle Graphics project that generates a colorful city skyline scene. The program creates buildings with random heights, widths, and window layouts, along with a bright sun and a grassy ground. Each execution produces a slightly different skyline due to the use of randomization.

## Features

* Randomly generated building heights and widths
* Multiple building color themes
* Automatically generated window patterns
* Bright sun and green ground background
* Sky-blue city environment
* Built using Python's Turtle Graphics library

## Technologies Used

* Python 3
* Turtle Graphics
* Random Module

## How It Works

1. Creates a Turtle Graphics screen with a sky-blue background.
2. Draws a sun in the top-right corner.
3. Draws a green ground area.
4. Generates buildings with random:

   * Widths
   * Heights
   * Colors
   * Window rows and columns
5. Places buildings side by side to form a city skyline.

## Project Structure

* `draw_rectangle()` – Draws filled rectangles for buildings, windows, and ground.
* `draw_windows()` – Creates a grid of windows inside each building.
* `draw_building()` – Draws a building with random colors and windows.
* `draw_ground()` – Draws the ground section.
* `draw_sun()` – Draws the sun.
* Main loop – Generates and places buildings across the skyline.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/meghanacheppulla/turtle-city-skyline.git
   ```

2. Navigate to the project folder:

   ```bash
   cd turtle-city-skyline
   ```

3. Run the Python file:

   ```bash
   python skyline.py
   ```

## Sample Output

The program displays:

* A blue sky background
* A yellow sun
* A green ground area
* Randomly generated city buildings with illuminated windows

Each execution creates a unique city skyline.



