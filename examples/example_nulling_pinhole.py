import numpy as np
from astropy import units as u

from pywavefilters.optical_elements.filter.pinhole import Pinhole
from pywavefilters.optical_elements.general.lens import Lens
from pywavefilters.wavefronts.errors.power_spectral_density import get_power_spectral_density_error
from pywavefilters.wavefronts.errors.zernike import get_zernike_error
from pywavefilters.wavefronts.wavefront import Wavefront

# Parameters
grid_size = 401
wavelength = 15e-6 * u.meter
beam_diameter = 0.003 * u.meter
rms = wavelength / 100
zernike_modes_1 = [(5, rms)]
zernike_modes_2 = [(6, rms)]

# Define wavefront
wavefront_1 = Wavefront(wavelength, beam_diameter, grid_size)
wavefront_2 = Wavefront(wavelength, beam_diameter, grid_size)

# Add phase errors
phase_error_zernike_1 = get_zernike_error(wavelength, beam_diameter, zernike_modes_1, grid_size)
phase_error_psd_1 = get_power_spectral_density_error(wavelength, beam_diameter, rms, grid_size,
                                                     correlation_length=20000 / u.meter, plot_psd=False)
phase_error_zernike_2 = get_zernike_error(wavelength, beam_diameter, zernike_modes_2, grid_size)
phase_error_psd_2 = get_power_spectral_density_error(wavelength, beam_diameter, rms, grid_size,
                                                     correlation_length=20000 / u.meter, plot_psd=False)

wavefront_1.add_phase(phase_error_zernike_1)
wavefront_1.add_phase(phase_error_psd_1)
wavefront_2.add_phase(phase_error_zernike_2)
wavefront_2.add_phase(phase_error_psd_2)

# Define optical elements
focal_length = 0.003 * u.meter
lens = Lens(focal_length)
pinhole = Pinhole(1.22, beam_diameter, grid_size)

# Transform to focal plane and apply pinholes
wavefront_1.apply(lens)
wavefront_2.apply(lens)

intensity_unfiltered = (wavefront_1 + wavefront_2).intensity

wavefront_1.apply(pinhole)
wavefront_2.apply(pinhole)

# Combine wavefronts
wavefront_const = wavefront_1 + wavefront_2
wavefront_dest = wavefront_1 - wavefront_2

# Calculate null depth and throughput
intensity_filtered = wavefront_const.intensity
null_depth = np.sum(wavefront_dest.intensity) / np.sum(wavefront_const.intensity)
throughput = np.sum(intensity_filtered) / np.sum(intensity_unfiltered)

print('Null Depth: ', null_depth)
print('Throughput: ', throughput)
