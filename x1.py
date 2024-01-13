import pygame
import numpy as np

# تعریف ابعاد اتاق
ROOM_WIDTH, ROOM_HEIGHT = 16, 16

# تعریف ابعاد و رنگ‌ها
CELL_SIZE = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# تعریف اتاق به صورت شطرنجی با خانه‌های کثیف رندوم
room = np.zeros((ROOM_HEIGHT, ROOM_WIDTH))
for i in range(ROOM_HEIGHT):
    for j in range(ROOM_WIDTH):
        if np.random.random() < 0.3:
            room[i, j] = 1


class Object:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        new_x = dx
        new_y = dy
        self.x = new_x
        self.y = new_y


def draw_room(screen):
    for i in range(ROOM_HEIGHT):
        for j in range(ROOM_WIDTH):
            cell_color = WHITE
            border_color = BLACK
            if room[i, j] == 1:
                cell_color = GREEN
            pygame.draw.rect(screen, cell_color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, border_color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)


def draw_object(screen, obj):
    pygame.draw.circle(screen, BLUE, (obj.x * CELL_SIZE + CELL_SIZE // 2, obj.y * CELL_SIZE + CELL_SIZE // 2),
                       CELL_SIZE // 2)


def draw_end_screen(screen):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 40)
    text1 = font.render("Room is Clear", True, BLACK)
    text2 = font.render("Start Again", True, BLACK)
    text3 = font.render("Exit", True, BLACK)

    screen.blit(text1, (150, 200))
    pygame.draw.rect(screen, BLACK, (200, 300, 200, 50), 2)
    screen.blit(text2, (220, 310))
    pygame.draw.rect(screen, BLACK, (200, 400, 200, 50), 2)
    screen.blit(text3, (250, 410))


def main():
    pygame.init()
    screen = pygame.display.set_mode((ROOM_WIDTH * CELL_SIZE, ROOM_HEIGHT * CELL_SIZE))
    pygame.display.set_caption("جارو برقی")

    running = True
    current_row, current_col = 0, 0

    # ایجاد یک جسم و قرار دادن آن در خانه اول
    obj = Object(0, 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if current_row >= ROOM_HEIGHT:
            if np.sum(room) == 0:
                # اتاق تمیز است
                pygame.display.set_caption("اتاق تمیز است")
                draw_end_screen(screen)
                pygame.display.flip()

                while True:
                    event = pygame.event.wait()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        running = False
                        break
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if 200 <= event.pos[0] <= 400 and 300 <= event.pos[1] <= 350:
                            # شروع مجدد
                            current_row, current_col = 0, 0
                            room.fill(0)
                            for i in range(ROOM_HEIGHT):
                                for j in range(ROOM_WIDTH):
                                    if np.random.random() < 0.3:
                                        room[i, j] = 1
                            obj = Object(0, 0)
                            pygame.display.set_caption("جارو برقی")
                            screen.fill(BLACK)
                            break
                        elif 200 <= event.pos[0] <= 400 and 400 <= event.pos[1] <= 450:
                            # خروج از برنامه
                            pygame.quit()
                            running = False
                            break

        if running:
            # بررسی خانه فعلی
            if room[current_row, current_col] == 1:
                room[current_row, current_col] = 0

            screen.fill(BLACK)
            draw_room(screen)
            obj.move(current_col, current_row)
            draw_object(screen, obj)

            pygame.display.flip()

            pygame.time.delay(200)  # مکث 1 ثانیه

            # انتقال به خانه بعدی
            if current_row % 2 == 0:
                current_col += 1
                if current_col >= ROOM_WIDTH:
                    current_row += 1
                    current_col = ROOM_WIDTH - 1
            else:
                current_col -= 1
                if current_col < 0:
                    current_row += 1
                    current_col = 0

            if current_row >= ROOM_HEIGHT:
                pygame.display.set_caption("اتاق تمیز است")

    pygame.quit()


if __name__ == "__main__":
    main()
