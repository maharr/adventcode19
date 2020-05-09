import math

data = open("image.txt", "r")
image = data.read()



#image = '123456789012'

image_dim = [25, 6]

#image_dim = [3,2]

layers = len(image) // math.prod(image_dim)

layer_max_0 = [-1,100]


for layer in range(layers):
    count = 0
    for i in range(math.prod(image_dim)):
        pixel = image[(layer*math.prod(image_dim)) + i]
        if pixel == "0":
            count += 1
    if count < layer_max_0[1]:
    	layer_max_0[0] = layer
    	layer_max_0[1] = count
    
    #print(layer, count)

print(layer_max_0)

count_1 = 0
count_2 = 0
for i in range(math.prod(image_dim)):
        pixel = image[(layer_max_0[0]*math.prod(image_dim)) + i]
        if pixel == "1":
            count_1 += 1
        if pixel == "2":
        	count_2 += 1
print(count_1*count_2)

