from keras.preprocessing.image import load_img
from keras.preprocessing.image import save_img
from keras.preprocessing.image import img_to_array
img = load_img('1.jpg', color_mode='grayscale')
img_array = img_to_array(img)
save_img('1-1', img_array)
img = load_img('1_grayscale.jpg')
print(type(img))
print(img.format)
print(img.mode)
print(img.size)
img.show()