'''

this is my first we are so back project
it is a simple python program that generates a gif out of two up to 5 images
based on https://www.codedex.io/projects/create-a-gif-with-python

'''

# import libraries
import imageio.v3 as iio
import os
import numpy as np


def generalize_image_data(name_of_file):

    generalized_image_data = []
    image_data = iio.imread(name_of_file)
    # print(image_data.shape)

    if image_data.shape[0] == 1 : #remove singleton data
        image_data = np.squeeze(image_data)
        # image_data = np.squeeze(image_data)
    # print(image_data.shape)

    generalized_image_data = image_data
    
    return generalized_image_data


def hi():
    return "hello, welcome to your new world"


def giffy(file_names):
    # image file names in same location as code file
    # file_names = ['IMG_4738.HEIC', 'IMG_4739.HEIC', 'IMG_4740.HEIC', 'IMG_4741.HEIC']
    # file_names = ['1.png','3.png','2.png','4.png','5.png']

    # array to hold result image data
    resultImage = []

    # loop over files reading in image data
    for filename in file_names:
        tmp_img_data = generalize_image_data(filename)

        resultImage.append(tmp_img_data)

    # turn images into a gif
    iio.imwrite('go_gurl.gif', image=resultImage, duration=100, loop=0)
    # iio.imwrite('carpet.gif', image=resultImage, duration=800, loop=0)

    return


def check_gif_dimensions(name_of_gif):

    frames = iio.imread(name_of_gif, index=None) #read all frames
    output_dimensions = frames[0].shape
    
    return output_dimensions


def main():
    myMessage = hi()
    # gif_size = check_gif_dimensions('carpet.gif')
    # generalize_image_data("IMG_4740.HEIC")
    giffy(file_names = ['1.png','3.png','2.png','4.png','5.png'])

    print(myMessage)
    # print(gif_size)

if __name__ == "__main__":
    main()

    

