# teh DSP

Note: this project is still WIP

## Project description

-   STM32 MCU works as USB audio class device to enable I2C audio output from computer it is connected to
-   STM32 I2S output is connected to ADAU1701 DSP IC
-   ADAU1701 is used as crossover, separate individual equalizers for main speakers & subwoofer and for volume control/mute/invert
-   ADAU1701 I2S output is connected to PCM5102A DAC, which outputs line level signal to amplifier
-   ADAU1701 analog audio output is connected to subwoofer
-   STM32 connects to ESP32 via serial connection. STM32 forwards volume change and mute events from computer to ESP32
-   ESP32 is connected to ADAU1701 with I2C. Volume level is set on ADAU1701
-   ESP32 has a web interface, which can be used to set volume, sub level, mute etc
-   ESP32 has ability to control subwoofer power with Tasmota based switch, like Sonoff S20

## Components

-   [ADAU1701 DSP board](https://store.sure-electronics.com/product/AA-AP23122)
-   [Interface extension kit](https://store.sure-electronics.com/product/AA-AA11428)
-   [ADAU1701 programmer](https://store.sure-electronics.com/product/DB-DP11219), [ESP-based programmer](https://ez.analog.com/dsp/sigmadsp/f/q-a/164008/sharing-tcpi-interface-for-sigma-studio-using-esp8266-or-esp32) should work too

## DSP program

![DSP program](/docs/dsp_program.png?raw=true)
