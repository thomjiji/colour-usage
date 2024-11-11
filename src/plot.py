from colour.colorimetry.datasets.illuminants import SDS_ILLUMINANTS
import colour.plotting

# colour.plotting.plot_RGB_colourspaces_in_chromaticity_diagram_CIE1931(
#     ["ITU-R BT.2020", "ACEScg"]
# )

# colour.plotting.diagrams.plot_sds_in_chromaticity_diagram_CIE1931()

# # Plot D65 in CIE1931
# d65 = SDS_ILLUMINANTS["D65"]
# d60 = SDS_ILLUMINANTS["D60"]
# colour.plotting.diagrams.plot_sds_in_chromaticity_diagram_CIE1931([d65, d60])

colour.plotting.plot_ellipses_MacAdam1942_in_chromaticity_diagram_CIE1931()
colour.plotting.plot_ellipses_MacAdam1942_in_chromaticity_diagram_CIE1960UCS()
colour.plotting.plot_ellipses_MacAdam1942_in_chromaticity_diagram_CIE1976UCS()
