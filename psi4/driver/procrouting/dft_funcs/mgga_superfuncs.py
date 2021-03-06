#
# @BEGIN LICENSE
#
# Psi4: an open-source quantum chemistry software package
#
# Copyright (c) 2007-2017 The Psi4 Developers.
#
# The copyrights for code used from other parties are included in
# the corresponding files.
#
# This file is part of Psi4.
#
# Psi4 is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, version 3.
#
# Psi4 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with Psi4; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# @END LICENSE
#
"""
List of MGGA SuperFunctionals built from LibXC primitives.
"""

from psi4 import core


def build_dldf_superfunctional(name, npoints, deriv, restricted):

    # Call this first
    sup = core.SuperFunctional.blank()
    sup.set_max_points(npoints)
    sup.set_deriv(deriv)

    # => User-Customization <= #

    # No spaces, keep it short and according to convention
    sup.set_name('dlDF')
    sup.set_description('    Dispersionless Hybrid Meta-GGA XC Functional\n')
    sup.set_citation('    Pernal et. al., Phys. Rev. Lett., 103, 263201, 2009\n')

    # Add member functionals
    x_coef = 0.6144129
    dldf_x = core.LibXCFunctional('XC_HYB_MGGA_X_DLDF', restricted)
    # dldf_x.set_alpha(1.0 - x_coef)
    sup.add_x_functional(dldf_x)
    sup.add_c_functional(core.LibXCFunctional('XC_MGGA_C_DLDF', restricted))

    sup.set_x_alpha(x_coef)

    # Call this last
    sup.allocate()
    return (sup, False)


def build_dldfd09_superfunctional(name, npoints, deriv, restricted):
    sup, disp = build_dldf_superfunctional(name, npoints, deriv, restricted)
    sup.set_name('dlDF+D09')

    return (sup, ('dlDF', '-DAS2009'))


def build_dldfd10_superfunctional(name, npoints, deriv, restricted):
    sup, disp = build_dldf_superfunctional(name, npoints, deriv, restricted)
    sup.set_name('dlDF+D')

    return (sup, ('dlDF', '-DAS2010'))


def build_m06_l_superfunctional(name, npoints, deriv, restricted):

    # Call this first
    sup = core.SuperFunctional.blank()
    sup.set_max_points(npoints)
    sup.set_deriv(deriv)

    # => User-Customization <= #

    # No spaces, keep it short and according to convention
    sup.set_name('M06-L')
    sup.set_description('    M06-L Meta-GGA XC Functional\n')
    sup.set_citation('    Y. Zhao and D. G. Truhlar, J. Chem. Phys. 125, 194101, 2006\n')

    # Add member functionals
    sup.add_x_functional(core.LibXCFunctional('XC_MGGA_X_M06_L', restricted))
    sup.add_c_functional(core.LibXCFunctional('XC_MGGA_C_M06_L', restricted))

    # Call this last
    sup.allocate()
    return (sup, False)


def build_m11_l_superfunctional(name, npoints, deriv, restricted):

    # Call this first
    sup = core.SuperFunctional.blank()
    sup.set_max_points(npoints)
    sup.set_deriv(deriv)

    # => User-Customization <= #

    # No spaces, keep it short and according to convention
    sup.set_name('M11-L')
    sup.set_description('    M11-L Meta-GGA XC Functional\n')
    sup.set_citation('    R. Peverati and D. G. Truhlar, J. Phys. Chem. Lett. 3, 117-124, 2012\n')

    # Add member functionals
    sup.add_x_functional(core.LibXCFunctional('XC_MGGA_X_M11_L', restricted))
    sup.add_c_functional(core.LibXCFunctional('XC_MGGA_C_M11_L', restricted))

    # Call this last
    sup.allocate()
    return (sup, False)


def build_mn12_l_superfunctional(name, npoints, deriv, restricted):

    # Call this first
    sup = core.SuperFunctional.blank()
    sup.set_max_points(npoints)
    sup.set_deriv(deriv)

    # => User-Customization <= #

    # No spaces, keep it short and according to convention
    sup.set_name('MN12-L')
    sup.set_description('    MN12-L Meta-GGA XC Functional\n')
    sup.set_citation('    R. Peverati and D. G. Truhlar, Phys. Chem. Chem. Phys. 14, 13171-13174, 2012\n')

    # Add member functionals
    sup.add_x_functional(core.LibXCFunctional('XC_MGGA_X_MN12_L', restricted))
    sup.add_c_functional(core.LibXCFunctional('XC_MGGA_C_MN12_L', restricted))

    # Call this last
    sup.allocate()
    return (sup, False)


def build_mn15_l_superfunctional(name, npoints, deriv, restricted):

    # Call this first
    sup = core.SuperFunctional.blank()
    sup.set_max_points(npoints)
    sup.set_deriv(deriv)

    # => User-Customization <= #

    # No spaces, keep it short and according to convention
    sup.set_name('MN15-L')
    sup.set_description('    MN15-L Meta-GGA XC Functional\n')
    sup.set_citation('    H. S. Yu, X. He, and D. G. Truhlar, J. Chem. Theory Comput. 12, 1280-1293, 2016\n')

    # Add member functionals
    sup.add_x_functional(core.LibXCFunctional('XC_MGGA_X_MN15_L', restricted))
    sup.add_c_functional(core.LibXCFunctional('XC_MGGA_C_MN15_L', restricted))

    # Call this last
    sup.allocate()
    return (sup, False)


