import matplotlib.pyplot as plt 
from astropy.visualization import astropy_mpl_style
from astropy.io import fits 
from astropy.utils.data import get_pkg_data_filename

image_file = get_pkg_data_filename('tutorials/FITS-images/HorseHead.fits')
# fits.info(image_file)



plt.style.use(astropy_mpl_style)

image_data = fits.getdata(image_file, ext = 0)

print (image_data.shape)

plt.figure()
plt.imshow(image_data,cmap='gray')
plt.colorbar()
plt.show()

