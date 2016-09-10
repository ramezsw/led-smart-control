This is the Java fuzzy logic controller based on JFuzzyLogic framework and Fuzzy Control Language.

To run simply execute LEDControlDimmer.java, Java 8 is required for this to execute

The JFuzzyLogic Library must be installed to run, however it is added as a JAR file to the java project so the code should run as it is.

a .FCL code is included, it is the main fuzzy logic control code used within the project, it is accessed by LEDControlDimmer using the JfuzzyLogic API. The output of this system should be further processed by the linux server where the control output is sent to the LED hardware drivers to control the average dimming levels accross the LED lights that correspond to the driver.

This code connects to the mongoDB that contains the sensor values.
