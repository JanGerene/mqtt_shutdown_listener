# mqtt_shutdown_listener
python script subscribing to mqtt shutdown topic on node "192.168.1.18" with payload "raspberrypi4"
The system will shut down when the above message is received.
This script is started as a service on boot
The script uses the paho-mqtt module which should be installed globally with `pip install paho-mqtt`

## To start the service at boot:
1. copy the script to the home directory 
1. copy the service file `sudo cp mqtt_shutdown_listener/mqtt-shutdown.service /lib/systemd/system/`
2. reload sytemd `sudo systemctl daemon-reload`

### note 
/tmp directory should be world writeable for logging purposes