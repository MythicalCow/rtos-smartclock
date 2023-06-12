**Video Demonstration**: https://youtu.be/1vFQBE2QWlg

# rtos-smartclock
A smart clock with weather, time, and alarm system using FreeRTOS. Custom quote is displayed on an 8x8 LED matrix. The system makes use of libraries such as Arduino_FreeRTOS, LedControl, LiquidCrystal for the Arduino script. For the Raspberry Pi script the serial, requests, and datetime libraries were used. The Raspberry Pi communicates with the Arduino over a serial protocol using a USB cable at a baudrate of 115200.
The various functions of the clock have been organized into several FreeRTOS tasks detailed below.

### readSerial
This task has the highest priority on the RTOS scheduler. When serial data is available from the Raspberry Pi the task reads this data into two strings which are used for the time and weather display on the LCD display. The system enters a critical task state while updating the variables that store time and weather to prevent other tasks from reading corrupted or incomplete data.

### updateLCD
This task updates the liquid crystal display every 1 second allowing the time and weather to be updated. It has the second highest priority after the readSerial task.

### updateLEDMatrix
This task updates the 8x8 LED Matrix using hexadecimal arrays of size 8. Each hexadecimal represents one row on the matrix. A separate array is used to tell this task which hexadecimal arrays to use to create the custom quote. After the quote is finished the task is paused for 20 seconds using the vTaskDelay functionality. The quote isn't incredibly important for clock functionality and hence has a lower priority.

### updateTime
This task updates the time every second manually to allow the clock to function without the clock synchronization from the raspberry pi in case the raspberry pi loses connection. This is mainly a backup task and hence has the lowest priority.

