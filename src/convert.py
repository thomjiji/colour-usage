import colour

print(colour.matrix_RGB_to_RGB("ITU-R BT.2020", "ACES2065-1", "CAT02"))

print(f"srgb wp: {colour.models.RGB_COLOURSPACE_sRGB.whitepoint}")
print(f"bt2020 wp: {colour.models.RGB_COLOURSPACE_BT2020.whitepoint}")
