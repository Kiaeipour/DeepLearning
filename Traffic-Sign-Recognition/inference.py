import argparse
import numpy as np
import cv2
from tensorflow.keras.models import load_model

parser = argparse.ArgumentParser()
parser.add_argument("--input_model",type=str,help="Please Enter path of input model/  Example: model.h5")
parser.add_argument("--input_image",type=str,help="Please Enter path of input image/  Example: image.jpg")
arg = parser.parse_args()
model = load_model(arg.input_model)

image = cv2.imread(arg.input_image)
image = cv2.resize(image,(32,32))
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
image = image / 255.0
image = np.expand_dims(image,axis=0)
predict = np.argmax(model.predict(image))

if predict==0: print("Speed limit (20km/h)")
elif predict==1: print("Speed limit (30km/h)")
elif predict==2: print("Speed limit (50km/h)")
elif predict==3: print("Speed limit (60km/h)")
elif predict==4: print("Speed limit (70km/h)")
elif predict==5: print("Speed limit (80km/h)")
elif predict==6: print("End of speed limit (80km/h)")
elif predict==7: print("Speed limit (100km/h)")
elif predict==8: print("Speed limit (120km/h)")
elif predict==9: print("No passing")
elif predict==10: print("No passing veh over 3.5 tons")
elif predict==11: print("Right-of-way at intersection")
elif predict==12: print("Priority road")
elif predict==13: print("Yield")
elif predict==14: print("Stop")
elif predict==15: print("No vehicles")
elif predict==16: print("Veh > 3.5 tons prohibited")
elif predict==17: print("No entry")
elif predict==18: print("General caution")
elif predict==19: print("Dangerous curve left")
elif predict==20: print("Dangerous curve right")
elif predict==21: print("Double curve")
elif predict==22: print("Bumpy road")
elif predict==23: print("Slippery road")
elif predict==24: print("Road narrows on the right")
elif predict==25: print("Road work")
elif predict==26: print("Traffic signals")
elif predict==27: print("Pedestrians")
elif predict==28: print("Children crossing")
elif predict==29: print("Bicycles crossing")
elif predict==30: print("Beware of ice/snow")
elif predict==31: print("Wild animals crossing")
elif predict==32: print("End speed + passing limits")
elif predict==33: print("Turn right ahead")
elif predict==34: print("Turn left ahead")
elif predict==35: print("Ahead only")
elif predict==36: print("Go straight or right")
elif predict==37: print("Go straight or left")
elif predict==38: print("Keep right")
elif predict==39: print("Keep left")
elif predict==40: print("Roundabout mandatory")
elif predict==41: print("End of no passing")
elif predict==42: print("End no passing veh > 3.5 tons")