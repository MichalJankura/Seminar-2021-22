import math

for uhol in range(0,91,5):
    uhol_v_radianoch = math.radians(uhol)
    sin_uhla = math.sin(uhol_v_radianoch)
    cos_uhla = math.cos(uhol_v_radianoch)
    print(f"{uhol:3} {sin_uhla:6.3f} {cos_uhla:6.3f}")

for uhol in range(0,361,10):
    uhol_v_radianoch = math.sin(uhol_v_radianoch)
    stlpec = int(sin_uhla * 35+40)
    print(""* stlpec + "SIN")
