import time
import traceback
from image import CropImage
from watchdog.events import FileSystemEventHandler


# To Do: Apply multithreading image processing

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_created(event):
        """
        Handler for dogwatch event
        :param event: Event object from dogwatch
        :return: None
        """
        path = event.src_path
        if path.endswith(".jpg"):
            try:
                start_time = time.time()
                image = CropImage(path)
                image.process_image()
                print(" Image {} processed in {}".format(path.split("/")[-1], (time.time() - start_time) * 1000))
            except Exception as e:
                print("Image processing failed with exception {}".format(e))
                traceback.print_exc()
