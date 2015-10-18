################################################################################
# Written by Nicholas Bowman and Nelson Liu                                    #
# DubHacks 2015                                                                #
# Last modified 10/17/15                                                       #
# This class recieves sign language input from the Leap Motion, and then       #
# decodes it and outputs it as audio (speaks it).                              #
################################################################################

import subprocess
import requests
from GenerationTrainingSet import captureGesture();

class Translator():
    def classify(self, gestureData):
        # Should only return data if confidence is above a certain threshold.
        return requests.post("AZURE URL HERE", data = "gestureData");

def main():
    # Create a translation object
    translator = Translator()

    # Receive gesture data from the Leap Motion, and then send it to our
    # Azure ML classification web service.
    classificationResult = translator.classify(captureGesture())

    # Form bash command to say.
    bashCommand = "say \"" + classificationResult + "\"";

    # If confidence in classification result is above some threshold, then say
    # the classificationResult.
    if(classificationConfidence > .8):
        subprocess.Popen(bashCommand)


if __name__ == "__main__":
    while True:
        main()
