# The kinetic energy

One thing that is particularly important to check whenever we run an MD simulation is whether or not the energy is being conserved.  To check the energy is conserved we need to store the potential that is calculated every time the forces are calculated.  As well as calculating the potential though we also need to calculate the kinetic energy.  The kinetic energy can be computed using a simple function of the velocities of the atoms, which you should know.

Your task in this exercise is thus to write a function called `kinetic` that takes in a list of velocities and that returns a single scalar value for the total kinetic energy for all the atoms.  To get you started I have given you a set of velocities that you can use to test your function.  The total kinetic energy for this particular set of velocities is ???.

N.B.  In this exercise, we are operating in natural units.  We have thus set the masses of all the atoms equal to one.  If we were using the Lennard Jones potential to describe a real element such as Argon there would be two parameters in the potential called epsilon and sigma that set the typical energy of interaction for a pair of atoms and the size of the atoms.  Once again though, because we are using natural units, we have set these two parameters equal to one.
