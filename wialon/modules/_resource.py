
class Resource:
    def __init__(self, session):
        self.session session

    def update_orders_notification(self, resourceId, ordersNotification):
        """
                Parameters
          Name    Description   resourceId  resource id 
         ordersNotification  orders notification template settings JSON JSON keys{
        "sms":<text>,/* sms notification text */
        "subj":<text>,/* email subject */
        "text":<text>,/* email text */
        "html":<uint>,/* email text as html (1 - yes) */ 
        "currency":<text>,/* currency */
        "dns":<text>,/* locator URL (without http://)*/
        "driverPushMsg":{/* driver PUSH notification settings */
        "crR":{
            "t":<text>/* notification text upon new route creation */
          },
            "delR":{
            "t":<text>/* notification text upon route deleting */
            },
            "updC":{
            "t":<text>/* notification text upon contact details changing */
            },
            "attO":{
            "t":<text>/* notification text upon files attaching */
            },
            "detO":{
                    "t":<text>/* notification text upon files deleting */
            },
            "updG":{
                    "t":<text>/* notification text upon order parameters changing */
                },    
            "vtD":{
                    "t":<text>/* notification text upon delivery time exceeding */
            },
            "utD":{
                    "t":<text>/* notification text upon unloading time exceeding */
            },
            "trk":{
                    "t":<text>/* notification text upon deviation from a route */
            }
            "skp":{
                    "t":<text>/* notification text upon skiping a order */
            },
            "stO":{
                    "t":<text>/* notification text upon order non-confirmation by courier/operator */
            }    
            }, 
        }Tegs of notification body and email subject
          Name    Description   %ORDER_NAME%  order name 
         %ORDER_ARRIVAL_TIME%  arrival time 
         %ORDER_COST%  order cost 
         %ORDER_COMMENT%  comment to order 
         %LOCATOR_LINK%  link to locator to order unit Response{ }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/update_orders_notification", **params)


    def upload_tag_image(self, itemId, tagId, eventHash):
        """
                 To delete an image, use the command Tags (e.g. passengers): create, edit, delete.
        Parameters
         Name  Description  itemId  resource ID 
         tagId  tag ID 
         eventHash  name of event which will be generated after uploading the image (optional parameter) To upload an image, use a POST request with multiple contents (multipart/form-data), where one part contains parameters and the other contains the image. 
        For example:Request URL: https://hst-api.wialon.com/wialon/ajax.html?
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/upload_tag_image", **params)


    def cleanup_trailer_interval(self, resourceId, trailerId, timeFrom, timeTo):
        """
                Parameters
         Name  Description  resourceId  resource ID 
         trailerId  trailer ID 
         timeFrom  interval beginning 
         timeTo  interval end Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/cleanup_trailer_interval", **params)


    def cleanup_driver_interval(self, resourceId, driverId, timeFrom, timeTo):
        """
                Parameters
         Name  Description  resourceId  resource ID 
         driverId  driver ID 
         timeFrom  interval beginning 
         timeTo  interval end Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/cleanup_driver_interval", **params)


    def upload_driver_image(self, itemId, driverId, eventHash):
        """
                 To delete an image, use the command Drivers: create, edit, delete.
        Parameters
         Name  Description  itemId  resource ID 
         driverId  driver ID 
         eventHash  name of event which will be generated after uploading the image (optional parameter) To upload an image, use a POST request with multiple contents (multipart/form-data), where one part contains parameters and the other contains the image. 
        For example:Request URL: https://hst-api.wialon.com/wialon/ajax.html?
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/upload_driver_image", **params)


    def driver_operate(self, phoneNumber, password, say, message, timeSend, ej, appId, appType):
        """
                With "sid"
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/driver_operate", **params)


    def get_unit_trailers(self, unitId):
        """
                Parameters
         Name  Description  unitId  unit ID Response{
            <text>:[/* resource ID */
        {
            "id":<text>,/* trailer ID*/
            "nm":<text>,/* trailer name*/
        }, ...
            ], ...
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/get_unit_trailers", **params)


    def upload_tacho_file(self, outputFlag, eventHash):
        """
                To bind uploaded file content to specified driver use that signature:
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/upload_tacho_file", **params)


    def update_tag_units(self, itemId, units):
        """
                Parameters
         Name  Description  itemId  resource ID 
         units  array of units IDs Response{
        "tagrun":[<long>]/* array of auto attachable units */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/update_tag_units", **params)


    def update_trailer_units(self, itemId, units):
        """
                Parameters
         Name  Description  itemId  resource ID 
         units  array of units IDs Response{
        "trlrun":[<long>]/* array of auto attachable units */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/update_trailer_units", **params)


    def get_orders_notification(self, resourceId):
        """
                Parameters
          Name    Description    resourceId   resource id Response{} /* orders notification template settings as JSON */ JSON format
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/get_orders_notification", **params)


    def upload_zone_image(self, itemId, id, eventHash, oldItemId, oldZoneId):
        """
                 To delete an image, use the command Geofences: create, edit, delete.
         To get an image, use Geofence image.
        Parameters
         Name  Description  itemId  resource ID 
         id  geofence ID 
         eventHash  event name, which will be generated after uploading the image
         oldItemId  resource id of other Geofence to set its image (optional parameter)
         oldZoneId  other Geofence id of to set its image (optional parameter)To upload an image, use a POST request with multiple contents (multipart/form-data), where one part contains parameters and the other contains the image. 
        For example:Request URL: https://hst-api.wialon.com/wialon/ajax.html?
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/upload_zone_image", **params)


    def get_unit_drivers(self, unitId):
        """
                Parameters
         Name  Description  unitId  unit ID Response{
            <text>:[/* resource ID */
        {
            "id":<text>,/* driver ID*/
            "nm":<text>,/* driver name*/
            "ph":<text>/* driver phone number*/
        }, ...
            ], ...
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/get_unit_drivers", **params)


    def get_job_data(self, itemId, col):
        """
                Parameters
         Name  Description  itemId  resource ID 
         col  array of jobs IDs Response[
        {
        "id":<long>,/* job ID */
        "n":<text>,/* name */
        "d":<text>,/* description */
        "r":<text>,/* execution type (see below) */
        "at":<uint>,/* activation time */
        "m":<uint>,/* maximal executions count, 0 - unlimited */
                        "fl":<uint>,/* delete job after maximal executions count, 1 - yes */ 
        "tz":<int>,/* timezone (sec) */
        "l":<text>,/* language used for job */
        "st":{/* state */
        "e":<int>,/* enabled/disabled */
        "c":<uint>,/* executions count */
        "l":<uint>/* time of last execution */
        },
        "sch":{/* time limitation */
        "f1":<uint>,/* beginning of interval 1 */
        "f2":<uint>,/* beginning of interval 2 */
        "t1":<uint>,/* ending of interval 1 */
        "t2":<uint>,/* ending of interval 2 */
        "m":<uint>,/* days of month mask */
        "y":<uint>,/* months mask */
        "w":<uint>/* days of week mask */
        },
        "act":{/* actions (list of actions see below) */
        "t":<text>,/* type */
        "p":{/* parameters */
        <text>:<text>,/* name: value */
        ...
        }
        },
        "ct":<uint>,    /* creation time */  
        "mt":<uint>     /* last modification time */
        }
        ]Execution can be either of two types: form a detailed list of execution times or set an interval between executions. If you choose the first option (exact schedule), the format of r field should be “1 …” (after 1 you indicate execution time and if there are several, separate them by space). Time format can be either “hours:minutes” or just “hours”. If you choose the second option (constant interval between executions), the format of r field should be “1 …” (after 2 indicate time interval in Unix format). 
        Action types
         Execute a command over unit(s), GPRS traffic accounting, Change access to units, Mileage accounting, Engine hours accounting, Send fuel information by e-mail or SMS, Send a report by e-mail.Execute a command over unit(s)"act":{
        "t":"exec_unit_cmd",/* action type */
        "p":{
        "cmd_name":<text>,/* command name */
        "cmd_type":<text>,/* command type */
        "cmd_param":<text>,/* command parameter */
        "link_type":<text>,/* link type */
        "timeout":<text>,/* during this time system will try to execute command, sec */
        "units":<text>/* list of units/unit groups ID's (comma-separated) */
        }
        } You can see list of avalible command type here List of available commands
        GPRS traffic accounting"act":{
        "t":"reset_unit_bytes_counter",/* action type */
        "p":{
        "reset_bytes":<text>,/* reset counter value (1 - yes, 2 - no) */
        "store_bytes":<text>,/* store counter value in unit log (1 - yes, 0 - no) */
        "units":<text>/* list of units/unit groups ID's (comma-separated) */
        }
        }Change access to units"act":{
        "t":"change_access_user",/* action type */
        "p":{
        "acl_bits":<text>,/* 1 - set bit, 0 - remove bit */
        "acl_mask":<text>,/* mask of bits which must be changed */
        "units":<text>,/* list of units/unit groups ID's (comma-separated) */
        "users":<text>/* list of users IDs (comma-separated) */
        }
        }Mileage accounting"act":{
        "t":"reset_unit_mileage_counter",/* action type */
        "p":{
        "param_name":<text>,/*
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/get_job_data", **params)


    def get_trailer_bindings(self, resourceId, unitId, trailerId, timeFrom, timeTo):
        """
                 Current request can't be executed simultaneously with following requests:
         report/exec_report, report/export_result, report/get_result_chart, report/get_result_map, messages/load_interval, render/create_messages_layer, unit/get_trips, resource/get_driver_bindings, all requests from chapter Export and import, account/get_account_history.Parameters
         Name  Value  resourceId  resource ID 
         unitId  unit ID (0 - all units) 
         trailerId  trailer ID (0 - all trailers) 
         timeFrom  interval beginning 
         timeTo  interval end Response{
        <text>:[{/* trailer ID */
        "t":<unit>,/* time of binding/unbinding*/
        "u":<long>/* unit ID - binding, 0 - unbinding */
        }],
        ...
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/get_trailer_bindings", **params)


    def driver_status(self, phoneNumber, password, app, fl):
        """
                Params
         Name  Description  phoneNumber  driver phone number 
         password  mobile key 
         app  app name for the generated token 
         fl  optional flags (1 - return token, 2 - return status even if driver is not binded ) Response{
        "drv":{/* driver params */
            "rid":<uint>,   /* resource id */
            "id":<text>,    /* driver id */
            "nm":<text>}    /* driver name */
        },    
        "un":{/* unit params */
            "nm":<text>, 
            "cls":<uint>,     
            "id":<uint>,    
            "mu":<uint>,
            "ct":<uint>,    
            "ftp":{ ... },
            "pos":{ ... },
            "lmsg":{ ... },
            "uri":<text>,
            "ugi":<uint>,
            "uacl":<int>
        },
        "uh":<text>,    /* encrypted device information (for WiaTag) */
        "ul":<text>,    /* encrypted phone number */
        "h":<text>      /* token */
        } Parameters description and entry of "pos", "lmsg"  you can find here: Units
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/driver_status", **params)


    def update_trailers_group(self, itemId, id, callMode, n, d, drs, f):
        """
                Parameters
         Name  Description  itemId  resource ID 
         id  trailer group ID 
         callMode  action: create, update, delete 
         Parameters required only for create and update: 
         n  name 
         d  description 
         drs  array of trailers IDs 
         f  flags: not used at the moment Response
        On create and edit:[
        <long>,/* group ID */
        {
        "id":<long>,/* group ID */
        "n":<text>,/* name */
        "d":<text>,/* description */
        "drs":[<uint>]/* array of trailers IDs */
        }
        ]On delete:[
        <long>,/* group ID */
        null
        ]
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/update_trailers_group", **params)


    def upload_trailer_image(self, itemId, trailerId, eventHash):
        """
                 To delete an image, use the command Trailers: create, edit, delete.
        Parameters
         Name  Description  itemId  resource ID 
         trailerId  trailer ID 
         eventHash  name of event, which will be generated after uploading the image (optional parameter) To upload an image, use a POST request with multiple contents (multipart/form-data), where one part contains parameters and the other contains the image. 
        For example:Request URL:https: //hst-api.wialon.com/wialon/ajax.html?
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/upload_trailer_image", **params)


    def update_email_template(self, resourceId, subject, body, flags):
        """
                Params
         Name  Description  resourceId  resource ID пользователя 
         subject  letter subject 
         body  letter body
         flags  use default template: 0 - yes,1 - no Response{"error":0}/* if success */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/update_email_template", **params)


    def create_zone_by_track(self, layerName, itemId, unitId, n, c, w):
        """
                Params
         Name  Description  layerName  track layer name 
         itemId  resource ID 
         unitId  unit ID 
         n  geofence name 
         c  color (ARGB) 
         w  line thickness Response{
        "all_zones":<uint>, /* number of new geofences (10 000 points in one) */
        "created_zone":<uint>/* number of created geofences */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/create_zone_by_track", **params)


    def get_tag_bindings(self, resourceId, unitId, tagId, timeFrom, timeTo):
        """
                 Current request can't be executed simultaneously with following requests:
         report/exec_report, report/export_result, report/get_result_chart, report/get_result_map, messages/load_interval, render/create_messages_layer, unit/get_trips, resource/get_trailer_bindings, all requests from chapter Export and import, account/get_account_history.Parameters
         Name  Value  resourceId  resource ID 
         unitId  unit ID (0 - all units) 
         tagId  tag ID (0 - all tags) 
         timeFrom  interval beginning 
         timeTo  interval end Response{
        <text>:[{/* tag ID */
        "t":<unit>,/* time of binding/unbinding*/
        "u":<uint>,/* unit ID if binding, 0 if unbinding */
        "pu":<uint>,/* previous unit ID if unbinding, 0 if binding */
        "f":<uint>/* timeout unbinding, 4 - yes */
        }],
        ...
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/get_tag_bindings", **params)


    def update_zones_group(self, itemId, id, callMode, n, d, zns, f):
        """
                Parameters
         Name  Description  itemId  resource ID 
         id  geofences group ID 
         callMode  action: create, update, delete 
         Parameters required only for create and update: 
         n  name 
         d  description 
         zns  array of geofences IDs 
         f  flags: not used at the moment Response
        On create and edit:[
        <long>,/* group ID */
        {
        "id":<long>,/* group ID */
        "n":<text>,/* name */
        "d":<text>,/* description */
        "zns":[<uint>]/* array of geofences IDs */
        }
        ]On delete:[
        <long>,/* group ID */
        null
        ]
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/update_zones_group", **params)


    def update_driver_units(self, itemId, units):
        """
                Parameters
         Name  Description  itemId  resource ID 
         units  array of units IDs Response{
        "drvrun":[<long>]/* array of auto attachable units */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/update_driver_units", **params)


    def get_driver_bindings(self, resourceId, unitId, driverId, timeFrom, timeTo):
        """
                 Current request can't be executed simultaneously with following requests:
         report/exec_report, report/export_result, report/get_result_chart, report/get_result_map, messages/load_interval, render/create_messages_layer, unit/get_trips, resource/get_trailer_bindings, all requests from chapter Export and import, account/get_account_history.Parameters
         Name  Value  resourceId  resource ID 
         unitId  unit ID (0 - all units) 
         driverId  driver ID (0 - all drivers) 
         timeFrom  interval beginning 
         timeTo  interval end Response{
        <text>:[{/* driver ID */
        "t":<unit>,/* time of binding/unbinding*/
        "u":<long>/* unit ID if binding, 0 if unbinding */
        }],
        ...
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/get_driver_bindings", **params)


    def update_tag_message(self, resourceId, unitId, tagId, time, callMode):
        """
                Parameters
         Name  Description  resourceId  resource ID 
         unitId  unit ID to update to binding, 0 to update to unbinding 
         tagId  tag ID 
         time  time 
         callMode  mode: update, delete Response{}/* empty object if success, else - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/update_tag_message", **params)


    def get_zone_data(self, itemId, col, flags):
        """
                Parameters
         Name  Description  Comments  itemId  resource ID  
         col  array of geofences IDs  
         flags  flags, that determine format
        of result JSON  optional
        by default 0x1С Флаги “flags”:
         Значение  Описание  0x01  area 
         0X02  perimeter 
         0X04  boundary and center points 
         0X08  all points 
         0X10  basic properties Response[/* array with geofences data */
        {
        "n":<text>,/* geofence name*/
        "d":<text>,/* description */
        "id":<long>,/* zone id inside resource/account zone array  */
        "rid":<long>,/* resource/account id */
        "t":<byte>,/* type: 1 - line, 2 - polygon, 3 - circle */
        "w":<uint>,/* line thickness or circle radius */
        "f":<uint>,/* geofence flags (see below) */
        "c":<uint>,/* color (ARGB) */
        "tc":<uint>,/* text color RGB */
        "ts":<uint>,/* font size */
        "min":<uint>,/* show on map from this zoom */
        "max":<uint>,/* show on map till this zoom */
        "i":<ushort>,/* check sum of image (CRC16) */
        "path":<text>,/* short path to default icon */
        "ar":<double>,  /* area */
        "pr":<double>,  /* perimeter */
        "libId":<long>,/* id of icon library , 0 - id for default icon library */
        "jp":<JSON>,     /* custom JSON */
        "b":{/* boundary */
        "min_x":<double>,/* minimal longitude */
        "min_y":<double>,/* minimal latitude */
        "max_x":<double>,/* maximal longitude */
        "max_y":<double>,/* maximal latitude */
        "cen_x":<double>,/* longitude of center  */
        "cen_y":<double>/* latitude of center */
        },
        "p":[/* array of geofence points */
        {
        "x":<double>,/* longitude */
        "y":<double>,/* latitude */
        "r":<uint>/* radius */
        },
        ...
        ],
        "ct":<uint>,    /* creation time */  
        "mt":<uint>     /* last modification time */
        },
        ...
        ]Geofence flags “f”:
         0x20 – show shape, 0x40 – do not simplify.
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/get_zone_data", **params)


    def bind_unit_trailer(self, resourceId, unitId, trailerId, time, mode):
        """
                Parameters
         Name  Description  resourceId  resource ID 
         unitId  unit ID
         trailerId  trailer ID 
         time  time (0 - current time) 
         mode  mode: 1 - binding, 0 - unbinding Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/bind_unit_trailer", **params)


    def get_notification_data(self, itemId, col):
        """
                Parameters
         Name  Description  itemId  resource ID 
         col  array of notifications IDs Response[
        {
        "id":<long>,/* notification ID */
        "n":<text>,/* name */
        "txt":<text>,/* text of notification */
        "ta":<uint>,/* activation time (UNIX format) */
        "td":<uint>,/* deactivation time (UNIX format) */
        "ma":<uint>,/* maximal alarms count (0 - unlimited) */
        "mmtd":<uint>,/* maximal time interval between messages (seconds) */
        "cdt":<uint>,/* timeout of alarm (seconds) */
        "mast":<uint>,/* minimal duration of alert state (seconds) */
        "mpst":<uint>,/* minimal duration of previous state (seconds) */
        "cp":<uint>,/* period of control relative to current time (seconds) */
        "fl":<uint>,/* notification flags (see below) */
        "tz":<uint>,/* timezone */
        "la":<text>,/* user language (two-lettered code) */
        "ac":<uint>,/* alarms count */
        "sch":{/* time limitation */
        "f1":<uint>,/* beginning of interval 1 (minutes from midnight) */
        "f2":<uint>,/* beginning of interval 2 (minutes from midnight) */
        "t1":<uint>,/* ending of interval 1 (minutes from midnight) */
        "t2":<uint>,/* ending of interval 2 (minutes from midnight) */
        "m":<uint>,/* days of month mask [1: 2^0, 31: 2^30] */
        "y":<uint>,/* months mask [Jan: 2^0, Dec: 2^11] */
        "w":<uint>/* days of week mask [Mon: 2^0, Sun: 2^6] */
        },
        "ctrl_sch":{/* maximal alarms count intervals shedule */
        "f1":<uint>,/* beginning of interval 1 (minutes from midnight) */
        "f2":<uint>,/* beginning of interval 2 (minutes from midnight) */
        "t1":<uint>,/* ending of interval 1 (minutes from midnight) */
        "t2":<uint>,/* ending of interval 2 (minutes from midnight) */
         "m":<uint>,/* days of month mask [1: 2^0, 31: 2^30] */
         "y":<uint>,/* months mask [Jan: 2^0, Dec: 2^11] */
         "w":<uint>/* days of week mask [Mon: 2^0, Sun: 2^6] */
        },
        "un":[<long>],/* array units/unit groups ID's */
        "act":[/* actions */
        {
        "t":<text>,/* action type (see below) */
        "p":{/* parameters */
        "blink": <text>,/* mini-map blinking when triggered */ 
        "color": <text>,/* online notification color */
        "url": <text>,/* url of sound */
        ...
        },
        ...
        }
        ],
        "trg":{/* control */
        "t":<text>,/* control type (see below) */
        "p":{/* parameters */
        <text>:<text>,/* parameter name: value */
        ...
        }
        },
        "ct":<uint>,        /* creation time */
        "mt":<uint>         /* last modification time */
        }
        ]Notification flags:
         Flag  Description  0x0  notification triggers for first message 
         0x1  notification triggers for every message 
         0x2  notification is disabled Action types
         Notify by e-mail, Notify by SMS, Display online notification in a popup window, Send mobile notification, Send a request, Send notification to Telegram, Register event for unit, Execute a command, Upload video, Change access to units, Set counter value, Store counter value as parameter, Register unit status, Modify unit groups, Send a report by e-mail, Create a round, Reset driver, Reset trailer.Notify by e-mail{
        "t":"email",/* action type */
        "p":{
        "email_to":<text>,/* e-mail address */
        "html":<text>,/* use HTML tags: 0 - no, 1 - yes  */
        "img_attach":<text>,/* attach image from notification: 1 - yes, 0 - no */
        "subj":<text>/* text of message */
        }
        }Notify by SMS{
        "t":"sms",/* action type */
        "p":{
        "phones":<text>/* list of phone numbers (semicolon-separated) */
        }
        }Display online notification in a popup window{
        "t":"message",/* action type */
        "p":{
        "color":<text>,/* notification color */
        "name":<text>,/* notification name */
        "url":<text>/* URL-address to notification sound */
        }
        }Send mobile notification{
        "t":"mobile_apps",/* action type */
        "p":{
        "apps":"{\"<text>\":[/* mobile app name */
        <uint>/* user id */
        ]}"
        }
        }Send a request{
        "t":"push_messages",/* action type */
        "p":{
        "url":<text>,/* server name (port may be defined), start it with "http(s)" */
        "get":<bool>/* request type: 1 - GET, 0 - POST */
        }
        }Send notification to Telegram{
        "t":"messenger_messages",/* action type */
        "p":{
        "chat_id":<text>,/* channel ID in Telegram */
        "token":<text>/* user token in Telegram */
        }
        }Register event for unit{
        "t":"event",/* action type */
        "p":{
        "flags":<text>/* register as: 0 - event, 1 - violation */
        }
        }Execute a command{
        "t":"exec_cmd",/* action type */
        "p":{
        "cmd_type":<text>,/* command type */
        "link":<text>,/* link type */
        "name":<text>,/* command name */
        "param":<text>/* parameters */
        }
        } You can see list of available command type here List of available commands
        Upload video{"t":"video_service", /* action type */
        "p":{ /* optional */
        "channel_mask":int, /* camera mask, by default from unit's properties "video_channel_mask" */
        "duration":long, /* video duration, by default - 60 sec */
        "base_url":text
         }
        }Change access to units{
        "t":"user_access",/* action type */
        "p":{
        "acl_bits":<text>,/* 1 - set bit, 0 - remove bit */
        "acl_mask":<text>,/* mask of bits which must be changed */
        "units":<text>,/* list of units IDs (comma-separated) */
        "users":<text>/* list of users IDs (comma-separated) */
        }
        }Set counter value{
        "t":"counter",/* action type */
        "p":{
        "engine_hours":<text>,/* engine hours counter value */
        "flags":<text>,/* counter flags (see below) */
        "mileage":<text>,/* mileage counter value */
        "traffic":<text>/* GPRS traffic counter value */
        }
        }Counter flags:
         1 - set mileage counter value 2 - set engine hours counter value 4 - set GPRS traffic counter value
        <h4 class="sectionedit18" id="stor
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/get_notification_data", **params)


    def update_tags_group(self, itemId, id, callMode, n, d, tgs):
        """
                Params
         Name  Description  itemId  resource ID 
         id  tags group ID (0 to create) 
         callMode  callmode: create, update, delete 
         Parameters required only for create and update:: 
         n  name 
         d  description 
         tgs  tags ID array Response
        On create and edit:[
        <long>,/* group ID */
        {
        "id":<long>,/* ID */
        "n":<text>,/* name  */
        "d":<text>,/* description */
        "tgs":[<uint>,...]      /* tags ID array */
        }
        ]On delete:[
        <long>,/* group ID */
        null
        ]
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/update_tags_group", **params)


    def bind_unit_driver(self, resourceId, unitId, driverId, time, mode):
        """
                Parameters
         Name  Description  resourceId  resource ID 
         unitId  unit ID
         driverId  driver ID 
         time  time (0 - current time) 
         mode  mode: 1 - bind, 0 - unbind Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/bind_unit_driver", **params)


    def update_drivers_group(self, itemId, id, callMode, n, d, drs, f):
        """
                Parameters
         Name  Description  itemId  resource ID 
         id  driver group ID 
         callMode  action: create, update, delete 
         Parameters required only for create and update: 
         n  name 
         d  description 
         drs  array of drivers IDs 
         f  flags: not used at the moment Response
        On create and edit:[
        <long>,/* group ID */
        {
        "id":<long>,/* group ID */
        "n":<text>,/* name */
        "d":<text>,/* description */
        "drs":[<uint>]/* array of drivers IDs */
        }
        ]On delete:[
        <long>,/* group ID */
        null
        ]
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/update_drivers_group", **params)


    def bind_unit_tag(self, resourceId, unitId, tagId, time, mode):
        """
                Parameters
         Name  Description  resourceId  resource ID 
         unitId  unit ID
         tagId  tag ID 
         time  time (0 - current time) 
         mode  mode: 1 - bind, 0 - unbind Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("resource/bind_unit_tag", **params)
