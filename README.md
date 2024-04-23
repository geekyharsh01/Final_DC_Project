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








