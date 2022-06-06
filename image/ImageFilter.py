from PIL import Image


class ImageFilter:
    def __init__(self, sampling_rate=4):
        """Class for fiddling with image representation.
        Stuff like dithering or representing pixels as different size circles.
        Sampling rate - Frequency of pixel sampling. If the effect makes 1 pixel into multiple
            (ie with the circle example) the rate at which pixels are converted is important to
            control the size of the output image.
            Sampling rate is 1/n where n is the size of the gap (in pixels) between sampling"""
        self.sampling_rate = sampling_rate

    def filter(self, input_image):
        input_pixels = input_image.load()
        output_image = Image.new(mode="RGB",
                                 size=
                                 (input_image.size[0] // self.sampling_rate,
                                  input_image.size[1] // self.sampling_rate))
        output_pixels = output_image.load()
        for x in range(input_image.size[0] // self.sampling_rate):
            for y in range(input_image.size[1] // self.sampling_rate):
                output_pixels[x, y] = input_pixels[
                    x * self.sampling_rate, y * self.sampling_rate]
        return output_image