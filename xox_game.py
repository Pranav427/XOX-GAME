import streamlit as st

# --- Game Logic ---
def check_winner(board):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

def make_move(index):
    board = st.session_state.board
    if board[index] == "" and not check_winner(board):
        board[index] = st.session_state.current_player
        winner = check_winner(board)
        if winner:
            st.session_state.scores[winner] += 1
        else:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# --- Page Config ---
st.set_page_config("XOX Game", layout="wide")
st.title("❌⭕ XOX Game")

# --- Initialize State ---
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.scores = {"X": 0, "O": 0, "Draw": 0}

# --- Scoreboard (Auto Layout) ---
st.markdown("## 📊 Scoreboard")
score_cols = st.columns(3)
score_cols[0].metric("Player X", st.session_state.scores["X"])
score_cols[1].metric("Player O", st.session_state.scores["O"])
score_cols[2].metric("Draws", st.session_state.scores["Draw"])

# --- Responsive Game Grid ---
st.markdown("## 🎮 Game Board")
rows = [st.columns(3) for _ in range(3)]
for i in range(3):
    for j in range(3):
        idx = i * 3 + j
        with rows[i][j]:
            st.button(
                label=st.session_state.board[idx] or " ",
                key=idx,
                on_click=make_move,
                args=(idx,),
                use_container_width=True  # Makes it stretch full width
            )

# --- Winner Display ---
winner = check_winner(st.session_state.board)
if winner:
    st.success(f"🎉 {winner} wins!" if winner != "Draw" else "🤝 It's a Draw!")

# --- Control Buttons ---
control_cols = st.columns(2)
if control_cols[0].button("🔄 Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"

if control_cols[1].button("🗑️ Reset Scores"):
    st.session_state.scores = {"X": 0, "O": 0, "Draw": 0}
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
