
class Report:
    def __init__(self, session):
        self.session = session

    def get_report_status(self, ):
        """
                Response:{"status":<code>} Status code  Description  1  In a queue
         2  Proceed 
         4  Done
         8  Canceled 
         16 Invalid  report \\no such report After successful result (“status”:“4” in response) execute request report/apply_report_result  without parameters:
        """
        params = locals()
        params.pop('self')
        return self.session.call("report_get_report_status", **params)


    def get_result_subrows(self, tableIndex, rowIndex):
        """
                 You can find an example of this request in the sample Reports.
         This command allows you to receive only a subrows up to the second level, if you want to get more nested rows - use request  report / select_result_rows .
        Parameters
         Name  Description  tableIndex  table index 
         rowIndex  row index Response[
        {
        "n":<uint>,/* row index (from 0) */
        "i1":<uint>,/* number of first message in specified interval */
        "i2":<uint>,/* number of last message in specified interval */
        "t1":<uint>,/* time of first message in specified interval */
        "t2":<uint>,/* time of last message in specified interval */
        "d":<int>,/* quantity of rows with next nesting level */
        "c":[/* cells array */
        <text>,/* text value of cell */
        {/* or object */
        "t":<text>,/* cell value */
        "y":<double>,/* latitude */
        "x":<double>/* longitude */
        }
        ]
        }
        ]If the specified row doesn't contain any nested rows, then the format of the response will be:{
        "error":0
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("report_get_result_subrows", **params)


    def get_result_rows(self, tableIndex, indexFrom, indexTo):
        """
                 Attention! Current command returns rows as array regardless their nesting level.
         You can find an example of this request in the sample Reports.
        Parameters
         Name  Description  tableIndex  index of report table 
         indexFrom  index of first requested row 
         indexTo  index of last requested row Response[
        {
        "n":<uint>,/* row index (from 0) */
        "i1":<uint>,/* number of first message in specified interval */
        "i2":<uint>,/* number of last message in specified interval */
        "t1":<uint>,/* time of first message in specified interval */
        "t2":<uint>,/* time of last message in specified interval */
        "d":<int>,/* quantity of rows with next nesting level */
        "c":[/* cells array */
        <text>,/* text value of cell */
        {/* or object */
        "t":<text>,/* cell value */
        "v":<double>,/* original cell value */
        "y":<double>,/* latitude */
        "x":<double>/* longitude */
        }
        ]
        }
        ]
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("report_get_result_rows", **params)


    def cleanup_result(self, ):
        """
                Response{
        "error":<int>/* error code (0 - if successful) */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("report_cleanup_result", **params)


    def get_report_tables(self, ):
        """
                Response[
        {
        "id":<uint>,/* table ID */
        "n":<text>,/* system table name */
        "l":<text>,/* default table name */
        "t":<text>,/* table type */
        "ct":<text>,/* type of template in which this table can be used */
        "pt":<text>,/* text parameters */
        "gt":<text>,/* advanced grouping settings */
        "col":[/* array of columns */
        {
        "n":<text>,/* system column name */
        "l":<text>,/* default column name */
        "sl":<text>,/* list of column headers (if it is a statistics table) */
        "t":<text>,/* column type */
        "f":<uint>/* column flags (see below) */
        }
        ]
        }
        ]Report template types are described in the chapter Get templates data.
        Column flags
         Flag  Description  0x01  show as table column 
         0x02  show as statistics column 
         0x04  show as global switcher 
         0x08  show as column with position data 
         0x10  show as chart axis Values for "pt"-param
         Value  Description  geozones  Geozones/units 
         unfinished_ival  Unfinished interval 
         duration  Duration 
         mileage  Mileage 
         base_eh_sensor  Engine hours sensor 
         engine_hours  Engine hours 
         speed  Speed 
         trips  Trips 
         stops  Stops 
         parkings  parkings 
         sensors  Sensors 
         sensor_name  Sensor mask 
         driver  Driver 
         trailer  Trailer 
         fillings  Fillings 
         thefts  Thefts 
         duration_format  Furation format 
         geozones_ex  Extended geozones/units 
         username  Username mask 
         route_points  Route points 
         event_mask  Events mask 
         rides  Rides, applicable for “Unit”-“Unfinished rides”, “Unit group”-“Rides” 
         fields_config  Fields type, applicable for “Custom fields” tables 
         units  Units, applicable for “Maneuvers” tables 
         interval  trace interval in minutes, applicable for “Unit” -“Sensor tracing” 
         group_zones_pass  “Consider group as a whole” option is available, applicable for “Unit group”-“Non-visited geofences” 
         routes  applicable for “Routes” tables 
         last_location  “Consider report interval” option is available, applicable for “Unit latest data” table 
         hide_total  “Total” checkbox is hidden for that table 
         groupitem  “Group itself” option is available, applicable for “Unit group” –> “Log” and “Custom Fields” tables 
         noschedule  No “Time limitation” option available, applicable for “Summary” and “Latest unit data” tables 
         hide_driver_split  “Retrieve intervals” checkbox is hidden in driver filter 
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("report_get_report_tables", **params)


    def get_result_chart(self, attachmentIndex, action, width, height, autoScaleY, pixelFrom, pixelTo, flags):
        """
                 Сurrent request can't be executed simultaneously with following requests:
         report/exec_report, report/export_result, report/get_result_map, messages/load_interval, render/create_messages_layer, unit/get_trips, resource/get_driver_bindings, resource/get_trailer_bindings, all requests from chapter Export and import , account/get_account_history. You can find an example of this request in the sample Reports.
        Parameters
         Name  Description  attachmentIndex  attachment index 
         action  action: 0 - set flags and render, 1 - zooming, 2 - auto scale of Y-axis 
         width  width 
         height  height 
         autoScaleY  auto scale of Y-axis: 0 - disable, 1 - enable 
         pixelFrom  zoom: from current pixel 
         pixelTo  zoom: to current pixel 
         flags  chart flags Chart flags:
         Flag  Description  0x01  put the header above the chart 
         0x02  put the header under the chart 
         0x04  do not show the header 
         0x40  set X-axis captions direction from up to down
         0x80  set X-axis captions direction from down to up 
         0x100  put the chart legend above the chart 
         0x200  put the chart legend under the chart 
         0x400  put the chart legend to the left from the chart 
         0x800  put the chart legend to the right from the chart 
         0x1000  always show the legend, even in case of one dataset Response
        Returns image in PNG format.
        """
        params = locals()
        params.pop('self')
        return self.session.call("report_get_result_chart", **params)


    def get_result_map(self, width, height):
        """
                 Current request can't be executed simultaneously with following requests:
         report/exec_report, report/export_result, report/get_result_chart, messages/load_interval, render/create_messages_layer, unit/get_trips, resource/get_driver_bindings, resource/get_trailer_bindings, all requests from chapter Export and import , account/get_account_history. You can find an example of this request in the sample Reports.
        Parameters
         Name  Description  width  width, max -1920 
         height  height, max -1080 Response
        Returns an image (png) of the map, on which tracks and markers are rendered.
        """
        params = locals()
        params.pop('self')
        return self.session.call("report_get_result_map", **params)


    def export_result(self, format, pageOrientation, pageSize, pageWidth, coding, delimiter, headings, compress, attachMap, extendBounds, hideMapBasis, outputFileName):
        """
                  Current request can't be executed simultaneously with following requests:
         report/exec_report, report/get_result_chart, report/get_result_map, messages/load_interval, render/create_messages_layer, unit/get_trips, resource/get_driver_bindings, resource/get_trailer_bindings, all requests from chapter Export and import , account/get_account_history.Parameters
         Name  Description  format  file format (see below) 
         Optional parameters:  on default 
         compress  compress report file: 0 - no, 1 - yes   1  
         pageOrientation  (pdf) page orientation : portrait, landscape   portrait  
         pageSize  (pdf) page format: a4, a3   a4  
         pageWidth  (pdf) page width: 0 - fixed, 1 - compact, 2 - no-wrap   0  
         coding  (csv) encoding: utf8, cp1251   utf8  
         delimiter  (csv) delimiter: semicolon   comma  
         headings  (csv) display headers: 0 - no, 1 - yes   0  
         attachMap  attach map (only for PDF and HTML): 0 - no,  1 - yes   0  
         extendBounds  extend map to include geozones (only for PDF and HTML): 0 - no,  1 - yes   0  
         hideMapBasis  hide map layer: 0 - no, 1 - yes   0  
         outputFileName  file name   Online_report   Clarification for extendBounds: - new logics implemented: on default the map is zoomed to fill tracks/markers/icons;
         when option enabled: map is also zoomed to fill geozones (they will be displayed on map);
         map won't be displayed at all if no zoom elements available (no tracks/markers/icons for default logics plus geozones for extendBounds enabled)File formats:
         1 - html; 2 - pdf; 4 - xls; 8 - xlsx; 16 - xml; 32 - csv.Response
        Returns a file of demanded format.
        """
        params = locals()
        params.pop('self')
        return self.session.call("report_export_result", **params)


    def get_report_data(self, itemId, col):
        """
                Parameters
         Name  Description  itemId  resource ID 
         col  array of templates IDs 
         flags  response flags  Flag HEX  Flag DEC  Description  0x0  0  full JSON (default) 
         0x1  1  base info and binded units/groups 
         0x2  2  base info and short tables info 
         0x4  4  base info and full tables info Response[
        {
        "id":<long>,/* template ID */
        "n":<text>,/* name */
        "ct":<text>,/* type (see below) */
        "p":<text>,/* parameters */
        "tbl":[/* tables */
        {
        "n":<text>,/* table type */
        "l":<text>,/* name */
        "c":<text>,/* list of columns */
        "cl":<text>,/* list of column labels */
        "s":<text>,/* list of columns (if it is statistics table) */
        "sl":<text>,/* list of column labels (if it is statistics table) */
        "p":<text>,/* table parameters */
        "sch":{/* time limitation */
        "f1":<uint>,/* beginning of interval 1 */
        "f2":<uint>,/* beginning of interval 2 */
        "t1":<uint>,/* ending of interval 1 */
        "t2":<uint>,/* ending of interval 2 */
        "m":<uint>,/* days of month mask  */
        "y":<uint>,/* months mask */
        "w":<uint>/* days of week mask */
        "fl":<uint>/* incomplete interval (0 - don't cut off , 1 - show and cut off, 2 - don't show in report, 3 - show and mark as incomplete) */
         
        },
        "f":<uint>/* table flags */
        }
        ]
        }
        ]Templates types:
         avl_unit; avl_unit_group; storage_user; avl_driver; avl_trailer; avl_resource; avl_retranslator; avl_route; avl_drivers_group; avl_trailers_group; avl_tag; avl_tags_group.Table flags are described in the chapter Execute report.
        To get types of tables which can be included into reports, use the request  get_report_tables.
        """
        params = locals()
        params.pop('self')
        return self.session.call("report_get_report_data", **params)


    def get_result_photo(self, attachmentIndex, border):
        """
                Parameters
         Name  Description  attachmentIndex  attachment index 
         border  max size of photo ( 0 - original size) Response
        Returns an image in PNG format.
        """
        params = locals()
        params.pop('self')
        return self.session.call("report_get_result_photo", **params)


    def hittest_chart(self, attachmentIndex, datasetIndex, valueX, valueY, flags):
        """
                Parameters
         Name  Description  attachmentIndex  chart's index 
         datasetIndex  dataset index (-1 - all datasets) 
         valueX  x-coordinate, pixels 
         valueY  y-coordinate, pixels 
         flags  flags Flags
         Flag HEX  Flag DEC  Description  0x1  get help to chart 
         0x2  get help to marker 
         0x4  use valueX as time Response{
        "x":<double>,/* X axis value */
        "textX":<text>,/* text value for X coordinate */
        "axisX":<text>,/* name of X axis */
        "y":[
            {
        "y":<int>,/* Y coordinate */
        "textY":<text>,/* coordinate is string */
        "axisY":<text>,/* axis Y */
        "name":<text>,/* name of chart */
        "color":<uint>/* color */
            },
            ...
        ]
        "msg":{/* message */
        ...
        }
        }Message formats are described in the chapter Data format: Messages.
        """
        params = locals()
        params.pop('self')
        return self.session.call("report_hittest_chart", **params)


    def get_result_video(self, attachmentIndex):
        """
                Parameters
         Name  Description  attachmentIndex  attachment index Response{
        "video_uri": <text>,/* link to video */
        "video_type": <text>/* type of video */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("report_get_result_video", **params)


    def render_json(self, attachmentIndex, width, useCrop, cropBegin, cropEnd):
        """
                Params
         Name  Description  attachmentIndex  attachment index 
         width  width 
         useCrop  crop the time interval: 1 - yes, 0 - no 
         cropBegin  start of inteval, UNIX time 
         cropEnd  end of interval, UNIX time Response{
            "datasets":{/* data */
                <text>:{/* chart's index */
                    "name":<text>,/* chart's name */
                    "color":<uint>,/* line color */
                    "y_axis":<uint>,/* use second y axis (for splitted charts with different measurements): 0 -no, 1 - yes */
                    "data": {
                        "x": [
                            <uint>,/* chart's trace (time) */
                            ...
                        ],
                        "y": [/* chart's trace (value) */
                            <int>,
                           ...
                        ]
                    },
                    "colors": [/* chart's color intervals */
         
                    [<uint>,/* interval start time */
                     <uint>],/* color */
                    ...
            ],
                },
                ...
            },
            "markers":[/* markers */
                {
                    "type":<uint>,/* type */
                    "x": [
                        <uint>,/* time */
                        ...
                    ]
                },
               ...
            ],
            "background_regions": [    /* backround intervals */
                {
                    "name":<text>,/* name */
                    "color":<uint>,/* color */
                    "priority":<uint>,/* priority */
                    "regions":[
                        [<uint>,/* interval start time */
                         <uint>/* interval end time */
                         ],
                        ...
                    ]
                },
                ...
            ]
        }Marker flags
         Flag HEX  Flag DEC  Description  0x4  4  event/violation 
         0x8  8  filling 
         0x10  16  image 
         0x20  32  parking 
         0x40  64  speeding 
         0x80  128  stop 
         0x100  256  theft 
         0x800  2048  video 
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("report_render_json", **params)
