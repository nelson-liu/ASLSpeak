################################################################################
# Written by Nicholas Bowman and Nelson Liu                                    #
# DubHacks 2015                                                                #
# Last modified 10/17/15                                                       #
# This class recieves sign language input from the Leap Motion, and then       #
# decodes it and outputs it as audio (speaks it).                              #
################################################################################

import subprocess
import urllib2
import Leap
import json
from GenerateTrainingSet import GenerateTrainingSet

class Translator():
    def classify(self, gestureData):
        dataList = gestureData.split(",");
        dataList.insert(0, "");
        print dataList;
        print len(dataList);
        data =  {

        "Inputs": {
            "input1":{
                    "ColumnNames": ["Col1", "Col2", "Col3", "Col4", "Col5", "Col6", "Col7", "Col8", "Col9", "Col10", "Col11", "Col12", "Col13", "Col14", "Col15", "Col16", "Col17", "Col18", "Col19", "Col20", "Col21", "Col22", "Col23", "Col24", "Col25", "Col26", "Col27", "Col28", "Col29", "Col30", "Col31", "Col32", "Col33", "Col34", "Col35", "Col36", "Col37", "Col38", "Col39", "Col40", "Col41", "Col42", "Col43", "Col44", "Col45", "Col46", "Col47", "Col48", "Col49", "Col50", "Col51", "Col52", "Col53", "Col54", "Col55", "Col56", "Col57", "Col58", "Col59", "Col60", "Col61", "Col62", "Col63", "Col64", "Col65", "Col66", "Col67", "Col68", "Col69", "Col70", "Col71", "Col72", "Col73", "Col74", "Col75", "Col76", "Col77", "Col78", "Col79", "Col80", "Col81", "Col82", "Col83", "Col84", "Col85", "Col86", "Col87", "Col88", "Col89", "Col90", "Col91", "Col92", "Col93", "Col94", "Col95", "Col96", "Col97", "Col98", "Col99", "Col100", "Col101", "Col102", "Col103", "Col104", "Col105", "Col106", "Col107", "Col108", "Col109", "Col110", "Col111", "Col112", "Col113", "Col114", "Col115", "Col116", "Col117", "Col118", "Col119", "Col120", "Col121", "Col122", "Col123", "Col124", "Col125", "Col126", "Col127", "Col128", "Col129", "Col130", "Col131", "Col132", "Col133", "Col134", "Col135", "Col136", "Col137", "Col138", "Col139", "Col140", "Col141", "Col142", "Col143", "Col144", "Col145", "Col146", "Col147", "Col148", "Col149", "Col150", "Col151", "Col152", "Col153", "Col154", "Col155", "Col156", "Col157", "Col158", "Col159", "Col160", "Col161", "Col162", "Col163", "Col164", "Col165", "Col166", "Col167", "Col168", "Col169", "Col170", "Col171", "Col172", "Col173", "Col174", "Col175", "Col176", "Col177", "Col178", "Col179", "Col180", "Col181", "Col182", "Col183", "Col184", "Col185", "Col186", "Col187", "Col188", "Col189", "Col190", "Col191", "Col192", "Col193", "Col194", "Col195", "Col196", "Col197", "Col198", "Col199", "Col200", "Col201", "Col202", "Col203", "Col204", "Col205", "Col206", "Col207", "Col208", "Col209", "Col210", "Col211", "Col212", "Col213", "Col214", "Col215", "Col216", "Col217", "Col218", "Col219", "Col220", "Col221", "Col222", "Col223", "Col224", "Col225", "Col226", "Col227", "Col228", "Col229", "Col230", "Col231", "Col232", "Col233", "Col234", "Col235", "Col236", "Col237", "Col238", "Col239", "Col240", "Col241", "Col242", "Col243", "Col244", "Col245", "Col246", "Col247", "Col248", "Col249", "Col250", "Col251", "Col252", "Col253", "Col254", "Col255", "Col256", "Col257", "Col258", "Col259", "Col260", "Col261", "Col262", "Col263", "Col264", "Col265", "Col266", "Col267", "Col268", "Col269", "Col270", "Col271", "Col272", "Col273", "Col274", "Col275", "Col276", "Col277", "Col278", "Col279", "Col280", "Col281", "Col282", "Col283", "Col284", "Col285", "Col286", "Col287", "Col288", "Col289", "Col290", "Col291", "Col292", "Col293", "Col294", "Col295", "Col296", "Col297", "Col298", "Col299", "Col300", "Col301", "Col302", "Col303", "Col304", "Col305", "Col306", "Col307", "Col308", "Col309", "Col310", "Col311", "Col312", "Col313", "Col314", "Col315", "Col316", "Col317", "Col318", "Col319", "Col320", "Col321", "Col322", "Col323", "Col324", "Col325", "Col326", "Col327", "Col328", "Col329", "Col330", "Col331", "Col332", "Col333", "Col334", "Col335", "Col336", "Col337", "Col338", "Col339", "Col340", "Col341", "Col342", "Col343", "Col344", "Col345", "Col346", "Col347", "Col348", "Col349", "Col350", "Col351", "Col352", "Col353", "Col354"],
                    "Values": [dataList,]
            },
        },
            "GlobalParameters": {}
        }

        body = str.encode(json.dumps(data))
        url = 'https://ussouthcentral.services.azureml.net/workspaces/43729486c1584499a4c7ad0ce8606446/services/5d419297cdc54379b0436c111fdce50f/execute?api-version=2.0&details=true'
        api_key = 'cZi1QbYjighLTuhB+3DtaTirlYjEIXlXBG4BhZWz+2dIFqupoBids7fxfh3lgER1se3AeBwe1Twgthnb9tjbrg==' # Replace this with the API key for the web service
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
        req = urllib2.Request(url, body, headers)
        response = urllib2.urlopen(req)
        result = response.read()
        resultsJSON = json.loads(result)
        predictedLetter = resultsJSON["Results"]["output1"]["value"]["Values"][0][-1];
        print predictedLetter
        confidence = resultsJSON["Results"]["output1"]["value"]["Values"][0][-2];
        print confidence
        return predictedLetter


def main():
    
     # Create a translation object
    translator = Translator()

            # create an object to capture gestures
    gestureListener = GenerateTrainingSet()

            # create a leap controller
    controller = Leap.Controller()


            # Receive gesture data from the Leap Motion, and then send it to our
            # Azure ML classification web service.
    classificationResult = translator.classify(gestureListener.captureGesture(controller))

            # Form bash command to say.
    bashCommand = "say \"" + classificationResult + "\""
    subprocess.Popen(bashCommand, shell = True)


if __name__ == "__main__":
    main()
