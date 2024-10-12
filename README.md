# Assistive Navigation System for the Visually Impaired

## Overview

This project is designed to assist visually impaired individuals in safely navigating their surroundings using computer vision and proximity sensors. The system provides real-time audio feedback about obstacles and other environmental elements, allowing users to move confidently and independently. This solution is being developed for a hackathon challenge with the goal of improving mobility for people with visual impairments.

## System Components

1. **Four Cameras**: Mounted around the user’s head to capture a 360-degree view of the surroundings. The system processes these camera feeds to identify objects and obstacles like vehicles, stairs, and other potential hazards.
2. **Two Proximity Sensors**: Placed near the feet to detect obstacles close to the ground, ensuring safe movement.
3. **Audio Feedback**: Real-time audio descriptions are sent to the user through headphones, with instructions like "car on the left, 2 meters away" to help with navigation.
4. **Voice Commands**: Users can adjust the feedback settings by giving voice commands, customizing the type and frequency of notifications they receive.

## Features

- **Object and Obstacle Detection**: Identifies obstacles such as stairs, vehicles, and other hazards to ensure safe navigation.
- **Proximity Alerts**: Alerts users when obstacles are detected near their feet for safer movement in close quarters.
- **Customizable Feedback**: Voice commands allow users to personalize the audio feedback based on their preferences.
- **Real-Time Audio**: Immediate audio instructions help users understand their environment and make informed decisions about movement.

## Getting Started

The repository contains code to:
- Run object detection on the camera feeds using the YOLO model.
- Process data from proximity sensors to identify nearby obstacles.
- Provide real-time audio feedback to users based on the detected objects and their proximity.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vojtech-balek/abbccc-oko360.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Connect the cameras and proximity sensors to the system.
2. Run the object detection and navigation system:
   ```bash
   python assistive_nav.py
   ```
3. Use voice commands to configure feedback preferences.

## Future Enhancements

- Enhanced object detection for more complex environments.
- Integration of AI-based personalized navigation assistance.

---

This project aims to make navigation safer and more accessible for individuals with visual impairments using cutting-edge technology.
