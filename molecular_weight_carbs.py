import math

def main():

    print ("Program designed to calculate the molecular weight of a carbohydrate")

    hydro_atom_value = 1.00794
    carbon_atom_value = 12.0107
    oxyg_atom_value = 15.9994
    
    
    hydro_atom = float(input("Please enter the number of hydrogen atoms: "))
    carbon_atom = float(input("Please enter the number of carbon atoms: "))
    oxyg_atom = float(input("Please enter the number of oxygen atoms: "))
    res_mol_weight = (hydro_atom*hydro_atom_value)+(carbon_atom*carbon_atom_value)+(oxyg_atom*oxyg_atom_value)

    print ("Result of the molecular weight is: {}".format(res_mol_weight))

main()



