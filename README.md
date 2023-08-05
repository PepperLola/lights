# PiLED
### A lights ecosystem for FRC teams
---

## About

PiLED is a project intended to make controlling lights on a robot using a coprocessor far easier. It allows for robot-coprocessor communication using an API built on top of NetworkTables.
This means the light states can change based on robot and game events like if the lights were controlled by the RoboRIO, all while pawning off any computation onto the coprocessor rather than the RIO.  
The main features of PiLED include:
- Easy disk image to get a Pi up and running
- Easy to use API to register LEDs and control effects
- Custom Pi HAT for power regulation and four connectors for LEDs
  
Planned features:
- Versatile 3d-printable connectors/mounts for Pi and LEDs
- Vary effects based on game stage
- Custom effects
- Support for more coprocessors

  
*Note: Currently only the Raspberry Pi 2-4 are supported. However, any board should work as long as the pinout is the same and the Python libraries listed in pi/requirements.txt behave the same.*

## Usage

### Installing on Pi
To flash the Pi with the disk image, follow these steps:
1. Download [Balena Etcher]() or the [Raspberry Pi Imager]()
2. Download the disk image from the [latest release](https://github.com/PepperLola/lights/releases/latest)
3. Plug the Raspberry Pi's SD card into your computer
4. Follow the steps in your chosen imaging software using the SD card and the downloaded disk image
5. After flashing, insert the SD card into the Pi. It should now be ready for use

### Installing the Java API
*TODO: Publish API, add instructions for publishing API locally using Maven*

### Robot Wiring
After imaging the Raspberry Pi, follow these steps to connect the Pi to the robot properly:
1. Attach the Pi HAT if it isn't already, and mount the Pi to the robot in a place where all necessary wires can reach
2. Connect the Pi over Ethernet to the RIO somehow. A [switch](TODO) is recommended, although the second port on the radio could be used
3. Plug in all LEDs to the ports on the Pi HAT. See the [wiki](TODO) for information on wiring without the HAT
4. Connect the power input of the Pi HAT to your PDH/PDP (not the VRM). Any port that outputs the battery voltage (~12V) and above 10A will work
5. Hope for no magic smoke when you turn on the robot

### Using the Java API
Example projects have been included in the `example/` directory. The API affords a lot of freedom when it comes to controlling LEDs, but these are the most important things to note:
- Set game stage
  - Set the game stage in each `init` method in `Robot.java` by calling `PiLED.getInstance().setStage(GameStage.< Game Stage >);` (substituting `< Game Stage >` for the corresponding game stage: Disabled, Auto, Teleop, etc.). This will allow effects to change based on the game stage (planned feature but not currently supported)
- Register LEDs
  - Create an `LED` instance with a name (string), port (0-4), and length (positive int)
  - Call `PiLED.getInstance().registerLED(< led >)` where `< led >` is the LED instance
  - Call `PiLED.getInstance().setAlliance()` with no arguments for the API to automatically get and store the alliance your robot is currently on (set in Driver Station or by FMS)
- Set Effects
  - Create an instance of an effect. This could be a built-in effect (such as `SolidEffect`, `RainbowEffect`, `BreatheEffect`, etc.; for a fully updated list, look at the [effects](/robot/src/main/java/com/pigmice/piled/effects) directory in `robot/`)
  - Call `PiLED.getInstance().setLEDEffect(< led >, < effect >)`, where `< led >` is the LED instance you want to run the effect on and `< effect >` is the effect instance you created previously

## Building

### Building the Image
This needs to be run on a Raspberry Pi with Ubuntu installed. Raspberry Pi OS will likely also work but has not been tested. To build the image, follow these steps:
1. Clone the [`lights-pi-gen`](https://github.com/PepperLola/lights-pi-gen) repository on the Pi and open it in the command line
2. Install the dependencies using `sudo apt-get install -y quilt qemu-user-static qemu-utils debootstrap zip libarchive-tools git curl grep`
3. Create a `config` file with containing `IMG_NAME=piled`. This can be done by running `echo "IMG_NAME=piled" > config`
4. Run `./build.sh`. The image iso file will be created in the `export-image/` directory
