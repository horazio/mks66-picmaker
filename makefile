run:
	python3 picmaker.py
	convert image.ppm image.png

clean:
	-rm -f *.ppm *.png