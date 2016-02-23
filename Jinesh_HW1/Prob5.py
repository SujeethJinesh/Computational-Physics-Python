def binding_energy(mass_number, atomic_number):

    atomic_number = float(atomic_number)   #ensuring no integer and float operation problems
    mass_number = float(mass_number)

    a_1 = 15.67
    a_2 = 17.23         #assigning values for all the a_#
    a_3 = 0.75
    a_4 = 93.2
    a_5 = a_5_switcher(atomic_number, mass_number)

    atom_binding_energy = a_1*mass_number - a_2*pow(mass_number, 2/3.0) - a_3*(pow(atomic_number,2.0)/pow(mass_number, 1/3.0)) - a_4*(pow(mass_number-2*atomic_number,2)/mass_number) + a_5/pow(mass_number, 0.5)

    #above is the equation to determine binding energy in MeV.

    print("The atom's binding energy is ", atom_binding_energy, " MeV.") #Final output.

"""This function is used to determine what value to give a_5"""

def a_5_switcher(atomic_number, mass_number):

    mod_mass_atomic_numbers = (mass_number - atomic_number) % 2 #calculates the modulo to determine if odd or even difference

    mod_atomic_number = atomic_number % 2 #calculates modulo to determine if odd or even

    if mod_mass_atomic_numbers == 1 and mod_atomic_number == 1:  #this is the switch statement to determine what to make a_5
        return -12.0
    elif mod_mass_atomic_numbers == 0 and mod_atomic_number == 0:
        return 12.0
    else:
        return 0