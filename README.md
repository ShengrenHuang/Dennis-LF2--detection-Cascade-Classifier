# Dennis-LF2--detection-Cascade-Classifier

在本練習中，我們參考[1] 設計一個視窗擷取程式，可以擷取視窗程式的畫面，透過不同的按鍵來決定當前視窗程式的畫面是否為positive image 還是 negative image。我們使用的視窗程式是知名電玩遊戲LF2，我們在一開始將人物dennis 在遊戲舞台中走動，並擷取他走動與被挨揍的畫面，試圖擷取Dennis 的 haar 特徵，之後我們選擇其他非dennis的腳色，在不同競技舞台擷取negative 畫面。蒐集好訓練用的image後，我們透過opencv 的 文件 [2]，先利用opencv_annotation.exe 來crop positive的影像，擷取出dennis的畫面，之後透過 opencv_createsamples.exe 來製作 positive.vec 用此當作訓練cascade classifier 的sample，最後利用opencv_traincascade.exe 結合negative image 訓練 我們的 cascade classifier。在實驗中可以準確的判定dennis的位置與是否出現在畫面中。 



![image](https://user-images.githubusercontent.com/108604868/183297280-b6b7cf12-3df2-4435-8848-d1704321fcca.png)











# Reference
[1] https://www.youtube.com/watch?v=XrCAvs9AePM&ab_channel=LearnCodeByGaming
[2] https://docs.opencv.org/4.2.0/dc/d88/tutorial_traincascade.html
