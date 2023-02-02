def map_wiimote_to_key(wiimote_index, wiimote_button, key):
    if wiimote[wiimote_index].buttons.button_down(wiimote_button):
        keyboard.setKeyDown(key)
    else:
        keyboard.setKeyUp(key)

def update():
    map_wiimote_to_key(0, WiimoteButtons.A, Key.Z)
    map_wiimote_to_key(0, WiimoteButtons.B, Key.X)
    
def nunchuckupdate():
    if wiimote[0].nunchuck.buttons.button_down(NunchuckButtons.Z):
        keyboard.setKeyDown(Key.Space)
    else:
        keyboard.setKeyUp(Key.Space)
        
    if wiimote[0].nunchuck.buttons.button_down(NunchuckButtons.C):
        keyboard.setKeyDown(Key.C)
    else:
        keyboard.setKeyUp(Key.C)
      
	if wiimote[0].nunchuck.stick.y > 50:
		keyboard.setKeyDown(Key.UpArrow)
		keyboard.setKeyUp(Key.DownArrow)
	elif wiimote[0].nunchuck.stick.y < -50:
		keyboard.setKeyDown(Key.DownArrow)
		keyboard.setKeyUp(Key.UpArrow)
	else:
		keyboard.setKeyUp(Key.DownArrow)
		keyboard.setKeyUp(Key.UpArrow)
	
	if wiimote[0].nunchuck.stick.x > 50:
		keyboard.setKeyDown(Key.RightArrow)
		keyboard.setKeyUp(Key.LeftArrow)
	elif wiimote[0].nunchuck.stick.x < -50:
		keyboard.setKeyDown(Key.LeftArrow)
		keyboard.setKeyUp(Key.RightArrow)
	else:
		keyboard.setKeyUp(Key.LeftArrow)
		keyboard.setKeyUp(Key.RightArrow)

if starting:
    wiimote[0].buttons.update += update
    wiimote[0].nunchuck.update += nunchuckupdate