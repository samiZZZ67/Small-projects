# Random Walk

This folder contains a small Python project that generates and visualizes a 2D random walk with `matplotlib`.

The project is split into two simple parts:

- `random_walk.py` creates the random-walk data.
- `rw_visual.py` plots the walk and lets you generate new walks in a loop.

## What It Does

Each walk starts at `(0, 0)` and keeps moving in random x and y directions until it reaches the requested number of points.

The visualization:

- draws the full path as a dense scatter plot
- colors points by progression so you can see the journey unfold
- highlights the starting point
- highlights the ending point
- hides axes so the movement itself stays the focus

## Files

### `random_walk.py`

Defines the `RandomWalk` class.

Main responsibilities:

- stores the x and y coordinates of the walk
- generates random step sizes and directions
- rejects steps that would not move anywhere
- builds the full walk automatically when an instance is created

By default, the class generates `5000` points unless another value is provided.

### `rw_visual.py`

Handles the plotting and user interaction.

Main responsibilities:

- creates a `RandomWalk` with `50000` points
- renders the points using `matplotlib`
- marks the start and end of the walk
- asks whether you want to generate another walk after the plot window closes

## Requirements

- Python 3
- `matplotlib`

Install the dependency with:

```bash
pip install matplotlib
```

## How To Run

From inside the `Random walk` folder, run:

```bash
python rw_visual.py
```

After the chart appears:

1. Close the plot window.
2. Enter `y` to generate another walk.
3. Enter `n` to stop.

## Screenshot

Here are three images here 
1.
![Random Walk Screenshot 1](1.jpg)
2.
![Random Walk Screenshot 2](2.jpg)
3.
![Random Walk Screenshot 3](3.jpg)
## Why This Project Is Nice

This is a good beginner-friendly example of combining:

- object-oriented Python
- randomness and simulation
- data visualization with `matplotlib`
- simple interactive command-line input

It is also easy to extend. For example, you could:

- change the number of points
- use different color maps
- connect points with lines instead of only scatter markers
- save the figure as an image
- experiment with different step distances

## Quick Summary

If you want a compact project that shows how random movement can turn into a visually interesting pattern, this folder does exactly that: generate a walk, plot it beautifully, and let the user keep exploring new paths.
