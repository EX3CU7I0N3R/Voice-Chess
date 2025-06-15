from voice_control import listen_for_move, confirm_move

def test_voice():
    while True:
        move = listen_for_move()
        if move:
            confirmed = confirm_move()
            if confirmed:
                print(f"✅ Confirmed move: {move}")
                break
            else:
                print("❌ Move not confirmed. Let's try again.")

if __name__ == "__main__":
    test_voice()