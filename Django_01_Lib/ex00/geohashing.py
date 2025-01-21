import sys
import antigravity




if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("usage: python3 geohashing.py ")
        sys.exit(1)
    latitude = float()
    longitude = float()
    datedow = str()
    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        datedow = sys.argv[3].encode('utf-8')
    except Exception as e:
        print(f"{e}")
        sys.exit(1)
       
    antigravity.geohash(latitude, longitude, datedow)