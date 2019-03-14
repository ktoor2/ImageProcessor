import time
from config.configs import Configs
from event_handler import Handler
from watchdog.observers import Observer


class Watcher:

    def __init__(self):
        self.configs = Configs.getInstance().config
        self.observer = Observer()

    def run(self):
        """
        Thread based event handler to poll input directory for new images
        :return: None
        """
        event_handler = Handler()
        self.observer.schedule(event_handler, self.configs["input_dir"], recursive=True)
        self.observer.start()
        print ("--Starting image processing App--")
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
            print ("--Exiting the program. Happy Farming!--")
        self.observer.join()


if __name__ == '__main__':
    w = Watcher()
    w.run()
