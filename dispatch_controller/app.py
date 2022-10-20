#!/bin/pyton3
from dispatch_controller.config import app

import dispatch_controller.actions.drones
import dispatch_controller.actions.medications

from dispatch_controller.logger import create_loggin
from dispatch_controller.schedulers.scheduler import log_battery_status

create_loggin()

log_battery_status()

@app.route("/")
def index(): return "Welcome to Drones Dispath Controller"

if __name__ == '__main__':
    app.run()
