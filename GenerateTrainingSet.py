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

        ## Hand 1 Finger 1 begins here ##
        hand1Finger1DirectionX = 0
        hand1Finger1DirectionX = 0
        hand1Finger1DirectionX = 0
        hand1Finger1Extended = 0
        # attributes of finger 1 metacarpals
        hand1Finger1MetacarpalCenterX = 0
        hand1Finger1MetacarpalCenterY = 0
        hand1Finger1MetacarpalCenterZ = 0
        hand1Finger1MetacarpalDirectionX = 0
        hand1Finger1MetacarpalDirectionY = 0
        hand1Finger1MetacarpalDirectionZ = 0
        hand1Finger1MetacarpalUpVectorX = 0
        hand1Finger1MetacarpalUpVectorY = 0
        hand1Finger1MetacarpalUpVectorZ = 0
        # attributes of finger 1 proximal phalanx bone
        hand1Finger1ProximalPhalanxBoneCenterX = 0
        hand1Finger1ProximalPhalanxBoneCenterY = 0
        hand1Finger1ProximalPhalanxBoneCenterZ = 0
        hand1Finger1ProximalPhalanxBoneDirectionX = 0
        hand1Finger1ProximalPhalanxBoneDirectionY = 0
        hand1Finger1ProximalPhalanxBoneDirectionZ = 0
        hand1Finger1ProximalPhalanxBoneUpVectorX = 0
        hand1Finger1ProximalPhalanxBoneUpVectorY = 0
        hand1Finger1ProximalPhalanxBoneUpVectorZ = 0
        # attributes of finger 1 intermediate phalanx bone
        hand1Finger1IntermediatePhalanxBoneCenterX = 0
        hand1Finger1IntermediatePhalanxBoneCenterY = 0
        hand1Finger1IntermediatePhalanxBoneCenterZ = 0
        hand1Finger1IntermediatePhalanxBoneDirectionX = 0
        hand1Finger1IntermediatePhalanxBoneDirectionY = 0
        hand1Finger1IntermediatePhalanxBoneDirectionZ = 0
        hand1Finger1IntermediatePhalanxBoneUpVectorX = 0
        hand1Finger1IntermediatePhalanxBoneUpVectorY = 0
        hand1Finger1IntermediatePhalanxBoneUpVectorZ = 0
        # attributes of finger 1 distal phalanx bone
        hand1Finger1DistalPhalanxBoneCenterX = 0
        hand1Finger1DistalPhalanxBoneCenterY = 0
        hand1Finger1DistalPhalanxBoneCenterZ = 0
        hand1Finger1DistalPhalanxBoneDirectionX = 0
        hand1Finger1DistalPhalanxBoneDirectionY = 0
        hand1Finger1DistalPhalanxBoneDirectionZ = 0
        hand1Finger1DistalPhalanxBoneUpVectorX = 0
        hand1Finger1DistalPhalanxBoneUpVectorY = 0
        hand1Finger1DistalPhalanxBoneUpVectorZ = 0
        hand1Finger1TipPositionX = 0
        hand1Finger1TipPositionY = 0
        hand1Finger1TipPositionZ = 0

        ## Hand 1 Finger 2 Begins Here ##

        hand1Finger2DirectionX = 0
        hand1Finger2DirectionX = 0
        hand1Finger2DirectionX = 0
        hand1Finger2Extended = 0
        # attributes of finger 2 metacarpals
        hand1Finger2MetacarpalCenterX = 0
        hand1Finger2MetacarpalCenterY = 0
        hand1Finger2MetacarpalCenterZ = 0
        hand1Finger2MetacarpalDirectionX = 0
        hand1Finger2MetacarpalDirectionY = 0
        hand1Finger2MetacarpalDirectionZ = 0
        hand1Finger2MetacarpalUpVectorX = 0
        hand1Finger2MetacarpalUpVectorY = 0
        hand1Finger2MetacarpalUpVectorZ = 0
        # attributes of finger 2 proximal phalanx bone
        hand1Finger2ProximalPhalanxBoneCenterX = 0
        hand1Finger2ProximalPhalanxBoneCenterY = 0
        hand1Finger2ProximalPhalanxBoneCenterZ = 0
        hand1Finger2ProximalPhalanxBoneDirectionX = 0
        hand1Finger2ProximalPhalanxBoneDirectionY = 0
        hand1Finger2ProximalPhalanxBoneDirectionZ = 0
        hand1Finger2ProximalPhalanxBoneUpVectorX = 0
        hand1Finger2ProximalPhalanxBoneUpVectorY = 0
        hand1Finger2ProximalPhalanxBoneUpVectorZ = 0
        # attributes of finger 2 intermediate phalanx bone
        hand1Finger2IntermediatePhalanxBoneCenterX = 0
        hand1Finger2IntermediatePhalanxBoneCenterY = 0
        hand1Finger2IntermediatePhalanxBoneCenterZ = 0
        hand1Finger2IntermediatePhalanxBoneDirectionX = 0
        hand1Finger2IntermediatePhalanxBoneDirectionY = 0
        hand1Finger2IntermediatePhalanxBoneDirectionZ = 0
        hand1Finger2IntermediatePhalanxBoneUpVectorX = 0
        hand1Finger2IntermediatePhalanxBoneUpVectorY = 0
        hand1Finger2IntermediatePhalanxBoneUpVectorZ = 0
        # attributes of finger 2 distal phalanx bone
        hand1Finger2DistalPhalanxBoneCenterX = 0
        hand1Finger2DistalPhalanxBoneCenterY = 0
        hand1Finger2DistalPhalanxBoneCenterZ = 0
        hand1Finger2DistalPhalanxBoneDirectionX = 0
        hand1Finger2DistalPhalanxBoneDirectionY = 0
        hand1Finger2DistalPhalanxBoneDirectionZ = 0
        hand1Finger2DistalPhalanxBoneUpVectorX = 0
        hand1Finger2DistalPhalanxBoneUpVectorY = 0
        hand1Finger2DistalPhalanxBoneUpVectorZ = 0
        hand1Finger2TipPositionX = 0
        hand1Finger2TipPositionY = 0
        hand1Finger2TipPositionZ = 0

        ## Hand 1 Finger 3 Begins Here ##

        hand1Finger3DirectionX = 0
        hand1Finger3DirectionX = 0
        hand1Finger3DirectionX = 0
        hand1Finger3Extended = 0
        # attributes of Finger 3 metacarpals
        hand1Finger3MetacarpalCenterX = 0
        hand1Finger3MetacarpalCenterY = 0
        hand1Finger3MetacarpalCenterZ = 0
        hand1Finger3MetacarpalDirectionX = 0
        hand1Finger3MetacarpalDirectionY = 0
        hand1Finger3MetacarpalDirectionZ = 0
        hand1Finger3MetacarpalUpVectorX = 0
        hand1Finger3MetacarpalUpVectorY = 0
        hand1Finger3MetacarpalUpVectorZ = 0
        # attributes of Finger 3 proximal phalanx bone
        hand1Finger3ProximalPhalanxBoneCenterX = 0
        hand1Finger3ProximalPhalanxBoneCenterY = 0
        hand1Finger3ProximalPhalanxBoneCenterZ = 0
        hand1Finger3ProximalPhalanxBoneDirectionX = 0
        hand1Finger3ProximalPhalanxBoneDirectionY = 0
        hand1Finger3ProximalPhalanxBoneDirectionZ = 0
        hand1Finger3ProximalPhalanxBoneUpVectorX = 0
        hand1Finger3ProximalPhalanxBoneUpVectorY = 0
        hand1Finger3ProximalPhalanxBoneUpVectorZ = 0
        # attributes of Finger 3 intermediate phalanx bone
        hand1Finger3IntermediatePhalanxBoneCenterX = 0
        hand1Finger3IntermediatePhalanxBoneCenterY = 0
        hand1Finger3IntermediatePhalanxBoneCenterZ = 0
        hand1Finger3IntermediatePhalanxBoneDirectionX = 0
        hand1Finger3IntermediatePhalanxBoneDirectionY = 0
        hand1Finger3IntermediatePhalanxBoneDirectionZ = 0
        hand1Finger3IntermediatePhalanxBoneUpVectorX = 0
        hand1Finger3IntermediatePhalanxBoneUpVectorY = 0
        hand1Finger3IntermediatePhalanxBoneUpVectorZ = 0
        # attributes of Finger 3 distal phalanx bone
        hand1Finger3DistalPhalanxBoneCenterX = 0
        hand1Finger3DistalPhalanxBoneCenterY = 0
        hand1Finger3DistalPhalanxBoneCenterZ = 0
        hand1Finger3DistalPhalanxBoneDirectionX = 0
        hand1Finger3DistalPhalanxBoneDirectionY = 0
        hand1Finger3DistalPhalanxBoneDirectionZ = 0
        hand1Finger3DistalPhalanxBoneUpVectorX = 0
        hand1Finger3DistalPhalanxBoneUpVectorY = 0
        hand1Finger3DistalPhalanxBoneUpVectorZ = 0
        hand1Finger3TipPositionX = 0
        hand1Finger3TipPositionY = 0
        hand1Finger3TipPositionZ = 0

        ## Hand 1 Finger 4 Begins Here ##

        hand1Finger4DirectionX = 0
        hand1Finger4DirectionX = 0
        hand1Finger4DirectionX = 0
        hand1Finger4Extended = 0
        # attributes of Finger 4 metacarpals
        hand1Finger4MetacarpalCenterX = 0
        hand1Finger4MetacarpalCenterY = 0
        hand1Finger4MetacarpalCenterZ = 0
        hand1Finger4MetacarpalDirectionX = 0
        hand1Finger4MetacarpalDirectionY = 0
        hand1Finger4MetacarpalDirectionZ = 0
        hand1Finger4MetacarpalUpVectorX = 0
        hand1Finger4MetacarpalUpVectorY = 0
        hand1Finger4MetacarpalUpVectorZ = 0
        # attributes of Finger 4 proximal phalanx bone
        hand1Finger4ProximalPhalanxBoneCenterX = 0
        hand1Finger4ProximalPhalanxBoneCenterY = 0
        hand1Finger4ProximalPhalanxBoneCenterZ = 0
        hand1Finger4ProximalPhalanxBoneDirectionX = 0
        hand1Finger4ProximalPhalanxBoneDirectionY = 0
        hand1Finger4ProximalPhalanxBoneDirectionZ = 0
        hand1Finger4ProximalPhalanxBoneUpVectorX = 0
        hand1Finger4ProximalPhalanxBoneUpVectorY = 0
        hand1Finger4ProximalPhalanxBoneUpVectorZ = 0
        # attributes of Finger 4 intermediate phalanx bone
        hand1Finger4IntermediatePhalanxBoneCenterX = 0
        hand1Finger4IntermediatePhalanxBoneCenterY = 0
        hand1Finger4IntermediatePhalanxBoneCenterZ = 0
        hand1Finger4IntermediatePhalanxBoneDirectionX = 0
        hand1Finger4IntermediatePhalanxBoneDirectionY = 0
        hand1Finger4IntermediatePhalanxBoneDirectionZ = 0
        hand1Finger4IntermediatePhalanxBoneUpVectorX = 0
        hand1Finger4IntermediatePhalanxBoneUpVectorY = 0
        hand1Finger4IntermediatePhalanxBoneUpVectorZ = 0
        # attributes of Finger 4 distal phalanx bone
        hand1Finger4DistalPhalanxBoneCenterX = 0
        hand1Finger4DistalPhalanxBoneCenterY = 0
        hand1Finger4DistalPhalanxBoneCenterZ = 0
        hand1Finger4DistalPhalanxBoneDirectionX = 0
        hand1Finger4DistalPhalanxBoneDirectionY = 0
        hand1Finger4DistalPhalanxBoneDirectionZ = 0
        hand1Finger4DistalPhalanxBoneUpVectorX = 0
        hand1Finger4DistalPhalanxBoneUpVectorY = 0
        hand1Finger4DistalPhalanxBoneUpVectorZ = 0
        hand1Finger4TipPositionX = 0
        hand1Finger4TipPositionY = 0
        hand1Finger4TipPositionZ = 0

        ## Hand 1 Finger 5 Begins Here ##

        hand1Finger5DirectionX = 0
        hand1Finger5DirectionX = 0
        hand1Finger5DirectionX = 0
        hand1Finger5Extended = 0
        # attributes of Finger 5 metacarpals
        hand1Finger5MetacarpalCenterX = 0
        hand1Finger5MetacarpalCenterY = 0
        hand1Finger5MetacarpalCenterZ = 0
        hand1Finger5MetacarpalDirectionX = 0
        hand1Finger5MetacarpalDirectionY = 0
        hand1Finger5MetacarpalDirectionZ = 0
        hand1Finger5MetacarpalUpVectorX = 0
        hand1Finger5MetacarpalUpVectorY = 0
        hand1Finger5MetacarpalUpVectorZ = 0
        # attributes of Finger 5 proximal phalanx bone
        hand1Finger5ProximalPhalanxBoneCenterX = 0
        hand1Finger5ProximalPhalanxBoneCenterY = 0
        hand1Finger5ProximalPhalanxBoneCenterZ = 0
        hand1Finger5ProximalPhalanxBoneDirectionX = 0
        hand1Finger5ProximalPhalanxBoneDirectionY = 0
        hand1Finger5ProximalPhalanxBoneDirectionZ = 0
        hand1Finger5ProximalPhalanxBoneUpVectorX = 0
        hand1Finger5ProximalPhalanxBoneUpVectorY = 0
        hand1Finger5ProximalPhalanxBoneUpVectorZ = 0
        # attributes of Finger 5 intermediate phalanx bone
        hand1Finger5IntermediatePhalanxBoneCenterX = 0
        hand1Finger5IntermediatePhalanxBoneCenterY = 0
        hand1Finger5IntermediatePhalanxBoneCenterZ = 0
        hand1Finger5IntermediatePhalanxBoneDirectionX = 0
        hand1Finger5IntermediatePhalanxBoneDirectionY = 0
        hand1Finger5IntermediatePhalanxBoneDirectionZ = 0
        hand1Finger5IntermediatePhalanxBoneUpVectorX = 0
        hand1Finger5IntermediatePhalanxBoneUpVectorY = 0
        hand1Finger5IntermediatePhalanxBoneUpVectorZ = 0
        # attributes of Finger 5 distal phalanx bone
        hand1Finger5DistalPhalanxBoneCenterX = 0
        hand1Finger5DistalPhalanxBoneCenterY = 0
        hand1Finger5DistalPhalanxBoneCenterZ = 0
        hand1Finger5DistalPhalanxBoneDirectionX = 0
        hand1Finger5DistalPhalanxBoneDirectionY = 0
        hand1Finger5DistalPhalanxBoneDirectionZ = 0
        hand1Finger5DistalPhalanxBoneUpVectorX = 0
        hand1Finger5DistalPhalanxBoneUpVectorY = 0
        hand1Finger5DistalPhalanxBoneUpVectorZ = 0
        hand1Finger5TipPositionX = 0
        hand1Finger5TipPositionY = 0
        hand1Finger5TipPositionZ = 0

        ## Hand 2 Finger 1 begins here ##
        hand2Finger1DirectionX = 0
        hand2Finger1DirectionX = 0
        hand2Finger1DirectionX = 0
        hand2Finger1Extended = 0
        # attributes of finger 1 metacarpals
        hand2Finger1MetacarpalCenterX = 0
        hand2Finger1MetacarpalCenterY = 0
        hand2Finger1MetacarpalCenterZ = 0
        hand2Finger1MetacarpalDirectionX = 0
        hand2Finger1MetacarpalDirectionY = 0
        hand2Finger1MetacarpalDirectionZ = 0
        hand2Finger1MetacarpalUpVectorX = 0
        hand2Finger1MetacarpalUpVectorY = 0
        hand2Finger1MetacarpalUpVectorZ = 0
        # attributes of finger 1 proximal phalanx bone
        hand2Finger1ProximalPhalanxBoneCenterX = 0
        hand2Finger1ProximalPhalanxBoneCenterY = 0
        hand2Finger1ProximalPhalanxBoneCenterZ = 0
        hand2Finger1ProximalPhalanxBoneDirectionX = 0
        hand2Finger1ProximalPhalanxBoneDirectionY = 0
        hand2Finger1ProximalPhalanxBoneDirectionZ = 0
        hand2Finger1ProximalPhalanxBoneUpVectorX = 0
        hand2Finger1ProximalPhalanxBoneUpVectorY = 0
        hand2Finger1ProximalPhalanxBoneUpVectorZ = 0
        # attributes of finger 1 intermediate phalanx bone
        hand2Finger1IntermediatePhalanxBoneCenterX = 0
        hand2Finger1IntermediatePhalanxBoneCenterY = 0
        hand2Finger1IntermediatePhalanxBoneCenterZ = 0
        hand2Finger1IntermediatePhalanxBoneDirectionX = 0
        hand2Finger1IntermediatePhalanxBoneDirectionY = 0
        hand2Finger1IntermediatePhalanxBoneDirectionZ = 0
        hand2Finger1IntermediatePhalanxBoneUpVectorX = 0
        hand2Finger1IntermediatePhalanxBoneUpVectorY = 0
        hand2Finger1IntermediatePhalanxBoneUpVectorZ = 0
        # attributes of finger 1 distal phalanx bone
        hand2Finger1DistalPhalanxBoneCenterX = 0
        hand2Finger1DistalPhalanxBoneCenterY = 0
        hand2Finger1DistalPhalanxBoneCenterZ = 0
        hand2Finger1DistalPhalanxBoneDirectionX = 0
        hand2Finger1DistalPhalanxBoneDirectionY = 0
        hand2Finger1DistalPhalanxBoneDirectionZ = 0
        hand2Finger1DistalPhalanxBoneUpVectorX = 0
        hand2Finger1DistalPhalanxBoneUpVectorY = 0
        hand2Finger1DistalPhalanxBoneUpVectorZ = 0
        hand2Finger1TipPositionX = 0
        hand2Finger1TipPositionY = 0
        hand2Finger1TipPositionZ = 0

        ## Hand 2 Finger 2 Begins Here ##

        hand2Finger2DirectionX = 0
        hand2Finger2DirectionX = 0
        hand2Finger2DirectionX = 0
        hand2Finger2Extended = 0
        # attributes of finger 2 metacarpals
        hand2Finger2MetacarpalCenterX = 0
        hand2Finger2MetacarpalCenterY = 0
        hand2Finger2MetacarpalCenterZ = 0
        hand2Finger2MetacarpalDirectionX = 0
        hand2Finger2MetacarpalDirectionY = 0
        hand2Finger2MetacarpalDirectionZ = 0
        hand2Finger2MetacarpalUpVectorX = 0
        hand2Finger2MetacarpalUpVectorY = 0
        hand2Finger2MetacarpalUpVectorZ = 0
        # attributes of finger 2 proximal phalanx bone
        hand2Finger2ProximalPhalanxBoneCenterX = 0
        hand2Finger2ProximalPhalanxBoneCenterY = 0
        hand2Finger2ProximalPhalanxBoneCenterZ = 0
        hand2Finger2ProximalPhalanxBoneDirectionX = 0
        hand2Finger2ProximalPhalanxBoneDirectionY = 0
        hand2Finger2ProximalPhalanxBoneDirectionZ = 0
        hand2Finger2ProximalPhalanxBoneUpVectorX = 0
        hand2Finger2ProximalPhalanxBoneUpVectorY = 0
        hand2Finger2ProximalPhalanxBoneUpVectorZ = 0
        # attributes of finger 2 intermediate phalanx bone
        hand2Finger2IntermediatePhalanxBoneCenterX = 0
        hand2Finger2IntermediatePhalanxBoneCenterY = 0
        hand2Finger2IntermediatePhalanxBoneCenterZ = 0
        hand2Finger2IntermediatePhalanxBoneDirectionX = 0
        hand2Finger2IntermediatePhalanxBoneDirectionY = 0
        hand2Finger2IntermediatePhalanxBoneDirectionZ = 0
        hand2Finger2IntermediatePhalanxBoneUpVectorX = 0
        hand2Finger2IntermediatePhalanxBoneUpVectorY = 0
        hand2Finger2IntermediatePhalanxBoneUpVectorZ = 0
        # attributes of finger 2 distal phalanx bone
        hand2Finger2DistalPhalanxBoneCenterX = 0
        hand2Finger2DistalPhalanxBoneCenterY = 0
        hand2Finger2DistalPhalanxBoneCenterZ = 0
        hand2Finger2DistalPhalanxBoneDirectionX = 0
        hand2Finger2DistalPhalanxBoneDirectionY = 0
        hand2Finger2DistalPhalanxBoneDirectionZ = 0
        hand2Finger2DistalPhalanxBoneUpVectorX = 0
        hand2Finger2DistalPhalanxBoneUpVectorY = 0
        hand2Finger2DistalPhalanxBoneUpVectorZ = 0
        hand2Finger2TipPositionX = 0
        hand2Finger2TipPositionY = 0
        hand2Finger2TipPositionZ = 0

        ## Hand 2 Finger 3 Begins Here ##

        hand2Finger3DirectionX = 0
        hand2Finger3DirectionX = 0
        hand2Finger3DirectionX = 0
        hand2Finger3Extended = 0
        # attributes of Finger 3 metacarpals
        hand2Finger3MetacarpalCenterX = 0
        hand2Finger3MetacarpalCenterY = 0
        hand2Finger3MetacarpalCenterZ = 0
        hand2Finger3MetacarpalDirectionX = 0
        hand2Finger3MetacarpalDirectionY = 0
        hand2Finger3MetacarpalDirectionZ = 0
        hand2Finger3MetacarpalUpVectorX = 0
        hand2Finger3MetacarpalUpVectorY = 0
        hand2Finger3MetacarpalUpVectorZ = 0
        # attributes of Finger 3 proximal phalanx bone
        hand2Finger3ProximalPhalanxBoneCenterX = 0
        hand2Finger3ProximalPhalanxBoneCenterY = 0
        hand2Finger3ProximalPhalanxBoneCenterZ = 0
        hand2Finger3ProximalPhalanxBoneDirectionX = 0
        hand2Finger3ProximalPhalanxBoneDirectionY = 0
        hand2Finger3ProximalPhalanxBoneDirectionZ = 0
        hand2Finger3ProximalPhalanxBoneUpVectorX = 0
        hand2Finger3ProximalPhalanxBoneUpVectorY = 0
        hand2Finger3ProximalPhalanxBoneUpVectorZ = 0
        # attributes of Finger 3 intermediate phalanx bone
        hand2Finger3IntermediatePhalanxBoneCenterX = 0
        hand2Finger3IntermediatePhalanxBoneCenterY = 0
        hand2Finger3IntermediatePhalanxBoneCenterZ = 0
        hand2Finger3IntermediatePhalanxBoneDirectionX = 0
        hand2Finger3IntermediatePhalanxBoneDirectionY = 0
        hand2Finger3IntermediatePhalanxBoneDirectionZ = 0
        hand2Finger3IntermediatePhalanxBoneUpVectorX = 0
        hand2Finger3IntermediatePhalanxBoneUpVectorY = 0
        hand2Finger3IntermediatePhalanxBoneUpVectorZ = 0
        # attributes of Finger 3 distal phalanx bone
        hand2Finger3DistalPhalanxBoneCenterX = 0
        hand2Finger3DistalPhalanxBoneCenterY = 0
        hand2Finger3DistalPhalanxBoneCenterZ = 0
        hand2Finger3DistalPhalanxBoneDirectionX = 0
        hand2Finger3DistalPhalanxBoneDirectionY = 0
        hand2Finger3DistalPhalanxBoneDirectionZ = 0
        hand2Finger3DistalPhalanxBoneUpVectorX = 0
        hand2Finger3DistalPhalanxBoneUpVectorY = 0
        hand2Finger3DistalPhalanxBoneUpVectorZ = 0
        hand2Finger3TipPositionX = 0
        hand2Finger3TipPositionY = 0
        hand2Finger3TipPositionZ = 0

        ## Hand 2 Finger 4 Begins Here ##

        hand2Finger4DirectionX = 0
        hand2Finger4DirectionX = 0
        hand2Finger4DirectionX = 0
        hand2Finger4Extended = 0
        # attributes of Finger 4 metacarpals
        hand2Finger4MetacarpalCenterX = 0
        hand2Finger4MetacarpalCenterY = 0
        hand2Finger4MetacarpalCenterZ = 0
        hand2Finger4MetacarpalDirectionX = 0
        hand2Finger4MetacarpalDirectionY = 0
        hand2Finger4MetacarpalDirectionZ = 0
        hand2Finger4MetacarpalUpVectorX = 0
        hand2Finger4MetacarpalUpVectorY = 0
        hand2Finger4MetacarpalUpVectorZ = 0
        # attributes of Finger 4 proximal phalanx bone
        hand2Finger4ProximalPhalanxBoneCenterX = 0
        hand2Finger4ProximalPhalanxBoneCenterY = 0
        hand2Finger4ProximalPhalanxBoneCenterZ = 0
        hand2Finger4ProximalPhalanxBoneDirectionX = 0
        hand2Finger4ProximalPhalanxBoneDirectionY = 0
        hand2Finger4ProximalPhalanxBoneDirectionZ = 0
        hand2Finger4ProximalPhalanxBoneUpVectorX = 0
        hand2Finger4ProximalPhalanxBoneUpVectorY = 0
        hand2Finger4ProximalPhalanxBoneUpVectorZ = 0
        # attributes of Finger 4 intermediate phalanx bone
        hand2Finger4IntermediatePhalanxBoneCenterX = 0
        hand2Finger4IntermediatePhalanxBoneCenterY = 0
        hand2Finger4IntermediatePhalanxBoneCenterZ = 0
        hand2Finger4IntermediatePhalanxBoneDirectionX = 0
        hand2Finger4IntermediatePhalanxBoneDirectionY = 0
        hand2Finger4IntermediatePhalanxBoneDirectionZ = 0
        hand2Finger4IntermediatePhalanxBoneUpVectorX = 0
        hand2Finger4IntermediatePhalanxBoneUpVectorY = 0
        hand2Finger4IntermediatePhalanxBoneUpVectorZ = 0
        # attributes of Finger 4 distal phalanx bone
        hand2Finger4DistalPhalanxBoneCenterX = 0
        hand2Finger4DistalPhalanxBoneCenterY = 0
        hand2Finger4DistalPhalanxBoneCenterZ = 0
        hand2Finger4DistalPhalanxBoneDirectionX = 0
        hand2Finger4DistalPhalanxBoneDirectionY = 0
        hand2Finger4DistalPhalanxBoneDirectionZ = 0
        hand2Finger4DistalPhalanxBoneUpVectorX = 0
        hand2Finger4DistalPhalanxBoneUpVectorY = 0
        hand2Finger4DistalPhalanxBoneUpVectorZ = 0
        hand2Finger4TipPositionX = 0
        hand2Finger4TipPositionY = 0
        hand2Finger4TipPositionZ = 0

        ## Hand 2 Finger 5 Begins Here ##

        hand2Finger5DirectionX = 0
        hand2Finger5DirectionX = 0
        hand2Finger5DirectionX = 0
        hand2Finger5Extended = 0
        # attributes of Finger 5 metacarpals
        hand2Finger5MetacarpalCenterX = 0
        hand2Finger5MetacarpalCenterY = 0
        hand2Finger5MetacarpalCenterZ = 0
        hand2Finger5MetacarpalDirectionX = 0
        hand2Finger5MetacarpalDirectionY = 0
        hand2Finger5MetacarpalDirectionZ = 0
        hand2Finger5MetacarpalUpVectorX = 0
        hand2Finger5MetacarpalUpVectorY = 0
        hand2Finger5MetacarpalUpVectorZ = 0
        # attributes of Finger 5 proximal phalanx bone
        hand2Finger5ProximalPhalanxBoneCenterX = 0
        hand2Finger5ProximalPhalanxBoneCenterY = 0
        hand2Finger5ProximalPhalanxBoneCenterZ = 0
        hand2Finger5ProximalPhalanxBoneDirectionX = 0
        hand2Finger5ProximalPhalanxBoneDirectionY = 0
        hand2Finger5ProximalPhalanxBoneDirectionZ = 0
        hand2Finger5ProximalPhalanxBoneUpVectorX = 0
        hand2Finger5ProximalPhalanxBoneUpVectorY = 0
        hand2Finger5ProximalPhalanxBoneUpVectorZ = 0
        # attributes of Finger 5 intermediate phalanx bone
        hand2Finger5IntermediatePhalanxBoneCenterX = 0
        hand2Finger5IntermediatePhalanxBoneCenterY = 0
        hand2Finger5IntermediatePhalanxBoneCenterZ = 0
        hand2Finger5IntermediatePhalanxBoneDirectionX = 0
        hand2Finger5IntermediatePhalanxBoneDirectionY = 0
        hand2Finger5IntermediatePhalanxBoneDirectionZ = 0
        hand2Finger5IntermediatePhalanxBoneUpVectorX = 0
        hand2Finger5IntermediatePhalanxBoneUpVectorY = 0
        hand2Finger5IntermediatePhalanxBoneUpVectorZ = 0
        # attributes of Finger 5 distal phalanx bone
        hand2Finger5DistalPhalanxBoneCenterX = 0
        hand2Finger5DistalPhalanxBoneCenterY = 0
        hand2Finger5DistalPhalanxBoneCenterZ = 0
        hand2Finger5DistalPhalanxBoneDirectionX = 0
        hand2Finger5DistalPhalanxBoneDirectionY = 0
        hand2Finger5DistalPhalanxBoneDirectionZ = 0
        hand2Finger5DistalPhalanxBoneUpVectorX = 0
        hand2Finger5DistalPhalanxBoneUpVectorY = 0
        hand2Finger5DistalPhalanxBoneUpVectorZ = 0
        hand2Finger5TipPositionX = 0
        hand2Finger5TipPositionY = 0
        hand2Finger5TipPositionZ = 0

        # populate hand data
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
                hand1ArmDirectionVector = hand1.arm.direction
                hand1ArmDirectionX += hand1ArmDirectionVector[0]
                hand1ArmDirectionY += hand1ArmDirectionVector[1]
                hand1ArmDirectionZ += hand1ArmDirectionVector[2]
                hand1ArmCenterVector = hand1.arm.elbow_position + (hand1.arm.wrist_position - hand1.arm.elbow_position) * .05
                hand1ArmCenterX += hand1ArmCenterVector[0]
                hand1ArmCenterY += hand1ArmCenterVector[1]
                hand1ArmCenterZ += hand1ArmCenterVector[2]
                hand1ArmUpVector = hand1.arm.basis[1]
                hand1ArmUpVectorX += hand1ArmUpVector[0]
                hand1ArmUpVectorY += hand1ArmUpVector[1]
                hand1ArmUpVectorZ += hand1ArmUpVector[2]
                if ( previousFrame and previousFrame.valid):
                    hand1TranslationVector = hand1.translation(previousFrame)
                    hand1TranslationX += hand1TranslationVector[0]
                    hand1TranslationY += hand1TranslationVector[1]
                    hand1TranslationZ += hand1TranslationVector[2]
                    hand1RotationAxisVector = hand1.rotationAxis(previousFrame)
                    hand1RotationAxisX += hand1RotationAxisVector[0]
                    hand1RotationAxisY += hand1RotationAxisVector[1]
                    hand1RotationAxisZ += hand1RotationAxisVector[2]
                    hand1RotationAngle += hand1.rotationAngle(previousFrame)
            if ( frame.hands[1] is not None):
                hand2 = frame.hands[1]
                if ( hand2.isLeft):
                    hand2Type += -1
                else:
                    hand2Type += 1
                hand2DirectionVector = hand2.direction
                hand2DirectionX += hand2DirectionVector[0]
                hand2DirectionY += hand2DirectionVector[1]
                hand2DirectionZ += hand2DirectionVector[2]
                hand2PalmPositionVector += hand2.palm_position
                hand2PalmPositionX += hand2PalmPositionVector[0]
                hand2PalmPositionY += hand2PalmPositionVector[1]
                hand2PalmPositionZ += hand2PalmPositionVector[2]
                hand2GrabStrength += hand2.grab_strength
                hand2PinchStrength += hand2.pinch_strength
                hand2Confidence += hand2.confidence
                hand2ArmDirectionVector = hand2.arm.direction
                hand2ArmDirectionX += hand2ArmDirectionVector[0]
                hand2ArmDirectionY += hand2ArmDirectionVector[1]
                hand2ArmDirectionZ += hand2ArmDirectionVector[2]
                hand2ArmCenterVector = hand2.arm.elbow_position + (hand2.arm.wrist_position - hand2.arm.elbow_position) * .05
                hand2ArmCenterX += hand2ArmCenterVector[0]
                hand2ArmCenterY += hand2ArmCenterVector[1]
                hand2ArmCenterZ += hand2ArmCenterVector[2]
                hand2ArmUpVector = hand2.arm.basis[1]
                hand2ArmUpVectorX += hand2ArmUpVector[0]
                hand2ArmUpVectorY += hand2ArmUpVector[1]
                hand2ArmUpVectorZ += hand2ArmUpVector[2]
                if ( previousFrame and previousFrame.valid):
                    hand2TranslationVector = hand2.translation(previousFrame)
                    hand2TranslationX += hand2TranslationVector[0]
                    hand2TranslationY += hand2TranslationVector[1]
                    hand2TranslationZ += hand2TranslationVector[2]
                    hand2RotationAxisVector = hand2.rotationAxis(previousFrame)
                    hand2RotationAxisX += hand2RotationAxisVector[0]
                    hand2RotationAxisY += hand2RotationAxisVector[1]
                    hand2RotationAxisZ += hand2RotationAxisVector[2]
                    hand2RotationAngle += hand2.rotationAngle(previousFrame)




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
