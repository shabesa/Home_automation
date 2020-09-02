

String command;

// track motors


void setup(){

    // Begining serial communication 
    Serial.begin(9600);


    // Setting the cutter pins
    pinMode(13, OUTPUT);
 

}

void loop(){
    
    // Getting the command
    while(Serial.available() == 0);
    command = Serial.readString();

    // Executing command

    // Starting to cut the waste
    if(command == "on"){
        digitalWrite(13, HIGH);
    }

    // Stopping the roller
    else if(command == "off"){     
        digitalWrite(13, LOW);
    }

    
    // Final error capturing 
    else{
        Serial.println("invalid");
    }

}
