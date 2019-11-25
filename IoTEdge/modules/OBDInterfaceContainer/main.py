import requests
import obd
from obd import OBDStatus
import time
import datetime
import pint
from pint import UnitRegistry
from flask import Flask, request, redirect, Response, url_for, jsonify

application = Flask(__name__)
ureg = pint.UnitRegistry()

class OBDInterface:
    def __init__(self):
        self.connection = obd.OBD()
        while self.connection.status() == OBDStatus.NOT_CONNECTED:
            print("<{0}> Waiting for OBD Connection...".format(datetime.datetime.now().time()))
            time.sleep(10)
            self.connection = obd.OBD()
            if self.connection.status() == OBDStatus.CAR_CONNECTED:
                print("OBD Connected")

    def sendOBDCommand(self, cmdName):
        try:
            resp = self.connection.query(obd.commands[cmdName])
            json_resp = "{}"
            if "Quantity" in str(type(resp.value)):
                json_resp = jsonify((resp.value.magnitude, str(resp.value.units)))
            else:
                json_resp = jsonify(resp.value)
            return "\"{0}\":{1}".format(cmdName, json_resp.get_data(as_text=True))
        except Exception as err:
            return "obd error: {0}".format(err)

obdint = OBDInterface()

@application.route('/obd_send/<command>', methods=['GET'])
def obd_send(command):
    if command == "elm_version":
        return obdint.sendOBDCommand("ELM_VERSION")
    elif command == "elm_voltage":
        return obdint.sendOBDCommand("ELM_VOLTAGE")
    elif command == "get_dtc":
        return obdint.sendOBDCommand("GET_DTC")
    elif command == "get_current_dtc":
        return obdint.sendOBDCommand("GET_CURRENT_DTC")
    elif command == "vin":
        return obdint.sendOBDCommand("VIN")
    elif command == "pids_a":
        return obdint.sendOBDCommand("PIDS_A")
    elif command == "status":
        return obdint.sendOBDCommand("STATUS")
    elif command == "freeze_dtc":
        return obdint.sendOBDCommand("FREEZE_DTC")
    elif command == "fuel_status":
        return obdint.sendOBDCommand("FUEL_STATUS")
    elif command == "engine_load":
        return obdint.sendOBDCommand("ENGINE_LOAD")
    elif command == "coolant_temp":
        return obdint.sendOBDCommand("COOLANT_TEMP")
    elif command == "short_fuel_trim_1":
        return obdint.sendOBDCommand("SHORT_FUEL_TRIM_1")
    elif command == "long_fuel_trim_1":
        return obdint.sendOBDCommand("LONG_FUEL_TRIM_1")
    elif command == "short_fuel_trim_2":
        return obdint.sendOBDCommand("SHORT_FUEL_TRIM_2")
    elif command == "long_fuel_trim_2":
        return obdint.sendOBDCommand("LONG_FUEL_TRIM_2")
    elif command == "fuel_pressure":
        return obdint.sendOBDCommand("FUEL_PRESSURE")
    elif command == "intake_pressure":
        return obdint.sendOBDCommand("INTAKE_PRESSURE")
    elif command == "rpm":
        return obdint.sendOBDCommand("RPM")
    elif command == "speed":
        return obdint.sendOBDCommand("SPEED")
    elif command == "timing_advance":
        return obdint.sendOBDCommand("TIMING_ADVANCE")
    elif command == "intake_temp":
        return obdint.sendOBDCommand("INTAKE_TEMP")
    elif command == "maf":
        return obdint.sendOBDCommand("MAF")
    elif command == "throttle_pos":
        return obdint.sendOBDCommand("THROTTLE_POS")
    elif command == "air_status":
        return obdint.sendOBDCommand("AIR_STATUS")
    elif command == "o2_sensors":
        return obdint.sendOBDCommand("O2_SENSORS")
    elif command == "o2_b1s1":
        return obdint.sendOBDCommand("O2_B1S1")
    elif command == "o2_b1s2":
        return obdint.sendOBDCommand("O2_B1S2")
    elif command == "o2_b1s3":
        return obdint.sendOBDCommand("O2_B1S3")
    elif command == "o2_b1s4":
        return obdint.sendOBDCommand("O2_B1S4")
    elif command == "o2_b2s1":
        return obdint.sendOBDCommand("O2_B2S1")
    elif command == "o2_b2s2":
        return obdint.sendOBDCommand("O2_B2S2")
    elif command == "o2_b2s3":
        return obdint.sendOBDCommand("O2_B2S3")
    elif command == "o2_b2s4":
        return obdint.sendOBDCommand("O2_B2S4")
    elif command == "obd_compliance":
        return obdint.sendOBDCommand("OBD_COMPLIANCE")
    elif command == "o2_sensors_alt":
        return obdint.sendOBDCommand("O2_SENSORS_ALT")
    elif command == "aux_input_status":
        return obdint.sendOBDCommand("AUX_INPUT_STATUS")
    elif command == "run_time":
        return obdint.sendOBDCommand("RUN_TIME")
    elif command == "pids_b":
        return obdint.sendOBDCommand("PIDS_B")
    elif command == "distance_w_mil":
        return obdint.sendOBDCommand("DISTANCE_W_MIL")
    elif command == "fuel_rail_pressure_vac":
        return obdint.sendOBDCommand("FUEL_RAIL_PRESSURE_VAC")
    elif command == "fuel_rail_pressure_direct":
        return obdint.sendOBDCommand("FUEL_RAIL_PRESSURE_DIRECT")
    elif command == "o2_s1_wr_voltage":
        return obdint.sendOBDCommand("O2_S1_WR_VOLTAGE")
    elif command == "o2_s2_wr_voltage":
        return obdint.sendOBDCommand("O2_S2_WR_VOLTAGE")
    elif command == "o2_s3_wr_voltage":
        return obdint.sendOBDCommand("O2_S3_WR_VOLTAGE")
    elif command == "o2_s4_wr_voltage":
        return obdint.sendOBDCommand("O2_S4_WR_VOLTAGE")
    elif command == "o2_s5_wr_voltage":
        return obdint.sendOBDCommand("O2_S5_WR_VOLTAGE")
    elif command == "o2_s6_wr_voltage":
        return obdint.sendOBDCommand("O2_S6_WR_VOLTAGE")
    elif command == "o2_s7_wr_voltage":
        return obdint.sendOBDCommand("O2_S7_WR_VOLTAGE")
    elif command == "o2_s8_wr_voltage":
        return obdint.sendOBDCommand("O2_S8_WR_VOLTAGE")
    elif command == "command_egr":
        return obdint.sendOBDCommand("COMMANDED_EGR")
    elif command == "egr_error":
        return obdint.sendOBDCommand("EGR_ERROR")
    elif command == "evaporative_purge":
        return obdint.sendOBDCommand("EVAPORATIVE_PURGE")
    elif command == "fuel_level":
        return obdint.sendOBDCommand("FUEL_LEVEL")
    elif command == "warmups_since_dtc_clear":
        return obdint.sendOBDCommand("WARMUPS_SINCE_DTC_CLEAR")
    elif command == "distance_since_dtc_clear":
        return obdint.sendOBDCommand("DISTANCE_SINCE_DTC_CLEAR")
    elif command == "evap_vapor_pressure":
        return obdint.sendOBDCommand("EVAP_VAPOR_PRESSURE")
    elif command == "barometric_pressure":
        return obdint.sendOBDCommand("BAROMETRIC_PRESSURE")
    elif command == "o2_s1_wr_current":
        return obdint.sendOBDCommand("O2_S1_WR_CURRENT")
    elif command == "o2_s2_wr_current":
        return obdint.sendOBDCommand("O2_S2_WR_CURRENT")
    elif command == "o2_s3_wr_current":
        return obdint.sendOBDCommand("O2_S3_WR_CURRENT")
    elif command == "o2_s4_wr_current":
        return obdint.sendOBDCommand("O2_S4_WR_CURRENT")
    elif command == "o2_s5_wr_current":
        return obdint.sendOBDCommand("O2_S5_WR_CURRENT")
    elif command == "o2_s6_wr_current":
        return obdint.sendOBDCommand("O2_S6_WR_CURRENT")
    elif command == "o2_s7_wr_current":
        return obdint.sendOBDCommand("O2_S7_WR_CURRENT")
    elif command == "o2_s8_wr_current":
        return obdint.sendOBDCommand("O2_S8_WR_CURRENT")
    elif command == "catalyst_temp_b1s1":
        return obdint.sendOBDCommand("CATALYST_TEMP_B1S1")
    elif command == "catalyst_temp_b2s1":
        return obdint.sendOBDCommand("CATALYST_TEMP_B2S1")
    elif command == "catalyst_temp_b1s2":
        return obdint.sendOBDCommand("CATALYST_TEMP_B1S2")
    elif command == "catalyst_temp_b2s2":
        return obdint.sendOBDCommand("CATALYST_TEMP_B2S2")
    elif command == "pids_c":
        return obdint.sendOBDCommand("PIDS_C")
    elif command == "status_drive_cycle":
        return obdint.sendOBDCommand("STATUS_DRIVE_CYCLE")
    elif command == "control_module_voltage":
        return obdint.sendOBDCommand("CONTROL_MODULE_VOLTAGE")
    elif command == "absolute_load":
        return obdint.sendOBDCommand("ABSOLUTE_LOAD")
    elif command == "commanded_equiv_ratio":
        return obdint.sendOBDCommand("COMMANDED_EQUIV_RATIO")
    elif command == "relative_throttle_pos":
        return obdint.sendOBDCommand("RELATIVE_THROTTLE_POS")
    elif command == "ambiant_air_temp":
        return obdint.sendOBDCommand("AMBIANT_AIR_TEMP")
    elif command == "throttle_pos_b":
        return obdint.sendOBDCommand("THROTTLE_POS_B")
    elif command == "throttle_pos_c":
        return obdint.sendOBDCommand("THROTTLE_POS_C")
    elif command == "throttle_pos_d":
        return obdint.sendOBDCommand("ACCELERATOR_POS_D")
    elif command == "throttle_pos_e":
        return obdint.sendOBDCommand("ACCELERATOR_POS_E")
    elif command == "throttle_pos_f":
        return obdint.sendOBDCommand("ACCELERATOR_POS_F")
    elif command == "throttle_actuator":
        return obdint.sendOBDCommand("THROTTLE_ACTUATOR")
    elif command == "run_time_mil":
        return obdint.sendOBDCommand("RUN_TIME_MIL")
    elif command == "time_since_dtc_cleared":
        return obdint.sendOBDCommand("TIME_SINCE_DTC_CLEARED")
    elif command == "max_values":
        return obdint.sendOBDCommand("MAX_VALUES")
    elif command == "max_maf":
        return obdint.sendOBDCommand("MAX_MAF")
    elif command == "fuel_type":
        return obdint.sendOBDCommand("FUEL_TYPE")
    elif command == "ethanol_percent":
        return obdint.sendOBDCommand("ETHANOL_PERCENT")
    elif command == "evap_vapor_pressure_abs":
        return obdint.sendOBDCommand("EVAP_VAPOR_PRESSURE_ABS")
    elif command == "evap_vapor_pressure_alt":
        return obdint.sendOBDCommand("EVAP_VAPOR_PRESSURE_ALT")
    elif command == "short_o2_trim_b1":
        return obdint.sendOBDCommand("SHORT_O2_TRIM_B1")
    elif command == "long_o2_trim_b1":
        return obdint.sendOBDCommand("LONG_O2_TRIM_B1")
    elif command == "short_o2_trim_b2":
        return obdint.sendOBDCommand("SHORT_O2_TRIM_B2")
    elif command == "long_o2_trim_b2":
        return obdint.sendOBDCommand("LONG_O2_TRIM_B2")
    elif command == "fuel_rail_pressure_abs":
        return obdint.sendOBDCommand("FUEL_RAIL_PRESSURE_ABS")
    elif command == "relative_accel_pos":
        return obdint.sendOBDCommand("RELATIVE_ACCEL_POS")
    elif command == "hybrid_battery_remaining":
        return obdint.sendOBDCommand("HYBRID_BATTERY_REMAINING")
    elif command == "oil_temp":
        return obdint.sendOBDCommand("OIL_TEMP")
    elif command == "fuel_inject_timing":
        return obdint.sendOBDCommand("FUEL_INJECT_TIMING")
    elif command == "fuel_rate":
        return obdint.sendOBDCommand("FUEL_RATE")
    elif command == "emission_req":
        return obdint.sendOBDCommand("EMISSION_REQ")

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8082)
