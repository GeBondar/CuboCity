from subprocess import call
from PIL import Image
import zbarlight

def getCode(file_path):
	"This function gets text from QR code"
	with open(file_path,'rb') as image_file:
		image = Image.open(image_file)
		image.load()
	code = zbarlight.scan_codes('qrcode', image)
	return code

def makePhoto(file_path):
	call(['fswebcam',file_path])
