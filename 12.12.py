from numpy import asarray
from numpy import clip
from PIL import Image
image = Image.open('1.jpg')
pixels = asarray(image)
pixels = pixels.astype('float32')
mean, std = pixels.mean(), pixels.std()
print ('Mean: %.3f, Standard Deviation: %.3f' %(mean, std))
pixels = (pixels-mean) / std
pixels = clip(pixels, -1.0, 1.0)
pixels = (pixels + 1.0) / 2.0
mean, std = pixels.mean(), pixels.std()
print('Mean: %.3f, Standard Deviation: %.3f' % (mean, std))
print ('Min: %.3f, Max: %.3f' % (pixels.min(), pixels.max()))