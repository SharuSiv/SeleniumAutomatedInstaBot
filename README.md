# SeleniumAutomatedInstaBot
Developed a Selenium-based automated bot using PyCharm, designed to proactively engage with users by sending automated messages and managing friend requests. This versatile bot enhances user engagement and attracts new followers by autonomously interacting with the platform's community.

How to use the bot:

create an account, or have an instagram account which you would like to use to send automatic replies

Clone the repository in the directory of your choosing:

$ git clone https://github.com/SharuSiv/SeleniumAutomatedInstaBot

change directory into the cloned directory

$ cd SeleniumAutomatedInstaBot

open the project in an IDE of your choice (I used PyCharm for this project)

Before starting the program you would need to place messages you would like to send users in line 34:


![image](https://github.com/SharuSiv/SeleniumAutomatedInstaBot/assets/122399531/a21bb4e6-004a-4996-8e07-884069f32220)


Run the program and you will recieve two prompts to input your username and password

make sure that the username and password are correct!

The terminal will then ask you if you would like to send friend requests. You need to ensure that the username is accurately sent to the terminal or you would risk sending a friend request to the wrong user.

After you are done sending requests the exception handling will start catching exceptions. I placed the max amount of tries to 10. After the program tries to find user messages 10 times it will automatically exit and close the browser. if you would like your program to run longer, you can change the amount of retries in line 49: 


![image](https://github.com/SharuSiv/SeleniumAutomatedInstaBot/assets/122399531/412af916-98ab-4223-a83f-e2a351b18355)
