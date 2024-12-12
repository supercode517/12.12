from keras.preprocessing.image import load_img
img = load_img(1.jpg)
print(type(img))
print(img.format)
print(img.mode)
print(img.size)
img.show()