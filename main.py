import time, random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# for this project, used firefox as the webdriver
browser = webdriver.Firefox()
browser.implicitly_wait(5)

#driver navigates to instagram main page
browser.get('https://www.instagram.com/')
def login(username,password):
    #inserts the username and password, and logs in to instagram
    browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input").send_keys(username)
    browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input").send_keys(password)
    browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button").click()
    #clears the pop ups after login
    time.sleep(3)
    #clears the save your login info
    browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div").click()
    time.sleep(3)
    #clears the notification box
    browser.find_element(By.XPATH, "//button[text()='Not Now']").click()

def friendreq(user):
    #redirects to search page, sends username inputted in search field
    browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div").click()
    browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input").send_keys(user)
    # waits for search query to return results
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='x9f619 x78zum5 xdt5ytf x1iyjqo2 x6ikm8r x1odjw0f xh8yej3 xocp1fn']")))
    user_profile_link = browser.find_element(By.XPATH, "//a[contains(@href, '/" + user + "/')]")
    user_profile_link.click()
    browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div/button").click()

def message_reply():
    messages = ["PLACE MESSAGES HERE"]
    message_box = browser.find_element(By.XPATH, "//div[@aria-label='Message']")
    random_word = random.choice(messages)
    for char in random_word:
        message_box.send_keys(char)
        time.sleep(0.1)
    browser.find_element(By.XPATH, "//div[@class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1i0vuye x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37 xfs2ol5' and @role='button' and @tabindex='0']").click()
    browser.find_element(By.XPATH, "//a[@aria-label='Direct messaging - 0 new notifications link']").click()
# Function to continuously monitor incoming messages and respond
def monitor_messages():
    max_retries = 10  # Set the maximum number of retries
    retry_count = 0
    browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/div/span/div/a/div").click()

    while retry_count < max_retries:
        try:
            # Wait for the message input field to load
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]")))

            # Check if there are new messages
            new_messages = browser.find_element(By.CSS_SELECTOR, "*[class*='x1xc55vz']")

            # Check if the last message is from the other user (assuming last message is at the bottom)
            if new_messages:
                # Find the associated button element within the parent element
                button_element = new_messages.find_element(By.XPATH, "./..")

                # Perform actions on the button
                button_element.click()
                message_reply()
                # Wait for a while before checking again (adjust the sleep duration as needed)

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            retry_count+=1
            time.sleep(5)  # Wait before retrying


#main driver code here
username = input("type in the username of your bot: ")
password = input("type in the password of the bot: ")
login(username,password)
while True:
    user_input = input("Do you want to send a friend request (Y/N)? ").strip().upper()
    if user_input == 'N':
        break  # Exit the loop if the user enters 'N'
    elif user_input != 'Y':
        print("Invalid input. Please enter 'Y' or 'N'.")
        continue  # Prompt the user again for a valid input

    # Your code to be executed while the user input is 'Y' goes here
    username = input("Type the EXACT username of the person you would like to request:")
    friendreq(username)

monitor_messages()

browser.close()

