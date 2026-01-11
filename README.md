# Laser Maze Tripwire Project

This project is a beginner-friendly Raspberry Pi “spy mission” style **laser tripwire** setup. You can test the laser, LED, and buzzer modules before building the full maze with sensors.


## 🛠️ Project Overview

- **Goal:** Create a real-world “laser maze” where breaking a laser beam triggers an alarm (LED + buzzer).  
- **Components:** Laser, LDR (photoresistor), 10kΩ resistor, LED via MOSFET driver, buzzer, Raspberry Pi.  
- **Learning Outcomes:**  
  - Raspberry Pi GPIO control  
  - Breadboard wiring basics  
  - Using sensors to trigger outputs  
  - Simple Python programming

## 🔌 Current Setup

### 1. Laser Module
- 3-pin 5V laser module  
- Connections:
  - **VCC (+)** → 5V rail on breadboard (Pi Pin 2)  
  - **GND (−)** → GND rail on breadboard (Pi Pin 6)  
  - **S pin** → red rail (5V) for now (laser always ON; later will connect to GPIO for control)  

### 2. LED via MOSFET
- Connect MOSFET input to a GPIO pin  
- Power LED module from 5V and GND rails  

### 3. Buzzer Module
- **VCC** → 5V rail  
- **GND** → GND rail  
- **Signal** → GPIO pin  

### 4. LDR (Photoresistor) — **Not Connected Yet**
- Wait until you get a **10kΩ resistor**  
- Will use as a voltage divider to detect laser beam interruptions safely

## 📝 Python Scripts

### `test_each_component.py`
- Tests **Laser**, **LED**, and **Buzzer** individually  
- Press **Enter** to move between components  
- Turns each ON for 3 seconds, then OFF  
- Cleans up GPIO after testing  

**Next Steps:** Once LDR + resistor are ready, the script can be extended to detect the **beam being blocked** and trigger the alarm automatically.

## ⚡ Safety Notes
- **Do not connect LDR directly to GPIO** without resistor — could damage Pi  
- Keep laser **pointed safely**; avoid shining in eyes  
- MOSFET protects Pi from LED high current, always double-check wiring  


## 📌 Reminders for Next Session
1. **Buy a 10kΩ resistor** for the LDR voltage divider  
2. Wire **LDR + resistor** in series between 5V and GND  
3. Connect the **signal row** to a GPIO pin for beam detection  
4. Update Python script to:  
   - Detect beam broken  
   - Trigger buzzer and LED when beam is interrupted  
5. Consider controlling **laser S pin with GPIO** to turn lasers on/off programmatically  
6. Plan multiple lasers for a **full maze setup**  


## 💡 Tips for Breadboard Wiring
- Red rail → 5V  
- Blue rail → GND  
- Keep LDR + resistor on separate rows for easy troubleshooting  
- Label wires or color-code for clarity


# Adding Laser Module 

- Connect Raspberry in +/- (4 Power; 14 Ground)
- Add Laser inside breadboard (a-e) in its own row
- Connect +/- with Laser breadboard row
- Connect Raspberry Pie GPIO 17 (Pin 11) with S inside breadboard