def build_mgga_ms0_superfunctional(name, npoints, deriv, restricted):

    # Call this first
    sup = core.SuperFunctional.blank()
    sup.set_max_points(npoints)
    sup.set_deriv(deriv)

    # => User-Customization <= #

    # No spaces, keep it short and according to convention
    sup.set_name('MGGA_MS0')
    sup.set_description('    MGGA_MS0 Meta-GGA XC Functional\n')
    sup.set_citation('    J. Sun et. al., J. Chem. Phys. 137, 051101, 2012\n')

    # Add member functionals
    sup.add_x_functional(core.LibXCFunctional('XC_MGGA_X_MS0', restricted))
    sup.add_c_functional(core.LibXCFunctional('XC_GGA_C_REGTPSS', restricted))

    # Call this last
    sup.allocate()
    return (sup, False)


def build_mgga_ms1_superfunctional(name, npoints, deriv, restricted):

    # Call this first
    sup = core.SuperFunctional.blank()
    sup.set_max_points(npoints)
    sup.set_deriv(deriv)

    # => User-Customization <= #

    # No spaces, keep it short and according to convention
    sup.set_name('MGGA_MS1')
    sup.set_description('    MGGA_MS1 Meta-GGA XC Functional\n')
    sup.set_citation('    J. Sun et. al., J. Chem. Phys. 138, 044113, 2013\n')

    # Add member functionals
    sup.add_x_functional(core.LibXCFunctional('XC_MGGA_X_MS1', restricted))
    sup.add_c_functional(core.LibXCFunctional('XC_GGA_C_REGTPSS', restricted))

    # Call this last
    sup.allocate()
    return (sup, False)


def build_mgga_ms2_superfunctional(name, npoints, deriv, restricted):

    # Call this first
    sup = core.SuperFunctional.blank()
    sup.set_max_points(npoints)
    sup.set_deriv(deriv)

    # => User-Customization <= #

    # No spaces, keep it short and according to convention
    sup.set_name('MGGA_MS2')
    sup.set_description('    MGGA_MS2 Meta-GGA XC Functional\n')
    sup.set_citation('    J. Sun et. al., J. Chem. Phys. 138, 044113, 2013\n')

    # Add member functionals
    sup.add_x_functional(core.LibXCFunctional('XC_MGGA_X_MS2', restricted))
    sup.add_c_functional(core.LibXCFunctional('XC_GGA_C_REGTPSS', restricted))

    # Call this last
    sup.allocate()
    return (sup, False)


def build_scan_superfunctional(name, npoints, deriv, restricted):
    # Disabled below, no SCAN correlation in LibXC 3.0.0
    # SCAN correlation results unreliable.

    # Call this first
    sup = core.SuperFunctional.blank()
    sup.set_max_points(npoints)
    sup.set_deriv(deriv)

    # => User-Customization <= #

    # No spaces, keep it short and according to convention
    sup.set_name('SCAN')
    sup.set_description('    SCAN Meta-GGA XC Functional\n')
    sup.set_citation('    J. Sun, A. Ruzsinszky, and J. P. Perdew, Phys. Rev. Lett. 115, 036402, 2015\n')

    # Add member functionals
    sup.add_x_functional(core.LibXCFunctional('XC_MGGA_X_SCAN', restricted))
    sup.add_c_functional(core.LibXCFunctional('XC_MGGA_C_SCAN', restricted))

    # Call this last
    sup.allocate()
    return (sup, False)


def build_tpss_superfunctional(name, npoints, deriv, restricted):

    # Call this first
    sup = core.SuperFunctional.blank()
    sup.set_max_points(npoints)
    sup.set_deriv(deriv)

    # => User-Customization <= #

    # No spaces, keep it short and according to convention
    sup.set_name('TPSS')
    sup.set_description('    TPSS Meta-GGA XC Functional\n')
    sup.set_citation('   J. Tao, J. P. Perdew, V. N. Staroverov, G. E. Scuseria, Phys. Rev. Lett., 91, 146401, 2003\n')

    # Add member functionals
    sup.add_x_functional(core.LibXCFunctional('XC_MGGA_X_TPSS', restricted))
    sup.add_c_functional(core.LibXCFunctional('XC_MGGA_C_TPSS', restricted))

    # Call this last
    sup.allocate()
    return (sup, False)


def build_revtpss_superfunctional(name, npoints, deriv, restricted):

    # Call this first
    sup = core.SuperFunctional.blank()
    sup.set_max_points(npoints)
    sup.set_deriv(deriv)

    # => User-Customization <= #

    # No spaces, keep it short and according to convention
    sup.set_name('REVTPSS')
    sup.set_description('    revised TPSS Meta-GGA XC Functional\n')
    sup.set_citation('   J. Sun  et. al., Phys. Rev. B, 84, 035117, 2011\n')

    # Add member functionals
    sup.add_x_functional(core.LibXCFunctional('XC_MGGA_X_REVTPSS', restricted))
    sup.add_c_functional(core.LibXCFunctional('XC_MGGA_C_REVTPSS', restricted))

    # Call this last
    sup.allocate()
    return (sup, False)


mgga_superfunc_list = {
    "dldf": build_dldf_superfunctional,
    "dldf+d09": build_dldfd09_superfunctional,
    "dldf+d": build_dldfd10_superfunctional,
    "m06-l": build_m06_l_superfunctional,
    "m11-l": build_m11_l_superfunctional,
    "mn12-l": build_mn12_l_superfunctional,
    "mn15-l": build_mn15_l_superfunctional,
    "mgga_ms0": build_mgga_ms0_superfunctional,
    "mgga_ms1": build_mgga_ms1_superfunctional,
    "mgga_ms2": build_mgga_ms2_superfunctional,
    #    "scan": build_scan_superfunctional, # XC_MGGA_C_SCAN not present in LibXC 3.0.0
    "tpss": build_tpss_superfunctional,
    "revtpss": build_revtpss_superfunctional,
}
