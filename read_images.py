import os.path
from Image import Image

if __name__ == "__main__":
	dir = os.path.dirname(os.path.realpath(__file__)) + '\\images'
	for filename in os.listdir(dir):
		if filename != '__pycache__' :
			finfo = open(dir + '\\' + filename)
			explod_file = finfo.name.split('.')
			extension = explod_file[-1]
			if extension == 'bmp' :
				image = Image()
				image.setFilename( dir + '\\' + filename )
				if image.loadContent():
					print( 'Image information:' )
					print( 'Width: ' + str(image.getWidth()) + ' pixels' )
					print( 'Width: ' + str(image.getHeight()) + ' pixels' )
					print( 'Filename: ' + image.getFilename() )
					image.readGreenValues()
				else:
					print( 'Image not imported' )