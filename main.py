"""
DUST - Dastardly Unexpected Strange Textures
Basically a toolkit for me to make cool images with noise. Really surprised anyone's reading this. o/
Written by Rinbadagin, Jun 5 2022. Rewrite of previous spaghetti.
Not made with ease of understanding in mind or loads of comments so if you try and puzzle this then good luck.
"""

from noise.NoiseGenerator import NoiseGenerator
from image.ImageGenerator import ImageGenerator
import pyfastnoisesimd as fns
from time import time_ns


def demo_main():
    identifier = time_ns()
    n_g = NoiseGenerator(seed=(identifier-42)%2**31,
                         n_threads=64, 
                         noise_type=fns.NoiseType.Cubic, 
                         frequency=0.001, 
                         octaves=2, 
                         lacunarity=0.05, 
                         gain=0.05, 
                         perturb_type=fns.PerturbType.Normalise)
    i_g = ImageGenerator(dimensions=(256, 256))
    i_g.populate_image(n_g.get_noise(seed=identifier+1337, 
                                     dimensions=(256, 256)))
    i_g.image.save(f"past/img-{identifier}-singular.png")
    i_g.generate_mosaic(seed=identifier, 
                        mosaic_side_length=3,
                        dimensions=(16, 16))
    i_g.image.save(f"past/img-{identifier}-mosaic.png")
    i_g.image.show()


if __name__ == "__main__":
    demo_main()
