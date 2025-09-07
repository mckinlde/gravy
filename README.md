# gravy

A voice command interface to a web browser; uses LLM code generation to operate a webdriver

Flowchart:

Voice -> JSON
JSON -> AI command
AI command -> DOM (inspect element)
Selenium *click*
UI updates as though user clicked with mouse

Repo Structure:

/:
- main.py: Entry point / game loop, listens for voice commands, calls LLM APIs to generate code, and executes code as needed
- prompt.text: System prompt, wraps voice commands in main.py
- output.wav: Placeholder file for recorded voice commands

/utils/:
- driver_session.py: wrapper for webdriver session management, abstracts Selenium WebDriver state from the rest of the app.
- SpeechToText.py: wrapper for [recording / transcribing audio](https://pypi.org/project/SpeechRecognition/)
- SPA_utils.py: Utility functions for Single Page Application (SPA) interactions using Selenium.

/logs/:
- /html_captures/: folder for holding HTML file snapshots saved by webdriver
- /browser_console/: folder for holding browser console snapshots saved by webdriver
- /stderr/: folder for holding local console output

TODO: I want to conditionally use /logs/ as LLM input for agentic debugging while managing context window

/OpenAI/
- streamCommand.py: wrapper for handling OpenAI API



## Snippets:

### Add python to PowerShell Path:
```
$env:Path = "C:\Python313;$env:Path"
```
### .venv:
```
python -m venv .venv
.venv\Scripts\activate
```
### update requirements.txt:
```
pip freeze > requirements.txt
```

Bye!