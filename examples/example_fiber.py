from astropy import units as u

from wavefront_filtering.optical_elements.filter.fiber_optics.fiber import Fiber
from wavefront_filtering.optical_elements.lens import Lens
from wavefront_filtering.util.plot import plot_intensity_pupil_plane, plot_intensity_focal_plane, \
    plot_initial_wavefront_error
from wavefront_filtering.wavefronts.wavefront import Wavefront

# Define wavefront
wavelength = 1e-5 * u.meter
initial_intensity = 10 * u.watt ** 0.5 / u.meter
zernike_modes = [(4, wavelength / 10)]
beam_diameter = 0.003 * u.meter
number_of_pixels = 100

wavefront = Wavefront(wavelength,
                      initial_intensity,
                      zernike_modes,
                      beam_diameter,
                      number_of_pixels)

# Define optical elements
focal_length = 0.008 * u.meter

lens = Lens(focal_length)

fiber = Fiber(wavelength,
              beam_diameter,
              21e-6 * u.meter,
              125e-6 * u.meter,
              1.6,
              1.59,
              number_of_pixels,
              lens)

# Apply optical elements to wavefront and plot at each stage
plot_initial_wavefront_error(wavefront)

plot_intensity_pupil_plane(wavefront)

wavefront.apply(lens)

plot_intensity_focal_plane(wavefront, dimensionless=True)

wavefront.apply(fiber)

plot_intensity_focal_plane(wavefront, dimensionless=True, title='Intensity Focal Plane After Fiber')

wavefront.apply(lens)

plot_intensity_pupil_plane(wavefront)
