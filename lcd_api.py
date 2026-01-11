import time

class LcdApi:
    LCD_CLR = 0x01
    LCD_HOME = 0x02
    LCD_ENTRY_MODE = 0x04
    LCD_DISPLAY_CONTROL = 0x08
    LCD_FUNCTION_SET = 0x20
    LCD_SET_CGRAM_ADDR = 0x40
    LCD_SET_DDRAM_ADDR = 0x80

    def __init__(self, num_lines, num_columns):
        self.num_lines = num_lines
        self.num_columns = num_columns
        self.cursor_x = 0
        self.cursor_y = 0
        self.backlight = True

    def clear(self):
        self.hal_write_command(self.LCD_CLR)
        time.sleep_ms(2)
        self.cursor_x = 0
        self.cursor_y = 0

    def move_to(self, cursor_x, cursor_y):
        self.cursor_x = cursor_x
        self.cursor_y = cursor_y
        addr = cursor_x & 0x3f
        if cursor_y & 1: addr += 0x40
        if cursor_y & 2: addr += self.num_columns
        self.hal_write_command(self.LCD_SET_DDRAM_ADDR | addr)

    def putstr(self, string):
        for char in string:
            self.putchar(char)

    def putchar(self, char):
        if char == '\n':
            self.cursor_x = 0
            self.cursor_y += 1
            if self.cursor_y >= self.num_lines: self.cursor_y = 0
            self.move_to(self.cursor_x, self.cursor_y)
        else:
            self.hal_write_data(ord(char))
            self.cursor_x += 1
            if self.cursor_x >= self.num_columns: self.putchar('\n')

    def hal_write_command(self, cmd): raise NotImplementedError
    def hal_write_data(self, data): raise NotImplementedError