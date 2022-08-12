# Dennis-LF2--detection-Cascade-Classifier
 

Referring to [1], we design a detection algorithm based on a cascade classifier to locate the character named Dennis while playing the well-known fighting game---Little fighter 2. Firstly, we developed a window capture software to capture Dennis's movements, such as walking, jumping, and being hit by other characters. With the frames of Dennis's actions, we can establish the positive images to train our cascade classifier. We then utilize opencv_annotation.exe [2] to crop the region of interest on positive images to extract the main features of Dennis. And we export the positive.vec with the aid of opencv_createsamples.exe [2]. On the other hand, we capture some scenes without Dennis to gain our negative images. Finally, we trained the cascade classifier through opencv_traincascade.exe [2] with 16 stages. The result shows that the detection algorithm works well.  





![image](https://user-images.githubusercontent.com/108604868/184274974-82d122e8-f8dd-4029-aaf2-61cafc7bd8fb.png)






https://user-images.githubusercontent.com/108604868/184274990-d94bfc43-efa9-4844-8708-5486b16f7c01.mp4








# Reference
[1] Training a Cascade Classifier - OpenCV Object Detection in Games #8:  
https://www.youtube.com/watch?v=XrCAvs9AePM&ab_channel=LearnCodeByGaming .   
[2] Cascade Classifier Training:  
https://docs.opencv.org/4.2.0/dc/d88/tutorial_traincascade.html .
