# Button Class
class Button():
    # Initializing the button
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        # Button image
        self.image = image
        # Button position
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        # Button font
        self.font = font
        # Color when not hovered over
        self.base_color = base_color
        # Color when hovered over
        self.hovering_color = hovering_color
        # Text input
        self.text_input = text_input
        # Button text
        self.text = self.font.render(self.text_input, True, self.base_color)
        # If there's no button image, then set the button text as the image
        if self.image is None:
            self.image = self.text
        # Button rectangle
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
    
    # Update method, puts the button on the screen
    def update(self, screen):
        # If there is an image, blit it to the screen
        if self.image is not None:
            screen.blit(self.image, self.rect)
        # Blit the text to the screen
        screen.blit(self.text, self.text_rect)

    # Check for input method, checks whether the button is pressed
    def checkForInput(self, position):
        # If pressed, return True
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        # Otherwise return False
        return False
    
    # Change color method, checks whether the button is hovered over and changes the color
    def changeColor(self, position):
        # If hovered over, change the color to the hovered color
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        # Else leave it be
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

class ToggleButton(Button):
    # Initializing the button
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        super().__init__(image, pos, text_input, font, base_color, hovering_color)
        # Boolean indicating whether the button is toggled
        self.toggled = False
    
    # Check for input method, checks whether the button is pressed and toggles its state
    def checkForInput(self, position):
        # If pressed, toggle the state
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.toggled = not self.toggled
            return True
        # Otherwise return False
        return False
    
    # Change color method, checks whether the button is hovered over and changes the color
    def changeColor(self, position):
        # If hovered over, change the color to the hovered color
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            if not self.toggled:
                self.text = self.font.render(self.text_input, True, self.hovering_color)
        # Else leave it be
        else:
            if not self.toggled:
                self.text = self.font.render(self.text_input, True, self.base_color)
            else:
                self.text = self.font.render(self.text_input, True, self.hovering_color)   