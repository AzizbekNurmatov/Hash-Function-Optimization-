# Hash-Function-Optimization-
Hash Function Optimization 

This project is a demonstration of using three optimization techniques: hill climbing, simulated annealing, and Nelder-Mead. Each technique is applied to it's own respective function and then these results are visualized on different graphs 

Libraries Utilized: numpy, matplotlib.pyplot, scipy.optimize, matplotlib.animation

1) Hill Climbing:
- Applied to the Function: f(x)=sin(2πx)+0.1x^2
- Hill Climbing is a simple optimization technique that starts with an initial guess for
the solution and attempts to improve it by taking small steps in the search space

2) Simulated Annealing: 
- Simulated Annealing is a more sophisticated optimization algorithm that allows
worse solutions with a certain probability, particularly at higher "temperatures."
- The idea is to escape local minima by sometimes allowing the algorithm to make a
"bad" move in hopes of finding a better global minimum.
- Two parameters, a and b, are utizlied from a hash function in order to minimize the collision rate and rehash count

3) Nelder-Mead
Applied to the Function: f(x)=x^2+3x+5
- Nelder-Mead Algorithm is an optimization algorithm that works by refining a
simplex, a geometric shape made up of multiple vertices (points in space)

Conclusion: Each of these optimization techniques provide unique approachces to mimizing the cost function of the hash table that is being worked on in the file. Hill climbing improves the parameters iteratively but it has risks in getting stuck with local minim, making it less optimal for problems like hash optimization. Simulated annealing is better at searching for a broader search space and avoiding local minima when it allows for some uphill moves, which would mean it's better optimized for finding global optima. Nelder-Mead is the more balanced approach as it navigates parameter spaces more efficiently, allowing for it to converge more efficiently and faster in low-dimensional problems like the hash table optimization. Overall, the choice of technique depends on the problem requirements, with Nelder-Mead being ideal for quick convergence, while Simulated Annealing is better for more complex landscapes where a global solution is desired.
