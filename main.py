import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

from utils.SpeechToText import record_audio, transcribe_audio

from OpenAI.streamCommand import openai

demo = False

def start_driver():
    """Initializes the Chrome WebDriver."""
    chrome_browser_binary_path = "binaries\\chrome-win64\\chrome-win64\\chrome.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_browser_binary_path

    chrome_driver_path = "binaries\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
    chrome_service = ChromeService(chrome_driver_path)

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return driver

def click_restaurants(driver):
    """Clicks on the 'Restaurants' button in Google Maps."""
    try:
        restaurants_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Restaurants']/ancestor::button"))
        )
        print("Restaurants button found:", restaurants_button)
        restaurants_button.click()
        print("Clicked on the Restaurants button.")
    except Exception as e:
        print("Error: Restaurants button not found or not clickable.", e)

def generate_function(prompt):
    """Generates a Python code snippet based on the given prompt."""
    # Assuming you have a working connection to OpenAI API for code generation
    response = openai.get(f'generate a python code snippet that will: {prompt}')
    print(response)

    # Example of what the generated function might look like
    func_name = "click_restaurants"  # Example function name
    func_param = "driver"  # Example parameter
    func_body = "driver.get('https://www.google.com/maps/search/restaurants')"  # Example body
    new_function = f"def {func_name}({func_param}):\n   {func_body}"
    
    return new_function

def run_function(command):
    """Executes the dynamically generated function."""
    try:
        exec(command)  # Use Python's exec() to run the dynamically created function
        print("Command executed.")
    except Exception as e:
        print("Error with generated function:", e)

def main():
    """Main function that runs the entire program."""
    driver = start_driver()

    url = "https://www.google.com/"  # Replace with the specific Google Maps URL
    driver.get(url)

    quit_program = False
    while not quit_program:
        input("Press any key to start recording: ")

        # Record and transcribe audio
        output_file = "output.wav"
        transcription_file = "transcription.txt"

        try:
            print("Recording audio...")
            record_audio(output_file, duration=3)  # Record audio for 3 seconds
            print("Transcribing audio...")
            transcribe_audio(output_file, transcription_file)  # Save transcription to a file
            print("Audio transcribed successfully.")
        except Exception as e:
            print("Error with audio processing:", e)

        # Open the transcription file and read its content
        with open(transcription_file, 'r') as file:
            transcription_content = file.read()
            print(f"Done recording, I heard: {transcription_content}")

            # Check transcription content and perform actions accordingly
            transcription_lower = transcription_content.lower()
            if "restaurants" in transcription_lower:
                print("The transcription contains 'restaurants'. Triggering action...")
                click_restaurants(driver)
            elif "back" in transcription_lower or "previous" in transcription_lower:
                driver.back()
            elif "forward" in transcription_lower or "next" in transcription_lower:
                driver.forward()
            elif "quit" in transcription_lower:
                quit_program = True
            elif "google maps" in transcription_lower:
                driver.get("https://www.google.com/maps")
            else:
                if demo:
                    driver.get(f"https://www.google.com/maps/search/{transcription_lower}/")
                else:
                    # Use OpenAI to generate a Python snippet based on the transcription
                    command = generate_function(transcription_lower)
                    run_function(command)

    # Close the WebDriver
    driver.quit()
    print("Program finished.")

if __name__ == "__main__":
    main()
