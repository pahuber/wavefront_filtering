# PyWaveFilters

`PyWaveFilters` is a small Python package to simulate wavefront filtering with pinholes and fibers.

## Features

### Model Wavefront Phase Errors

Wavefront phase errors can be modeled in the following two ways:

* using **Zernike polynomials** and
* using a K-correlation-based **power spectral density (PSD)** distribution.

### Model Wavefront Filters

To simulate the filtering of wavefront, two different kinds of filters can be modeled:

* spatial filters in the form of **pinholes** and
* modal filters in the form of **single mode fibers**.

## Examples

Examples for how to use the code can be found under `\examples`. Four examples are included:

* `example_pinhole.py`: A simple example of how to filter an aberrated wavefront using a **pinhole**, illustrating how
  the phase and intensity behave at the different stages.
* `example_fiber.py`: A simple example of how to filter an aberrated wavefront using a **fiber**, illustrating how the
  phase and intensity behave at the different stages.
* `example_nulling_pinhole.py`: An example to simulate a simple **nulling interferometer** and investigate the impact of
  filtering by **pinhole**.
* `example_nulling_fiber.py`: An example to simulate a simple **nulling interferometer** and investigate the impact of
  filtering by **fiber**.