import math

data = open("image.txt", "r")
image = data.read()



#image = '0222112222120000'

image_dim = [25, 6]

#image_dim = [2,2]

layers = len(image) // math.prod(image_dim)

final_image = "2" * math.prod(image_dim)

#print(final_image)

for i in range(math.prod(image_dim)):
    count = 0
    for layer in range(layers):
        pixel = image[(layer*math.prod(image_dim)) + i]
        if final_image[i:i+1] == "2" and pixel != "2":
            final_image = final_image[:i] + pixel + final_image[i+1:]
            #print(final_image)



for i in range(image_dim[1]):
    for j in range(image_dim[0]):
        if final_image[i*image_dim[0] + j] == "1":
            print(final_image[i*image_dim[0] + j], end='')
        else:
            print(" ",end='')
    print("")
