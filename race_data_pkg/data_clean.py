import pandas as pd

column_name_dict = {
     'accelerationsource[calculated/measured/undefined]': 'accel_source',
     'accuracy_m': 'accuracy_m',
     'air density': 'air_density',
     'altitude': 'altitude',
     'barometric pressure': 'barometric_pressure',
     'barometric temperature': 'barometric_temp',
     'bat_celsius': 'bat_celsius',
     'battery voltage': 'battery_voltage',
     'brake': 'brake',
     'brake pressure - front left': 'brake_pressure_fl',
     'brake pressure - front right': 'brake_pressure_fr',
     'brake pressure - rear left': 'brake_pressure_rl',
     'brake pressure - rear right': 'brake_pressure_rr',
     'brakepressure': 'brake_pressure',
     'cold tire pressure - front left': 'cold_tire_pressure_fl',
     'cold tire pressure - front right': 'cold_tire_pressure_fr',
     'cold tire pressure - rear left': 'cold_tire_pressure_rl',
     'cold tire pressure - rear right': 'cold_tire_pressure_rr',
     'coolant_celsius': 'coolant_celsius',
     'date': 'start_date',
     'distance_km': 'distance_km',
     'distance_mile': 'distance_mile',
     'driverpower': 'driver_power',
     'engine coolant level': 'engine_coolant_level',
     'enginepower': 'engine_power',
     'fixtype[combustion,csc,electric,hybrid]': 'fix_type',
     'file': 'file',
     'fuel': 'fuel',
     'fuel level': 'fuel_level',
     'fuel pressure': 'fuel_pressure',
     'fuel usage per hour': 'fuel_usage_per_hour',
     'gear': 'gear',
     'gps distance': 'gps_distance',
     'gps_distance': 'gps_distance',
     'gps lateral acceleration': 'gps_lat_acceleration',
     'gps longitudinal acceleration': 'gps_long_acceleration',
     'gps speed': 'gps_speed',
     'gpsdifferential[unknown/2d3d/dgps/invalid]': 'gps_differential',
     'gpsfix[nofix/2d/3d/virtual/indoor]': 'gps_fix',
     'gpsinterpolated[false/true]': 'gps_interpolated',
     'hand brake position': 'hand_brake_position',
     'hdop': 'hdop',
     'heading': 'heading',
     'heading_deg': 'heading',
     'height_ft': 'height_ft',
     'height_m': 'height_m',
     'iat_celsius': 'iat_celsius',
     'is car on track': 'is_car_on_track',
     'is driver on track': 'is_driver_on_track',
     'lap number': 'lap_number',
     'lap time': 'lap_time',
     'lapindex': 'lap_number',
     'lateral acceleration': 'lat_acceleration',
     'lateralg': 'gps_lat_acceleration',
     'latitude': 'latitude',
     'lean': 'lean',
     'linealg': 'gps_lon_acceleration',
     'longitude': 'longitude',
     'longitudinal acceleration': 'long_acceleration',
     'maf': 'maf',
     'manifold absolute pressure': 'manifold_absolute_pressure',
     'map': 'map',
     'number of satellites': 'num_satellites',
     'odo': 'odo',
     'oil level': 'oil_level',
     'oil pressure': 'oil_pressure',
     'oil temperature': 'oil_temp',
     'oil_celsius': 'oil_celsius',
     'oippressure': 'oil_pressure',
     'on pit road': 'on_pit_road',
     'pitch': 'pitch',
     'pitch rate': 'pitch_rate',
     'push to pass pressed': 'push_to_pass_pressed',
     'relative humidity': 'relative_humidity',
     'ride height - front left': 'ride_height_fl',
     'ride height - front right': 'ride_height_fr',
     'ride height - rear left': 'ride_height_rl',
     'ride height - rear right': 'ride_height_rr',
     'roll': 'roll',
     'roll rate': 'roll_rate',
     'rpm': 'rpm',
     'satellites': 'num_satellites',
     'session time': 'session_time',
     'shock deflection - front left': 'shock_deflection_fl',
     'shock deflection - front right': 'shock_deflection_fr',
     'shock deflection - rear left': 'shock_deflection_rl',
     'shock deflection - rear right': 'shock_deflection_rr',
     'shock velocity - front left': 'shock_velocity_fl',
     'shock velocity - front right': 'shock_velocity_fr',
     'shock velocity - rear left': 'shock_velocity_rl',
     'shock velocity - rear right': 'shock_velocity_rr',
     'speed - front left': 'speed_fl',
     'speed - front right': 'speed_fr',
     'speed - rear left': 'speed_rl',
     'speed - rear right': 'speed_rr',
     'speed_kph': 'kph',
     'speed_mph': 'mph',
     'start date': 'start_date',
     'start time': 'start_time',
     'steering angle': 'steering_angle',
     'steering wheel torque': 'steering_wheel_torque',
     'steeringangle': 'steering_angle',
     'steeringanglerate': 'steering_angle_rate',
     'supportlevel': 'support_level',
     'throttle': 'throttle_position',
     'throttle position': 'throttle_position',
     'time': 'start_time',
     'time_lap': 'lap_time',
     'tire carcass temperature - front left left': 'tire_carcass_temp_fl_left',
     'tire carcass temperature - front left middle': 'tire_carcass_temp_fl_middle',
     'tire carcass temperature - front left right': 'tire_carcass_temp_fl_right',
     'tire carcass temperature - front right left': 'tire_carcass_temp_fr_left',
     'tire carcass temperature - front right middle': 'tire_carcass_temp_fr_middle',
     'tire carcass temperature - front right right': 'tire_carcass_temp_fr_right',
     'tire carcass temperature - rear left left': 'tire_carcass_temp_rl_left',
     'tire carcass temperature - rear left middle': 'tire_carcass_temp_rl_middle',
     'tire carcass temperature - rear left right': 'tire_carcass_temp_rl_right',
     'tire carcass temperature - rear right left': 'tire_carcass_temp_rr_left',
     'tire carcass temperature - rear right middle': 'tire_carcass_temp_rr_middle',
     'tire carcass temperature - rear right right': 'tire_carcass_temp_rr_right',
     'tire pressure - front left': 'tire_pressure_fl',
     'tire pressure - front right': 'tire_pressure_fr',
     'tire pressure - rear left': 'tire_pressure_rl',
     'tire pressure - rear right': 'tire_pressure_rr',
     'tire temperature - front left left': 'tire_temp_fl_left',
     'tire temperature - front left middle': 'tire_temp_fl_middle',
     'tire temperature - front left right': 'tire_temp_fl_right',
     'tire temperature - front right left': 'tire_temp_fr_left',
     'tire temperature - front right middle': 'tire_temp_fr_middle',
     'tire temperature - front right right': 'tire_temp_fr_right',
     'tire temperature - rear left left': 'tire_temp_rl_left',
     'tire temperature - rear left middle': 'tire_temp_rl_middle',
     'tire temperature - rear left right': 'tire_temp_rl_right',
     'tire temperature - rear right left': 'tire_temp_rr_left',
     'tire temperature - rear right middle': 'tire_temp_rr_middle',
     'tire temperature - rear right right': 'tire_temp_rr_right',
     'tire wear - front left left': 'tire_wear_fl_left',
     'tire wear - front left middle': 'tire_wear_fl_middle',
     'tire wear - front left right': 'tire_wear_fl_right',
     'tire wear - front right left': 'tire_wear_fr_left',
     'tire wear - front right middle': 'tire_wear_fr_middle',
     'tire wear - front right right': 'tire_wear_fr_right',
     'tire wear - rear left left': 'tire_wear_rl_left',
     'tire wear - rear left middle': 'tire_wear_rl_middle',
     'tire wear - rear left right': 'tire_wear_rl_right',
     'tire wear - rear right left': 'tire_wear_rr_left',
     'tire wear - rear right middle': 'tire_wear_rr_middle',
     'tire wear - rear right right': 'tire_wear_rr_right',
     'track temperature': 'track_temp',
     'vertical acceleration': 'vertical_acceleration',
     'water temperature': 'water_temp',
     'wheel_speed_fl_delta_kph': 'wheel_speed_fl',
     'wheel_speed_fr_delta_kph': 'wheel_speed_fr',
     'wheel_speed_kph': 'wheel_speed_kph',
     'wheel_speed_mph': 'wheel_speed_kmh',
     'wheel_speed_rl_delta_kph': 'wheel_speed_rl',
     'wheel_speed_rr_delta_kph': 'wheel_speed_rr',
     'wind direction': 'wind_direction',
     'wind velocity': 'wind_velocity',
     'yaw': 'yaw',
     'yaw rate': 'yaw_rate',
     'yawrate': 'yaw_rate',
     'accel_source': 'accel_source',
     'air_density': 'air_density',
     'barometric_pressure': 'barometric_pressure',
     'barometric_temp': 'barometric_temp',
     'battery_voltage': 'battery_voltage',
     'brake_pressure_fl': 'brake_pressure_fl',
     'brake_pressure_fr': 'brake_pressure_fr',
     'brake_pressure_rl': 'brake_pressure_rl',
     'brake_pressure_rr': 'brake_pressure_rr',
     'brake_pressure': 'brake_pressure',
     'cold_tire_pressure_fl': 'cold_tire_pressure_fl',
     'cold_tire_pressure_fr': 'cold_tire_pressure_fr',
     'cold_tire_pressure_rl': 'cold_tire_pressure_rl',
     'cold_tire_pressure_rr': 'cold_tire_pressure_rr',
     'start_date': 'start_date',
     'driver_power': 'driver_power',
     'engine_coolant_level': 'engine_coolant_level',
     'engine_power': 'engine_power',
     'fix_type': 'fix_type',
     'fuel_level': 'fuel_level',
     'fuel_pressure': 'fuel_pressure',
     'fuel_usage_per_hour': 'fuel_usage_per_hour',
     'gps_lat_acceleration': 'gps_lat_acceleration',
     'gps_long_acceleration': 'gps_long_acceleration',
     'gps_speed': 'gps_speed',
     'gps_differential': 'gps_differential',
     'gps_fix': 'gps_fix',
     'gps_interpolated': 'gps_interpolated',
     'hand_brake_position': 'hand_brake_position',
     'is_car_on_track': 'is_car_on_track',
     'is_driver_on_track': 'is_driver_on_track',
     'lap_number': 'lap_number',
     'lap_time': 'lap_time',
     'lat_acceleration': 'lat_acceleration',
     'gps_lon_acceleration': 'gps_lon_acceleration',
     'long_acceleration': 'long_acceleration',
     'manifold_absolute_pressure': 'manifold_absolute_pressure',
     'num_satellites': 'num_satellites',
     'oil_level': 'oil_level',
     'oil_pressure': 'oil_pressure',
     'oil_temp': 'oil_temp',
     'on_pit_road': 'on_pit_road',
     'pitch_rate': 'pitch_rate',
     'push_to_pass_pressed': 'push_to_pass_pressed',
     'relative_humidity': 'relative_humidity',
     'ride_height_fl': 'ride_height_fl',
     'ride_height_fr': 'ride_height_fr',
     'ride_height_rl': 'ride_height_rl',
     'ride_height_rr': 'ride_height_rr',
     'roll_rate': 'roll_rate',
     'session_time': 'session_time',
     'shock_deflection_fl': 'shock_deflection_fl',
     'shock_deflection_fr': 'shock_deflection_fr',
     'shock_deflection_rl': 'shock_deflection_rl',
     'shock_deflection_rr': 'shock_deflection_rr',
     'shock_velocity_fl': 'shock_velocity_fl',
     'shock_velocity_fr': 'shock_velocity_fr',
     'shock_velocity_rl': 'shock_velocity_rl',
     'shock_velocity_rr': 'shock_velocity_rr',
     'speed_fl': 'speed_fl',
     'speed_fr': 'speed_fr',
     'speed_rl': 'speed_rl',
     'speed_rr': 'speed_rr',
     'kph': 'kph',
     'mph': 'mph',
     'start_time': 'start_time',
     'steering_angle': 'steering_angle',
     'steering_wheel_torque': 'steering_wheel_torque',
     'steering_angle_rate': 'steering_angle_rate',
     'support_level': 'support_level',
     'throttle_position': 'throttle_position',
     'tire_carcass_temp_fl_left': 'tire_carcass_temp_fl_left',
     'tire_carcass_temp_fl_middle': 'tire_carcass_temp_fl_middle',
     'tire_carcass_temp_fl_right': 'tire_carcass_temp_fl_right',
     'tire_carcass_temp_fr_left': 'tire_carcass_temp_fr_left',
     'tire_carcass_temp_fr_middle': 'tire_carcass_temp_fr_middle',
     'tire_carcass_temp_fr_right': 'tire_carcass_temp_fr_right',
     'tire_carcass_temp_rl_left': 'tire_carcass_temp_rl_left',
     'tire_carcass_temp_rl_middle': 'tire_carcass_temp_rl_middle',
     'tire_carcass_temp_rl_right': 'tire_carcass_temp_rl_right',
     'tire_carcass_temp_rr_left': 'tire_carcass_temp_rr_left',
     'tire_carcass_temp_rr_middle': 'tire_carcass_temp_rr_middle',
     'tire_carcass_temp_rr_right': 'tire_carcass_temp_rr_right',
     'tire_pressure_fl': 'tire_pressure_fl',
     'tire_pressure_fr': 'tire_pressure_fr',
     'tire_pressure_rl': 'tire_pressure_rl',
     'tire_pressure_rr': 'tire_pressure_rr',
     'tire_temp_fl_left': 'tire_temp_fl_left',
     'tire_temp_fl_middle': 'tire_temp_fl_middle',
     'tire_temp_fl_right': 'tire_temp_fl_right',
     'tire_temp_fr_left': 'tire_temp_fr_left',
     'tire_temp_fr_middle': 'tire_temp_fr_middle',
     'tire_temp_fr_right': 'tire_temp_fr_right',
     'tire_temp_rl_left': 'tire_temp_rl_left',
     'tire_temp_rl_middle': 'tire_temp_rl_middle',
     'tire_temp_rl_right': 'tire_temp_rl_right',
     'tire_temp_rr_left': 'tire_temp_rr_left',
     'tire_temp_rr_middle': 'tire_temp_rr_middle',
     'tire_temp_rr_right': 'tire_temp_rr_right',
     'tire_wear_fl_left': 'tire_wear_fl_left',
     'tire_wear_fl_middle': 'tire_wear_fl_middle',
     'tire_wear_fl_right': 'tire_wear_fl_right',
     'tire_wear_fr_left': 'tire_wear_fr_left',
     'tire_wear_fr_middle': 'tire_wear_fr_middle',
     'tire_wear_fr_right': 'tire_wear_fr_right',
     'tire_wear_rl_left': 'tire_wear_rl_left',
     'tire_wear_rl_middle': 'tire_wear_rl_middle',
     'tire_wear_rl_right': 'tire_wear_rl_right',
     'tire_wear_rr_left': 'tire_wear_rr_left',
     'tire_wear_rr_middle': 'tire_wear_rr_middle',
     'tire_wear_rr_right': 'tire_wear_rr_right',
     'track_temp': 'track_temp',
     'vertical_acceleration': 'vertical_acceleration',
     'water_temp': 'water_temp',
     'wheel_speed_fl': 'wheel_speed_fl',
     'wheel_speed_fr': 'wheel_speed_fr',
     'wheel_speed_kmh': 'wheel_speed_kmh',
     'wheel_speed_rl': 'wheel_speed_rl',
     'wheel_speed_rr': 'wheel_speed_rr',
     'wind_direction': 'wind_direction',
     'wind_velocity': 'wind_velocity',
     'yaw_rate': 'yaw_rate'
    }

