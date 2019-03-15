import cv2
import os
import numpy as np
from location import Location
from config.configs import Configs


class CropImage:

    def __init__(self, path):
        self.configs = Configs.getInstance().config
        image_split = path.split("/")
        self.crop_type = image_split[-2]
        self.image_name = image_split[-1]
        self.image_path = path
        self.image = self.open_image()

    def open_image(self):
        return cv2.imread(self.image_path, 1)

    def process_image(self):
        """
        runs steps for processing image
        :return: None
        """
        self.extract_location()
        self.resize_image()
        self.filter_color_image()
        self.save_image()

    def extract_location(self):
        cordinate_dict = Location(self.image_path).get_lat_lon()
        if cordinate_dict:
            print("Found location cordinates {} & {}".format(cordinate_dict["lat"], cordinate_dict["lon"]))
            with open(self.configs["locations_file"], 'a+') as f:
                f.write(str(cordinate_dict["lon"]) + ',' + str(cordinate_dict["lat"]) + ',' + self.crop_type + '\n')

    def resize_image(self):
        self.image = cv2.resize(self.image, (self.configs["image_size"]["width"], self.configs["image_size"]["height"]))

    def filter_color_image(self):
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (20, 25, 25), (97, 255, 255))
        imask = mask > 0
        green_and_yellow = np.zeros_like(self.image, np.uint8)
        green_and_yellow[imask] = self.image[imask]
        self.image = green_and_yellow

    def save_image(self):
        process_dir = os.path.join(self.configs["processed_dir"], self.crop_type)
        if not os.path.exists(process_dir):
            os.mkdir(process_dir)
        cv2.imwrite(os.path.join(process_dir, self.image_name), self.image)

