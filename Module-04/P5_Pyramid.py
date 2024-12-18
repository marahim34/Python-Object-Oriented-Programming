import pyautogui
import time

n = int(input("Enter the number of rows for the pyramid: "))

pyramid = "\n".join("#" * i for i in range(1, n + 1))

with open("pyramid_output.txt", "w") as file:
    file.write(pyramid)

print("Pyramid has been written to 'pyramid_output.txt'.")

print("Open a text editor and place the cursor where you want the pyramid to appear.")
time.sleep(5)  

for line in pyramid.split("\n"):
    pyautogui.typewrite(line) 
    pyautogui.press("enter") 

print("Pyramid typing complete!")
