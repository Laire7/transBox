import cv2
import matplotlib.pyplot as plt

 
'''
Read an image from imahe path
'''
def read_image( image_path ): 
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)        
    return image

'''
Draw the bounding box on image
@param image - the image 
@param tl - bounding box top left corner
@param br - bounding box top bottom right
@return: a copy of input image with the bounding box on it
'''
def draw_boundingbox( image, tl, br ):
    copied_image = image.copy()
    image = cv2.rectangle(copied_image, tl, br, (0, 0, 255), 3)          
    return copied_image

'''Show image'''
def show_image( image ):
    # Drawing picture
    #plt.figure( figsize = (15,15) )
    plt.axis('off')
    plt.imshow( image )
    plt.show()

'''Plot all images in a list'''
def plot_images( images_list ):
    import math
    num_cols = 5
    num_rows = math.ceil( len(images_list) / num_cols )
    figsize = (10,10)
    fig = plt.figure( figsize=figsize)

    for i in range (0, len(images_list) ):
        info = images_list[i]
        x1, y1, x2, y2 = info[1]
        print(f'x1:{x1} y1:{y1} x2:{x2} y2:{y2}')
        image = draw_boundingbox( info[0], (x1, y1), (x2, y2) )
        
        axi = fig.add_subplot(num_rows, num_cols, i+1)
        axi.axis( 'off' )
        axi.set_title( ("%.1f" % info[2] ) )
        axi.imshow( image )

def main():
    # img = read_image('k1_f_0.jpg')
    img = cv2.imread('k1_f_0.jpg')
    cv2.imshow('img', img)

# if __name__ == "__main__":
import os, cv2
from matplotlib import pyplot as plt
# print(os.getcwd())
basicPath = os.path.join(os.getcwd(),'yolov11', 'transBox', 'guarana')
# basicPath = 'c:\Users\syoun\yolov11\transBox\guarana\'
print(basicPath)
os.chdir(basicPath)
plt.figure(figsize=(12, 12))
plt.axis('off')
imgFile = 'k1_f_0.jpg'
img = cv2.imread(imgFile, cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
plt.imshow(imgFile)
# img = cv2.imread(imgFile)
# cv2.imshow('img', img)
# cv2.waitKey()
# cv2.destroyAllWindows()