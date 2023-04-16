import matplotlib.pyplot as plt 
import numpy as np 

from astropy.io import fits
from astropy.visualization import astropy_mpl_style
from PIL import Image

plt.style.use(astropy_mpl_style)

image = Image.open('glx.jpg')

xsize,ysize = image.size
print(f"Image size :{xsize}x{ysize}")
print(f"Image bands : {image.getbands()}")
ax = plt.imshow(image)
plt.show()


r,g,b = image.split()

r_data = np.array(r.getdata())
g_data = np.array (g.getdata())
b_data = np.array(b.getdata())

# print(r_data.shape)
r_data = r_data.reshape(xsize,ysize)
g_data = g_data.reshape(xsize,ysize)
b_data = b_data.reshape(xsize,ysize)


red = fits.PrimaryHDU(data= r_data)
red.header['LATOBS'] = "32:11:56"
red.header ['LANGOBS'] = "110:56"

green = fits.PrimaryHDU(data=g_data)
green.header['LATOBS'] = "32:11:56"
green.header['LONGOBS'] = "110:56"
green.writeto('green.fits')

blue = fits.PrimaryHDU(data=b_data)
blue.header['LATOBS'] = "32:11:56"
blue.header['LONGOBS'] = "110:56"
blue.writeto('blue.fits')

from pprint import pprint

pprint(red.header)

