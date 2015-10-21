# ASLSpeak
Decode sign language using the Leap Motion, and speak it!
Winner of "Best Overall Use of Microsoft Tech" and "Best Use of Data".
Built by
 - [Nelson Liu](https://github.com/nelson-liu/)
 - [Nick Bowman](https://github.com/nick-bowman)

in 24 hours at DubHacks 2015. [ASLSpeak on DevPost](http://devpost.com/software/aslspeak)

Dataset Details
================================

1. Title: Sign Language Recognition Data

2. Source Information
   -- Creators:
   - [Nelson Liu](https://github.com/nelson-liu/)
   - [Nick Bowman](https://github.com/nick-bowman)

3. Past Usage:
   -- "ASLSpeak", a project that utilizes machine learning to translate sign language to spoken word.

4. Relevant Information:

   The objective is to identify a gesture as one of the 26 letters in the sign language alphabet. We collected the data with the Leap Motion, and trimmed it to 534 features. We created 20 training examples for each of the 26 letters; given more time, we would definitely look to create more.

5. Number of Instances: 520

6. Number of Attributes: 534 (Letter category and 533 numeric features)

7. Attribute Information:
See line 1161 of [GenerateTrainingSet.py](https://github.com/nelson-liu/ASLSpeak/blob/master/GenerateTrainingSet.py)

8. Missing Attribute Values: None

9. Class Distribution:
 	20 A	20 B 20 C 20 D 20 E 20 F 20 G
 	20 H 20 I 20 J 20 K 20 L 20 M 20 N
 	20 O 20 P 20 Q 20 R 20 S 20 T 20 U
 	20 V 20 W 20 X 20 Y 20 Z
