from controller import Robot
from controller import Keyboard

robot = Robot()
kb = Keyboard()

# create unique identifier for each device
motorA = robot.getDevice("A motor")
motorB = robot.getDevice("B motor")
motorC = robot.getDevice("C motor")
motorD = robot.getDevice("D motor")
motorE = robot.getDevice("E motor")
motorF = robot.getDevice("F motor")


timestep = int(robot.getBasicTimeStep())
kb.enable(timestep)


motora_pos = 0
motorb_pos = 0
motorc_pos = 0
motord_pos = 0
motore_pos = 0
motorf_pos = 0

# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    key_pressed = kb.getKey()   
    print(key_pressed) 
    
    if(key_pressed == 49):
        motora_pos += 0.005
        
    if(key_pressed == 50):
        motora_pos -= 0.005
        
    if(key_pressed == 51):
        motorb_pos += 0.01
        
    if(key_pressed == 52):
        motorb_pos-=0.01
        
    if(key_pressed == 53):
        motorc_pos += 0.01
        
    if(key_pressed == 54):
        motorc_pos -= 0.01
        
    if(key_pressed == 55):
        motord_pos += 0.01
        
    if(key_pressed == 56):
        motord_pos -= 0.01
        
    if(key_pressed == 57):
        motore_pos += 0.01
    if(key_pressed == 48):
        motore_pos -= 0.01
         
    if(key_pressed == 81):
        motorf_pos += 0.01
        
    if(key_pressed == 87):
        motorf_pos -= 0.01
        
    motorA.setPosition(motora_pos)
    motorB.setPosition(motorb_pos)
    motorC.setPosition(motorc_pos)
    motorD.setPosition(motord_pos)
    motorE.setPosition(motore_pos)
    motorF.setPosition(motorf_pos)

    