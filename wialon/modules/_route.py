
class Route:
    def __init__(self, session):
        self.session session

    def get_round_data(self, itemId, col):
        """
                Parameters
         Name  Description  itemId  route ID 
         col  array of rounds IDs Response[
        {
        "id":<long>,/* round ID */
        "n":<text>,/* name */
        "d":<text>,/* description */
        "tz":<uint>,/* timezone */
        "u":<long>,/* unit appointed to this round: if not specified - first unit of "cu" array which goes out from the first check point */
        "cu":[<long>],/* array of unit IDs */
        "pt":[/* check points */
        {
        "n":<text>,/* name */
        "f":<uint>,/* type */
        "u":<long>,/* unit ID, 0 - if check point not of the type: check point from unit */
        "y":<double>,/* latitude */
        "x":<double>,/* longitude */
        "r":<uint>/* radius */
        }
        ],
        "sh":{/* schedule */
        "id":<long>,/* ID */
        "n":<text>,/* name */
        "f":<uint>,/* type */
        "tz":<uint>,/* timezone */
        "cfg":{/* custom configuration (example) */
        "enabled":<byte>,/* auto create rounds for current schedule: 1 - enable, 0 - disable */
        "name":<text>,/* name */
        "roundFlags":<uint>,/* round flags (see below) */
        "units":[<long>],/* array of units IDs */
        "validityPeriod":<uint>/* validity period */
        },
        "tm":[/* time of passing points */
        {
        "at":<uint>,/* arrival time */
        "ad":<uint>,/* deviation from arrival time */
        "dt":<uint>,/* departure time */
        "dd":<uint>/* deviation from departure time */
        }
        ],
        "sch":{/* time limitation */
        "f1":<uint>,/* beginning of interval 1 */
        "f2":<uint>,/* beginning of interval 2 */
        "t1":<uint>,/* ending of interval 1 */
        "t2":<uint>,/* ending of interval 2 */
        "m":<uint>,/* days of month mask */
        "y":<uint>,/* months mask */
        "w":<uint>/* days of week mask */
        }
        },
        "at":<uint>,/* activation time */
        "vt":<uint>,/* time from which validity period begins */
        "vp":<uint>,/* validity period */
        "f":<uint>,/* round flags (see below) */
        "st":{/* round state */
        "st":{/* general round state */
        "pi":<uint>,/* check point index, if 4294967295 - round isn't started */
        "ps":<uint>,/* state flags + event flags (see below) */
        "ut":<uint>/* last event time */
        },
        "pts":{ /* state by points */
        <text>:{/* check point ID */
        "st": <uint>,/* event flags (see below) */
        "tm": <uint>/* last event time */
        },
        ...
        }
        }
        }
        ]Types of check points are described in the chapter Update check points. 
        Schedule types are described in the chapter Schedules: create, edit, delete.
        Round flags
          Flag   Description   0x0   check points order: strict  
          0x2   remove finished rounds from the timeline 
          0x10   check points order: skipping possible 
          0x20   allows to make reports upon performance on a round 
          0x40   check points order: arbitrary Round state flags
          Flag   Description   0x010000   not active 
          0x020000   finished 
          0x040000   expecting arrival 
          0x080000   expecting departure 
          0x200000   is late 
          0x400000   outrun 
          0x800000   stopped Event flags
          Flag   Description   0x1   round begins 
          0x2   round finished 
          0x4   round aborted 
          0x8   arrive in check point 
          0x10   pass check point 
          0x20   depart from check point 
          0x40   registered late arrival 
          0x80   registered outrun 
          0x100   pass check point in time  
          0x200   delayed arrival 
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("route/get_round_data", **params)


    def get_all_rounds(self, itemId, timeFrom, timeTo, fullJson):
        """
                Parameters
         Name  Description  itemId  route ID 
         timeFrom  interval beginning 
         timeTo  interval end 
         fullJson  response format: 1 - detailed information, 0 - short information Response
        Short information:{
        "actual":[/* rounds with state "in progress" and "finished" */
        {
        ...
        }
        ],
        "history":[/* rounds with status "history" */
        {
        ...
        }
        ],
        "virtual":[/* rounds with status "waiting" */
        {
        "time":<uint>,/* beginning of round */
        "schedule":{/* schedule */
        "id":<long>,/* ID */
        "n":<text>,/* name */
        "f":<uint>,/* type */
        "tz":<uint>,/* timezone */
        "cfg":{/* custom configuration (example) */
        "autoName":/* use automatically generated name:  0 - no, 1 - yes */
        "enabled":1,/* auto create rounds for current schedule: 1 - enable, 0 - disable */
        "name":<text>,/* round name */
        "roundFlags":<uint>,/* round flags */
        "units":[<long>],/* array of units IDs */
        "validityPeriod":<uint>/* validity period */
        },
        "tm":[/* time of passing points */
        {
        "at":<uint>,/* arrival time */
        "ad":<uint>,/* deviation from arrival time */
        "dt":<uint>,/* departure time */
        "dd":<uint>/* deviation from departure time */
        }
        ],
        "sch":{
        "f1":<uint>,/* beginning of interval 1 */
        "f2":<uint>,/* beginning of interval 2 */
        "t1":<uint>,/* ending of interval 1 */
        "t2":<uint>,/* ending of interval 2 */
        "m":<uint>,/* days of month mask */
        "y":<uint>,/* months mask */
        "w":<uint>/* days of week mask */
        }
        }
        }
        ]
        }Format of “actual” and “history” arrays is similar to one described in the chapter Load rounds for interval (short information).
        Schedules types are described in the chapter Schedules: create, edit, delete.
        Detailed information:
        Detailed information has similar format as short information except the following: format of elements of “actual” and “history” arrays will be the same as one described in the chapter Round information.
        """
        params = locals()
        params.pop('self')
        return self.session.call("route/get_all_rounds", **params)


    def get_schedule_time(self, itemId, scheduleId, timeFrom, timeTo):
        """
                Parameters
         Nane  Description  itemId  route ID 
         scheduleId  schedule ID  
         timeFrom  interval beginning 
         timeTo  interval end Response[
        {
        "time":<uint>/* time of round beginning */
        }
        ]
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("route/get_schedule_time", **params)


    def update_round(self, itemId, id, callMode, n, d, u, at, vt, vp, sh, cu, f, tz):
        """
                Parameters
         Name  Description  itemId  route ID 
         id  round ID 
         callMode  action: create, update, delete 
        Parameters required only to create and update: 
          sh   schedule ID 
         You can find description of other parameters in the chapter Round information. Response
        On create and edit:[
        <long>,/* round ID */
        {
        "id":<long>,/* round ID */
        "n":<text>,/* name */
        "d":<text>,/* description */
        "sh":<text>,/* schedule name */
        "f":<uint>,/* round flags */
        "tz":<uint>,/* timezone */
        "u":<long>,/* unit attached to this round: if not specified - first unit from the "cu" array, which goes out from the first check point, will be assigned */
        "at":<uint>,/* activation time */
        "vt":<uint>,/* time from which validity period begins */
        "vp":<uint>,/* validity periodя */
        "sts":<uint>,/* round state flags */
        "st":{/* round state */
        "st":{/* general round state */
        "pi":<uint>,/* check point index, if 4294967295 - round isn't started */
        "ps":<uint>,/* state flags + event flags */
        "ut":<uint>/* last event time */
        },
        "pts":{ /* state by pointsм */
        <text>:{/* check point ID */
        "st": <uint>,/* event flags */
        "tm": <uint>/* last event time */
        },
        ...
        }
        }
        }
        ]Values of round state and event flags are described in the chapter Round information.
        On delete:[
        <long>,/* round ID */
        null
        ] ;
        """
        params = locals()
        params.pop('self')
        return self.session.call("route/update_round", **params)


    def load_rounds(self, itemId, timeFrom, timeTo, fullJson):
        """
                Parameters
         Name  Description  itemId  route ID 
         timeFrom  interval beginning 
         timeTo  interval end 
         fullJson  response format: 1 - detailed information, 0 - short information Response
        Short information:[
        {
        "id":<long>,/* round ID */
        "n":<text>,/* name */
        "d":<text>,/* description */
        "sh":<text>,/* schedule name */
        "f":<uint>,/* round flags */
        "tz":<uint>,/* timezone */
        "u":<long>,/* unit, assigned on this round */
        "at":<uint>,/* activation time */
        "vt":<uint>,/* time from which validity period begins */
        "vp":<uint>,/* validity period */
        "sts":<uint>,/* round state flags */
        "st":{/* round state */
        "st":{/* general round state */
        "pi":<uint>,/* check point index, if 4294967295 - round isn't started */
        "ps":<uint>,/* state flags + event flags */
        "ut":<uint>/* last event time */
        },
        "pts":{/* state by points */
        <text>:{/* check point ID */
        "st": <uint>,/* event flags */
        "tm": <uint>/* last event time */
        }
        }
        }
        }
        ]Round state flags and event flags can be found in the chapter Round information.
        Detailed information:
        The format of the response will be the same as one described in the chapter Round information.
        """
        params = locals()
        params.pop('self')
        return self.session.call("route/load_rounds", **params)