def mph_convert(speed_column, units = 'kph'):
    if units == 'kph':
        speed = speed_column * 0.62137
    else:
        speed = speed_column
    return speed

def time_conv(time_col):
    seconds_list = []
    minutes_list = []
    for time in time_col.to_list():
        seconds = time/1000000000
        minutes = int(seconds//60)
        remaining_seconds = seconds -minutes*60
        whole_seconds = str(int(remaining_seconds)).zfill(2)
        partial_seconds = str(remaining_seconds%1)[1:5]
        minutes_seconds = "%s:%s%s" % (minutes, whole_seconds, partial_seconds)
        seconds_list.append(seconds)
        minutes_list.append(minutes_seconds)
    times = {'seconds':seconds_list,'minutes':minutes_list}
    return times

def tsv_import(filename, meta_id, speed_units, column_lookup):
    df_final = pd.read_csv(filename, delimiter = "\t")
    new_cols = []
    for col_name in df_final.columns:
        new_cols.append(column_lookup[col_name.lower()])
    df_final.columns = new_cols
    df_final['upload_meta_id'] = meta_id
    df_final['mph'] = mph_convert(df_final['gps_speed'],speed_units)
    return df_final

def vbo_import(filename,meta_id, speed_units):    
    with open(filename) as f:
        for x, line in enumerate(f):
            #print(line)
            header = False
            comments = False
            session_data = False
            laptiming = False
            column_names = False
            data = False
            if x == 0:
                file_create = line
            elif line.strip() == '[header]':
                header, comments, session_data, laptiming, column_names, data = True, False, False, False, False, False
                header_data = []
            elif line.strip() == '[comments]':
                header, comments, session_data, laptiming, column_names, data = False, True, False, False, False, False
                comments_data = []
            elif line.strip() == '[session data]':
                header, comments, session_data, laptiming, column_names, data = False, False, True, False, False, False
                session_data = []
            elif line.strip() == '[laptiming]':
                header, comments, session_data, laptiming, column_names, data = False, False, False, True, False, False 
                laptiming_data = []
            elif line.strip() == '[column names]':
                header, comments, session_data, laptiming, column_names, data = False, False, False, False, True, False 
                column_names_data = []
                column_line = x
            elif line.strip() == '[data]':
                header, comments, session_data, laptiming, column_names, data = False, False, False, False, False, True
                lap_data = []
                data_line = x
            if header:
                header_data.append(line)
            elif comments:
                comments_data.append(line)
            elif session_data:
                session_data.append(line)
            elif laptiming:
                laptiming_data.append(line)
            elif column_names:
                if column_line != x:
                    column_names_data.append(line)
            elif data:
                if data_line != x:
                    lap_data.append(line.split('\t'))
        raw_data_dict = {}    
        raw_data_dict['file_create'] = file_create
        raw_data_dict['header'] = header_data
        raw_data_dict['comments'] = comments_data
        raw_data_dict['session_data'] = session_data
        raw_data_dict['laptiming'] = laptiming_data
        raw_data_dict['column_names'] = column_names_data
        raw_data_dict['data'] = lap_data
    return raw_data_dict