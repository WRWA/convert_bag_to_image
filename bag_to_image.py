#####################################################
##               Read bag from file                ##
#####################################################


# First import library
import pyrealsense2 as rs
# Import Numpy for easy array manipulation
import numpy as np
# Import OpenCV for easy image rendering
import cv2
# Import argparse for command-line options
import argparse
# Import os.path for file path manipulation
import os.path

# Create object for parsing command-line options
parser = argparse.ArgumentParser(description="Read recorded bag file and display depth stream in jet colormap.\
                                Remember to change the stream fps and format to match the recorded.")
# Add argument which takes path to a bag file as an input
parser.add_argument("-i", "--input", type=str, help="Path to the bag file")
# Parse the command line arguments to an object
args = parser.parse_args()
# Safety if no parameter have been given
if not args.input:
    print("No input paramater have been given.")
    print("For help type --help")
    exit()
# Check if the given file have bag extension
if os.path.splitext(args.input)[1] != ".bag":
    print("The given file is not of correct file format.")
    print("Only .bag files are accepted")
    exit()
try:
    pipeline = rs.pipeline()
    config = rs.config()
    rs.config.enable_device_from_file(config, args.input)
    config.enable_stream(rs.stream.color, rs.format.rbg8, 30)

    # Start streaming from file
    pipeline.start(config)
    frame_idx = 0
    
    # Streaming loop
    while True:
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        
        img = np.asanyarray(color_frame.get_data())
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        cv2.imwrite('./image/'+str(frame_idx)+'.png', img)
        
        frame_idx = frame_idx + 1
finally:
    pass
