from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


class Location:

    def __init__(self, path):
        self.path = path
        self.gps_data = {}
        self.cordinates = {}

    def get_lat_lon(self):
        image = Image.open(self.path)
        info = image._getexif()
        if info:
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                if decoded == "GPSInfo":
                    for t in value:
                        sub_decoded = GPSTAGS.get(t, t)
                        self.gps_data[sub_decoded] = value[t]
                    self.get_cordinates()
        return self.cordinates

    def get_cordinates(self):
        gps_latitude = self.gps_data.get('GPSLatitude', None)
        gps_latitude_ref = self.gps_data.get('GPSLatitudeRef', None)
        gps_longitude = self.gps_data.get('GPSLongitude', None)
        gps_longitude_ref = self.gps_data.get('GPSLongitudeRef', None)

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = self.convert_to_degress(gps_latitude)
            if gps_latitude_ref != "N":
                lat = 0 - lat
            self.cordinates["lat"] = lat

            lon = self.convert_to_degress(gps_longitude)
            if gps_longitude_ref != "E":
                lon = 0 - lon
            self.cordinates["lon"] = lon

    def convert_to_degress(self, value):
        d0 = value[0][0]
        d1 = value[0][1]
        d = float(d0) / float(d1)

        m0 = value[1][0]
        m1 = value[1][1]
        m = float(m0) / float(m1)

        s0 = value[2][0]
        s1 = value[2][1]
        s = float(s0) / float(s1)

        return d + (m / 60.0) + (s / 3600.0)
