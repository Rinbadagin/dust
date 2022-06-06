from PIL import Image

from image.ImageFilter import ImageFilter


class BrownFilter(ImageFilter):
    def filter(self, input_image):
        input_pixels = input_image.load()
        output_image = Image.new(mode="RGB",
                                 size=
                                 (input_image.size[0] // self.sampling_rate,
                                  input_image.size[1] // self.sampling_rate))
        output_pixels = output_image.load()
        for x in range(input_image.size[0] // self.sampling_rate):
            for y in range(input_image.size[1] // self.sampling_rate):
                r, g, b = input_pixels[
                    x * self.sampling_rate, y * self.sampling_rate]
                r *= (0x96 * (g / 128))/255
                g *= (0x4B * (g / 128))/255
                b *= (255 - (r*b))
                output_pixels[x, y] = (int(r), int(g), int(b))
        return output_image
