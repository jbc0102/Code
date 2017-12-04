import math
import os
import errno
import shutil


def get_grid_dim(x):
    factors = prime_powers(x)
    if len(factors) % 2 == 0:
        i = int(len(factors) / 2)
        return factors[i], factors[i - 1]
    i = len(factors) // 2
    return factors[i], factors[i]


def prime_powers(n):
    factors = set()
    for x in range(1, int(math.sqrt(n)) + 1):
        if n % x == 0:
            factors.add(int(x))
            factors.add(int(n // x))
    return sorted(factors)


def empty_dir(path):
    for the_file in os.listdir(path):
        file_path = os.path.join(path, the_file)

        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exepotion as e:
            print('Warning: {}'.format(e))


def creat_dir(path):
    try:
        os.mkdir(path)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise


def prepare_dir(path, empty=False):
    if not os.path.exists(path):
        creat_dir(path)

    if empty:
        empty_dir(path)