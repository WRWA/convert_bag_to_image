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
    rs.config.enable_device_from_file(config, bag_file,repeat_playback=False )
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
        #####################################################
2
##               Read bag from file                ##
3
#####################################################
4
## edit here
5
​
6
bag_file = './test.bag'
7
save_dir = './image/'
8
img_format = '.png'
9
​
10
#####################################################
11
# First import library
12
import pyrealsense2 as rs
13
import numpy as np
14
import cv2
15
import os.path
16
​
17
if os.path.splitext(bag_file)[1] != ".bag":
18
    print("The given file is not of correct file format.")
19
    print("Only .bag files are accepted")
20
    exit()
21
​
22
try:
23
    pipeline = rs.pipeline()
24
    config = rs.config()
25
    rs.config.enable_device_from_file(config, bag_file)
26
    config.enable_stream(rs.stream.color, rs.format.rgb8, 30)
27
​
28
    # Start streaming from real
29
    pipeline.start(config)
30
    frame_idx = 0
31
    cv2.namedWindow("Color Stream", cv2.WINDOW_AUTOSIZE)
32
    
33
    # Streaming loop
34
    while  True:
35
        frames = pipeline.wait_for_frames()
36
        color_frame = frames.get_color_frame()
37
        img = np.asanyarray(color_frame.get_data())
38
        frame_idx = frame_idx + 1
39
        
40
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
41
        cv2.imwrite(save_dir + str(frame_idx) + img_format, img)
42
        print('image saved as ', frame_idx, img_format)
43
        cv2.imshow("Color Stream", img) 
44
​
45
        key = cv2.waitKey(1)cv2.imwrite(save_dir + str(frame_idx) + img_format, img)
        print('image saved as ', frame_idx, img_format)
        cv2.imshow("Color Stream", img) 

        key = cv2.waitKey(1)
        # if pressed escape exit program
        if key == 27:
            cv2.destroyAllWindows()
            break

finally:
    pass
