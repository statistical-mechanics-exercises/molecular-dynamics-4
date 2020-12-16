import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_kinetic(self) : 
        for i in range(10) :
            vel = np.zeros([7,2])
            myeng = 0
            for j in range(7) : 
               vel[j,0], vel[j,1] = np.random.normal(), np.random.normal()
               myeng = myeng + vel[j,0]*vel[j,0] / 2 + vel[j,1]*vel[j,1] / 2
            self.assertTrue( np.abs( kinetic(vel) - myeng )<1e-6, "your function does not calculate the kinetic energies correctly" )
