# Daily Bible Verse Script (Python)

Currently, the only script that matters is bot.py. Look at this file for reference. 

 ## User & Developer Guide

 ### Feature 1: command bot
 In a specified channel, type "!verse" and enter. Bible Bot will share the verse of the day. 
 
 ### Feature 2: message scheduler
 Bible Bot sends a verse everyday at a specified timestamp. 

 ### Customization & Generic Guideline:
 For developers, these two features in bot.py can be slightly modified based on goals that suit for various needs.
 1. Download the repo and modify the code. 
 2. Create an application on Discord Developer Console (Tons of tutorials online). Obtain the token. 
 3. Host the code somewhere that it can be executed constantly. i.e. Host it on a AWS server and run the script using screen command (see Useful Resource No.2 below).

 ## Where is the script hosted and run?

 AWS Lightsail - ubuntu

 ## Useful Resource: 

1. https://github.com/Dannycademy/nextcord-bot-series/tree/master

2. 
  - How to keep running remote script? - https://serverfault.com/questions/827997/run-remote-script-monitoring-his-activity-without-keeping-connection
  - how to exit screen? - inside screen, type exit
