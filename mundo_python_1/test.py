# Uso para testar modificaçoes nos coodigos separadamente

import time
import pyautogui
# paint
pyautogui.press('win')
pyautogui.write('Paint')
pyautogui.press('enter')
pyautogui.moveTo(360,88)
# cofig 
pyautogui.moveTo(1679,496)
pyautogui.click()
pyautogui.moveTo(857,108)
pyautogui.click()
pyautogui.moveTo(889,313)
pyautogui.click()
pyautogui.mouseDown(379,275)
# s
pyautogui.click(interval=0.3)
pyautogui.mouseDown(318,311)
pyautogui.mouseDown(183,319)
pyautogui.mouseDown(209,420)
pyautogui.mouseDown(332,410)
pyautogui.mouseDown(351,538)
pyautogui.mouseDown(217,522)
# o
time.sleep(0.3)
pyautogui.click(interval=0.3)

pyautogui.mouseDown(453,288)
pyautogui.mouseDown(589,299)
pyautogui.mouseDown(581,532)
pyautogui.mouseDown(451,516)
pyautogui.mouseDown(453,288)
# u
time.sleep(0.3)
pyautogui.click(interval=0.3)

pyautogui.mouseDown(664,293)
pyautogui.mouseDown(672,524)
pyautogui.mouseDown(800,530)
pyautogui.mouseDown(782,309)
# g
time.sleep(0.3)
pyautogui.click(interval=0.3)

pyautogui.mouseDown(908,630)
pyautogui.mouseDown(767,622)
pyautogui.mouseDown(741,784)
pyautogui.mouseDown(905,788)
pyautogui.mouseDown(892,707)
pyautogui.mouseDown(820,702)
# A
time.sleep(0.3)
pyautogui.click(interval=0.3)

pyautogui.mouseDown(960,787)
pyautogui.mouseDown(1026,630)
pyautogui.mouseDown(1059,774)
pyautogui.mouseDown(1044,712)
pyautogui.mouseDown(993,705)
# Y
time.sleep(0.3)
pyautogui.click(interval=0.3)

pyautogui.mouseDown(1226,627)
pyautogui.mouseDown(1130,778)
pyautogui.mouseDown(1183,700)
pyautogui.mouseDown(1138,635)

pyautogui.mouseUp()
