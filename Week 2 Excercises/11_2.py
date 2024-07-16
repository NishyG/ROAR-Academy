from matplotlib import image
from matplotlib import pyplot
import os

path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna.bmp'
data = image.imread(filename)


filename_flag = "C:\\Users\\Anish\\Pictures\\Screenshots\\flag.jpg"
data_flag = image.imread(filename_flag)
data_flag_resized = data_flag[:, :data.shape[1], :4]

# Display image information
print('Image type is: ', type(data))
print('Image shape is: ', data.shape)

plot_data = data.copy()
plot_data[ :data_flag_resized.shape[0], :data.shape[1]-400, :3] = data_flag_resized[ :data_flag_resized.shape[0], :data.shape[1]-400, :3]

# use pyplot to plot the image
pyplot.imshow(plot_data)
pyplot.show()