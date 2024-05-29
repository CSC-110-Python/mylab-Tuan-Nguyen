import math
from constants import earth_g, mars_g
height = int(input('Height in meters: '))
if __name__ == '__main__':
    print('Earth:', math.sqrt(2 * height / earth_g), 'seconds')
    print('Mars:', math.sqrt(2 * height / mars_g), 'seconds')