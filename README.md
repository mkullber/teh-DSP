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
