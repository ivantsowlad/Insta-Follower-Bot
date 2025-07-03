from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

IG_LOGIN = "your_account_login"
IG_PASSWORD = "your_account_password"
IG_WEB = "https://www.instagram.com/"
SIMILAR_ACCOUNT = "account_with_followers"


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(f"{IG_WEB}accounts/login/")

        sleep(1)
        cookies = self.driver.find_element(By.CSS_SELECTOR, "button[class='_a9-- _ap36 _a9_1']")
        cookies.click()

        sleep(1)
        username = self.driver.find_element(By.CSS_SELECTOR, "input[name='username']")
        username.send_keys(IG_LOGIN)
        password = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password.send_keys(IG_PASSWORD)
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        sleep(15)
        reject_saving = self.driver.find_element(By.CSS_SELECTOR, "div[role='button']")
        reject_saving.click()

    def find_followers(self):
        sleep(2)
        self.driver.get(f"{IG_WEB}{SIMILAR_ACCOUNT}/followers")
        input("Press Enter after click on 'followers'.")
        modal_xpath = "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
        modal = self.driver.find_element(By.XPATH, value=modal_xpath)
        for i in range(50):
            print(i)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        popup_x = ("/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/"
                   "div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div")
        popup = self.driver.find_elements(By.XPATH, value=popup_x)
        print(f"Length of popup is: {len(popup)}")

        subscribed = 0
        for i in popup:
            sleep(0.5)
            follow_button_index = popup.index(i) + 2
            print(follow_button_index)
            follow_button_path = f"/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{follow_button_index}]/div/div/div/div[3]/div/button"
            follow_button = self.driver.find_element(By.XPATH, follow_button_path)
            print(follow_button.text)
            name = i.find_element(By.XPATH, "./div/div/div/div[2]/div/div/span/span")
            print(name.text)
            if follow_button.text == "Follow":
                follow_button.click()
                subscribed += 1
                print(f"I have subscribed: {subscribed}.")
            else:
                print("Subscribed, pass.")
                continue


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
