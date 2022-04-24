Yaaay this builds and runs now! d1a9b0b80a2883a843b7ca03fde3798e11a2d5a4

I can run this

```python
from machine import Pin, SPI
from ssd1306 import SSD1306_SPI
width = 128
height = 64
SPI2_HOST = 2  # appears in esp-who/components/modules/lcd/who_lcd.c
hspi = SPI(SPI2_HOST)
dc = Pin(7)
rst = Pin(11)
cs = Pin(8)
display = SSD1306_SPI(width, height, hspi, dc, rst, cs)
```

And nothing breaks. I can call `.text` and `.show` and `poweroff` and `poweron`... but nothing changes.

Lots of mystery numbers need to be figured out in `modules/*.py`. A good reference for that would be the [esp-who driver code](https://github.com/espressif/esp-who/tree/master/components/screen/controller_driver/ssd1306).

---

Notes:

My environment when I successfully built this "board":

```
declare -x COLORFGBG="7;0"
declare -x COLORTERM="truecolor"
declare -x COMMAND_MODE="unix2003"
declare -x HOME="/Users/bob"
declare -x IDF_PATH="/Users/bob/git/esp-idf"
declare -x IDF_PYTHON_ENV_PATH="/Users/bob/.espressif/python_env/idf4.4_py3.9_env"
declare -x IDF_TOOLS_EXPORT_CMD="/Users/bob/git/esp-idf/export.sh"
declare -x IDF_TOOLS_INSTALL_CMD="/Users/bob/git/esp-idf/install.sh"
declare -x ITERM_PROFILE="Default"
declare -x ITERM_SESSION_ID="w0t2p0:97EFAC01-32B4-4799-81D5-FF59349803F4"
declare -x LANG="en_US.UTF-8"
declare -x LC_TERMINAL="iTerm2"
declare -x LC_TERMINAL_VERSION="3.4.15"
declare -x LOGNAME="bob"
declare -x LaunchInstanceID="7DA423B2-46D8-4E70-B47E-C7C56E4411A0"
declare -x OLDPWD="/Users/bob/git/micropython/ports/esp32/boards/ESP32_S3_EYE"
declare -x OPENOCD_SCRIPTS="/Users/bob/.espressif/tools/openocd-esp32/v0.11.0-esp32-20211220/openocd-esp32/share/openocd/scripts"
declare -x PATH="/Users/bob/git/esp-idf/components/esptool_py/esptool:/Users/bob/git/esp-idf/components/espcoredump:/Users/bob/git/esp-idf/components/partition_table:/Users/bob/git/esp-idf/components/app_update:/Users/bob/.espressif/tools/xtensa-esp32-elf/esp-2021r2-patch3-8.4.0/xtensa-esp32-elf/bin:/Users/bob/.espressif/tools/xtensa-esp32s2-elf/esp-2021r2-patch3-8.4.0/xtensa-esp32s2-elf/bin:/Users/bob/.espressif/tools/xtensa-esp32s3-elf/esp-2021r2-patch3-8.4.0/xtensa-esp32s3-elf/bin:/Users/bob/.espressif/tools/riscv32-esp-elf/esp-2021r2-patch3-8.4.0/riscv32-esp-elf/bin:/Users/bob/.espressif/tools/esp32ulp-elf/2.28.51-esp-20191205/esp32ulp-elf-binutils/bin:/Users/bob/.espressif/tools/esp32s2ulp-elf/2.28.51-esp-20191205/esp32s2ulp-elf-binutils/bin:/Users/bob/.espressif/tools/openocd-esp32/v0.11.0-esp32-20211220/openocd-esp32/bin:/Users/bob/.espressif/python_env/idf4.4_py3.9_env/bin:/Users/bob/git/esp-idf/tools:/Library/Frameworks/Python.framework/Versions/3.11/bin:/usr/local/opt/coreutils/libexec/gnubin:/Users/bob/.cargo/bin:/Users/bob/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/TeX/texbin"
declare -x PWD="/Users/bob/git/micropython/ports/esp32"
declare -x RUST_BACKTRACE="1"
declare -x SECURITYSESSIONID="186a8"
declare -x SHELL="/bin/bash"
declare -x SHLVL="1"
declare -x SSH_AUTH_SOCK="/private/tmp/com.apple.launchd.RR7KXcQCBv/Listeners"
declare -x TERM="xterm-256color"
declare -x TERM_PROGRAM="iTerm.app"
declare -x TERM_PROGRAM_VERSION="3.4.15"
declare -x TERM_SESSION_ID="w0t2p0:97EFAC01-32B4-4799-81D5-FF59349803F4"
declare -x TMPDIR="/var/folders/sy/zc4fnbpj0ql5b1rn1l7404cr0000gn/T/"
declare -x USER="bob"
declare -x XPC_FLAGS="0x0"
declare -x XPC_SERVICE_NAME="0"
declare -x __CFBundleIdentifier="com.googlecode.iterm2"
declare -x __CF_USER_TEXT_ENCODING="0x0:0:0"
```
