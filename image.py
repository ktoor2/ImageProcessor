from location import Location
from config.configs import Configs


class CropImage:

    def __init__(self, path):
        self.configs = Configs.getInstance().config
        self.image_path = path

    def process_image(self):
        """
        runs steps for processing image
        :return: None
        """
        self.extract_location()
        #self.resize_image()
        #self.save_image()

    def extract_location(self):

        cordinate_dict = Location(self.image_path).get_lat_lon()
        if cordinate_dict:
            print("Found location cordinates {} & {}".format(cordinate_dict["lat"],cordinate_dict["lon"]))


