import math

def main():

    print("Calculus Sphere Volume & Surface")
    radius = float(input("Please enter radius value: "))
    #pi = 3.1415
   
    volume_sph = ((4/3) * (math.pi * (radius**3)))
    
    area_sph = 4*(math.pi*(radius**2))


    print ("Volume = {}" "\nArea = {}".format(volume_sph,area_sph))
main()