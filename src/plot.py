from colour.colorimetry.datasets.illuminants import SDS_ILLUMINANTS
import colour.plotting
import numpy as np


# plot_kwargs = [
#     {"color": "r"},
#     {"color": "g"},
#     {"color": "b"},
#     {"marker": None},
#     {"linestyle": "dashed"},
# ]
#
# colour.plotting.models.plot_RGB_colourspaces_in_chromaticity_diagram(
#     [
#         "ACES2065-1",
#         "ACEScg",
#         "ITU-R BT.2020",
#         "DaVinci Wide Gamut",
#         "FilmLight E-Gamut",
#     ],
#     plot_kwargs=plot_kwargs,
# )

# colour.plotting.diagrams.plot_sds_in_chromaticity_diagram_CIE1931()

# # Plot D65 in CIE1931
# d65 = SDS_ILLUMINANTS["D65"]
# d60 = SDS_ILLUMINANTS["D60"]
# colour.plotting.diagrams.plot_sds_in_chromaticity_diagram_CIE1931([d65, d60])

# colour.plotting.plot_ellipses_MacAdam1942_in_chromaticity_diagram_CIE1931()
# colour.plotting.plot_ellipses_MacAdam1942_in_chromaticity_diagram_CIE1960UCS()
# colour.plotting.plot_ellipses_MacAdam1942_in_chromaticity_diagram_CIE1976UCS()

# colour.plotting.plot_RGB_colourspaces_gamuts(
#     ["ITU-R BT.709", "ACEScg", "S-Gamut"],
#     show_spectral_locus=True,
#     spectral_locus_colour="r",
# )

RGB = np.random.random((128, 128, 10))
colour.plotting.plot_RGB_scatter(
    RGB,
    show_spectral_locus=True,
    spectral_locus_colour="r",
)
