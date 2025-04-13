# Simulation-Attempts

A collection of minimal, concept-driven simulations exploring emergent behavior in artificial environments.

* ```adaptive-agent-growth.ipynb``` - This notebook models agent-based growth and movement on a 2D grid, inspired by Richard Dawkins' *The Blind Watchmaker*.  Agents evolve over generations using simple rules for size and direction, with movement choices biased by prior actions to simulate adaptive dynamics.

* ```adaptive-growth-with-selection.ipynb``` - An evolution simulation inspired by Dawkins, advancing on the first version. This model implements inheritable genes for movement bias, random mutation during reproduction (not based on behaviour), explicit selection favouring the top 40% by size, and a survival threshold based on minimum size.
