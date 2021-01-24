import math

def main():

    time_elpsd = float(input("Please enter the time elapsed between the flash and the sound: "))

    spd_sound_mts = 343

    res = time_elpsd*spd_sound_mts

    print ("The Lightning was aprox : {} meters away".format(res))

main()