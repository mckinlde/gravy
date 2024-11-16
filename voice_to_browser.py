from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

# Correct import statement for the custom module
from speechtoJSON.SpeechToText import record_audio, transcribe_audio

demo = False

def start_driver():
    # Specify 'options' as details for the Chrome Browser executable
    chrome_browser_binary_path = "binaries\chrome-win64\chrome-win64\chrome.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_browser_binary_path

    # Specify 'service' as details for the ChromeDriver executable
    chrome_driver_path = "binaries\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    chrome_service = ChromeService(chrome_driver_path) # https://github.com/orgs/community/discussions/44279

    # Use [chrome_options, chrome_service] in the webdriver constructor
    driver = webdriver.Chrome(service = chrome_service, options=chrome_options)
    return driver

def click_restaurants():
    try:
        # Wait for the "Restaurants" button to be clickable
        restaurants_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Restaurants']/ancestor::button"))
        )
        
        # Confirm success with a print statement
        print("Restaurants button found:", restaurants_button)
            
        # Optionally, click the button
        restaurants_button.click()
        print("Clicked on the Restaurants button.")

    except Exception as e:
        print("Error: Restaurants button not found or not clickable.", e)

def generate_function(prompt):
    # generate a click_restaurants function
    response = openai.get(f'generate a python code snippet that will: {prompt}')
    print(response)

    # func_name = "" # GET NAME
    # func_param = "" # GET PARAMETERS
    # func_body = "" # GET CODE

    # new_function = f"def {func_name}({func_param}):\n   {func_body}"
    # new_function()


def run_function():
    # run a click_restaurants function
    print("todo")

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the Google Maps page
url = "https://www.google.com/"  # Replace with the specific Google Maps URL
driver.get(url)

quit = False
while quit==False:
    # Wait for user input
    input("any key to start recording: ")

    # Record audio using the function imported from the custom module
    output_file = "output.wav"
    transcription_file = "transcription.txt"

    try:
        print("Recording audio...")
        record_audio(output_file, duration=3)  # Record audio for 5 seconds
        print("Transcribing audio...")
        transcribe_audio(output_file, transcription_file)  # Save transcription to a file
        print("Audio transcribed successfully.")
    except Exception as e:
        print("Error with audio processing:", e)

    # Open the transcription file and read its content
    with open(transcription_file, 'r') as file:
        transcription_content = file.read()  # Read the entire content of the file
        print(f"Done recording, I heard: {transcription_content}")
        
        # Check if the transcription content contains both "restaurants" and "click"
        if "restaurants" in transcription_content.lower():
            print("The transcription contains 'restaurants'. Triggering action...")
            # Add your code here to perform the desired action
            click_restaurants()
        elif "back" in transcription_content.lower() or "previous" in transcription_content.lower():
            driver.back()
        elif "forward" in transcription_content.lower() or "next"  in transcription_content.lower():
            driver.forward()
        elif "quit" in transcription_content.lower():
            quit = True
        elif "google maps" in transcription_content.lower():
            driver.get("https://www.google.com/maps")
        else:
            if demo:
                driver.get(f"https://www.google.com/maps/search/{transcription_content.lower()}/")
            else:
                # use openAI to generate a python snippet that does transcription_content.lower()
                command = generate_function(transcription_content.lower())
                # run the python snippet
                try:
                    # driver.command
                    print(command)
                    # TODO: command needs to be bound as a function and called, idk how to do that yet
                except Exception as e:
                    print("Error with generated function:", e)



try:
    print("prompt")
#     response
except Exception as e:
    print("Error: ", e)
finally:
    # Close the WebDriver
    driver.quit()
