################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class GenerateTrainingSet(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    words_to_define = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    NUM_TRAINING_EXAMPLES = 20
    NUM_FRAME_GRABS = 10


    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def doTheThing(self, controller):
        writeFile = open("/Users/NickBowman/Desktop/trainingSet.txt", "w")
        for word in self.words_to_define:
            for i in xrange(0, self.NUM_TRAINING_EXAMPLES):
                print "Make gesture now"
                result = self.generateGesture(controller)
                writeFile.write(result + '\n')
                print "Gesture successfully recorded. Next one starts in three seconds."
                time.sleep(3)


    def generateGesture(self, controller):
        frames = []
        ans = ""
        for i in range(0, self.NUM_FRAME_GRABS):
            frameGrab = controller.frame()
            frames.append(frameGrab);
            print frameGrab
            time.sleep(0.1)
        previousFrame = None
        sumHands = 0
        sumFingers = 0
        sumTranlsationX = 0
        sumTranslationY = 0
        sumTranslationZ = 0
        rotationAxisX = 0
        rotationAxisY = 0
        rotationAxisZ = 0
        rotationAngle = 0

        hand1Type = 0
        hand1DirectionX = 0
        hand1DirectionY = 0
        hand1DirectionZ = 0
        hand1PalmPositionX = 0
        hand1PalmPositionY = 0
        hand1PalmPositionZ = 0
        hand1GrabStrength = 0
        hand1PinchStrength = 0
        hand1Confidence = 0
        hand1ArmDirectionX = 0
        hand1ArmDirectionY = 0
        hand1ArmDirectionZ = 0
        hand1ArmCenterX = 0
        hand1ArmCenterY = 0
        hand1ArmCenterZ = 0
        hand1ArmUpVectorX = 0
        hand1ArmUpVectorY = 0
        hand1ArmUpVectorZ = 0
        hand1TranslationX = 0
        hand1TranslationY = 0
        hand1TranslationZ = 0
        hand1RotationAxisX = 0
        hand1RotationAxisY = 0
        hand1RotationAxisZ = 0
        hand1RotationAngle = 0

        hand2Type = 0
        hand2DirectionX = 0
        hand2DirectionY = 0
        hand2DirectionZ = 0
        hand2PalmPositionX = 0
        hand2PalmPositionY = 0
        hand2PalmPositionZ = 0
        hand2GrabStrength = 0
        hand2PinchStrength = 0
        hand2Confidence = 0
        hand2ArmDirectionX = 0
        hand2ArmDirectionY = 0
        hand2ArmDirectionZ = 0
        hand2ArmCenterX = 0
        hand2ArmCenterY = 0
        hand2ArmCenterZ = 0
        hand2ArmUpVectorX = 0
        hand2ArmUpVectorY = 0
        hand2ArmUpVectorZ = 0
        hand2TranslationX = 0
        hand2TranslationY = 0
        hand2TranslationZ = 0
        hand2RotationAxisX = 0
        hand2RotationAxisY = 0
        hand2RotationAxisZ = 0
        hand2RotationAngle = 0

        hand1Finger1DirectionX = 0
        hand1Finger1DirectionX = 0
        hand1Finger1DirectionX = 0
        hand1Finger1Extended = 0
        hand1Finger1MetacarpalCenterX = 0
        hand1Finger1MetacarpalCenterY = 0 
        hand1Finger1MetacarpalCenterZ = 0
        hand1Finger1MetacarpalDirection: (0.6, 0.7, -0.5)
        Up vector: (-0.5, 0.7, 0.5)
        Center: (-29.6, 168.5, 78.4)
        Direction: (0.9, 0.3, -0.2)
        Up vector: (-0.2, 0.9, 0.5)
        Center: (7.5, 180.8, 68.8)
        Direction: (0.9, 0.2, -0.3)
        Up vector: (-0.1, 0.9, 0.4)
        Center: (33.3, 186.1, 60.7)
        Direction: (0.9, 0.1, -0.3)
        Up vector: (0.0, 0.9, 0.4)
        Tip position: (39.0, 186.7, 58.6) mm

        for frame in frames:
            sumHands += len(frame.hands)
            sumFingers += len(frame.fingers)
            if ( previousFrame and previousFrame.valid):
                translationVector = frame.translation(previousFrame)
                sumTranlsationX += translationVector[0]
                sumTranslationY += translationVector[1]
                sumTranslationZ += translationVector[2]
                rotationAxisVector = frame.rotation_axis(previousFrame)
                rotationAxisX += rotationAxisVector[0]
                rotationAxisY += rotationAxisVector[1]
                rotationAxisZ += rotationAxisVector[2]
                rotationAngle += frame.rotation_angle[previousFrame]
            if ( frame.hands[0] is not None):
                hand1 = frame.hands[0]
                if ( hand1.isLeft):
                    hand1Type += -1
                else:
                    hand1Type += 1
                hand1DirectionVector = hand1.direction
                hand1DirectionX += hand1DirectionVector[0]
                hand1DirectionY += hand1DirectionVector[1]
                hand1DirectionZ += hand1DirectionVector[2]
                hand1PalmPositionVector += hand1.palm_position
                hand1PalmPositionX += hand1PalmPositionVector[0]
                hand1PalmPositionY += hand1PalmPositionVector[1]
                hand1PalmPositionZ += hand1PalmPositionVector[2]
                hand1GrabStrength += hand1.grab_strength
                hand1PinchStrength += hand1.pinch_strength
                hand1Confidence += hand1.confidence
                hand1ArmDirectionVector
                hand1ArmDirectionX += 0
                hand1ArmDirectionY += 0
                hand1ArmDirectionZ += 0
                hand1ArmCenterX += 0
                hand1ArmCenterY += 0
                hand1ArmCenterZ += 0
                hand1ArmUpVectorX += 0
                hand1ArmUpVectorY += 0
                hand1ArmUpVectorZ += 0
                hand1TranslationX += 0
                hand1TranslationY += 0
                hand1TranslationZ += 0
                hand1RotationAxisX += 0
                hand1RotationAxisY += 0
                hand1RotationAxisZ += 0
                hand1RotationAngle += 0





        return ans

def main():
    # Create a sample listener and controller.
    listener = GenerateTrainingSet()
    controller = Leap.Controller()

    # Have a sample listener recieve events from the controller
    controller.add_listener(listener)
    listener.doTheThing(controller)

if __name__ == "__main__":
    main()
