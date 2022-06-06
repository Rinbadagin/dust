import math
import string
import numpy

from PIL import Image

digs = string.digits + string.ascii_letters
# note 0th lambda is used by default when no lambda is provided
# also note reliance on custom array should depend on the order the lambdas are provided
# as the array cannot be accessed before its been generated
demo_lambdas = [lambda n, custom_arrays, x, y: (math.fabs(n) % 1) * 255,
                lambda n, custom_arrays, x, y: (((n*custom_arrays[0][x,y])*255)%255),
                lambda n, custom_arrays, x, y: (n*1024)%255,
                lambda n, custom_arrays, x, y: ((255-custom_arrays[1][x,y])*n)%255]


def get_custom_arrays_from_noise(noise_arrays, funcs):
    """Task: Get arrays modified by a given lambda which can be dependent on values from previously computed arrays
        Inputs: noise array(s), function array - size of output array will be the max of noise and lambda array length
        Outputs array(s) of noise-based information. Can be used for colour or further modified
        Functions must take 4 arguments, a noise array, the previously computed custom arrays, and the current x
        and y values in the loop. Output is the intensity of the output for that coordinate.
    """
    custom_arrays = []
    for i in range(len(funcs)):
        if not callable(funcs[i]):
            # potential off by 1 TODO: i%len(noise_arrays) different to index required
            col_array = numpy.zeros(noise_arrays[i % len(noise_arrays)].shape)
            for x in range(noise_arrays[i % len(noise_arrays)].shape[0]):
                for y in range(noise_arrays[i % len(noise_arrays)].shape[1]):
                    col_array[x, y] = demo_lambdas[0](noise_arrays[i % len(noise_arrays)][x, y], custom_arrays, x, y)
            custom_arrays.append(col_array)
        else:
            col_array = numpy.zeros(noise_arrays[i % len(noise_arrays)].shape)
            for x in range(noise_arrays[i % len(noise_arrays)].shape[0]):
                for y in range(noise_arrays[i % len(noise_arrays)].shape[1]):
                    col_array[x, y] = funcs[i](noise_arrays[i % len(noise_arrays)][x, y], custom_arrays, x, y)
            custom_arrays.append(col_array)
    for i in range(len(custom_arrays)):
        custom_arrays[i] = custom_arrays[i].astype(numpy.int64)
    return custom_arrays


def map2d1d(x, y, modulus):
    return int(f"{number_to_base(x, modulus - 1)}{number_to_base(y, modulus - 1)}",
               modulus - 1)


def number_to_base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[x % base])
        x = x // base

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)


def merge_images(images, generate_column=True, mosaic_side_length=-1, debug=False):
    # rewrite for n images parsed in array
    if len(images) == 2:
        (width0, height0) = images[0].size
        (width1, height1) = images[1].size

        if generate_column:
            result_width = width0
            result_height = height0 + height1
        else:
            result_width = width0 + width1
            result_height = height0

        result = Image.new('RGB', (result_width, result_height))
        result.paste(im=images[0], box=(0, 0))
        if generate_column:
            result.paste(im=images[1], box=(0, height0))
        else:
            result.paste(im=images[1], box=(width0, 0))
        return result
    if int(math.sqrt(len(images))) ** 2 == len(images):
        side_length = int(math.sqrt(len(images)))
        if generate_column:
            columns = []
            for x in range(side_length):
                if debug:
                    print(f'Basis index: {x * side_length}')
                basis = images[x * side_length]
                for y in range(side_length - 1):
                    if debug:
                        print(f'X: {x} Y: {y}')
                        print(f'Selecting image index: {map2d1d(x, y, mosaic_side_length) + x + 1}')
                    basis = merge_images([basis, images[
                        int(f"{number_to_base(x, mosaic_side_length - 1)}" +
                            f"{number_to_base(y, mosaic_side_length - 1)}",
                            mosaic_side_length - 1) + x + 1]], True, mosaic_side_length, debug)
                columns.append(basis)
            result = columns[0]
            for i in range(len(columns) - 1):
                result = merge_images([result, columns[i + 1]], False, mosaic_side_length, debug)
            return result
