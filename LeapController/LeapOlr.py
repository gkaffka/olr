################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import Leap, sys, thread, time, serial, os, random
from time import sleep
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture, Finger

def play_sound():
    sound="sound{}".format(random.randint(1,7))
    os.system("mpg123 /home/kaffka/olr/LeapController/{}.mp3".format(sound))

class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']


    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Defines the conection with the arduino 
        ser = serial.Serial('/dev/ttyACM0', 9600) 
        # Get the most recent frame and report some basic information  
        frame = controller.frame()

        #print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
               #frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

        # Get hands
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"

            # print "  %s, id %d, position: %s" % (
            #     handType, hand.id, hand.palm_position)

            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
            # print "  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
            #     direction.pitch * Leap.RAD_TO_DEG,
            #     normal.roll * Leap.RAD_TO_DEG,
            #     direction.yaw * Leap.RAD_TO_DEG)

            # Get arm bone
            arm = hand.arm
            # print "  Arm direction: %s, wrist position: %s, elbow position: %s" % (
            #     arm.direction,
            #     arm.wrist_position,
            #     arm.elbow_position)

            # Get fingers
            indicador  = hand.fingers.finger_type(Finger.TYPE_INDEX)[0]
            mindinho  = hand.fingers.finger_type(Finger.TYPE_PINKY)[0]
            dedao  = hand.fingers.finger_type(Finger.TYPE_THUMB)[0]
            anelar  = hand.fingers.finger_type(Finger.TYPE_RING)[0]
            medio  = hand.fingers.finger_type(Finger.TYPE_MIDDLE)[0]

            ind_apontado = indicador.bone(3).direction.z > 0
            med_apontado = medio.bone(3).direction.z > 0
            ane_apontado = anelar.bone(3).direction.z > 0
            mind_apontado = mindinho.bone(3).direction.z > 0
            ded_apontado = dedao.bone(3).direction.y < 0

            if ind_apontado and not(med_apontado) and not(ane_apontado) and not(mind_apontado):
                print "Indicador"
                ser.write('I') 
                play_sound()
                sleep(2)
            elif med_apontado and ind_apontado and not(ane_apontado) and not(mind_apontado):
                print "Medio e Indicador"
                ser.write('M')
                play_sound() 
                sleep(2)
            elif ane_apontado and ind_apontado and med_apontado and not(mind_apontado):
                print "Medio, Indicador e Anelar"
                ser.write('A')
                play_sound() 
                sleep(2)
            elif ded_apontado and not(ind_apontado) and not(med_apontado) and not(ane_apontado) and not(mind_apontado):
                print "Dedao Ok"
                ser.write('D') 
                play_sound()
                sleep(2)
                
                         

        # Get tools
        for tool in frame.tools:

            print "  Tool id: %d, position: %s, direction: %s" % (
                tool.id, tool.tip_position, tool.direction)

        # Get gestures
        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                circle = CircleGesture(gesture)

                # Determine clock direction using the angle between the pointable and the circle normal
                if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
                    clockwiseness = "clockwise"
                else:
                    clockwiseness = "counterclockwise"

                # Calculate the angle swept since the last frame
                swept_angle = 0
                if circle.state != Leap.Gesture.STATE_START:
                    previous_update = CircleGesture(controller.frame(1).gesture(circle.id))
                    swept_angle =  (circle.progress - previous_update.progress) * 2 * Leap.PI

                print "  Circle id: %d, %s, progress: %f, radius: %f, angle: %f degrees, %s" % (
                        gesture.id, self.state_names[gesture.state],
                        circle.progress, circle.radius, swept_angle * Leap.RAD_TO_DEG, clockwiseness)

            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swipe = SwipeGesture(gesture)
                # print "  Swipe id: %d, state: %s, position: %s, direction: %s, speed: %f" % (
                #         gesture.id, self.state_names[gesture.state],
                #         swipe.position, swipe.direction, swipe.speed)    
                if hand.is_left:
                    ser.write('F') 
                    print "Swipe mao esquerda"
                    play_sound()           
                else:
                    ser.write('E') 
                    play_sound()   
                    print "Swipe mao direita"
                          

            if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                keytap = KeyTapGesture(gesture)
                print "  Key Tap id: %d, %s, position: %s, direction: %s" % (
                        gesture.id, self.state_names[gesture.state],
                        keytap.position, keytap.direction )

            if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
                screentap = ScreenTapGesture(gesture)
                print "  Screen Tap id: %d, %s, position: %s, direction: %s" % (
                        gesture.id, self.state_names[gesture.state],
                        screentap.position, screentap.direction )

        if not (frame.hands.is_empty and frame.gestures().is_empty):
            print ""

    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
