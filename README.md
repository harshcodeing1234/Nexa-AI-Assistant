# Nexa AI - Voice Assistant

**Version 1.5** | Released March 2026

A Python-based voice assistant powered by SambaNova's DeepSeek-V3.1 AI that can perform various tasks through voice commands.

## Features

### Core Features
- **Voice Recognition**: Listens and responds to voice commands with 5-second phrase limit
- **AI Chat**: Conversational AI using SambaNova's DeepSeek-V3.1 model (200 token responses)
- **Text-to-Speech**: Female voice (Zira) responses with adjustable speed (default: 130 WPM)
- **Web Navigation**: Opens any website via voice command with smart fallback
- **YouTube Integration**: Play songs/videos directly on YouTube
- **Application Launcher**: Launch 10+ system applications (Notepad, Calculator, Chrome, VS Code, CMD, PowerShell, Word, Excel, PowerPoint, Outlook, Camera)

### System Control & Monitoring
- **Time Query**: Get current time via voice
- **System Stats**: Check battery percentage, CPU usage, and RAM usage
- **Volume Control**: Mute/unmute system audio using nircmd
- **Screenshot**: Capture and save screenshots automatically
- **Power Management**: Shutdown and restart with voice confirmation
- **System Cleanup**: Clean temporary files with file count report

### Advanced Features
- **AI Prompts**: Generate AI responses and auto-save to SambaNova folder
- **Chat History**: View complete conversation history with the AI
- **Chat Reset**: Clear conversation history on demand
- **News Headlines**: Fetch top 5 US news headlines via NewsAPI
- **Task Manager**: Add, remove, and list personal tasks
- **Timer**: Set countdown timers with voice notification
- **Jokes**: Get random programming jokes or API-fetched jokes
- **Wikipedia Search**: Quick 2-sentence Wikipedia summaries
- **Smart Search**: Automatic fallback to Google search for unknown queries

## Prerequisites

- Python 3.13+
- Microphone for voice input
- Internet connection
- SambaNova API key
- NewsAPI key (optional, for news feature)

## Installation

1. Clone or download this repository

2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

4. Install required packages:
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install speechrecognition pyttsx3 pywhatkit wikipedia openai psutil pyautogui streamlit pyaudio
```

5. Add your SambaNova API key in `config.py`:
```python
api_key = "YOUR_SAMBANOVA_API_KEY_HERE"
news_api_key = "YOUR_NEWSAPI_KEY_HERE"  # Optional
```

## Usage

Run the main program:
```bash
python main.py
```

### Voice Commands

**Open Websites:**
- "Open YouTube"
- "Open Google"
- "Open Wikipedia"
- "Open ChatGPT"
- "Open Instagram/Facebook/Twitter/LinkedIn"
- "Open GitHub"
- "Open Amazon/Flipkart"
- "Open Gmail/Drive"
- "Open Netflix/Hotstar/Spotify"
- "Open WhatsApp Web"

**Open Applications:**
- "Open Notepad/Calculator/Chrome/VS Code"
- "Open CMD/PowerShell"
- "Open Word/Excel/PowerPoint/Outlook"
- "Open Camera"

**System Commands:**
- "What's time" - Get current time
- "Battery" - Check battery percentage
- "CPU" - Check CPU usage
- "RAM" - Check RAM usage
- "Screenshot" - Capture screenshot
- "Mute/Unmute" - Control system volume
- "Shutdown/Restart" - Power management (with confirmation)
- "Clean system" - Remove temporary files

**AI Features:**
- "Using AI [question]" - Generate AI response and save to file
- "Play [song name]" - Play song on YouTube
- "Chat history" - View conversation history
- "Reset chat" - Clear chat history
- "Wikipedia [topic]" - Get Wikipedia summary

**Task Management:**
- "Add task [task name]" - Add a new task
- "Remove task [task name]" - Remove a task
- "Show tasks/List tasks" - Display all tasks

**Other Features:**
- "News" - Get top 5 US news headlines
- "Timer" - Set a countdown timer (will ask for seconds)
- "Joke" - Get a random joke

**General Chat:**
- Ask any question for conversational AI response

## Project Structure

```
Nexa AI/
├── main.py           # Main application file
├── config.py         # API key configuration
├── pyttsx.py         # Text-to-speech module
├── requirements.txt  # Python dependencies
├── nircmd.exe        # Volume control utility
├── .gitignore        # Git ignore rules
├── SambaNova/        # Saved AI prompt responses
└── venv/             # Virtual environment
```

## Files Description

- **main.py**: Core application with voice recognition, AI integration, and command processing
- **config.py**: Stores SambaNova and NewsAPI keys
- **pyttsx.py**: Custom text-to-speech engine with female voice configuration
- **nircmd.exe**: Windows utility for system volume control

## Configuration

### Voice Settings
Modify speech speed in `pyttsx.py`:
```python
speak(message, speed=120)  # Adjust speed (default: 130)
```

### AI Model
Change AI model in `main.py`:
```python
model="DeepSeek-V3.1"  # SambaNova model
```

## Notes

- Ensure microphone permissions are granted
- API key must be valid and have sufficient quota
- Generated AI responses are saved in the `SambaNova/` folder
- Chat history persists until "reset chat" command or program restart

## Troubleshooting

**Microphone not working:**
- Check microphone permissions
- Verify microphone is set as default input device

**API errors:**
- Verify API key is correct in `config.py`
- Check internet connection
- Ensure API quota is not exceeded

**Voice recognition errors:**
- Speak clearly near the microphone
- Reduce background noise
- Check if `speech_recognition` is properly installed

## License

This project is for educational purposes.

## Version History

### Version 1.5 (March 2026) - Current Release
**Major Changes:**
- Migrated from Google Gemini to SambaNova's DeepSeek-V3.1 AI model
- Enhanced application launcher with 10+ apps (added Chrome, VS Code, CMD, PowerShell, Word, Excel, PowerPoint, Outlook, Camera)
- Added system monitoring features (Battery, CPU, RAM usage)
- Implemented volume control (Mute/Unmute) using nircmd utility
- Added screenshot capture functionality
- Implemented power management (Shutdown/Restart with confirmation)
- Added system cleanup feature for temporary files
- Integrated NewsAPI for top 5 US news headlines
- Added task management system (Add, Remove, List tasks)
- Implemented countdown timer with voice notification
- Added joke feature with API integration and fallback jokes
- Enhanced Wikipedia search with 2-sentence summaries
- Improved smart search with automatic Google fallback
- Added phrase time limit (5 seconds) for voice recognition
- Configured AI responses to 200 tokens max
- Set default TTS speed to 130 WPM

**New Commands:**
- Battery, CPU, RAM status checks
- Mute/Unmute system audio
- Screenshot capture
- Shutdown/Restart system
- Clean system temporary files
- News headlines
- Task management (Add/Remove/List)
- Timer functionality
- Joke command
- Wikipedia search

### Version 1.0 (Initial Release)
**Core Features:**
- Basic voice recognition and command processing
- Google Gemini AI integration for conversational chat
- Text-to-speech with female voice (Zira)
- Website navigation (YouTube, Google, social media, etc.)
- YouTube song/video playback
- Basic application launcher (Notepad, Calculator)
- Time query functionality
- AI prompt generation and file saving
- Chat history viewing
- Chat reset functionality

## Security Warning

⚠️ **Important**: The `config.py` file contains an exposed API key. For production use:
- Never commit API keys to version control
- Use environment variables instead
- Regenerate the exposed API key immediately
