'''
The following code is used to assess the accuracy of a model for the test data.
'''

from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from tensorflow import keras

image_size= (180, 180)
batch_size = 32

model = load_model('Epoch200_with_generated_images_data/save_at_75.h5')     

test_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "Data/test",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)


test_loss, test_acc = model.evaluate(test_ds)
print('test loss:', test_loss)
print('test acc:', test_acc)
