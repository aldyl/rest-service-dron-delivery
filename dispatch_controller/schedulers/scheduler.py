

from dispatch_controller.config import app, scheduler
from dispatch_controller.model.dron import Dron, DronSchema


@scheduler.task('interval', id='do_job_1', seconds=120, misfire_grace_time=900)
def log_battery_status():
    app.app_context().push()
    drones = Dron.query.all()

    if drones is not None:

        # Serialize the data for the response
        drones_schema = DronSchema(many=True)    
        _drones = drones_schema.dump(drones)

        for dron in _drones:
            batteryload = dron.get("batteryload" )
            status = "dicharged"
            if batteryload > 25:
                status = "charged"
                app.logger.info({"dronid" : dron.get("dronid"), "batteryload" : batteryload, "batterystatus" : status})
            else: 
                app.logger.warning({"dronid" : dron.get("dronid"), "batteryload" : batteryload, "batterystatus" : status})
            

