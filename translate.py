################################################################################
# Written by Nicholas Bowman and Nelson Liu                                    #
# DubHacks 2015                                                                #
# Last modified 10/17/15                                                       #
# This class recieves sign language input from the Leap Motion, and then       #
# decodes it and outputs it as audio (speaks it).                              #
################################################################################

import subprocess
import requests
import Leap
from GenerateTrainingSet import GenerateTrainingSet

class Translator():
    def classify(self, gestureData):
        # Should only return data if confidence is above a certain threshold.
        return requests.post("AZURE URL HERE", data = "gestureData")

def main():
    while True:
        # Create a translation object
        translator = Translator()

        # create an object to capture gestures
        gestureListener = GenerateTrainingSet()

        # create a leap controller
        controller = Leap.Controller()


        # Receive gesture data from the Leap Motion, and then send it to our
        # Azure ML classification web service.
        classificationResult = translator.classify(gestureListener.generateGesture(controller))

        # Form bash command to say.
        bashCommand = "say \"" + classificationResult + "\""


if __name__ == "__main__":
    main()
