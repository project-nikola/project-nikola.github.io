"""The starting point for the automation system

1. Discover nodes on network.
2. Calibrate sensing nodes.
3. Collect data from each node.
4. Save data to csv file.

"""
import glob
import logging
import serial
import signal
import sys

from .models import Coordinator
from .models import Node
from .util import write_to_csv

LOGGING = True  # Write to CSV files?
DISCOVER_TIME = 10  # seconds
RECEIVE_TIME = 10  # seconds
coordinator = None
serialport = None


def signal_shutdown(signum, frame):
    """Always halt the xbee threads and close the serial connection."""
    global coordinator
    global serialport

    logging.debug("halting coordinator threads.")
    coordinator.halt()
    logging.debug("closing serial port.")
    serialport.close()


def setup():
    """Attach signal handler and initialize coordinator and serialport."""
    global coordinator
    global serialport
    signal.signal(signal.SIGINT, signal_shutdown)

    # Platform specific serialports.
    if sys.platform == 'darwin':
        port = glob.glob('/dev/tty.usbserial*')[0]
    elif sys.platform == 'win32':
        port = 'COM9'
    else:  # Raspberry Pi
        port = glob.glob('/dev/ttyUSB*')

    logging.debug("open serial port.")
    serialport = serial.Serial(port)
    logging.debug("initialize the coordinator.")
    coordinator = Coordinator(serialport)


def main():
    global coordinator

    # Initialize coordinator and serialport.
    setup()

    # Discover nodes with same PANID.
    nodes = coordinator.discover_nodes(DISCOVER_TIME)

    while True:
        # Receive sensor data from discovered nodes.
        responses = coordinator.receive_sensor_data(RECEIVE_TIME)

        # Actuate nodes.
        for node in nodes:
            if node.type == Node.node_types['ac']:
                coordinator.actuate(node)

        if LOGGING:
            write_to_csv(responses)

    # Halt XBee threads and close serialport.
    signal_shutdown(0, None)

if __name__ == '__main__':
    main()
