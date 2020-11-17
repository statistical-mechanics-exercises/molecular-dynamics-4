import numpy as np

def kinetic( vel ) :
  ke = 0
  # Your code to calculate the kinetic energy should go here
  
  return ke

# This command reads in the velocities that are contained in the file called velocities.txt
vel = np.loadtxt( "velocities.txt" )
# This prints out the total kinetic energy of the atoms whose velocities are specified 
# in velocities.  If you have implemented the function correctly this kinetic energy
# should be 0.2950
print( kinetic( vel ) )
