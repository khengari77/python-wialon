
class Unit:
    def __init__(self, session):
        self.session session

    def update_fuel_level_params(self, itemId, flags, ignoreStayTimeout, minFillingVolume, minTheftTimeout, minTheftVolume, filterQuality, fillingsJoinInterval, theftsJoinInterval, extraFillingTimeout):
        """
                Parameters
         Name  Description  itemId  unit ID 
         flags  flags of fillings and thefts (see Fuel consumption) 
         ignoreStayTimeout   ignore the messages after the start of motion, sec 
         minFillingVolume  minimum fuel filling volume, litres 
         minTheftTimeout  minimum stay timeout to detect fuel theft, sec 
         minTheftVolume  minimum fuel theft volume, litres 
         filterQuality  filter quality (0..255) 
         fillingsJoinInterval  timeout to separate consecutive fillings, sec 
         theftsJoinInterval  timeout to separate consecutive thefts, sec 
         extraFillingTimeout  timeout to detect final filling volume, sec Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_fuel_level_params", **params)


    def update_image(self, itemId, oldItemId):
        """
                From library:
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_image", **params)


    def update_traffic_counter(self, itemId, newValue, regReset):
        """
                Parameters
         Name  Description  itemId  unit ID 
         newValue  new value of GPRS traffic counter (KB) 
         regReset  log changes: 0 - no, 1 - yes Response{
        "cnkb":<uint>,/* value of GPRS traffic counter */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_traffic_counter", **params)


    def registry_maintenance_event(self, date, info, duration, cost, location, x, y, description, mileage, eh, done_svcs, itemId):
        """
                Parameters
         Name  Description  date  date 
         info  kind of work 
         duration  duration 
         cost  cost 
         location  location 
         x  longitude 
         y  latitude 
         description  description 
         mileage  mileage 
         eh  engine hours 
         done_svcs  list of services (comma-separated) 
         itemId  unit ID Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/registry_maintenance_event", **params)


    def exec_cmd(self, itemId, commandName, linkType, param, timeout, flags):
        """
                Parameters
         Name  Description  itemId  unit ID 
         commandName  command name 
         linkType  link type (see Commands: create, edit, delete) 
         param  parameters (if necessary) 
         timeout  timeout for command to wait in commands queue, in seconds 
         flags  flags for choosing phone number to execute command:
        0 - use any (primary, then secondary),
        0x1 - use primary,
        0x2 - use secondary. 
        0x10 - send param in JSON format Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/exec_cmd", **params)


    def update_trip_detector(self, itemId, type, gpsCorrection, minSat, minMovingSpeed, minStayTime, maxMessagesDistance, minTripTime, minTripDistance):
        """
                Parameters
         Name  Description  itemId  unit ID 
         type  type of movement detection (see Trip detection) 
         gpsCorrection  allow GPS correction: 0 - no, 1 - yes 
         minSat  min satellites count 
         minMovingSpeed  min moving speed, km/h 
         minStayTime  min parking time, seconds 
         maxMessagesDistance  max distance between messages, meters 
         minTripTime  min trip time, seconds 
         minTripDistance  min trip distance, meters Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_trip_detector", **params)


    def update_phone(self, itemId, phoneNumber):
        """
                 Character '+' in phone number should be replaced by code %2B.
        Parameters
         Name  Description  itemId  unit ID 
         phoneNumber  new phone number Response{
        "ph":<text>/* phone number */
        }Errors
         Code  Value  1002  new phone number matches the old one, or such number already exists Other errors can also occur.
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_phone", **params)


    def update_fuel_impulse_params(self, itemId, maxImpulses, skipZero):
        """
                Parameters
         Name  Description  itemId  unit ID 
         maxImpulses  max impulses 
         skipZero  skip first zero value Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_fuel_impulse_params", **params)


    def get_trips(self, itemId, msgsSource, timeFrom, timeTo):
        """
                 Current request can't be executed simultaneously with following requests:
         report/exec_report, report/export_result, report/get_result_chart, report/get_result_map, messages/load_interval, render/create_messages_layer, resource/get_driver_bindings, resource/get_trailer_bindings, all requests from chapter Export and import, account/get_account_history.Parameters
         Name  Description  itemId  unit ID 
         timeFrom  interval beginning 
         timeTo  interval end 
         msgsSource  name of message layer (only one layer is available); 
         values: 1 – message loader used Response[{
        "from":{/* starting point of the trip */
        "i":<unit>,/* index of message */
        "t":<unit>,/* time */
        "p":{/* position */
        "y":<double>,/* latitude */
        "x":<double>/* longitude */
        }
        },
        "to":{/* ending point of the trip */
        "i":<unit>,/* index of message */
        "t":<unit>,/* time */
        "p":{/* position */
        "y":<double>,/* latitude*/
        "x":<double>/* longitude */
        }
        },
        "m":<double>/* mileage (meters) */
        }]
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/get_trips", **params)


    def calc_sensors(self, source, indexFrom, indexTo, unitId, sensorId, width):
        """
                Parameters
         Name  Description  source  source of messages - layer name, if empty - messages loader will be used by default 
         indexFrom  index of first message 
         indexTo  index of last message 
         unitId  unit ID 
         sensorId  ID sensor: if 0 - return values of all sensors 
         width  desired number of elements to respond, aggregation is used (see below), optional  If source is defined then unitId must be defined too. If source is NOT defined then write down any value in unitId (it is not used) – messages are put from message loader directly.
        Explanation of 'width' param
        When you need fixed quantity of sensor values and aggregated (i.e. preprocessed), then you may use 'width' param. For example you may get preprocessed data to form and zoom charts.Logics is as follows:1. the system finds all messages within asked bounds;2. then it splits all the interval into width subintervals;3. in every subinterval it finds the very first sensor value (left), the last one (right), minimal one (bottom) maximal one (top). Described values will merge into final server response.
        Response[/* array of messages data */
        {/* value(s) of sensor(s) from one message */
        <text>:<double|text>,/* sensor ID: sensor value */
        ...
        }
        ]If width is defined, then the response will be as follows:[
        [
        {
        "name":<sensor_name>,
        "data":[
           {
        "left":[<unix_time1>,<value1>],
        "right":[<unix_time2>,<value2>],
        "bottom":[<unix_time3>,<value3>],
        "top":[<unix_time4>,<value4>]
           },
        ...
        ]
        },
        ...
        ]
        ]where <sensor_name> – sensor name,<unix_timeN> – message UNIX-time,valueN – sensor value in a message,left – the first sensor value in a subinterval and its time,right – the last sensor value in a subinterval and its time,bottom – minimal sensor value  in a subinterval and its time,top – maximal sensor value in a subinterval and its time.
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/calc_sensors", **params)


    def update_accelerometers_calibration(self, itemId, timeFrom, timeTo):
        """
                or
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_accelerometers_calibration", **params)


    def get_fuel_settings(self, itemId):
        """
                Parameters
         Name  Description  itemId  unit ID Response{
        "calcTypes":<uint>,/* method of calculating fuel consumption (see below) */
        "fuelLevelParams":{/* detection of fuel fillings/thefts */
        "flags":<uint>,/* flags of fillings and thefts (see below) */
        "ignoreStayTimeout":<uint>,/* ignore the messages after the start of motion, sec */
        "minFillingVolume":<double>,/* minimum fuel filling volume, litres */
        "minTheftTimeout":<uint>,/* minimum stay timeout to detect fuel theft, sec */
        "minTheftVolume":<double>,/* minimum fuel theft volume, litres */
        "filterQuality":<ubyte>,/* filter quality (0..255) */
        "fillingsJoinInterval":<uint>,/* timeout to separate consecutive fillings, sec */
        "theftsJoinInterval":<uint>,/* timeout to separate consecutive thefts, sec */
        "extraFillingTimeout":<uint>/* timeout to detect final filling volume, sec */
        },
        "fuelConsMath":{/* consumption math */
        "idling":<double>,/* idling, litres per hour */
        "urban":<double>,/* urban cycle, litres per 100 km */
        "suburban":<double>,/* suburban cycle, litres per 100 km */
        "loadCoef":<uint>/* coefficient when moving under load */
        },
        "fuelConsRates":{/* consumption by rates */
        "consSummer":<double>,/* summer consumption, litres per 100 km */
        "consWinter":<double>,/* winter consumption, litres per 100 km */
        "winterMonthFrom":<uint>,/* winter from (month: 0-11) */
        "winterDayFrom":<uint>,/* winter from (day 1-31) */
        "winterMonthTo":<uint>,/* winter to (month 0-11) */
        "winterDayTo":<uint>/* winter to (day 1-31) */
        },
        "fuelConsImpulse":{/* impulse fuel consumption sensors */
        "maxImpulses":<uint>,/* max impulses */
        "skipZero":<uint>/* skip first zero value */
        }
        }Method of calculating fuel consumption:
         Flag  Description  0x0  do not use fuel consumption in reports 
         0x01  consumption math 
         0x02  fuel level sensors 
         0x04  replace invalid values with math consumption 
         0x08  absolute fuel consumption sensors 
         0x10  impulse fuel consumption sensors 
         0x20  instant fuel consumption sensors 
         0x40  consumption by rates Flags of fillings and thefts:
         Flag  Description  0x01  merge same name sensors (fuel level) 
         0x02  filter fuel level sensors values 
         0x04  merge same name sensors (fuel consumption) 
         0x08  detect fuel filling only while stopped 
         0x10  time-based fuel level sensors consumption 
         0x40  ignore filtration when calculating filling volume 
         0x80  ignore filtration when calculating theft volume 
         0x100  detect fuel theft in motion 
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/get_fuel_settings", **params)


    def update_phone2(self, itemId, phoneNumber):
        """
                 Character '+' in phone number should be replaced by code %2B.
        Parameters
         Name  Description  itemId  unit ID 
         phoneNumber  new phone number Response{
        "ph2":<text>/* phone number */
        }Errors
         Code  Value  1002  new phone number matches the old one, or such number already exists Other errors can also occur.
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_phone2", **params)


    def get_video_settings(self, itemId):
        """
                Parameters
         Name  Description  itemId  unit ID Response{"settings":[
          {"flags":1,"name":"cam"}, /* name = camera name, flags = 1 camera is active */
          {"flags":3,"name":"cam1"},/* name = camera name, flags = 3 camera and video saving is active */
          ...]
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/get_video_settings", **params)


    def update_fuel_calc_types(self, itemId, calcTypes):
        """
                Parameters
         Name  Description  itemId  unit ID 
         calcTypes  types of fuel consumption calculation (see Fuel consumption) Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_fuel_calc_types", **params)


    def update_mileage_counter(self, itemId, newValue):
        """
                 You can find an example of this request in the sample Creating, editing and deleting items.
        Parameters
         Name  Description  itemId  unit ID 
         newValue  new value of mileage counter (km) Response{
        "cnm":<uint>/* value of mileage counter */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_mileage_counter", **params)


    def update_messages_filter(self, itemId, enabled, skipInvalid, minSats, maxHdop, maxSpeed, lbsCorrection):
        """
                Parameters
         Name  Description  itemId  unit ID 
         enabled  1 - enable filtration of unit position information in messages, 0 - disable 
         skipInvalid  skip invalid messages 
         minSats  minimum satellites 
         maxHdop  maximum HDOP value 
         maxSpeed  maximum speed value 
         lbsCorrection  allow positioning by cellular base stations Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_messages_filter", **params)


    def get_command_definition_data(self, itemId, col):
        """
                Params
         Name  Description  itemId  unit ID 
         col  command ID's array Response
        The same as create and update command
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/get_command_definition_data", **params)


    def update_video_status(self, units, status):
        """
                Parameters
         Name  Description  units  units ID array 
         status  billing statusstatus: 0 - billing deactivation, 1 - billing activation.
        For example, 
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_video_status", **params)


    def update_calc_flags(self, itemId, newValue):
        """
                Parameters
         Name  Description  itemId  unit ID 
         newValue  new counter calculation flags (see below) Counter calculation flags:
         Flag  Description  0x000  Mileage counter: GPS 
         0x001  Mileage counter: Mileage sensor 
         0x002  Mileage counter: Relative odometer 
         0x003  Mileage counter: GPS + engine ignition sensor 
         0x010  Engine hours counter: Engine ignition sensor 
         0x020  Engine hours counter: Absolute engine hours sensor 
         0x040  Engine hours counter: Relative engine hours sensor 
         0x100  Auto calculation of mileage from new messages 
         0x200  Auto calculation of engine hours from new messages 
         0x400  Auto calculation of GPRS traffic Response{
        "cfl":<uint>/* flags applied */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_calc_flags", **params)


    def registry_custom_event(self, date, x, y, description, violation, itemId, nt):
        """
                Parameters
         Name  Description  date  date 
         x  longitude 
         y  latitude 
         description  description 
         violation  violation: 0 - common event, 1 - violation 
         itemId  unit ID 
         nt  notification text The nt parameter is passed when registering an event for online notification. The text of the triggered notification is transferred to it.Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/registry_custom_event", **params)


    def update_access_password(self, itemId, accessPassword):
        """
                Parameters
         Name  Description  itemId  unit ID 
         accessPassword  new access password Response{
        "psw":<text>/* new access password */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_access_password", **params)


    def calc_last_message(self, unitId, sensors, flags):
        """
                Parameters
         Name  Description  unitId  unit ID 
         sensors  array of sensors IDs (optional parameter, if not specified or empty - return values of all sensors) 
         flags  flags (optional): if 1, then calculate sensor value by last valid param value If there is not parameter in message, the flags = 1 will return value from last valid message.If there is parameter in messages,but the sensor is validated by table/other sensors, then it will return the NA (-348201.3876) value in any case. The other way to get always valid sensor's valye is to get event type sensors from eventsResponse{
        <text>:<double|text>,/* sensor ID: sensor value */
        ...
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/calc_last_message", **params)


    def update_hw_params(self, hwId, action):
        """
                Parameters
        Required parameters:
         Name  Description  hwId  hardware type ID 
         action  action:
        set - set configuration;
        check_config - check if hardware has parameters for configuring;
        download_file - download configuration file;
        get - get configurationAdditional parameters, if action = set:{
        "itemId":<long>,
        "params_data":{
        "params": [{
        "name":<text>,
        "type":<text>,
        "value":<text|int|double>,
        "reset":<uint>,
        "set_psw":<uint>
        }],
        "reset_all":<uint>,
        "full_data":<uint>
        }
        } Name  Description  itemId  unit ID 
         params_data  parameters data 
         params  array of parameters configurations 
         name  parameter name 
         type  parameter type (see below) 
         value  parameter value 
         reset  flag: 1 - reset on default value, 0 - do not reset 
         set_psw  flag (if parameter type “password”): 1 - change password, 0 - do not change 
         reset_all  reset hardware type configuration 
         full_data  if 0 - then “value” store path of uploading file, if 1 -  then “value” store HEX-string Parameter types:
         text; file; long; double; int; bool; password.If the parameter is of “file” type, use a POST request with multiple contents (multipart/form-data) to upload it.
        For example:POST /wialon/ajax.html?
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_hw_params", **params)


    def update_service_interval(self, itemId, id, callMode, n, t, im, it, ie, pm, pt, pe, c):
        """
                Parameters
         Name  Description  itemId  unit ID 
         id  service interval ID 
         callMode  action: create, update, delete 
        Parameters required only to create and update:
         n  name of interval 
         t  description 
         im  mileage interval 
         it  days interval 
         ie  engine hours interval 
         pm  last service for mileage interval, km 
         pt  last service for days interval, sec (UTC) 
         pe  last service for engine hours interval, h 
         c  done times Response
        On create and edit:[
        <long>,/* service interval ID */
        {
        "id":<long>,/* service interval ID */
        "n":<text>,/* name */
        "t":<text>,/* description */
        "im":<uint>,/* mileage interval */
        "it":<uint>,/* days interval */
        "ie":<uint>,/* engine hours interval */
        "pm":<uint>,/* last service for mileage interval, km */
        "pt":<uint>,/* last service for days interval, sec (UTC) */
        "pe":<uint>,/* last service for engine hours interval, h */
        "c":<uint>/* done times */
        }
        ]On delete:[
        <long>,/* service interval ID */
        null
        ]
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_service_interval", **params)


    def add_video_packets(self, units, packets):
        """
                Parameters
         Name  Description  units  units ID array 
         packets  number of packages addedFor example, 
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/add_video_packets", **params)


    def get_drive_rank_settings(self, itemId):
        """
                Response
        Returns the list of drive rank criteria and its parameters. IF criteria aren't defined then empty object returned {}.{
            "acceleration":[...],
            "brake":[...],
            "global":{...},
            "turn":[...],
            "sensor":[...],
            "speeding":[...],
            "harsh":[...]
         } All criteria and parameters are defined in  update drive rank parameters.
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/get_drive_rank_settings", **params)


    def upload_image(self, itemId, eventHash):
        """
                Parameters
         Name  Description  itemId  unit ID 
         eventHash  event name which will be generated after uploading the image (optional parameter) To upload an image, use a POST request with multiple contents (multipart/form-data), where one part contains parameters and the other contains the image.
        For example:Request URL: https://hst-api.wialon.com/wialon/ajax.html?
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/upload_image", **params)


    def update_device_type(self, itemId, deviceTypeId, uniqueId):
        """
                Parameters
         Name  Description  itemId  unit ID 
         deviceTypeId  new device type 
         uniqueId  new unique ID You can get all available hardware types using the command  get_hw_types.
        Response{
        "uid":<text>,/* unique ID */
        "hw":<long>/* hardware type */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_device_type", **params)


    def registry_status_event(self, date, description, itemId):
        """
                Parameters
         Name  Description  date  date 
         description  description 
         itemId  unit ID Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/registry_status_event", **params)


    def update_video_autopay(self, units, value):
        """
                Parameters
         Name  Descriptions  units  units ID array 
         value  value of auto-purchase of traffic packetsFoe example, 
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_video_autopay", **params)


    def update_command_definition(self, itemId, id, callMode, n, c, l, p, a):
        """
                Parameters
         Name  Description  itemId  unit ID 
         id  command ID 
         callMode  action: create, update, delete 
        Parameters required only for create and update:
         n  command name 
         c  type (see below) 
         l  link type (see below) 
         p  parameters 
         a  access level: rights that user must have to execute current command (see  Access flags: General and  Access flags: Units and unit groups) 
        Optional (to copy command from other unit):
         oldItemId  copied command unit ID 
         oldCmdId  copied command ID Command types:
         block_engine - block engine; unblock_engine - unblock engine; custom_msg - custom message; driver_msg - message to driver; download_msgs - download messages; query_pos - query position; query_photo - query snapshot; output_on - activate output; output_off - deactivate output; send_position - send coordinates; set_report_interval - set data transfer interval; upload_cfg - upload configuration; upload_sw - upload firmware.Link types:
         empty string - auto; tcp - TCP; udp - UDP; vrt - virtual; gsm - SMS.Response
        On create and edit:[
        <long>,/* command ID */
        {
        "id":<long>,/* command ID */
        "n":<text>,/* command name */
        "c":<text>,/* command type */
        "l":<text>,/* link type */
        "p":<text>,/* parameters */
        "a":<uint>/* access level */
        }
        ]On delete:[
        <long>,/* command ID */
        null
        ]
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_command_definition", **params)


    def get_trip_detector(self, itemId):
        """
                Parameters
         Name  Description  itemId  unit ID Response{
        "type":<uint>,/* type of movement detection (see below) */
        "gpsCorrection":<uint>,/* allow GPS correction: 0 - no, 1 - yes */
        "minSat":<uint>,/* min satellites count */
        "minMovingSpeed":<uint>,/* min moving speed, km/h */
        "minStayTime":<uint>,/* min parking time, seconds */
        "maxMessagesDistance":<uint>,/* max distance between messages, meters */
        "minTripTime":<uint>,/* min trip time, seconds */
        "minTripDistance":<uint>/* min trip distance, meters */
        }Types of movement detection:
          Value   Description   1   GPS speed 
          2   GPS coordinates 
          3   Engine ignition sensor 
          4   Mileage sensor 
          5   Relative odometer 
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/get_trip_detector", **params)


    def get_accelerometers_calibration(self, itemId):
        """
                Response{
             "acceleration":           /* acceleration calibration coefficients */
                 {
                   "coef_x":<double>,    /* coefficient by x-axis */
                   "coef_y":<double>,    /* coefficient by y-axis */
                   "coef_z":<double>,    /* coefficient by z-axis */
                   "cos":<double>,       /* cosine of angle between theoretical and extimated axis */
                   "sin":<double>        /* sine of angle between theoretical and extimated axis */
                 },
             "brake":{ ... },         /* brake calibration coefficients */
             "turn":{ ... },          /* turn calibration coefficients */
             "vertical":{ ... },      /* vertical axis calibration coefficients */
             "crc":<uint>,            /* accelerometer sensors check sum */
             "dateinput":<uint>       /* calibration date */
          }If accelerometer is not calibrated then {error:0} returned.
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/get_accelerometers_calibration", **params)


    def update_fuel_rates_params(self, itemId, consSummer, consWinter, winterMonthFrom, winterDayFrom, winterMonthTo, winterDayTo):
        """
                Parameters
         Name  Description  itemId  unit ID 
         consSummer  summer consumption, litres per 100 km 
         consWinter  winter consumption, litres per 100 km 
         winterMonthFrom  winter from (month: 0-11) 
         winterDayFrom  winter from (day 1-31) 
         winterMonthTo  winter to (month 0-11) 
         winterDayTo  winter to (day 1-31) Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_fuel_rates_params", **params)


    def update_fuel_math_params(self, itemId, idling, urban, suburban, loadCoef):
        """
                Parameters
         Name  Description  itemId  unit ID 
         idling  idling, litres per hour 
         urban  urban cycle, litres per 100 km 
         suburban  suburban cycle, litres per 100 km  
         loadCoef  coefficient when moving under load Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_fuel_math_params", **params)


    def get_messages_filter(self, itemId):
        """
                Parameters
         Name  Description  itemId  unit ID Response{
        "enabled":<uint>,/* 1 - enable filtration of unit position information in messages, 0 - disable */
        "skipInvalid":<uint>,/* skip invalid messages */
        "minSats":<uint>,/* minimum satellites */
        "maxHdop":<uint>,/* maximum HDOP value */
        "maxSpeed":<uint>/* maximum speed value */
        "lbsCorrection":<double>,/* allow positioning by cellular base stations */
        "wifiCorrection":<bool>,/* allow positioning by Wi-Fi */
        "wifiAccuracy":<double>,/* required accuracy in meters */
        "minWifiPoints":<uint>,/* minimum points to positioning*/
        "maxWifiPoints":<uint>/* maximum points to positioning */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/get_messages_filter", **params)


    def get_vin_info(self, vin):
        """
                Params
         Name  Description  vin  VIN number Response
        If success: {
            {
        "vin_lookup_result":{
            "pflds":[/* profile fields */
        {"n":<text>,/* field name */
        "v":<text>},/* field value */
        ...
            ]
        }
            }
        }If fail:{
            "vin_lookup_result":{
        "error":<bool>,/* true if error */
        "message":<text>,/* error message */
        "reasons":[/* error reasons */
            <text>,
            ...
        ]
            }
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/get_vin_info", **params)


    def update_eh_counter(self, itemId, newValue):
        """
                Parameters
         Name  Description  itemId  unit ID 
         newValue  new value of engine hours counter (h) Response{
        "cneh":<uint>/* value of engine hours counter (h) */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_eh_counter", **params)


    def update_unique_id2(self, itemId, uniqueId2):
        """
                Parameters
         Name  Description  itemId  unit ID 
         uniqueId2  new second unique ID Response{
        "uid2":<text>/* second unique ID */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_unique_id2", **params)


    def registry_fuel_filling_event(self, date, volume, cost, location, deviation, x, y, description, itemId):
        """
                Parameters
         Name  Description  date  date 
         volume  filled volume, lt 
         cost  cost 
         location  location 
         deviation  time deviation (±), min 
         x  longitude 
         y  latitude 
         description  description 
         itemId  unit ID Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/registry_fuel_filling_event", **params)


    def update_activity_settings(self, itemId, type):
        """
                Response{ } /* success execution */Parameters
         Name  Description  itemId  unit ID 
         type  source type Parameter “type” values:
         Value  Description  0  None 
         1  Bindings 
         2  Tachograph Getting the selected source
        To get the selected source, use the command unit/get_activity_settings
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/update_activity_settings", **params)


    def get_report_settings(self, itemId):
        """
                Parameters
         Name  Description  itemId  unit ID Response{
        "speedLimit":<uint>,/* speed limit, km/h */
        "maxMessagesInterval":<uint>,/* maximum interval between messages, seconds */
        "dailyEngineHoursRate":<uint>,/* daily engine hours rate, seconds */
        "urbanMaxSpeed":<uint>,/* urban speed limit, km/h */
        "mileageCoefficient":<uint>/* mileage coefficient */
        "fuelRateCoefficient":<uint>,   /* Fuel consumption, l/100 км (gal/miles) */
        "speedingTolerance":<uint>,/* allowed speeding, km/h (used if speedingMode = 1) */
        "speedingMinDuration":<uint>,   /* min speeding time, seconds */
        "speedingMode":<uint>           /* speeding detection mode: 0 - use speedLimit, 1 - use map data */
        }If speedingMode = 0 and speedLimit = 0 then no any speeding table is built.
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit/get_report_settings", **params)
