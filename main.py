"""
DUST - Dastardly Unexpected Strange Textures
Basically a toolkit for me to make cool images with noise. Really surprised anyone's reading this. o/
Written by Rinbadagin, Jun 5 2022. Rewrite of previous spaghetti.
Not made with ease of understanding in mind or loads of comments so if you try and puzzle this then good luck.
"""
from image.LandFilter import LandFilter
from noise.LayeredNoiseGenerator import LayeredNoiseGenerator
from noise.NoiseGenerator import NoiseGenerator
from image.ImageGenerator import ImageGenerator
from image.ImageFilter import ImageFilter
from image.ImageUtils import *
import pyfastnoisesimd as fns
from time import time_ns

identifier = time_ns()


def main():
    n_g1 = LayeredNoiseGenerator(layers=6, seed=identifier, noise_type=fns.NoiseType.Perlin, frequency=0.0001)
    i_g = ImageGenerator(dimensions=(1024, 1024))
    i_g.populate_image(n_g1.get_noise(seed=identifier, dimensions=(1024, 1024)), lambda_array=demo_lambda_arrays[1])
    i_f = ImageFilter(sampling_rate=2)
    i_g.image.save(f"past/img-{identifier}-raw.png")
    i_f.filter(i_g.image).show()


def demo_main():
    n_g = NoiseGenerator(seed=(identifier - 42) % 2 ** 31,
                         n_threads=64,
                         noise_type=fns.NoiseType.Simplex,
                         frequency=0.0005,
                         octaves=6,
                         lacunarity=0.02,
                         gain=0.02,
                         perturb_type=fns.PerturbType.NoPerturb)
    i_g = ImageGenerator(dimensions=(256, 256))
    i_g.populate_image(n_g.get_noise(seed=identifier + 1337,
                                     dimensions=(256, 256)))
    i_g.image.save(f"past/img-{identifier}-singular.png")
    i_g.image.show()
    i_g.generate_mosaic(noise_generator=n_g,
                        seed=identifier,
                        mosaic_side_length=3,
                        dimensions=(128, 128))
    i_g.image.save(f"past/img-{identifier}-mosaic.png")
    i_g.image.show()
    i_f = ImageFilter()
    i_f.filter(i_g.image).show()


if __name__ == "__main__":
    main()
