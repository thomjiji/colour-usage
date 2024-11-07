import colour

mid_gray_point_di = colour.models.oetf_DaVinciIntermediate(0.18)
mid_gray_point_tlog = colour.models.log_encoding_FilmLightTLog(0.18)
mid_gray_point_acescct = colour.models.log_encoding_ACEScct(0.18)
mid_gray_point_logc3 = colour.models.log_encoding_ARRILogC3(0.18)
mid_gray_point_logc4 = colour.models.log_encoding_ARRILogC4(0.18)
mid_gray_point_applelog = colour.models.log_encoding_AppleLogProfile(0.18)

print(f"mid_gray_point_di: {mid_gray_point_di}")
print(f"mid_gray_point_tlog: {mid_gray_point_tlog}")
print(f"mid_gray_point_acescct: {mid_gray_point_acescct}")
print(f"mid_gray_point_logc3: {mid_gray_point_logc3}")
print(f"mid_gray_point_logc4: {mid_gray_point_logc4}")
print(f"mid_gray_point_applelog: {mid_gray_point_applelog}")
