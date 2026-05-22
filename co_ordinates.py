from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Clicked at → X: {x}, Y: {y}")

# Start listening
with mouse.Listener(on_click=on_click) as listener:
    print("Click anywhere to get coordinates... Press CTRL+C to stop.")
    listener.join()