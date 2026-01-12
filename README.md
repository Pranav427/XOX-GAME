# ❌⭕ XOX Game (Tic-Tac-Toe) using Streamlit

## 📌 Project Overview
This is a simple and interactive **XOX (Tic-Tac-Toe) game** built using **Streamlit**.  
The game supports two players (X and O), maintains a live scoreboard, and provides a clean, responsive user interface.

It demonstrates the use of **session state**, **UI components**, and **event-driven logic** in Streamlit.

---

## 🎯 Features
- Two-player XOX game (Player X vs Player O)
- Automatic winner and draw detection
- Live scoreboard for X, O, and Draws
- Responsive 3×3 game board layout
- Restart game and reset score options
- Clean and simple UI

---

## ⚙️ Technologies Used
- Python
- Streamlit

---

## 📂 Project Structure

XOX-Game/
│ ---
├── app.py # Main Streamlit application ---
└── README.md # Project documentation
---


---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies
pip install streamlit

### 2️⃣ Run the application
streamlit run app.py

### 3️⃣ Open in browser
The app will open automatically at:
http://localhost:8501

---

## 🎮 How to Play
1. Player X starts the game
2. Players take turns clicking on the grid
3. First player to align 3 symbols (row, column, or diagonal) wins
4. If all cells are filled with no winner, the game ends in a draw
5. Use **Restart Game** to play again
6. Use **Reset Scores** to clear the scoreboard

---

## 📈 Game Logic
- The board is managed using `st.session_state`
- Winner is checked after every move
- Scores update automatically
- Draws are detected when the board is full

---

## ⭐ Why This Project Matters
- Demonstrates Streamlit fundamentals
- Shows event-driven UI handling
- Uses session state effectively
- Beginner-friendly but well-structured project
- Good mini project for Python / Streamlit portfolios

---

## ✅ Status
Completed

---

## 👤 Author
Pranav Obili 
