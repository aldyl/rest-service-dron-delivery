#!/bin/pyton3
from dispatch_controller.config import app

import dispatch_controller.actions.drones
import dispatch_controller.actions.medications 


@app.route("/")
def index(): return "Welcome to Drones Dispath Controller"

if __name__ == '__main__':
    app.run()
