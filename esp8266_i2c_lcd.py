import time
from lcd_api import LcdApi

MASK_RS = 0x01
MASK_RW = 0x02
MASK_E = 0x04
MASK_BACKLIGHT = 0x08
SHIFT_BACKLIGHT = 3

class I2cLcd(LcdApi):
    def __init__(self, i2c, i2c_addr, num_lines, num_columns):
        self.i2c = i2c
        self.i2c_addr = i2c_addr
        self.i2c.writeto(self.i2c_addr, bytearray([0]))
        time.sleep_ms(20)
        for val in [0x30, 0x30, 0x30, 0x20]:
            self.hal_write_init_nibble(val)
            time.sleep_ms(5)
        super().__init__(num_lines, num_columns)
        self.hal_write_command(0x28)
        self.hal_write_command(0x0C)
        self.hal_write_command(0x06)
        self.clear()

    def hal_write_init_nibble(self, nibble):
        byte = (nibble & 0xF0) | MASK_BACKLIGHT
        self.i2c.writeto(self.i2c_addr, bytearray([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytearray([byte]))

    def hal_write_command(self, cmd): self.hal_write_eight_bits(cmd, 0)
    def hal_write_data(self, data): self.hal_write_eight_bits(data, MASK_RS)

    def hal_write_eight_bits(self, value, mode):
        for val in [value & 0xF0, (value << 4) & 0xF0]:
            nibble = val | mode | (self.backlight << SHIFT_BACKLIGHT)
            self.i2c.writeto(self.i2c_addr, bytearray([nibble | MASK_E]))
            self.i2c.writeto(self.i2c_addr, bytearray([nibble]))