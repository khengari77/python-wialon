
class Events:
    def __init__(self, session):
        self.session = session

    def unload(self, ):
        """
                Response{ }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("events_unload", **params)


    def check_updates(self, lang, measure, detalization):
        """
                Parameters
        All parameters are optional.
          Param    Description   Default value  lang  languare (2-symbol code)   en  
        measure  measure:
        0 - si,
        1 - us,
        2 - imperial   from user's settings  
         detalization  output flags (see below)   0x7  Output flags
         Flag  Descrition  0x1  Basic JSON: event start - event end 
         0x2  Specified detector data 
         0x4  User parameters (those which user stated for this event) 
         0x10  Full JSON. Every detector treats it its own way 
         0x20  Formatted value Sensor type
         type
        value   Description    How events registered    1   Switcher sensors:
        engine operation;
        digital;
        engine efficiency;
        private mode;
        alarm trigger;
        counter(switch to ON/to OFF)
         Events are registered from ON position
        to OFF position. 
          2   Instant sensors:
        odometer;
        relative engine hours;
        instant fuel consumption;
        counter(instant)  Events are registered from the first non-
        zero value to the last non-zero one. 
          3   Differential sensors : mileage;
        engine hours;
        impulse fuel consumption;
        absolute fuel consumption;
        counter(differential + with overflow);
        fuel level impulse sensor  Events are registered from start of value
        increasing to the end of it. 
          4   Analog sensors: temperature;
        engine rpm;
        voltage;
        weight sensor;
        accelerometer;
        temperature coefficient;
        custom  Events are not registered. Response
        0x1 flag
        Returns basic JSON (equal to all sensor groups)"<type_name>": {
        "<sensor_id>": {
        "from": {
        "t":<uint>,/* time (UNIX-time) */
        "y":<double>,/* latitude */
        "x":<double>/* longitude */
        },
        "to": {
        "t":<uint>,/* time (UNIX-time) */
        "y":<double>,/* latitude */
        "x":<double>/* longitude */
        },
        "m":<uint>,/* last message received time */
        "f":<uint> /* service flag */
        }
        }0x2 flag
        Returns specified detector data"ignition": {
        "<sensor_id>": 
        {
            "state":<uint>,/* state: 0 - off, 1 - on */
            "type": 1,/* sensor type: switcher sensor */
            "hours":<uint>,/* engine hours for all history, sec */
            "switches":<uint>,/* number of swithes for all hoistory */
            "value":<bool>/* current value */
        }
        ...
        }Here are listed all sensor types for sensors:"sensors": {
        "<sensor_id1>": 
        {
            "state":<uint>,/* state: 0 - off, 1 - on */
            "type": 1,/* sensor type: switcher sensor */
            "hours":<uint>,/* engine hours for all history, sec */
            "switches":<uint>,/* number of swithes for all hoistory */
            "value":<bool>/* current value */
        },
        "<sensor_id2>": 
        {
            "type": 2,/* sensor type: instant sensor */
            "counter":<uint>,/* message sequence conuter in event */
            "summary":<uint>,/* value summary in event */
            "total_counter":<uint>,/* number of messages in history */
            "total_summary"<uint>,/* value summary in history */
            "value":<double> /* last value; if -348201.3876 -- value unknown */
        },
        "<sensor_id3>": 
        {
            "type": 3,/* sensor type: differential sensor */
            "counter":<uint>,/* value sum in event */
            "total_counter":<uint>,/* value sum in history */
            "value":<double> /* last value; if -348201.3876 -- value unknown */
        },
        "<sensor_id4>": 
        {
            "type": 4,/* sensor type: analog sensor */
            "value":<double> /* last value; if -348201.3876 -- value unknown */
        }
        }
        "lls": {
        "<sensor_id>":
        {
            "value":<double>, /* last message value with calculated level */
            "level":<double>, /* average median value  (FLS filtration value is used) */
            "filled":<double> /* fuel filled */
        }
        }
        "trips": {
        "state":<bool>,/* state: 0 - parking, 1 - trip, 2 - stop */
        "max_speed":<uint>,/* max speed in trip */
        "curr_speed":<uint>,/* current speed */
        "avg_speed":<uint>,/* average speed according to distance */
        "distance":<uint>,/* GPS mileage in trip */
        "odometer":<uint>,/* distance for all trips */
        "course":<uint>,/* course */
        "altitude":<uint>/* altitude */
        }
        "counters": {
        "engine_hours": <uint>,   /* engine hours counter */
        "mileage": <uint>,        /* mileage counter */
        "bytes": <uint>           /* GPRS traffic counter */ 
        }0x4 flag
        Returns user parameters
        Response depends on user definitions for current event."<type_name>": {
        "<sensor_id>": {
        "p":{/* user-defined object content */
        "test":2,
        "foo":"bar",
        "trips":1
        }
        }
        }0x10 flag
        Returns full JSON
        For sensors with both type=2 and type=3 (except FLS):"sensors": {
        "<sensor_id>": 
        {
            "msgs": [
        {
            "tm":<uint>,/* message time, UNIX-time */
            "v":<double>/* value */
        },
        ...
            ]
        },
        ...
        }For FLS:"lls": {
        "<sensor_id>": {
        "msgs": [
            {
        "tm":<uint>,/* message time, UNIX-time */
        "v":<double>,/* value */
        "l":<double>/* average median value  (FLS filtration value is used) */
            },
            ...
        ]
        }
        },
        ...
        }0x20 flag
        Returns formatted values"ignition": {
        "sensor_id": {
        "format": {
            "value":<text>/* formatted value  (usually "On"/"Off") */
        }
        }
        }
        "sensors": {
        "sensor_id": {
        "format": {
            "value":<text>/* formatted value, depends on sensor type and format */
        }
        }
        }
        "trips": {
        "format": {
        "distance":<text>,/* distance according to prev message */
        "avg_speed":<text>/* average speed according to "distance"  */
        }
        }
        "lls": {
        "sensor_id": {
        "format": {
            "value":<text>,/* formatted value, depends on sensor type and format */
            "filled":<text>/* fuel filled */
        }
        }
        }
        "counters": {
        "format": {
        "engine_hours":<uint>,   /* formatted value of engine hours counter */
        "mileage":<text>,        /* formatted value of mileage counter */
        "bytes":<uint>           /* formatted value of GPRS traffic counter */ 
        }
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("events_check_updates", **params)
