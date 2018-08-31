# SpeakEasy
An inability to communicate well often creates barriers that are nearly impossible to take down. 

SpeakEasy was built to help people improve their communicaiton skills by recording a video of them speaking, and then using deep learning and computer vision to give them useful feedback on where they can improve. 

## Team
* Fenil Doshi, Rohit Saha - worked on the deep learning and computer vision scripts using Jupyter Notebook
* Samuel Zhang, Tyler Jiang - built the web interface with HTML, CSS, JavaScript, Flask, and Python

Checkout a limited demo of the project here: [Front-end Demo](https://tyj144.github.io/speakeasy-frontend/)

## Recording the User
The user records themselves speaking (as if they are presenting or pitching something), then presses the "Analyze" button.
![Webcam](https://github.com/tyj144/speakeasy/blob/master/webcam.png)

## Breakdown of Video
The application performs an analysis of the video, telling you what your emotions were like, as well as places where you could switch up your word choice.
![Breakdown of Speech](https://github.com/tyj144/speakeasy/blob/master/breakdown_3.png)

_We had some issues integrating the video analysis scripts with the web app itself, so the application currently displays the analysis of one of our pre-recorded videos._

## Home Page
The landing page (inspired by the [Stripe design](https://stripe.com/)).
![Home Page](https://github.com/tyj144/speakeasy/blob/master/home.png)
