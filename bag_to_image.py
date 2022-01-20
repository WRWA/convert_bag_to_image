#####################################################
##               Read bag from file                ##
#####################################################
## edit here

bag_file = './test.bag'
save_dir = './image/'
img_format = '.png'

#####################################################
# First import library
import pyrealsense2 as rs
import numpy as np
import cv2
import os.path

if os.path.splitext(bag_file)[1] != ".bag":
    print("The given file is not of correct file format.")
    print("Only .bag files are accepted")
    exit()

try:
    pipeline = rs.pipeline()
    config = rs.config()
    rs.config.enable_device_from_file(config, bag_file)
    config.enable_stream(rs.stream.color, rs.format.rgb8, 30)

    # Start streaming from real
    pipeline.start(config)
    frame_idx = 0
    cv2.namedWindow("Color Stream", cv2.WINDOW_AUTOSIZE)
    
    # Streaming loop
    while  True:
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        img = np.asanyarray(color_frame.get_data())
        frame_idx = frame_idx + 1
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imwrite(save_dir + str(frame_idx) + img_format, img)
        print('image saved as ', frame_idx, img_format)
        cv2.imshow("Color Stream", img) 

        key = cv2.waitKey(1)
        # if pressed escape exit program
        if key == 27:
            cv2.destroyAllWindows()
            break
        
finally:
    pass
