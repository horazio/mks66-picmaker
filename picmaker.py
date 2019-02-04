f = open("image.ppm", "w+")
f.write("P3\n500 500\n255\n")



for i in range(500):
    for j in range(500):
        pixel = str(i) + " " + str(j) + " 0 "
        f.write(pixel) 

f.close()    