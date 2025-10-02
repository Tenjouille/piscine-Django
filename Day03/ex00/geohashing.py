import sys
from antigravity import geohash

def	geohashing():
	if len(sys.argv) != 4:
		print("Error: Arguments missing. You need a Latitude, longitude and DateDow.")
		return
	try:
		latitude = float(sys.argv[1])
	except:
		print("Error: Latitude must be a float number.")
		return
	try:
		longitude = float(sys.argv[2])
	except:
		print("Error: Longitude must be a float number.")
		return
	try:
		dateDow = sys.argv[3].encode()
	except:
		print("Error: dateDow must be a string to convert into byte")
		return
	
	geohash(latitude, longitude, dateDow)

if __name__ == "__main__":
	geohashing()