# Echo
Echo is an intelligent, environment-aware smart cane that acts as assistive tech for the visually or mentally impaired. Echo uses Computer Vision based Machine Learning to train and recognize the faces it sees an match them with names. 
___
## Overview

Today, over 5 million Americans are living with Alzheimer's. In fact, 1 in 10 people of age 65 and older has Alzheimer's or dementia. Often, those afflicted will have trouble remembering names from faces and recalling memories.

Right now, there's no assistive technology to help Alzheimer's patients remember people or recall faces. What if we could build a solution to this problem affecting millions worldwide??

**Echo does exactly that!**

Echo is an intelligent, environment-aware smart cane that acts as assistive tech for the visually or mentally impaired.

<!-- Echo is a piece of assistive technology that  -->


Our tech helps the owner keep track of people they meet and help the owner feel safer by letting them call assistance with the push of a button if they feel like they're in danger.

Using cameras, microphones, and state of the art artificial intelligence software including facial recognition, natural language processing, and speech to text software, Echo is able recognize familiar and new faces allowing patients to confidently meet new people and learn more about the world around them.

When Echo hears an introduction being made, it uses its camera to continuously train itself to recognize the person. Then, if it sees the person again it'll notify its owner that the acquaintance is there. Echo also has a button that, when pressed, will contact the authorities- this way, if the owner is in danger, help is one tap away.

## Frameworks and APIs
* Remembering Faces
  * OpenCV Facial Detection
  * OpenCV Facial Recognition
* Analyzing Speech
  * Google Cloud Speech-To-Text
  * Google Cloud Natural Language Processing
* IoT Communications
  * gstreamer for making TCP video and audio streams
  * SMTP for email capabilities (to contact authorities and relatives)

## Echo: The Hacking Process

There are many moving parts to Echo. We had to integrate an interface between Natural Language Processing and Facial Recognition. Furthermore, we had to manage a TCP stream between the Raspberry Pi, which interacts with our ML backend on a computer. Ensuring that all the parts seamlessly work involved hours of debugging and unit testing. Furthermore, we had to fine tune parameters such as stream quality to ensure that the Facial Recognition worked but we did not experience high latency.

Echo attempts to solve a simple problem: individuals with Alzheimer's often forget faces easily and need assistance in order to help them socially and functionally in the real world. We rely on the fact that by using AI/ML, we can train a model to help the individual in a way that other solutions cannot. By integrating this with technology like Natural Language Processing, we can create natural interfaces to an important problem.

We wanted to make sure that the form factor of our hack could be experience just by looking at it. On our cane, we have a Raspberry Pi, a camera, and a button. The button is a distress signal, which will alert the selected contacts in the event of an emergency. The camera is part of the TCP stream that is used for facial recognition and training. The stream server and recognition backend are managed by separate Python scripts on either end of the stack. This results in a stable connection between the smart cane and the backend system.

## Empowering the impaired

Echo empowers the impaired to become more independent and engage in their daily routines. This smart cane acts both as a helpful accessory that can catalyze social interaction and also a watchdog to quickly call help in an emergency. Currently Echo provides assistance in certain use cases, however it can be expanded to encompass much more. Echo is meant to be a convenient, embedded way to assist the elderly or visually impaired, and is a platform which can be added on to in the future. Features such as localization and navigation for the visually impaired and GPS tracking for individuals with Alzheimer's are both extremely useful and easily integratable into the Echo framework. This is only an echo of what it could be in the future.  


