import machine

# 初始化 I2C (優化佈線：使用與 VIN 同側的 Pin 13/14)
i2c = machine.I2C(0, scl=machine.Pin(14), sda=machine.Pin(13))

print('I2C Scanner (Pins: SDA=13, SCL=14)')
devices = i2c.scan()

if len(devices) == 0:
    print("No I2C device found! 請檢查 G13/G14 接線是否鬆脫。")
else:
    print('I2C devices found:', len(devices))
    for device in devices:
        print("At address: ", hex(device))