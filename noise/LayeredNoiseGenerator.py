from noise.NoiseGenerator import NoiseGenerator
import pyfastnoisesimd as fns


class LayeredNoiseGenerator(NoiseGenerator):
    def __init__(self, layers=3, seed=1, n_threads=32, noise_type=fns.NoiseType.Cellular, frequency=0.01,
                 octaves=7, lacunarity=0.002, gain=0.01, perturb_type=fns.PerturbType.NoPerturb):
        super(LayeredNoiseGenerator, self).__init__(seed, n_threads, noise_type, frequency, octaves, lacunarity, gain, perturb_type)
        self.layers = layers

    def get_noise(self, seed=15, dimensions=(128, 128)):
        noise_arrays = []
        original_noise_obj = self.noise
        for i in range(self.layers):
            print(self.noise.frequency)
            self.noise.frequency *= 4
            # note this line means that the output values wont always be between -1 and 1, range is then -2 to +2
            # which means that the default lambda will not deal with this normally resulting in disjointed spots at
            # high/low values
            noise_arrays.append(((super(LayeredNoiseGenerator, self).get_noise(seed=seed * i, dimensions=dimensions)) / ((i+4)/2)))
        self.noise = original_noise_obj
        noise_array = noise_arrays[0]
        for i in range(len(noise_arrays) - 1):
            noise_array += noise_arrays[i + 1]
        return noise_array
