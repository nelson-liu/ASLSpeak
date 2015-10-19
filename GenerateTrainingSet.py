################################################################################
# Written by Nicholas Bowman and Nelson Liu                                    #
# DubHacks 2015                                                                #
# Last modified 10/18/15                                                       #
# This class aids a user in creating custom training data for sign language    #
# translation with the Leap Motion controller.                                 #
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
        writeFile = open("/Users/NickBowman/Desktop/trainingSet.csv", "w")
        for word in self.words_to_define:
            for i in xrange(0, self.NUM_TRAINING_EXAMPLES):
                print "Make gesture now for %s" % word
                time.sleep(1)
                result = self.captureGesture(controller)
                writeFile.write(word + ',' + result + '\n')
                print "Gesture successfully recorded. That was time #%d Next one starts on enter..." % (i+1)
                raw_input("Press Enter to continue...")


    def captureGesture(self, controller):
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
        hand1Finger1DirectionY = 0
        hand1Finger1DirectionZ = 0
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
        hand1Finger2DirectionY = 0
        hand1Finger2DirectionZ = 0
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
        hand1Finger3DirectionY = 0
        hand1Finger3DirectionZ = 0
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
        hand1Finger4DirectionY = 0
        hand1Finger4DirectionZ = 0
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
        hand1Finger5DirectionY = 0
        hand1Finger5DirectionZ = 0
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
        hand2Finger1DirectionY = 0
        hand2Finger1DirectionZ = 0
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
        hand2Finger2DirectionY = 0
        hand2Finger2DirectionZ = 0
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
        hand2Finger3DirectionY = 0
        hand2Finger3DirectionZ = 0
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
        hand2Finger4DirectionY = 0
        hand2Finger4DirectionZ = 0
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
        hand2Finger5DirectionY = 0
        hand2Finger5DirectionZ = 0
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
            if ( previousFrame and previousFrame.is_valid):
                translationVector = frame.translation(previousFrame)
                sumTranlsationX += translationVector[0]
                sumTranslationY += translationVector[1]
                sumTranslationZ += translationVector[2]
                rotationAxisVector = frame.rotation_axis(previousFrame)
                rotationAxisX += rotationAxisVector[0]
                rotationAxisY += rotationAxisVector[1]
                rotationAxisZ += rotationAxisVector[2]
                rotationAngle += frame.rotation_angle(previousFrame)
            if ( frame.hands[0] is not None):
                hand1 = frame.hands[0]
                #if ( hand1.isLeft):
                 #   hand1Type += -1
                #else:
                 #   hand1Type += 1
                hand1DirectionVector = hand1.direction
                hand1DirectionX += hand1DirectionVector[0]
                hand1DirectionY += hand1DirectionVector[1]
                hand1DirectionZ += hand1DirectionVector[2]
                hand1PalmPositionVector = hand1.palm_position
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
                if ( previousFrame and previousFrame.is_valid):
                    hand1TranslationVector = hand1.translation(previousFrame)
                    hand1TranslationX += hand1TranslationVector[0]
                    hand1TranslationY += hand1TranslationVector[1]
                    hand1TranslationZ += hand1TranslationVector[2]
                    hand1RotationAxisVector = hand1.rotation_axis(previousFrame)
                    hand1RotationAxisX += hand1RotationAxisVector[0]
                    hand1RotationAxisY += hand1RotationAxisVector[1]
                    hand1RotationAxisZ += hand1RotationAxisVector[2]
                    hand1RotationAngle += hand1.rotation_angle(previousFrame)
                if(frame.hands[0].fingers[0] is not None):
                    ## Set Hand 1 Finger 1 ##
                    hand1Finger1 = frame.hands[0].fingers[0]
                    hand1Finger1DirectionVector = hand1Finger1.direction
                    hand1Finger1DirectionX += hand1Finger1DirectionVector[0]
                    hand1Finger1DirectionY += hand1Finger1DirectionVector[1]
                    hand1Finger1DirectionZ += hand1Finger1DirectionVector[2]
                    # attributes of finger 1 metacarpals
                    hand1Finger1MetacarpalCenter = hand1Finger1.bone(0).center
                    hand1Finger1MetacarpalCenterX += hand1Finger1MetacarpalCenter[0]
                    hand1Finger1MetacarpalCenterY += hand1Finger1MetacarpalCenter[1]
                    hand1Finger1MetacarpalCenterZ += hand1Finger1MetacarpalCenter[2]
                    hand1Finger1MetacarpalDirection = hand1Finger1.bone(0).direction
                    hand1Finger1MetacarpalDirectionX += hand1Finger1MetacarpalDirection[0]
                    hand1Finger1MetacarpalDirectionY += hand1Finger1MetacarpalDirection[1]
                    hand1Finger1MetacarpalDirectionZ += hand1Finger1MetacarpalDirection[2]
                    # attributes of finger 1 proximal phalanx bone
                    hand1Finger1ProximalPhalanxBoneCenter = hand1Finger1.bone(1).center
                    hand1Finger1ProximalPhalanxBoneCenterX += hand1Finger1ProximalPhalanxBoneCenter[0]
                    hand1Finger1ProximalPhalanxBoneCenterY += hand1Finger1ProximalPhalanxBoneCenter[1]
                    hand1Finger1ProximalPhalanxBoneCenterZ += hand1Finger1ProximalPhalanxBoneCenter[2]
                    hand1Finger1ProximalPhalanxBoneDirection = hand1Finger1.bone(1).direction
                    hand1Finger1ProximalPhalanxBoneDirectionX += hand1Finger1ProximalPhalanxBoneDirection[0]
                    hand1Finger1ProximalPhalanxBoneDirectionY += hand1Finger1ProximalPhalanxBoneDirection[1]
                    hand1Finger1ProximalPhalanxBoneDirectionZ += hand1Finger1ProximalPhalanxBoneDirection[2]
                    # attributes of finger 1 intermediate phalanx bone
                    hand1Finger1IntermediatePhalanxBoneCenter = hand1Finger1.bone(2).center
                    hand1Finger1IntermediatePhalanxBoneCenterX += hand1Finger1IntermediatePhalanxBoneCenter[0]
                    hand1Finger1IntermediatePhalanxBoneCenterY += hand1Finger1IntermediatePhalanxBoneCenter[1]
                    hand1Finger1IntermediatePhalanxBoneCenterZ += hand1Finger1IntermediatePhalanxBoneCenter[2]
                    hand1Finger1IntermediatePhalanxBoneDirection = hand1Finger1.bone(2).direction
                    hand1Finger1IntermediatePhalanxBoneDirectionX += hand1Finger1IntermediatePhalanxBoneDirection[0]
                    hand1Finger1IntermediatePhalanxBoneDirectionY += hand1Finger1IntermediatePhalanxBoneDirection[1]
                    hand1Finger1IntermediatePhalanxBoneDirectionZ += hand1Finger1IntermediatePhalanxBoneDirection[2]
                    # attributes of finger 1 distal phalanx bone
                    hand1Finger1DistalPhalanxBoneCenter = hand1Finger1.bone(3).center
                    hand1Finger1DistalPhalanxBoneCenterX += hand1Finger1DistalPhalanxBoneCenter[0]
                    hand1Finger1DistalPhalanxBoneCenterY += hand1Finger1DistalPhalanxBoneCenter[1]
                    hand1Finger1DistalPhalanxBoneCenterZ += hand1Finger1DistalPhalanxBoneCenter[2]
                    hand1Finger1DistalPhalanxBoneDirection = hand1Finger1.bone(3).direction
                    hand1Finger1DistalPhalanxBoneDirectionX += hand1Finger1DistalPhalanxBoneDirection[0]
                    hand1Finger1DistalPhalanxBoneDirectionY += hand1Finger1DistalPhalanxBoneDirection[1]
                    hand1Finger1DistalPhalanxBoneDirectionZ += hand1Finger1DistalPhalanxBoneDirection[2]
                    hand1Finger1TipPositionX += hand1Finger1.joint_position(3)[0]
                    hand1Finger1TipPositionY += hand1Finger1.joint_position(3)[1]
                    hand1Finger1TipPositionZ += hand1Finger1.joint_position(3)[2]
                if(frame.hands[0].fingers[1] is not None):
                    ## Set Hand 1 Finger 2 ##
                    hand1Finger2 = frame.hands[0].fingers[1]
                    hand1Finger2DirectionVector = hand1Finger2.direction
                    hand1Finger2DirectionX += hand1Finger2DirectionVector[0]
                    hand1Finger2DirectionY += hand1Finger2DirectionVector[1]
                    hand1Finger2DirectionZ += hand1Finger2DirectionVector[2]
                    # attributes of finger 2 metacarpals
                    hand1Finger2MetacarpalCenter = hand1Finger2.bone(0).center
                    hand1Finger2MetacarpalCenterX += hand1Finger2MetacarpalCenter[0]
                    hand1Finger2MetacarpalCenterY += hand1Finger2MetacarpalCenter[1]
                    hand1Finger2MetacarpalCenterZ += hand1Finger2MetacarpalCenter[2]
                    hand1Finger2MetacarpalDirection = hand1Finger2.bone(0).direction
                    hand1Finger2MetacarpalDirectionX += hand1Finger2MetacarpalDirection[0]
                    hand1Finger2MetacarpalDirectionY += hand1Finger2MetacarpalDirection[1]
                    hand1Finger2MetacarpalDirectionZ += hand1Finger2MetacarpalDirection[2]
                    # attributes of finger 2 proximal phalanx bone
                    hand1Finger2ProximalPhalanxBoneCenter = hand1Finger2.bone(1).center
                    hand1Finger2ProximalPhalanxBoneCenterX += hand1Finger2ProximalPhalanxBoneCenter[0]
                    hand1Finger2ProximalPhalanxBoneCenterY += hand1Finger2ProximalPhalanxBoneCenter[1]
                    hand1Finger2ProximalPhalanxBoneCenterZ += hand1Finger2ProximalPhalanxBoneCenter[2]
                    hand1Finger2ProximalPhalanxBoneDirection = hand1Finger2.bone(1).direction
                    hand1Finger2ProximalPhalanxBoneDirectionX += hand1Finger2ProximalPhalanxBoneDirection[0]
                    hand1Finger2ProximalPhalanxBoneDirectionY += hand1Finger2ProximalPhalanxBoneDirection[1]
                    hand1Finger2ProximalPhalanxBoneDirectionZ += hand1Finger2ProximalPhalanxBoneDirection[2]
                    # attributes of finger 2 intermediate phalanx bone
                    hand1Finger2IntermediatePhalanxBoneCenter = hand1Finger2.bone(2).center
                    hand1Finger2IntermediatePhalanxBoneCenterX += hand1Finger2IntermediatePhalanxBoneCenter[0]
                    hand1Finger2IntermediatePhalanxBoneCenterY += hand1Finger2IntermediatePhalanxBoneCenter[1]
                    hand1Finger2IntermediatePhalanxBoneCenterZ += hand1Finger2IntermediatePhalanxBoneCenter[2]
                    hand1Finger2IntermediatePhalanxBoneDirection = hand1Finger2.bone(2).direction
                    hand1Finger2IntermediatePhalanxBoneDirectionX += hand1Finger2IntermediatePhalanxBoneDirection[0]
                    hand1Finger2IntermediatePhalanxBoneDirectionY += hand1Finger2IntermediatePhalanxBoneDirection[1]
                    hand1Finger2IntermediatePhalanxBoneDirectionZ += hand1Finger2IntermediatePhalanxBoneDirection[2]
                    # attributes of finger 2 distal phalanx bone
                    hand1Finger2DistalPhalanxBoneCenter = hand1Finger2.bone(3).center
                    hand1Finger2DistalPhalanxBoneCenterX += hand1Finger2DistalPhalanxBoneCenter[0]
                    hand1Finger2DistalPhalanxBoneCenterY += hand1Finger2DistalPhalanxBoneCenter[1]
                    hand1Finger2DistalPhalanxBoneCenterZ += hand1Finger2DistalPhalanxBoneCenter[2]
                    hand1Finger2DistalPhalanxBoneDirection = hand1Finger2.bone(3).direction
                    hand1Finger2DistalPhalanxBoneDirectionX += hand1Finger2DistalPhalanxBoneDirection[0]
                    hand1Finger2DistalPhalanxBoneDirectionY += hand1Finger2DistalPhalanxBoneDirection[1]
                    hand1Finger2DistalPhalanxBoneDirectionZ += hand1Finger2DistalPhalanxBoneDirection[2]
                    hand1Finger2TipPositionX += hand1Finger2.joint_position(3)[0]
                    hand1Finger2TipPositionY += hand1Finger2.joint_position(3)[1]
                    hand1Finger2TipPositionZ += hand1Finger2.joint_position(3)[2]
                if(frame.hands[0].fingers[2] is not None):
                    ## Set Hand 1 Finger 3 ##
                    hand1Finger3 = frame.hands[0].fingers[2]
                    hand1Finger3DirectionVector = hand1Finger3.direction
                    hand1Finger3DirectionX += hand1Finger3DirectionVector[0]
                    hand1Finger3DirectionY += hand1Finger3DirectionVector[1]
                    hand1Finger3DirectionZ += hand1Finger3DirectionVector[2]
                    # attributes of finger 3 metacarpals
                    hand1Finger3MetacarpalCenter = hand1Finger3.bone(0).center
                    hand1Finger3MetacarpalCenterX += hand1Finger3MetacarpalCenter[0]
                    hand1Finger3MetacarpalCenterY += hand1Finger3MetacarpalCenter[1]
                    hand1Finger3MetacarpalCenterZ += hand1Finger3MetacarpalCenter[2]
                    hand1Finger3MetacarpalDirection = hand1Finger3.bone(0).direction
                    hand1Finger3MetacarpalDirectionX += hand1Finger3MetacarpalDirection[0]
                    hand1Finger3MetacarpalDirectionY += hand1Finger3MetacarpalDirection[1]
                    hand1Finger3MetacarpalDirectionZ += hand1Finger3MetacarpalDirection[2]
                    # attributes of finger 3 proximal phalanx bone
                    hand1Finger3ProximalPhalanxBoneCenter = hand1Finger3.bone(1).center
                    hand1Finger3ProximalPhalanxBoneCenterX += hand1Finger3ProximalPhalanxBoneCenter[0]
                    hand1Finger3ProximalPhalanxBoneCenterY += hand1Finger3ProximalPhalanxBoneCenter[1]
                    hand1Finger3ProximalPhalanxBoneCenterZ += hand1Finger3ProximalPhalanxBoneCenter[2]
                    hand1Finger3ProximalPhalanxBoneDirection = hand1Finger3.bone(1).direction
                    hand1Finger3ProximalPhalanxBoneDirectionX += hand1Finger3ProximalPhalanxBoneDirection[0]
                    hand1Finger3ProximalPhalanxBoneDirectionY += hand1Finger3ProximalPhalanxBoneDirection[1]
                    hand1Finger3ProximalPhalanxBoneDirectionZ += hand1Finger3ProximalPhalanxBoneDirection[2]
                    # attributes of finger 3 intermediate phalanx bone
                    hand1Finger3IntermediatePhalanxBoneCenter = hand1Finger3.bone(2).center
                    hand1Finger3IntermediatePhalanxBoneCenterX += hand1Finger3IntermediatePhalanxBoneCenter[0]
                    hand1Finger3IntermediatePhalanxBoneCenterY += hand1Finger3IntermediatePhalanxBoneCenter[1]
                    hand1Finger3IntermediatePhalanxBoneCenterZ += hand1Finger3IntermediatePhalanxBoneCenter[2]
                    hand1Finger3IntermediatePhalanxBoneDirection = hand1Finger3.bone(2).direction
                    hand1Finger3IntermediatePhalanxBoneDirectionX += hand1Finger3IntermediatePhalanxBoneDirection[0]
                    hand1Finger3IntermediatePhalanxBoneDirectionY += hand1Finger3IntermediatePhalanxBoneDirection[1]
                    hand1Finger3IntermediatePhalanxBoneDirectionZ += hand1Finger3IntermediatePhalanxBoneDirection[2]
                    # attributes of finger 3 distal phalanx bone
                    hand1Finger3DistalPhalanxBoneCenter = hand1Finger3.bone(3).center
                    hand1Finger3DistalPhalanxBoneCenterX += hand1Finger3DistalPhalanxBoneCenter[0]
                    hand1Finger3DistalPhalanxBoneCenterY += hand1Finger3DistalPhalanxBoneCenter[1]
                    hand1Finger3DistalPhalanxBoneCenterZ += hand1Finger3DistalPhalanxBoneCenter[2]
                    hand1Finger3DistalPhalanxBoneDirection = hand1Finger3.bone(3).direction
                    hand1Finger3DistalPhalanxBoneDirectionX += hand1Finger3DistalPhalanxBoneDirection[0]
                    hand1Finger3DistalPhalanxBoneDirectionY += hand1Finger3DistalPhalanxBoneDirection[1]
                    hand1Finger3DistalPhalanxBoneDirectionZ += hand1Finger3DistalPhalanxBoneDirection[2]
                    hand1Finger3TipPositionX += hand1Finger3.joint_position(3)[0]
                    hand1Finger3TipPositionY += hand1Finger3.joint_position(3)[1]
                    hand1Finger3TipPositionZ += hand1Finger3.joint_position(3)[2]
                if(frame.hands[0].fingers[3] is not None):
                    ## Set Hand 1 Finger 4 ##
                    hand1Finger4 = frame.hands[0].fingers[3]
                    hand1Finger4DirectionVector = hand1Finger4.direction
                    hand1Finger4DirectionX += hand1Finger4DirectionVector[0]
                    hand1Finger4DirectionY += hand1Finger4DirectionVector[1]
                    hand1Finger4DirectionZ += hand1Finger4DirectionVector[2]
                    # attributes of finger 4 metacarpals
                    hand1Finger4MetacarpalCenter = hand1Finger4.bone(0).center
                    hand1Finger4MetacarpalCenterX += hand1Finger4MetacarpalCenter[0]
                    hand1Finger4MetacarpalCenterY += hand1Finger4MetacarpalCenter[1]
                    hand1Finger4MetacarpalCenterZ += hand1Finger4MetacarpalCenter[2]
                    hand1Finger4MetacarpalDirection = hand1Finger4.bone(0).direction
                    hand1Finger4MetacarpalDirectionX += hand1Finger4MetacarpalDirection[0]
                    hand1Finger4MetacarpalDirectionY += hand1Finger4MetacarpalDirection[1]
                    hand1Finger4MetacarpalDirectionZ += hand1Finger4MetacarpalDirection[2]
                    # attributes of finger 4 proximal phalanx bone
                    hand1Finger4ProximalPhalanxBoneCenter = hand1Finger4.bone(1).center
                    hand1Finger4ProximalPhalanxBoneCenterX += hand1Finger4ProximalPhalanxBoneCenter[0]
                    hand1Finger4ProximalPhalanxBoneCenterY += hand1Finger4ProximalPhalanxBoneCenter[1]
                    hand1Finger4ProximalPhalanxBoneCenterZ += hand1Finger4ProximalPhalanxBoneCenter[2]
                    hand1Finger4ProximalPhalanxBoneDirection = hand1Finger4.bone(1).direction
                    hand1Finger4ProximalPhalanxBoneDirectionX += hand1Finger4ProximalPhalanxBoneDirection[0]
                    hand1Finger4ProximalPhalanxBoneDirectionY += hand1Finger4ProximalPhalanxBoneDirection[1]
                    hand1Finger4ProximalPhalanxBoneDirectionZ += hand1Finger4ProximalPhalanxBoneDirection[2]
                    # attributes of finger 4 intermediate phalanx bone
                    hand1Finger4IntermediatePhalanxBoneCenter = hand1Finger4.bone(2).center
                    hand1Finger4IntermediatePhalanxBoneCenterX += hand1Finger4IntermediatePhalanxBoneCenter[0]
                    hand1Finger4IntermediatePhalanxBoneCenterY += hand1Finger4IntermediatePhalanxBoneCenter[1]
                    hand1Finger4IntermediatePhalanxBoneCenterZ += hand1Finger4IntermediatePhalanxBoneCenter[2]
                    hand1Finger4IntermediatePhalanxBoneDirection = hand1Finger4.bone(2).direction
                    hand1Finger4IntermediatePhalanxBoneDirectionX += hand1Finger4IntermediatePhalanxBoneDirection[0]
                    hand1Finger4IntermediatePhalanxBoneDirectionY += hand1Finger4IntermediatePhalanxBoneDirection[1]
                    hand1Finger4IntermediatePhalanxBoneDirectionZ += hand1Finger4IntermediatePhalanxBoneDirection[2]
                    # attributes of finger 4 distal phalanx bone
                    hand1Finger4DistalPhalanxBoneCenter = hand1Finger4.bone(3).center
                    hand1Finger4DistalPhalanxBoneCenterX += hand1Finger4DistalPhalanxBoneCenter[0]
                    hand1Finger4DistalPhalanxBoneCenterY += hand1Finger4DistalPhalanxBoneCenter[1]
                    hand1Finger4DistalPhalanxBoneCenterZ += hand1Finger4DistalPhalanxBoneCenter[2]
                    hand1Finger4DistalPhalanxBoneDirection = hand1Finger4.bone(3).direction
                    hand1Finger4DistalPhalanxBoneDirectionX += hand1Finger4DistalPhalanxBoneDirection[0]
                    hand1Finger4DistalPhalanxBoneDirectionY += hand1Finger4DistalPhalanxBoneDirection[1]
                    hand1Finger4DistalPhalanxBoneDirectionZ += hand1Finger4DistalPhalanxBoneDirection[2]
                    hand1Finger4TipPositionX += hand1Finger4.joint_position(3)[0]
                    hand1Finger4TipPositionY += hand1Finger4.joint_position(3)[1]
                    hand1Finger4TipPositionZ += hand1Finger4.joint_position(3)[2]
                if(frame.hands[0].fingers[4] is not None):
                    ## Set Hand 1 Finger 5 ##
                    hand1Finger5 = frame.hands[0].fingers[4]
                    hand1Finger5DirectionVector = hand1Finger5.direction
                    hand1Finger5DirectionX += hand1Finger5DirectionVector[0]
                    hand1Finger5DirectionY += hand1Finger5DirectionVector[1]
                    hand1Finger5DirectionZ += hand1Finger5DirectionVector[2]
                    # attributes of finger 5 metacarpals
                    hand1Finger5MetacarpalCenter = hand1Finger5.bone(0).center
                    hand1Finger5MetacarpalCenterX += hand1Finger5MetacarpalCenter[0]
                    hand1Finger5MetacarpalCenterY += hand1Finger5MetacarpalCenter[1]
                    hand1Finger5MetacarpalCenterZ += hand1Finger5MetacarpalCenter[2]
                    hand1Finger5MetacarpalDirection = hand1Finger5.bone(0).direction
                    hand1Finger5MetacarpalDirectionX += hand1Finger5MetacarpalDirection[0]
                    hand1Finger5MetacarpalDirectionY += hand1Finger5MetacarpalDirection[1]
                    hand1Finger5MetacarpalDirectionZ += hand1Finger5MetacarpalDirection[2]
                    # attributes of finger 5 proximal phalanx bone
                    hand1Finger5ProximalPhalanxBoneCenter = hand1Finger5.bone(1).center
                    hand1Finger5ProximalPhalanxBoneCenterX += hand1Finger5ProximalPhalanxBoneCenter[0]
                    hand1Finger5ProximalPhalanxBoneCenterY += hand1Finger5ProximalPhalanxBoneCenter[1]
                    hand1Finger5ProximalPhalanxBoneCenterZ += hand1Finger5ProximalPhalanxBoneCenter[2]
                    hand1Finger5ProximalPhalanxBoneDirection = hand1Finger5.bone(1).direction
                    hand1Finger5ProximalPhalanxBoneDirectionX += hand1Finger5ProximalPhalanxBoneDirection[0]
                    hand1Finger5ProximalPhalanxBoneDirectionY += hand1Finger5ProximalPhalanxBoneDirection[1]
                    hand1Finger5ProximalPhalanxBoneDirectionZ += hand1Finger5ProximalPhalanxBoneDirection[2]
                    # attributes of finger 5 intermediate phalanx bone
                    hand1Finger5IntermediatePhalanxBoneCenter = hand1Finger5.bone(2).center
                    hand1Finger5IntermediatePhalanxBoneCenterX += hand1Finger5IntermediatePhalanxBoneCenter[0]
                    hand1Finger5IntermediatePhalanxBoneCenterY += hand1Finger5IntermediatePhalanxBoneCenter[1]
                    hand1Finger5IntermediatePhalanxBoneCenterZ += hand1Finger5IntermediatePhalanxBoneCenter[2]
                    hand1Finger5IntermediatePhalanxBoneDirection = hand1Finger5.bone(2).direction
                    hand1Finger5IntermediatePhalanxBoneDirectionX += hand1Finger5IntermediatePhalanxBoneDirection[0]
                    hand1Finger5IntermediatePhalanxBoneDirectionY += hand1Finger5IntermediatePhalanxBoneDirection[1]
                    hand1Finger5IntermediatePhalanxBoneDirectionZ += hand1Finger5IntermediatePhalanxBoneDirection[2]
                    # attributes of finger 5 distal phalanx bone
                    hand1Finger5DistalPhalanxBoneCenter = hand1Finger5.bone(3).center
                    hand1Finger5DistalPhalanxBoneCenterX += hand1Finger5DistalPhalanxBoneCenter[0]
                    hand1Finger5DistalPhalanxBoneCenterY += hand1Finger5DistalPhalanxBoneCenter[1]
                    hand1Finger5DistalPhalanxBoneCenterZ += hand1Finger5DistalPhalanxBoneCenter[2]
                    hand1Finger5DistalPhalanxBoneDirection = hand1Finger5.bone(3).direction
                    hand1Finger5DistalPhalanxBoneDirectionX += hand1Finger5DistalPhalanxBoneDirection[0]
                    hand1Finger5DistalPhalanxBoneDirectionY += hand1Finger5DistalPhalanxBoneDirection[1]
                    hand1Finger5DistalPhalanxBoneDirectionZ += hand1Finger5DistalPhalanxBoneDirection[2]
                    hand1Finger5TipPositionX += hand1Finger5.joint_position(3)[0]
                    hand1Finger5TipPositionY += hand1Finger5.joint_position(3)[1]
                    hand1Finger5TipPositionZ += hand1Finger5.joint_position(3)[2]
            if ( frame.hands[1] is not None):
                hand2 = frame.hands[1]
                # if ( hand2.isLeft):
                #     hand2Type += -1
                # else:
                #     hand2Type += 1
                hand2DirectionVector = hand2.direction
                hand2DirectionX += hand2DirectionVector[0]
                hand2DirectionY += hand2DirectionVector[1]
                hand2DirectionZ += hand2DirectionVector[2]
                hand2PalmPositionVector = hand2.palm_position
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
                if ( previousFrame and previousFrame.is_valid):
                    hand2TranslationVector = hand2.translation(previousFrame)
                    hand2TranslationX += hand2TranslationVector[0]
                    hand2TranslationY += hand2TranslationVector[1]
                    hand2TranslationZ += hand2TranslationVector[2]
                    hand2RotationAxisVector = hand2.rotation_axis(previousFrame)
                    hand2RotationAxisX += hand2RotationAxisVector[0]
                    hand2RotationAxisY += hand2RotationAxisVector[1]
                    hand2RotationAxisZ += hand2RotationAxisVector[2]
                    hand2RotationAngle += hand2.rotation_angle(previousFrame)
                if(frame.hands[1].fingers[0] is not None):
                    ## Set Hand 1 Finger 1 ##
                    hand2Finger1 = frame.hands[1].fingers[0]
                    hand2Finger1DirectionVector = hand2Finger1.direction
                    hand2Finger1DirectionX += hand2Finger1DirectionVector[0]
                    hand2Finger1DirectionY += hand2Finger1DirectionVector[1]
                    hand2Finger1DirectionZ += hand2Finger1DirectionVector[2]
                    # attributes of finger 1 metacarpals
                    hand2Finger1MetacarpalCenter = hand2Finger1.bone(0).center
                    hand2Finger1MetacarpalCenterX += hand2Finger1MetacarpalCenter[0]
                    hand2Finger1MetacarpalCenterY += hand2Finger1MetacarpalCenter[1]
                    hand2Finger1MetacarpalCenterZ += hand2Finger1MetacarpalCenter[2]
                    hand2Finger1MetacarpalDirection = hand2Finger1.bone(0).direction
                    hand2Finger1MetacarpalDirectionX += hand2Finger1MetacarpalDirection[0]
                    hand2Finger1MetacarpalDirectionY += hand2Finger1MetacarpalDirection[1]
                    hand2Finger1MetacarpalDirectionZ += hand2Finger1MetacarpalDirection[2]
                    # attributes of finger 1 proximal phalanx bone
                    hand2Finger1ProximalPhalanxBoneCenter = hand2Finger1.bone(1).center
                    hand2Finger1ProximalPhalanxBoneCenterX += hand2Finger1ProximalPhalanxBoneCenter[0]
                    hand2Finger1ProximalPhalanxBoneCenterY += hand2Finger1ProximalPhalanxBoneCenter[1]
                    hand2Finger1ProximalPhalanxBoneCenterZ += hand2Finger1ProximalPhalanxBoneCenter[2]
                    hand2Finger1ProximalPhalanxBoneDirection = hand2Finger1.bone(1).direction
                    hand2Finger1ProximalPhalanxBoneDirectionX += hand2Finger1ProximalPhalanxBoneDirection[0]
                    hand2Finger1ProximalPhalanxBoneDirectionY += hand2Finger1ProximalPhalanxBoneDirection[1]
                    hand2Finger1ProximalPhalanxBoneDirectionZ += hand2Finger1ProximalPhalanxBoneDirection[2]
                    # attributes of finger 1 intermediate phalanx bone
                    hand2Finger1IntermediatePhalanxBoneCenter = hand2Finger1.bone(2).center
                    hand2Finger1IntermediatePhalanxBoneCenterX += hand2Finger1IntermediatePhalanxBoneCenter[0]
                    hand2Finger1IntermediatePhalanxBoneCenterY += hand2Finger1IntermediatePhalanxBoneCenter[1]
                    hand2Finger1IntermediatePhalanxBoneCenterZ += hand2Finger1IntermediatePhalanxBoneCenter[2]
                    hand2Finger1IntermediatePhalanxBoneDirection = hand2Finger1.bone(2).direction
                    hand2Finger1IntermediatePhalanxBoneDirectionX += hand2Finger1IntermediatePhalanxBoneDirection[0]
                    hand2Finger1IntermediatePhalanxBoneDirectionY += hand2Finger1IntermediatePhalanxBoneDirection[1]
                    hand2Finger1IntermediatePhalanxBoneDirectionZ += hand2Finger1IntermediatePhalanxBoneDirection[2]
                    # attributes of finger 1 distal phalanx bone
                    hand2Finger1DistalPhalanxBoneCenter = hand2Finger1.bone(3).center
                    hand2Finger1DistalPhalanxBoneCenterX += hand2Finger1DistalPhalanxBoneCenter[0]
                    hand2Finger1DistalPhalanxBoneCenterY += hand2Finger1DistalPhalanxBoneCenter[1]
                    hand2Finger1DistalPhalanxBoneCenterZ += hand2Finger1DistalPhalanxBoneCenter[2]
                    hand2Finger1DistalPhalanxBoneDirection = hand2Finger1.bone(3).direction
                    hand2Finger1DistalPhalanxBoneDirectionX += hand2Finger1DistalPhalanxBoneDirection[0]
                    hand2Finger1DistalPhalanxBoneDirectionY += hand2Finger1DistalPhalanxBoneDirection[1]
                    hand2Finger1DistalPhalanxBoneDirectionZ += hand2Finger1DistalPhalanxBoneDirection[2]
                    hand2Finger1TipPositionX += hand2Finger1.joint_position(3)[0]
                    hand2Finger1TipPositionY += hand2Finger1.joint_position(3)[1]
                    hand2Finger1TipPositionZ += hand2Finger1.joint_position(3)[2]
                if(frame.hands[1].fingers[1] is not None):
                    ## Set Hand 1 Finger 2 ##
                    hand2Finger2 = frame.hands[1].fingers[1]
                    hand2Finger2DirectionVector = hand2Finger2.direction
                    hand2Finger2DirectionX += hand2Finger2DirectionVector[0]
                    hand2Finger2DirectionY += hand2Finger2DirectionVector[1]
                    hand2Finger2DirectionZ += hand2Finger2DirectionVector[2]
                    # attributes of finger 2 metacarpals
                    hand2Finger2MetacarpalCenter = hand2Finger2.bone(0).center
                    hand2Finger2MetacarpalCenterX += hand2Finger2MetacarpalCenter[0]
                    hand2Finger2MetacarpalCenterY += hand2Finger2MetacarpalCenter[1]
                    hand2Finger2MetacarpalCenterZ += hand2Finger2MetacarpalCenter[2]
                    hand2Finger2MetacarpalDirection = hand2Finger2.bone(0).direction
                    hand2Finger2MetacarpalDirectionX += hand2Finger2MetacarpalDirection[0]
                    hand2Finger2MetacarpalDirectionY += hand2Finger2MetacarpalDirection[1]
                    hand2Finger2MetacarpalDirectionZ += hand2Finger2MetacarpalDirection[2]
                    # attributes of finger 2 proximal phalanx bone
                    hand2Finger2ProximalPhalanxBoneCenter = hand2Finger2.bone(1).center
                    hand2Finger2ProximalPhalanxBoneCenterX += hand2Finger2ProximalPhalanxBoneCenter[0]
                    hand2Finger2ProximalPhalanxBoneCenterY += hand2Finger2ProximalPhalanxBoneCenter[1]
                    hand2Finger2ProximalPhalanxBoneCenterZ += hand2Finger2ProximalPhalanxBoneCenter[2]
                    hand2Finger2ProximalPhalanxBoneDirection = hand2Finger2.bone(1).direction
                    hand2Finger2ProximalPhalanxBoneDirectionX += hand2Finger2ProximalPhalanxBoneDirection[0]
                    hand2Finger2ProximalPhalanxBoneDirectionY += hand2Finger2ProximalPhalanxBoneDirection[1]
                    hand2Finger2ProximalPhalanxBoneDirectionZ += hand2Finger2ProximalPhalanxBoneDirection[2]
                    # attributes of finger 2 intermediate phalanx bone
                    hand2Finger2IntermediatePhalanxBoneCenter = hand2Finger2.bone(2).center
                    hand2Finger2IntermediatePhalanxBoneCenterX += hand2Finger2IntermediatePhalanxBoneCenter[0]
                    hand2Finger2IntermediatePhalanxBoneCenterY += hand2Finger2IntermediatePhalanxBoneCenter[1]
                    hand2Finger2IntermediatePhalanxBoneCenterZ += hand2Finger2IntermediatePhalanxBoneCenter[2]
                    hand2Finger2IntermediatePhalanxBoneDirection = hand2Finger2.bone(2).direction
                    hand2Finger2IntermediatePhalanxBoneDirectionX += hand2Finger2IntermediatePhalanxBoneDirection[0]
                    hand2Finger2IntermediatePhalanxBoneDirectionY += hand2Finger2IntermediatePhalanxBoneDirection[1]
                    hand2Finger2IntermediatePhalanxBoneDirectionZ += hand2Finger2IntermediatePhalanxBoneDirection[2]
                    # attributes of finger 2 distal phalanx bone
                    hand2Finger2DistalPhalanxBoneCenter = hand2Finger2.bone(3).center
                    hand2Finger2DistalPhalanxBoneCenterX += hand2Finger2DistalPhalanxBoneCenter[0]
                    hand2Finger2DistalPhalanxBoneCenterY += hand2Finger2DistalPhalanxBoneCenter[1]
                    hand2Finger2DistalPhalanxBoneCenterZ += hand2Finger2DistalPhalanxBoneCenter[2]
                    hand2Finger2DistalPhalanxBoneDirection = hand2Finger2.bone(3).direction
                    hand2Finger2DistalPhalanxBoneDirectionX += hand2Finger2DistalPhalanxBoneDirection[0]
                    hand2Finger2DistalPhalanxBoneDirectionY += hand2Finger2DistalPhalanxBoneDirection[1]
                    hand2Finger2DistalPhalanxBoneDirectionZ += hand2Finger2DistalPhalanxBoneDirection[2]
                    hand2Finger2TipPositionX += hand2Finger2.joint_position(3)[0]
                    hand2Finger2TipPositionY += hand2Finger2.joint_position(3)[1]
                    hand2Finger2TipPositionZ += hand2Finger2.joint_position(3)[2]
                if(frame.hands[1].fingers[2] is not None):
                    ## Set Hand 1 Finger 3 ##
                    hand2Finger3 = frame.hands[1].fingers[2]
                    hand2Finger3DirectionVector = hand2Finger3.direction
                    hand2Finger3DirectionX += hand2Finger3DirectionVector[0]
                    hand2Finger3DirectionY += hand2Finger3DirectionVector[1]
                    hand2Finger3DirectionZ += hand2Finger3DirectionVector[2]
                    # attributes of finger 3 metacarpals
                    hand2Finger3MetacarpalCenter = hand2Finger3.bone(0).center
                    hand2Finger3MetacarpalCenterX += hand2Finger3MetacarpalCenter[0]
                    hand2Finger3MetacarpalCenterY += hand2Finger3MetacarpalCenter[1]
                    hand2Finger3MetacarpalCenterZ += hand2Finger3MetacarpalCenter[2]
                    hand2Finger3MetacarpalDirection = hand2Finger3.bone(0).direction
                    hand2Finger3MetacarpalDirectionX += hand2Finger3MetacarpalDirection[0]
                    hand2Finger3MetacarpalDirectionY += hand2Finger3MetacarpalDirection[1]
                    hand2Finger3MetacarpalDirectionZ += hand2Finger3MetacarpalDirection[2]
                    # attributes of finger 3 proximal phalanx bone
                    hand2Finger3ProximalPhalanxBoneCenter = hand2Finger3.bone(1).center
                    hand2Finger3ProximalPhalanxBoneCenterX += hand2Finger3ProximalPhalanxBoneCenter[0]
                    hand2Finger3ProximalPhalanxBoneCenterY += hand2Finger3ProximalPhalanxBoneCenter[1]
                    hand2Finger3ProximalPhalanxBoneCenterZ += hand2Finger3ProximalPhalanxBoneCenter[2]
                    hand2Finger3ProximalPhalanxBoneDirection = hand2Finger3.bone(1).direction
                    hand2Finger3ProximalPhalanxBoneDirectionX += hand2Finger3ProximalPhalanxBoneDirection[0]
                    hand2Finger3ProximalPhalanxBoneDirectionY += hand2Finger3ProximalPhalanxBoneDirection[1]
                    hand2Finger3ProximalPhalanxBoneDirectionZ += hand2Finger3ProximalPhalanxBoneDirection[2]
                    # attributes of finger 3 intermediate phalanx bone
                    hand2Finger3IntermediatePhalanxBoneCenter = hand2Finger3.bone(2).center
                    hand2Finger3IntermediatePhalanxBoneCenterX += hand2Finger3IntermediatePhalanxBoneCenter[0]
                    hand2Finger3IntermediatePhalanxBoneCenterY += hand2Finger3IntermediatePhalanxBoneCenter[1]
                    hand2Finger3IntermediatePhalanxBoneCenterZ += hand2Finger3IntermediatePhalanxBoneCenter[2]
                    hand2Finger3IntermediatePhalanxBoneDirection = hand2Finger3.bone(2).direction
                    hand2Finger3IntermediatePhalanxBoneDirectionX += hand2Finger3IntermediatePhalanxBoneDirection[0]
                    hand2Finger3IntermediatePhalanxBoneDirectionY += hand2Finger3IntermediatePhalanxBoneDirection[1]
                    hand2Finger3IntermediatePhalanxBoneDirectionZ += hand2Finger3IntermediatePhalanxBoneDirection[2]
                    # attributes of finger 3 distal phalanx bone
                    hand2Finger3DistalPhalanxBoneCenter = hand2Finger3.bone(3).center
                    hand2Finger3DistalPhalanxBoneCenterX += hand2Finger3DistalPhalanxBoneCenter[0]
                    hand2Finger3DistalPhalanxBoneCenterY += hand2Finger3DistalPhalanxBoneCenter[1]
                    hand2Finger3DistalPhalanxBoneCenterZ += hand2Finger3DistalPhalanxBoneCenter[2]
                    hand2Finger3DistalPhalanxBoneDirection = hand2Finger3.bone(3).direction
                    hand2Finger3DistalPhalanxBoneDirectionX += hand2Finger3DistalPhalanxBoneDirection[0]
                    hand2Finger3DistalPhalanxBoneDirectionY += hand2Finger3DistalPhalanxBoneDirection[1]
                    hand2Finger3DistalPhalanxBoneDirectionZ += hand2Finger3DistalPhalanxBoneDirection[2]
                    hand2Finger3TipPositionX += hand2Finger3.joint_position(3)[0]
                    hand2Finger3TipPositionY += hand2Finger3.joint_position(3)[1]
                    hand2Finger3TipPositionZ += hand2Finger3.joint_position(3)[2]
                if(frame.hands[1].fingers[3] is not None):
                    ## Set Hand 1 Finger 4 ##
                    hand2Finger4 = frame.hands[1].fingers[3]
                    hand2Finger4DirectionVector = hand2Finger4.direction
                    hand2Finger4DirectionX += hand2Finger4DirectionVector[0]
                    hand2Finger4DirectionY += hand2Finger4DirectionVector[1]
                    hand2Finger4DirectionZ += hand2Finger4DirectionVector[2]
                    # attributes of finger 4 metacarpals
                    hand2Finger4MetacarpalCenter = hand2Finger4.bone(0).center
                    hand2Finger4MetacarpalCenterX += hand2Finger4MetacarpalCenter[0]
                    hand2Finger4MetacarpalCenterY += hand2Finger4MetacarpalCenter[1]
                    hand2Finger4MetacarpalCenterZ += hand2Finger4MetacarpalCenter[2]
                    hand2Finger4MetacarpalDirection = hand2Finger4.bone(0).direction
                    hand2Finger4MetacarpalDirectionX += hand2Finger4MetacarpalDirection[0]
                    hand2Finger4MetacarpalDirectionY += hand2Finger4MetacarpalDirection[1]
                    hand2Finger4MetacarpalDirectionZ += hand2Finger4MetacarpalDirection[2]
                    # attributes of finger 4 proximal phalanx bone
                    hand2Finger4ProximalPhalanxBoneCenter = hand2Finger4.bone(1).center
                    hand2Finger4ProximalPhalanxBoneCenterX += hand2Finger4ProximalPhalanxBoneCenter[0]
                    hand2Finger4ProximalPhalanxBoneCenterY += hand2Finger4ProximalPhalanxBoneCenter[1]
                    hand2Finger4ProximalPhalanxBoneCenterZ += hand2Finger4ProximalPhalanxBoneCenter[2]
                    hand2Finger4ProximalPhalanxBoneDirection = hand2Finger4.bone(1).direction
                    hand2Finger4ProximalPhalanxBoneDirectionX += hand2Finger4ProximalPhalanxBoneDirection[0]
                    hand2Finger4ProximalPhalanxBoneDirectionY += hand2Finger4ProximalPhalanxBoneDirection[1]
                    hand2Finger4ProximalPhalanxBoneDirectionZ += hand2Finger4ProximalPhalanxBoneDirection[2]
                    # attributes of finger 4 intermediate phalanx bone
                    hand2Finger4IntermediatePhalanxBoneCenter = hand2Finger4.bone(2).center
                    hand2Finger4IntermediatePhalanxBoneCenterX += hand2Finger4IntermediatePhalanxBoneCenter[0]
                    hand2Finger4IntermediatePhalanxBoneCenterY += hand2Finger4IntermediatePhalanxBoneCenter[1]
                    hand2Finger4IntermediatePhalanxBoneCenterZ += hand2Finger4IntermediatePhalanxBoneCenter[2]
                    hand2Finger4IntermediatePhalanxBoneDirection = hand2Finger4.bone(2).direction
                    hand2Finger4IntermediatePhalanxBoneDirectionX += hand2Finger4IntermediatePhalanxBoneDirection[0]
                    hand2Finger4IntermediatePhalanxBoneDirectionY += hand2Finger4IntermediatePhalanxBoneDirection[1]
                    hand2Finger4IntermediatePhalanxBoneDirectionZ += hand2Finger4IntermediatePhalanxBoneDirection[2]
                    # attributes of finger 4 distal phalanx bone
                    hand2Finger4DistalPhalanxBoneCenter = hand2Finger4.bone(3).center
                    hand2Finger4DistalPhalanxBoneCenterX += hand2Finger4DistalPhalanxBoneCenter[0]
                    hand2Finger4DistalPhalanxBoneCenterY += hand2Finger4DistalPhalanxBoneCenter[1]
                    hand2Finger4DistalPhalanxBoneCenterZ += hand2Finger4DistalPhalanxBoneCenter[2]
                    hand2Finger4DistalPhalanxBoneDirection = hand2Finger4.bone(3).direction
                    hand2Finger4DistalPhalanxBoneDirectionX += hand2Finger4DistalPhalanxBoneDirection[0]
                    hand2Finger4DistalPhalanxBoneDirectionY += hand2Finger4DistalPhalanxBoneDirection[1]
                    hand2Finger4DistalPhalanxBoneDirectionZ += hand2Finger4DistalPhalanxBoneDirection[2]
                    hand2Finger4TipPositionX += hand2Finger4.joint_position(3)[0]
                    hand2Finger4TipPositionY += hand2Finger4.joint_position(3)[1]
                    hand2Finger4TipPositionZ += hand2Finger4.joint_position(3)[2]
                if(frame.hands[1].fingers[4] is not None):
                    ## Set Hand 1 Finger 5 ##
                    hand2Finger5 = frame.hands[1].fingers[4]
                    hand2Finger5DirectionVector = hand2Finger5.direction
                    hand2Finger5DirectionX += hand2Finger5DirectionVector[0]
                    hand2Finger5DirectionY += hand2Finger5DirectionVector[1]
                    hand2Finger5DirectionZ += hand2Finger5DirectionVector[2]
                    # attributes of finger 5 metacarpals
                    hand2Finger5MetacarpalCenter = hand2Finger5.bone(0).center
                    hand2Finger5MetacarpalCenterX += hand2Finger5MetacarpalCenter[0]
                    hand2Finger5MetacarpalCenterY += hand2Finger5MetacarpalCenter[1]
                    hand2Finger5MetacarpalCenterZ += hand2Finger5MetacarpalCenter[2]
                    hand2Finger5MetacarpalDirection = hand2Finger5.bone(0).direction
                    hand2Finger5MetacarpalDirectionX += hand2Finger5MetacarpalDirection[0]
                    hand2Finger5MetacarpalDirectionY += hand2Finger5MetacarpalDirection[1]
                    hand2Finger5MetacarpalDirectionZ += hand2Finger5MetacarpalDirection[2]
                    # attributes of finger 5 proximal phalanx bone
                    hand2Finger5ProximalPhalanxBoneCenter = hand2Finger5.bone(1).center
                    hand2Finger5ProximalPhalanxBoneCenterX += hand2Finger5ProximalPhalanxBoneCenter[0]
                    hand2Finger5ProximalPhalanxBoneCenterY += hand2Finger5ProximalPhalanxBoneCenter[1]
                    hand2Finger5ProximalPhalanxBoneCenterZ += hand2Finger5ProximalPhalanxBoneCenter[2]
                    hand2Finger5ProximalPhalanxBoneDirection = hand2Finger5.bone(1).direction
                    hand2Finger5ProximalPhalanxBoneDirectionX += hand2Finger5ProximalPhalanxBoneDirection[0]
                    hand2Finger5ProximalPhalanxBoneDirectionY += hand2Finger5ProximalPhalanxBoneDirection[1]
                    hand2Finger5ProximalPhalanxBoneDirectionZ += hand2Finger5ProximalPhalanxBoneDirection[2]
                    # attributes of finger 5 intermediate phalanx bone
                    hand2Finger5IntermediatePhalanxBoneCenter = hand2Finger5.bone(2).center
                    hand2Finger5IntermediatePhalanxBoneCenterX += hand2Finger5IntermediatePhalanxBoneCenter[0]
                    hand2Finger5IntermediatePhalanxBoneCenterY += hand2Finger5IntermediatePhalanxBoneCenter[1]
                    hand2Finger5IntermediatePhalanxBoneCenterZ += hand2Finger5IntermediatePhalanxBoneCenter[2]
                    hand2Finger5IntermediatePhalanxBoneDirection = hand2Finger5.bone(2).direction
                    hand2Finger5IntermediatePhalanxBoneDirectionX += hand2Finger5IntermediatePhalanxBoneDirection[0]
                    hand2Finger5IntermediatePhalanxBoneDirectionY += hand2Finger5IntermediatePhalanxBoneDirection[1]
                    hand2Finger5IntermediatePhalanxBoneDirectionZ += hand2Finger5IntermediatePhalanxBoneDirection[2]
                    # attributes of finger 5 distal phalanx bone
                    hand2Finger5DistalPhalanxBoneCenter = hand2Finger5.bone(3).center
                    hand2Finger5DistalPhalanxBoneCenterX += hand2Finger5DistalPhalanxBoneCenter[0]
                    hand2Finger5DistalPhalanxBoneCenterY += hand2Finger5DistalPhalanxBoneCenter[1]
                    hand2Finger5DistalPhalanxBoneCenterZ += hand2Finger5DistalPhalanxBoneCenter[2]
                    hand2Finger5DistalPhalanxBoneDirection = hand2Finger5.bone(3).direction
                    hand2Finger5DistalPhalanxBoneDirectionX += hand2Finger5DistalPhalanxBoneDirection[0]
                    hand2Finger5DistalPhalanxBoneDirectionY += hand2Finger5DistalPhalanxBoneDirection[1]
                    hand2Finger5DistalPhalanxBoneDirectionZ += hand2Finger5DistalPhalanxBoneDirection[2]
                    hand2Finger5TipPositionX += hand2Finger5.joint_position(3)[0]
                    hand2Finger5TipPositionY += hand2Finger5.joint_position(3)[1]
                    hand2Finger5TipPositionZ += hand2Finger5.joint_position(3)[2]
            previousFrame = frame


        ans += str(sumHands/self.NUM_FRAME_GRABS) + ','
        ans += str(sumFingers/self.NUM_FRAME_GRABS) + ','
        ans += str(sumTranlsationX/self.NUM_FRAME_GRABS) + ','
        ans += str(sumTranslationY/self.NUM_FRAME_GRABS) + ','
        ans += str(sumTranslationZ/self.NUM_FRAME_GRABS) + ','
        ans += str(rotationAxisX/self.NUM_FRAME_GRABS) + ','
        ans += str(rotationAxisY/self.NUM_FRAME_GRABS) + ','
        ans += str(rotationAxisZ/self.NUM_FRAME_GRABS) + ','
        ans += str(rotationAngle/self.NUM_FRAME_GRABS) + ','


        # hand1Type = 0
        ans += str(hand1DirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1DirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1DirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1PalmPositionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1PalmPositionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1PalmPositionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1GrabStrength/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1PinchStrength/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Confidence/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1ArmDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1ArmDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1ArmDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1ArmCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1ArmCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1ArmCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1TranslationX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1TranslationY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1TranslationZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1RotationAxisX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1RotationAxisY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1RotationAxisZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1RotationAngle/self.NUM_FRAME_GRABS) + ','

        ans += str(hand2DirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2DirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2DirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2PalmPositionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2PalmPositionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2PalmPositionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2GrabStrength/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2PinchStrength/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Confidence/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2ArmDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2ArmDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2ArmDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2ArmCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2ArmCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2ArmCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2TranslationX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2TranslationY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2TranslationZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2RotationAxisX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2RotationAxisY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2RotationAxisZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2RotationAngle/self.NUM_FRAME_GRABS) + ','

        ans += str(hand1Finger1DirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1DirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1DirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1MetacarpalCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1MetacarpalCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1MetacarpalCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1MetacarpalDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1MetacarpalDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1MetacarpalDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1ProximalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1ProximalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1ProximalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1ProximalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1ProximalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1ProximalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1IntermediatePhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1IntermediatePhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1IntermediatePhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1IntermediatePhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1IntermediatePhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1IntermediatePhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1DistalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1DistalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1DistalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1DistalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1DistalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1DistalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1TipPositionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1TipPositionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger1TipPositionZ/self.NUM_FRAME_GRABS) + ','

        ans += str(hand1Finger2DirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2DirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2DirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2MetacarpalCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2MetacarpalCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2MetacarpalCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2MetacarpalDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2MetacarpalDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2MetacarpalDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2ProximalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2ProximalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2ProximalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2ProximalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2ProximalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2ProximalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2IntermediatePhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2IntermediatePhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2IntermediatePhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2IntermediatePhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2IntermediatePhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2IntermediatePhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2DistalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2DistalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2DistalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2DistalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2DistalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2DistalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2TipPositionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2TipPositionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger2TipPositionZ/self.NUM_FRAME_GRABS) + ','

        ans += str(hand1Finger3DirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3DirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3DirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3MetacarpalCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3MetacarpalCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3MetacarpalCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3MetacarpalDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3MetacarpalDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3MetacarpalDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3ProximalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3ProximalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3ProximalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3ProximalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3ProximalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3ProximalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3IntermediatePhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3IntermediatePhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3IntermediatePhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3IntermediatePhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3IntermediatePhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3IntermediatePhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3DistalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3DistalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3DistalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3DistalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3DistalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3DistalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3TipPositionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3TipPositionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger3TipPositionZ/self.NUM_FRAME_GRABS) + ','

        ans += str(hand1Finger4DirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4DirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4DirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4MetacarpalCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4MetacarpalCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4MetacarpalCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4MetacarpalDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4MetacarpalDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4MetacarpalDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4ProximalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4ProximalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4ProximalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4ProximalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4ProximalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4ProximalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4IntermediatePhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4IntermediatePhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4IntermediatePhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4IntermediatePhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4IntermediatePhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4IntermediatePhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4DistalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4DistalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4DistalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4DistalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4DistalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4DistalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4TipPositionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4TipPositionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger4TipPositionZ/self.NUM_FRAME_GRABS) + ','

        ans += str(hand1Finger5DirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5DirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5DirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5MetacarpalCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5MetacarpalCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5MetacarpalCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5MetacarpalDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5MetacarpalDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5MetacarpalDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5ProximalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5ProximalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5ProximalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5ProximalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5ProximalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5ProximalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5IntermediatePhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5IntermediatePhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5IntermediatePhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5IntermediatePhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5IntermediatePhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5IntermediatePhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5DistalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5DistalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5DistalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5DistalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5DistalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5DistalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5TipPositionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5TipPositionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand1Finger5TipPositionZ/self.NUM_FRAME_GRABS) + ','

        ans += str(hand2Finger1DirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1DirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1DirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1MetacarpalCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1MetacarpalCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1MetacarpalCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1MetacarpalDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1MetacarpalDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1MetacarpalDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1ProximalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1ProximalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1ProximalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1ProximalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1ProximalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1ProximalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1IntermediatePhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1IntermediatePhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1IntermediatePhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1IntermediatePhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1IntermediatePhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1IntermediatePhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1DistalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1DistalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1DistalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1DistalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1DistalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1DistalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1TipPositionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1TipPositionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger1TipPositionZ/self.NUM_FRAME_GRABS) + ','

        ans += str(hand2Finger2DirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2DirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2DirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2MetacarpalCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2MetacarpalCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2MetacarpalCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2MetacarpalDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2MetacarpalDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2MetacarpalDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2ProximalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2ProximalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2ProximalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2ProximalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2ProximalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2ProximalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2IntermediatePhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2IntermediatePhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2IntermediatePhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2IntermediatePhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2IntermediatePhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2IntermediatePhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2DistalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2DistalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2DistalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2DistalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2DistalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2DistalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2TipPositionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2TipPositionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger2TipPositionZ/self.NUM_FRAME_GRABS) + ','

        ans += str(hand2Finger3DirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3DirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3DirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3MetacarpalCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3MetacarpalCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3MetacarpalCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3MetacarpalDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3MetacarpalDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3MetacarpalDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3ProximalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3ProximalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3ProximalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3ProximalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3ProximalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3ProximalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3IntermediatePhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3IntermediatePhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3IntermediatePhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3IntermediatePhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3IntermediatePhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3IntermediatePhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3DistalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3DistalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3DistalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3DistalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3DistalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3DistalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3TipPositionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3TipPositionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger3TipPositionZ/self.NUM_FRAME_GRABS) + ','

        ans += str(hand2Finger4DirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4DirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4DirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4MetacarpalCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4MetacarpalCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4MetacarpalCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4MetacarpalDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4MetacarpalDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4MetacarpalDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4ProximalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4ProximalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4ProximalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4ProximalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4ProximalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4ProximalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4IntermediatePhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4IntermediatePhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4IntermediatePhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4IntermediatePhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4IntermediatePhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4IntermediatePhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4DistalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4DistalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4DistalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4DistalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4DistalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4DistalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4TipPositionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4TipPositionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger4TipPositionZ/self.NUM_FRAME_GRABS) + ','

        ans += str(hand2Finger5DirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5DirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5DirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5MetacarpalCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5MetacarpalCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5MetacarpalCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5MetacarpalDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5MetacarpalDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5MetacarpalDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5ProximalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5ProximalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5ProximalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5ProximalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5ProximalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5ProximalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5IntermediatePhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5IntermediatePhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5IntermediatePhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5IntermediatePhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5IntermediatePhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5IntermediatePhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5DistalPhalanxBoneCenterX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5DistalPhalanxBoneCenterY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5DistalPhalanxBoneCenterZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5DistalPhalanxBoneDirectionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5DistalPhalanxBoneDirectionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5DistalPhalanxBoneDirectionZ/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5TipPositionX/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5TipPositionY/self.NUM_FRAME_GRABS) + ','
        ans += str(hand2Finger5TipPositionZ/self.NUM_FRAME_GRABS)


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
