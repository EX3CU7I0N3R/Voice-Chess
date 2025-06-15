# 🎤 Voice Chess

A visually interactive chess game playable by **voice commands**!  
Built with Python, Pygame, SpeechRecognition, and pyttsx3 for a fun, accessible chess experience.

---

## 🧩 Stack & Methodologies

- **Python 3.8+**
- **Pygame** for GUI rendering
- **python-chess** for chess logic
- **SpeechRecognition** for voice input (Google Speech API)
- **pyttsx3** for offline text-to-speech feedback
- **OOP & Modular Design**: Clean, readable, and extensible codebase
- **Accessibility**: All spoken feedback is also printed to the console

---

## 🚀 Features

- Play chess using your voice: say moves like `E2 to E4` or `Knight to F3`
- Ask about the board:  
  - "Where are my knights?"  
  - "What is on E4?"  
  - "Last move" or "Summarize"
- Visual board with highlighted last move
- Audio feedback for moves, captures, and game state
- Handles common voice recognition errors (e.g., "night" → "knight")
- Opponent plays random legal moves

---

## 🖥️ Installation & First Run

### 1. **Clone the repository**
```bash
git clone https://github.com/yourusername/voice-chess.git
cd voice-chess
```

### 2. **Install dependencies**
It's recommended to use a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Mac/Linux

pip install -r requirements.txt
```

**requirements.txt** should contain:
```
pygame
python-chess
SpeechRecognition
pyttsx3
pyaudio
```
> **Note:**  
> On Windows, if you have trouble installing `pyaudio`, download the appropriate `.whl` from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install with `pip install <filename>.whl`.

### 3. **Download Assets**
- Ensure the `assets/` folder contains all required chess piece images (e.g., `white_king.png`, `black_queen.png`, etc.).
- Place move/capture sound files in a `sounds/` folder (`move_sound.wav`, `capture_sound.wav`).

### 4. **Run the Game**
```bash
python gui_board.py
```

---

## 🎮 How to Play

- **Say your move:**  
  `"E2 to E4"`, `"Knight to F3"`, etc.
- **Ask for info:**  
  `"Where are my bishops?"`, `"What is on D5?"`, `"Last move"`, `"Summarize"`
- **Quit:**  
  Say `"quit"`, `"exit"`, or close the window.

---

## 📝 Notes

- Requires an internet connection for Google Speech Recognition.
- All spoken feedback is also printed to the terminal for accessibility.
- If you have a microphone issue, check your system settings and ensure `pyaudio` is installed.

---


## 🤝 Contributing

Pull requests and suggestions are welcome!  
Please open an issue for bugs or feature requests.

---

## 📄 License

MIT License

---

**Enjoy playing chess with your voice!**
