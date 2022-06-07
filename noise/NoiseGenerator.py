import pyfastnoisesimd as fns
import pyfastnoisesimd.extension as ext


class NoiseGenerator:
    def __init__(self, seed=1, n_threads=32, noise_type=fns.NoiseType.Cellular, frequency=0.01,
                 octaves=7, lacunarity=0.002, gain=0.01, perturb_type=fns.PerturbType.NoPerturb):
        """Noise Generator class for keeping track of generation parameters and settings."""
        self.noise = fns.Noise(numWorkers=n_threads, seed=seed)
        self.noise.frequency = frequency
        self.noise.noiseType = noise_type
        self.noise.fractal.octaves = octaves
        self.noise.fractal.lacunarity = lacunarity
        self.noise.fractal.gain = gain
        self.noise.perturb.perturbType = self.perturb_type = perturb_type
        self.noise.cell.distanceFunc=fns.CellularDistanceFunction.Natural

    def get_noise(self, seed="unset", dimensions=(32, 32), start=(0, 0), debug=False):
        """Provides noise for given array and start position."""
        if debug:
            print(f'get_noise Seed: {seed} Dims: {dimensions}')
        if seed != "unset":
            """
            # Bad fix for sed not responding to changes.
            # Regenerates noise object for new seed value
            print("running fix.")
            old = self.noise
            noise = fns.Noise(seed=seed, numWorkers=old.numWorkers)
            noise.frequency = old.frequency
            noise.noiseType = old.noiseType
            noise.fractal.octaves = old.fractal.octaves
            noise.fractal.lacunarity = old.fractal.lacunarity
            noise.fractal.gain = old.fractal.gain
            noise.perturb.perturbType = self.perturb_type = old.perturb.perturbType
            self.noise=noise
            print(self.noise.seed)"""
            self.noise.seed = seed%(2**31)
        return self.noise.genAsGrid(dimensions, start)
