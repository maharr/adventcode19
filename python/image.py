import math

data = open("image.txt", "r")
image = data.read()



image = '123456789012'

#image_dim = [25, 6]

image_dim = [3,2]

layers = len(image) // math.prod(image_dim)


for layer in range(layers):
    count = 0
    for i in range(math.prod(image_dim)):
        
        #print("layer", layer, "i", i)
        pixel = image[(layer*math.prod(image_dim)) + i]
        if pixel == "0":
            print(pixel)
            count += 1
