#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>


#define BLYNK_TEMPLATE_ID "TMPL304D4e0jC"
#define BLYNK_TEMPLATE_NAME "human and animal detection"
#define BLYNK_AUTH_TOKEN "HsbMEkgUQq9t2LSk7m4AZDYYUuuE6LCG"

// Blynk
char auth[] = "HsbMEkgUQq9t2LSk7m4AZDYYUuuE6LCG";            
char ssid[] = "Laya's iPhone";                               
char pass[] = "Laya1234567"; 

String values;

void setup() {
  // put your setup code here, to run once:
 Serial.begin(9600);
  Blynk.begin(auth, ssid, pass,"blynk.cloud",80);
}

void loop() {
  // put your main code here, to run repeatedly:
 Blynk.run();
if (Serial.available() > 0) 
{
  values=Serial.readStringUntil('#');
}
if (values=="h")
{
 Serial.print("human");
  Blynk.logEvent("alert_msg","Warning!Restricted Area");
}
else if(values=="e")
{
  Serial.print("elephant");
  Blynk.logEvent("alert_msg","Warning!Elephant in zone A");
}
else if(values=="l")
{
  Serial.print("lion");
  Blynk.logEvent("alert_msg","Warning!Lion in zone A");
}
else if(values=="t")
{
  Serial.print("tiger");
  Blynk.logEvent("alert_msg","Warning!Tiger in zone A");
}
else if(values=="f")
{
  Serial.print("fox");
  Blynk.logEvent("alert_msg","Warning!fox in zone A");
}
else if(values=="b")
{
  Serial.print("bear");
  Blynk.logEvent("alert_msg","Warning!bear in zone A");
}

}

