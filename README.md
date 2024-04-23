Objective : this is the code to publish data(eg. sensor readings ) from nodes (devices like arduino ) and subscribe them on a central system (jetson nano in our case) , so in our code what we are doing is , we have conneced the 2 arduino unos to 2 potentiiometers and they are connected to one jetson nano ,as shown in demo video.

**Requirements**
Your should have ROS and arduino installed 

**steps to run** 
Step 1: Download the repository 
Step 2: GO to ros_arduino_ws/ArduinoSketch/ArduinoConnection/ArduinoConnection.ino 
![image](https://github.com/geekyharsh01/Final_DC_Project/assets/95271790/99376ce0-ba45-4b7b-8eef-7bd0c91da3aa)

Step 3: open this file in arduino . and then goto file choose preferences and then set path sketchbook location  to  Final_DC_Project/Arduino/  or you can go to manage libraries and download rosserrialpythonlibrary (for any error reffer to error.txt file)

Step 4: Now upload arduinoConnection.ino to the first arduino device and seconarduinoconnection.ino to the secon arduino device 

![image](https://github.com/geekyharsh01/Final_DC_Project/assets/95271790/2bdc7b9f-fef0-4a20-9c83-8ffbdc0bfb78)
Here you can see the Topic name on which each arduino will publish the sensor data 


Step 5: open a terminal and run command : **roscore** , let it run on this terminal and open new terminal and source the workspace on this terminal using the command : **source ros_arduino_ws/devel/setup.bash** and then launch the launch file using the command : **roslaunch arduino_test_comm arduino.launch**

Step 6: 

![image](https://github.com/geekyharsh01/Final_DC_Project/assets/95271790/9934305b-48b0-4071-a880-67b95e413e6a)

in this path/ folder you can see 4 python files :
1. firstArduino.py - this file contains subscriber code , this subscribes first arduino on the topic info_back_from_first and then prints signal value on terminal
2. seconArduino.py - this file contains subscriber code , this subscribes second arduino on the topic info_back_from_second and then prints signal value on terminal
3. subscribeAddPublish.py - this file subscribes to both the topics on which 2 ardunis are publising the data and then it adds the signal values from both arduino and prints the result on terminal and publish this sum on the topic AddedSignal so that other nodes can subscribe on this topic and can access the value
4. subscribeAddedSignal.py - this file subcribes on the topic addedSignal to which this subscribeAddPublish files publish the sum and then print


Step 7: Open new terminal type **rostopic list** to see the list of all the topics 

Step 8: To run the above 4 files there is simple command : 
  **source ros_arduino_ws/devel/setup.bash**
  **rosrun arduino_test_comm firstArduino.py**
  to run other files open new terminal then source it and then **rosrun arduino_test_comm subscribeAddPublish.py**


To see the procedure and results refer to the demo video given in this repo.









