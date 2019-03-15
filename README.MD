Image Processing pipeline for Granular


Steps to run image processor:

1. Install dependencies in requirements.txt
	(Note: Make sure BaseMap and all it's dependencies are installed for visualization. See https://matplotlib.org/basemap/users/installing.html)

2. Run python3 main.py
	
	-->This will start a watchdog service (event triggers) on the directory data/raw_images
	--> Any files (jpg, subdirectories)  added to the watchdog directory will trigger an event
	--> Subdirectory structure is recommended as it is easier to detect crop type based on subdirectory name

3. Copy data/photos to data/raw_images
	(Note: You can do this iteratively with each subdirectory(barley, corn, etc) as well)

4. The processed images can be found under data/processed_images
	(Note: All the directories are configurable under configs/configs.json)

5. Send a SIGINT ( ctrl + c) to stop the processor

5. The cordinates for the images can be found in data/visualize/cordinates.txt

6. To visualize the cordinates run ./visualize.py

---------------------------------------------------------------------------------------------

Future Improvements:

1. Use multithreading to process each image under a directory with a thread pool
2. Use API and webserver to visualize the cordinates at any point in time
3. Use a logging class instead of print statements
