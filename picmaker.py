f = open("image.ppm", "w+")
f.write("P3\n500 500\n255\n")


ray = []
for i in range(500):
    ray.append(0)    

ray[0] = 1

for i in range(500):
 
    for x in range(500):
        if(x < 499):
            ray[x + 1] += ray[x]
            ray[x + 1] %= 2
            
    for j in range(500):
        pixel = str(i * j % 255) + " " + str(255 * ray[j]) + " " + str(j * i % 255) + " "
        f.write(pixel) 

f.close()    