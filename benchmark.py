import time
import os
from pipeline import process_image

IMAGE_FOLDER = "images"

times = []

for img in os.listdir(IMAGE_FOLDER):

    path = os.path.join(IMAGE_FOLDER, img)

    start = time.time()

    process_image(path)

    end = time.time()

    times.append(end - start)

print("Total Images:", len(times))
print("Average Processing Time:", sum(times)/len(times))