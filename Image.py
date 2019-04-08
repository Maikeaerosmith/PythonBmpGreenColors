# https://en.wikipedia.org/wiki/BMP_file_format
import os.path
import math
import datetime

class Image:
	def __init__(self):
		self.filename = ''
		self.width = 0
		self.height = 0
		self.bitsPerPixel = 0
		self.content = []
	
	def setFilename(self, filename):
		self.filename = filename
	
	def setWidth(self, width):
		self.width = width
	
	def setHeight(self, height):
		self.height = height
	
	def setContent(self, content):
		self.content = content
	
	def getWidth(self):
		return self.width
	
	def getHeight(self):
		return self.height
	
	def getFilename(self):
		return self.filename
	
	def getContent(self):
		return self.content
	
	def loadContent(self):
		if not os.path.isfile( self.getFilename() ):
			return False
		else:
			file = open( self.getFilename(), 'rb' )
			if file.read(2) != b'BM':
				return False
			else:
				file.seek(2)
				tmp = file.read(4)
				size = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
				
				file.seek(0x0A)
				tmp = file.read(4)
				offsetPixelArray = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(0x0E)
				tmp = file.read(4)
				sizeHeader = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(0x12)
				tmp = file.read(4)
				bitmapWidth = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(0x16)
				tmp = file.read(4)
				bitmapHeight = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(0x1A)
				tmp = file.read(2)
				numberColorPlanes = (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(0x1C)
				tmp = file.read(2)
				numberBitsPerPixel = (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(0x1E)
				tmp = file.read(4)
				compressionMethod = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
				if compressionMethod != 0:
					return False
				
				file.seek(0x22)
				tmp = file.read(4)
				imageSize = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(0x26)
				tmp = file.read(4)
				horizontalResolution = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(0x2A)
				tmp = file.read(4)
				verticalResolution = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(0x2E)
				tmp = file.read(4)
				numberColorsPalette = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
				if numberColorsPalette != 0:
					return False
				
				file.seek(0x32)
				tmp = file.read(4)
				numberImportantColors = (16**6) * tmp[3] + (16**4) * tmp[2] + (16**2) * tmp[1] + (16**0) * tmp[0]
								
				file.seek(offsetPixelArray) # init in offset pixel array
				self.width = bitmapWidth
				self.height = bitmapHeight
				self.bitsPerPixel = numberBitsPerPixel
				self.content = []
				fill = int( math.ceil(numberBitsPerPixel * bitmapWidth / 32.0) * 4 ) - (numberBitsPerPixel//8) * bitmapWidth
				for i in range(bitmapHeight):
					row = []
					for i in range(bitmapWidth):
						rgb = file.read(3)
						r = rgb[2]
						g = rgb[1]
						b = rgb[0]
						row.append( [r,g,b] )
					file.read(fill)
					self.content.append( row )
				file.close()
				return True
		
	def readGreenValues(self):
		counter_green_pixels = 0
		counter_total_pixels = 0
		
		for i in range(len(self.content)):
			for j in range(len(self.content[i])):
				counter_total_pixels = counter_total_pixels + 1
				r = g = b = 0
				r = self.content[i][j][0]
				g = self.content[i][j][1]
				b = self.content[i][j][2]
				
				if int(g) >= 100 :
					if int(r) <= 100 and int(b) <= 100 :
						counter_green_pixels += 1
						
						
				if int(g) >= 130 :
					if int(r) <= 120 and int(b) <= 100 :
						counter_green_pixels += 1
						
						
				if int(g) >= 80 :
					if int(r) <= 70 and int(b) <= 50 :
						counter_green_pixels += 1
						
						
				if int(g) >= 60 :
					if int(r) <= 50 and int(b) <= 40 :
						counter_green_pixels += 1
						
						
				if int(g) >= 50 :
					if int(r) <= 60 and int(b) <= 25 :
						counter_green_pixels += 1
						
						
				if int(g) >= 50 :
					if int(r) <= 40 and int(b) <= 75 :
						counter_green_pixels += 1
						
						
				if int(g) >= 40 :
					if int(r) <= 30 and int(b) <= 20 :
						counter_green_pixels += 1
						
				
		percent_green_pixels = (100 * counter_green_pixels) / counter_total_pixels
		now = datetime.datetime.now()
		today = datetime.date.today()
		
		fileLog = open( 'log_' + str(today) +'.txt' ,'a+' )
		
		fileLog.write(str(now) + ': ')
		fileLog.write(self.getFilename() + ': ')
		fileLog.write('Width: ' + str(self.getWidth()) + ' pixels - Height: ' + str(self.getHeight()) + ' pixels - Total Pixels: ' + str(counter_total_pixels) + ' - Green Pixels:  ' + str(counter_green_pixels) + ' - ' + str(percent_green_pixels) + '%' + '\n\n' )
		
		fileLog.close()

		
			