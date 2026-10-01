# SPDX-FileCopyrightText: 2024 Johannes Fischer
#
# SPDX-License-Identifier: BSD-3-Clause
import time
import RPi.GPIO as GPIO

class GPIOReset:
    def __init__(self, en_pin: int, boot_pin: int):
        self._en_pin = en_pin
        self._boot_pin = boot_pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self._boot_pin, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self._en_pin, GPIO.OUT, initial=GPIO.HIGH)


    def cleanup(self):
        GPIO.cleanup()

    def bootloader_reset(self):
        """reset and enter DFU/bootloader/download mode"""
        GPIO.output(self._boot_pin, GPIO.HIGH)
        GPIO.output(self._en_pin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(self._boot_pin, GPIO.LOW)
        GPIO.output(self._en_pin, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(self._boot_pin, GPIO.HIGH)

    def hard_reset(self):
        """only hard-reset ESP32 without entering DFU"""
        GPIO.output(self._en_pin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(self._en_pin, GPIO.HIGH)
