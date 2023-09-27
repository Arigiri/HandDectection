# Hand drawing game

**Introduction**

This game is written on purpose of introducing the popular of A.I and Computer Vision. An filter that can draw by nose on tiktok influnce me to do this.

**Purpose of the game**

This game require you to draw the correct shape by moving your index finger tip.

**How this work**

### Hand detection

Using ***mediapipe*** library, you can preview on this [Google Mediapipe](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker)

Detect index finger tip at the index `8` and tracking the moving of the hand.
[Image of mediapipe](link)

**Track the hand moving**

Every time udpate the ***index finger tip point*** update, append that point to an array to track it.

**How to check the correction between your draw and goal shape**

***Dice Coefficient***
*Dice Coefficient* measures how similar a set and another set are.
[Dice Coefficient formula](link)
Result
[Picture result](link)


