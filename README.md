# RF2217 server for connecting ESP32 to a Raspberry PI

[![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD_3_Clause-yellow.svg)](./LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/cybergear-robotics/esp_rfc2217_server/graphs/commit-activity)
[![Language](https://img.shields.io/badge/Language-Python_3.8-purple.svg)](https://www.python.org/downloads/release/python-380/)

If you would like to connect to an Espressif SoC that is not directly connected to your system, you can use a remote serial port. This is useful when the chip is on a different machine, or for example when using WSL on Windows.

It is possible to connect to any networked remote serial port that supports RFC2217 (Telnet) protocol. To do this, specify the serial port to esptool as rfc2217://<host>:<port>. For example, to read information about your chip’s SPI flash, run:

This repository bases on the tool `esp_rfc2217_server.py` which is provided by the esptool. Instead of using RTS and DTR lines, the code uses two dedicated Raspberry PI GPIOs for restarting
and entering the ESP DFU (bootloader) mode. This code is only tested with a Raspberry PI 4 and ESP32S3.

## Schematics

* Raspberry Pi GPIO: 31 ->  BOOT Pin (ESP32S3)
* Raspberry Pi GPIO: 3 ->  EN Pin (ESP32S3)

* Raspberry Pi TX UART3: 7 ->  GPIO 43/UOTXD (ESP32S3)
* Raspberry Pi RX UART3: 29 ->  GPIO 44/UORXD (ESP32S3)

## On Raspberry PI:

As the UART 3 is used on the Raspberry PI 4, the required overlay should be enabled in `boot/config.txt`:

```
dtoverlay=uart3
```

The server runs on the Raspberry PI:

```
esp_rfc2217_server.py -p 5555 -b 115200 -v /dev/ttyAMA3 --boot-pin=31 --enable-pin=3
```

## On client:
```
esptool.py --port rfc2217://ADDRESS_OF_PI:5555?ign_set_control flash_id
```

## References

* [Remote Serial Ports by Espressif](https://docs.espressif.com/projects/esptool/en/latest/esp32/remote-serial-ports.html)
* [PySerial - RFC2217](https://pyserial.readthedocs.io/en/latest/url_handlers.html#rfc2217)
* [IETF RFC2217](https://datatracker.ietf.org/doc/html/rfc2217.html)