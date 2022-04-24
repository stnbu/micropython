include("$(PORT_DIR)/boards/manifest.py")

freeze("./modules", ["s3eye.py", "s3eye_lcd.py"])
freeze("$(MPY_DIR)/drivers/display", "ssd1306.py")
