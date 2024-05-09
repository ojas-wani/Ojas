import pyzed
import pyzed.sl as sl
import math
import cv2

zed = sl.Camera()

# Set the input from stream
init = sl.InitParameters()
init.set_from_stream("192.168.0.164", 30000) # Specify the IP and port of the sender
init.depth_mode = sl.DEPTH_MODE.ULTRA
init.coordinate_units = sl.UNIT.MILLIMETER

# Open the camera
err = zed.open(init)
if err != sl.ERROR_CODE.SUCCESS:
	exit(1)
	
image = sl.Mat()
depth_map = sl.Mat()
runtime_parameters = sl.RuntimeParameters()
if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS :
    # A new image and depth is available if grab() returns SUCCESS`
    zed.retrieve_image(image, sl.VIEW.LEFT) # Retrieve left image
    zed.retrieve_measure(depth_map, sl.MEASURE.DEPTH) # Retrieve depth`
    img = depth_map.get_data()

    print(img)

    cv2.imshow("i", img)
    key = cv2.waitKey(5)

# Close the camera
zed.close()