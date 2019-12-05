# Final-Project-Equation-of-Pendulum


This repository will store all the files concerning the final project due on December 2019 for the PHYS 25000 class at the University of Chicago.



All of the code was written in Python. The main functions for solving and plotting the differential equations were written in
separate files that I would then call in different files. The reason for doing this was to decrease the runtime of the code 
for each section, and permit me to work efficiently on different parts of the project at the same time. There are three main 
files that were implemented throughout the code: one in which the differential equations for the pendulum were defined; one 
in which the fourth order Runge-Kutta algorithm was defined; and one in which the different plotting functions that were 
to be used most frequently were defined.

The rest of the files are labeled by the section to which they correspond in the poster: section one corresponds to 
the simple harmonic oscillator and the damped oscillator; section two corresponds to the anharmonic oscillator; section three
was divided into two subsections: the convergence of limit cycles appears in section 3.1 while the butterfly effect appears 
in section 3.2; the last section corresponds to the bifurcation diagram.

## Code Generation

The Runge-Kutta algorithm implemented in this project was based mostly on the code for solving differential 
equations made available to us through a jupyter notebook for the PHYS 250 course. The Computational 
Physics textbook by Landau, Páez and Bordeianu was of great use for understanding this method and 
approaching the computational aspects of pendulum dynamics.

Note that, while all of the code presented for the plots generated for the poster, some of the code may take a 
long time to run. In particular, the bifurcation diagram presented in the plot may take from 5 to 6 hours. Of 
course, this depends on the number of iterations one decides to calculate and the period of time of the 
evolution of the pendulum one wants to consider.
