import pygame
import numpy as np
import os

# Initialize pygame
pygame.init()

# Set grid dimensions
rows, cols = 9, 7
cell_size = 50
margin = 2
width = cols * cell_size + (cols + 1) * margin + 200
height = rows * cell_size + (rows + 1) * margin + 100  # Extra space for the button and dropdown

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("9x7 Grid Drawing")

# Create grid state (0 for white, 1 for black)
grid = np.zeros((rows, cols), dtype=int)

# Initialize data storage
submissions = []
selected_number = 0
mouse_pressed = False
current_mouse_button = None

# Ensure the data directory exists
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "grid_data_dir")
os.makedirs(data_dir, exist_ok=True)

def draw_grid():
    screen.fill(GRAY)
    for row in range(rows):
        for col in range(cols):
            color = BLACK if grid[row, col] == 1 else WHITE
            pygame.draw.rect(
                screen,
                color,
                [
                    margin + col * (cell_size + margin),
                    margin + row * (cell_size + margin),
                    cell_size,
                    cell_size,
                ],
            )

    # Draw submit button
    pygame.draw.rect(screen, BLUE, [button_x, button_y, button_width, button_height])
    font = pygame.font.Font(None, 24)
    text = font.render("Submit", True, WHITE)
    text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    screen.blit(text, text_rect)

    # Draw dropdown label
    dropdown_label = font.render("Select File Number:", True, BLACK)
    screen.blit(dropdown_label, (dropdown_label_x, dropdown_label_y))

    # Draw dropdown options
    for i in range(10):
        option_color = BLUE if i == selected_number else WHITE
        pygame.draw.rect(
            screen,
            option_color,
            [dropdown_x, dropdown_y + i * (dropdown_height + margin), dropdown_width, dropdown_height]
        )
        option_text = font.render(str(i), True, BLACK)
        option_text_rect = option_text.get_rect(center=(dropdown_x + dropdown_width // 2, dropdown_y + i * (dropdown_height + margin) + dropdown_height // 2))
        screen.blit(option_text, option_text_rect)

# Button dimensions
button_width = 100
button_height = 40
button_x = (width - button_width) // 2
button_y = height - 60

# Dropdown dimensions
dropdown_width = 50
dropdown_height = 30
dropdown_x = margin + 450

# Dropdown label position
dropdown_label_x = margin + 400
dropdown_label_y = height - 500

# Adjust dropdown position
dropdown_y = dropdown_label_y + 30

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            # Check grid area
            col = (pos[0] - margin) // (cell_size + margin)
            row = (pos[1] - margin) // (cell_size + margin)

            # Check if click is within grid bounds
            if 0 <= row < rows and 0 <= col < cols:
                if event.button == 1:  # Left click
                    grid[row, col] = 1
                    current_mouse_button = 1
                    mouse_pressed = True
                elif event.button == 3:  # Right click
                    grid[row, col] = 0
                    current_mouse_button = 3
                    mouse_pressed = True

            # Check if Submit button is clicked
            if event.button == 1:  # Left click
                if button_x <= pos[0] <= button_x + button_width and button_y <= pos[1] <= button_y + button_height:
                    # Submit button clicked
                    vector = grid.flatten()
                    submissions.append(vector.tolist())

                    # Save to file
                    file_name = f"{selected_number}_grid_data.txt"
                    file_path = os.path.join(data_dir, file_name)
                    with open(file_path, "a") as f:
                        f.write(f"x{len(submissions)}: {vector.tolist()}\n")

                    # Reset grid
                    grid.fill(0)

                # Check if dropdown option is clicked
                for i in range(10):
                    option_rect = pygame.Rect(dropdown_x, dropdown_y + i * (dropdown_height + margin), dropdown_width, dropdown_height)
                    if option_rect.collidepoint(pos):
                        selected_number = i

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button in [1, 3]:  # Left or right click released
                mouse_pressed = False
                current_mouse_button = None

        elif event.type == pygame.MOUSEMOTION:
            if mouse_pressed:
                pos = pygame.mouse.get_pos()
                col = (pos[0] - margin) // (cell_size + margin)
                row = (pos[1] - margin) // (cell_size + margin)
                
                if 0 <= row < rows and 0 <= col < cols:
                    if current_mouse_button == 1:  # Left click
                        grid[row, col] = 1
                    elif current_mouse_button == 3:  # Right click
                        grid[row, col] = 0

    draw_grid()
    pygame.display.flip()

pygame.quit()

# Print confirmation
print(f"Saved {len(submissions)} submissions to corresponding files.")