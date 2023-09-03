
class Render:
    def __init__(self, session):
        self.session = session

    def remove_all_layers(self, ):
        """
                Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("render_remove_all_layers", **params)


    def create_messages_layer(self, layerName, itemId, timeFrom, timeTo, tripDetector, trackColor, trackWidth, arrows, points, pointColor, annotations, flags):
        """
                 Current request can't be executed simultaneously with following requests:
         report/exec_report, report/export_result, report/get_result_chart, report/get_result_map, messages/load_interval, unit/get_trips, resource/get_driver_bindings, resource/get_trailer_bindings, all requests from chapter Export and import, account/get_account_history. You can find an example of this request in the sample Messages.
        Parameters
         Name  Description  layerName  layer name 
         itemId  ID of unit which messages will be requested 
         timeFrom  interval beginning 
         timeTo  interval end 
         tripDetector  use trip detector: 0 - no, 1 - yes 
         trackColor  track color in ARGB format (A - alpha channel or transparency level), or “trip” (to coloring by trips, requires “tripDetector”:1) 
         trackWidth  track line width in pixels 
         arrows  show course of movement arrows: 0 - no, 1 - yes 
         points  show points at places where messages were received: 0 - no, 1 - yes 
         pointColor  points color 
         annotations  show annotations for points: 0 - no, 1 - yes 
         flags  display markers flags (optional parameter) Markers flags:
         Flag  Value  0x0001  grouping markers 
         0x0002  numbering for markers 
         0x0004  events markers 
         0x0008  fillings 
         0x0010  images 
         0x0020  parkings 
         0x0040  speedings 
         0x0080  stops 
         0x0100  thefts 
         0x0800  video markers Response{
        "name":<text>,/* layer name */
        "bounds":[/* layer bounds */
        <double>,/* minimal latitude */
        <double>,/* minimal longitude */
        <double>,/* maximal latitude */
        <double>/* maximal longitude */
        ],
        "units":[/* array of units */
        {
        "id":<long>,/* unit ID */
        "msgs":{/* information about messages */
        "count":<uint>,/* messages count */
        "first":{/* first message */
        "time":<uint>,/* time */
        "lat":<double>,/* latitude */
        "lon":<double>/* longitude */
        },
        "last":{/* last message */
        "time":<uint>,/* time */
        "lat":<double>,/* latitude */
        "lon":<double>/* longitude */
        }
        },
        "mileage":<double>,/* mileage for interval (metres) */
        "max_speed":<unit>/* maximal speed for interval */
        }
        ]
        }See also Get tiles of graphic layers.
        """
        params = locals()
        params.pop('self')
        return self.session.call("render_create_messages_layer", **params)


    def get_messages(self, layerName, indexFrom, indexTo, unitId):
        """
                Parameters
         Name  Description  layerName  layer name 
         indexFrom  index of the first requested message 
         indexTo  index of the last requested message 
         unitId  unit ID Response[/* array of messages */
        {
        ...
        }
        ]Message formats are described in the chapter  Data format: Messages.
        """
        params = locals()
        params.pop('self')
        return self.session.call("render_get_messages", **params)


    def delete_message(self, layerName, msgIndex, unitId):
        """
                Parameters
         Name  Description  layerName  layer name 
         msgIndex  message index 
         unitId  unit ID Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("render_delete_message", **params)


    def enable_layer(self, layerName, enable):
        """
                Parameters
         Name  Description  layerName  layer name 
         enable  make active: 0 - no 1 - yes Response{
        "enabled":<int>/* state: 0 - inactive; 1 - active */
        }See also Get tiles of graphic layers.
        """
        params = locals()
        params.pop('self')
        return self.session.call("render_enable_layer", **params)


    def remove_layer(self, layerName):
        """
                Parameters
         Name  Description  layerName  layer name Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("render_remove_layer", **params)


    def set_locale(self, tzOffset, language, flags, formatDate, density):
        """
                Parameters
         Name  Description  Notes  tzOffset  timezone  
         language  language (two-lettered code)  
         flags  flags:
        0 - metric system of measurement,
        1 - US system,
        2 - imperial system  optional 
         formatDate  date & time format (see below)  
         density  tile size  optional Date & time format
         Parameter   Description    %H   The hour of the day with leading zero if required (“00” to “23”) 
          %B   The full month name (“January” to “December”) 
          %b   Abbreviated month name (“Jan” to “Dec”) 
          %m   The month of the year with leading zero if required (“01” to “12”) 
          %l   The month of the year between 1-12 (“1” to “12”) 
          %P   Format Persian calendar (“01 Farvardin 1392 00:00:00”) 
          %A   The full day name (“Monday” to “Sunday”) 
          %a   Abbreviated day name (“Mon” to “Sun”) 
          %E   The day of the month with leading zero if required (“01” to “31”) 
          %e   The day of the month between 1 and 31 (“1” to “31”) 
          %I   The hour of the day with leading zero if required (“01” to “12”) 
          %M   The minute of the hour with leading zero if required (“00” or “59”) 
          %S   The seconds of the minute with leading zero if required (“00” to “59”) 
          %p   Displays the A.M./P.M. designator (“AM” or “PM”) 
          %Y   The full four digit year (“1999” or “2008”) 
          %y   The year as a two-digit number (“99” or “08”) Example:"formatDate":"%Y-%m-%E %H:%M:%S" It is necessary to escape the character “%” and pass it in the request as “%25”
        Result:2013-01-26 12:34:56Density
        Default tile size is 256*256.
          Value    Tile size    Ratio   1  256*256  1 
         2  378*378  1.5 
         3  512*512  2 
         4  768*768  3 
         5  1024*1024  4 Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("render_set_locale", **params)
