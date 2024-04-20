
#include <ros.h>
#include <std_msgs/Int32.h>

ros::NodeHandle nh;

std_msgs::Int32 outputMessage;

ros::Publisher pub("info_back_from_second", &outputMessage);


void setup(){
 // Serial.begin(57600);
  pinMode(A0,INPUT);
  nh.initNode();
  nh.advertise(pub);
  //nh.subscribe(sub);     
}

void loop(){
  outputMessage.data = analogRead(A0);
  pub.publish(&outputMessage);
 // Serial.println(outputMessage.data);
  
  nh.spinOnce();
  delay(1);
}
