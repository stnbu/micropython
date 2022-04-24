#!/bin/sh -xue

PORTS_DIR=$(dirname $0)/../..
cd $PORTS_DIR

TTY=$(ls /tmp/tty.usbmodem*)

make="make BOARD=ESP32_S3_EYE PORT=$TTY"

$make submodules
$make

# maybe...
## /Users/mburr/.espressif/python_env/idf4.4_py3.9_env/bin/python ../../../esp-idf/components/esptool_py/esptool/esptool.py -p (PORT) -b 460800 --before default_reset --after no_reset --chip esp32s3  write_flash --flash_mode dio --flash_size detect --flash_freq 80m 0x0 build-ESP32_S3_EYE/bootloader/bootloader.bin 0x8000 build-ESP32_S3_EYE/partition_table/partition-table.bin 0x10000 build-ESP32_S3_EYE/micropython.bin
