
class Messages:
    def __init__(self, session):
        self.session = session

    def get_packed_messages(self, itemId, timeFrom, timeTo, filtrationFlags):
        """
                 Сurrent request can't be executed simultaneously with following requests:
         report/exec_report, report/export_result, report/get_result_chart, report/get_result_map, render/create_messages_layer, unit/get_trips, resource/get_driver_bindings, resource/get_trailer_bindings, all requests from chapter Export and import, account/get_account_history.Parameters
         Name  Description  itemId  unit or resource ID (depends on type of message you want to get)
         timeFrom  interval beginning 
         timeTo  interval end 
         filtrationFlags  optional, 0 or 1, by default = 1 - message fillatraion by min satellites from unit's settings . Response{ "messages":"ok_kGkwyF????????????????" }  messages - points (coordinates) encoded by google polyline
        If difference between timeTo and timeFrom is more than 86400 sec, error 4 will be returned
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("messages_get_packed_messages", **params)


    def load_last(self, itemId, lastTime, lastCount, flags, flagsMask, loadCount):
        """
                Parameters
         Name  Parameters  itemId  unit or resource ID (depends on type of message you want to get) 
         lastTime  time for which messages are requested 
         lastCount  how many messages to load 
         flags  message flags: to load messages with defined flags only (see  Data format: Messages) 
         flagsMask  mask (see Load messages for interval) 
         loadCount  how many messages to return Response{
        "count":<uint>,/* messages count */
        "messages":[/* array of messages */
        {
        ...
        }
        ]
        }You can find message formats in the chapter  Data format: Messages.
        """
        params = locals()
        params.pop('self')
        return self.session.call("messages_load_last", **params)


    def get_messages(self, indexFrom, indexTo, timeFrom, timeTo, filter, flags, flagsMask, loadCount):
        """
                 You can find an example of this request in the sample Messages.
        Parameters
         Name  Description  indexFrom  index of the first message requested 
         indexTo  index of the last message requested 
         timeFrom  interval beginning 
         timeTo  interval end 
         filter  filter, search in “pos” and “p”
         flags  flags for loading messages (see below) 
         flagsMask  mask (see below) 
         loadCount  how many messages to return (0xffffffff - all found)  Method logic extended: you can use both old indexFrom/indexTo logic and new ones:- timeFrom/timeTo (we define message time to start and end);- timeFrom/loadCount (we define message time to start, it will display loadCount number of last messages);- timeTo/loadCount (we define message time to end , it will display loadCount number of last messages).“Filter” option can be used for any logic. Search is available in “pos” and “p” params. Even if there is no params under search in messages then all messages will be shown with minimal info like (“t”,“f”,“tp”,“i”,“o”).
        Response example (no filtering):[
            {
        "t": 1426233861,
        "f": 7,
        "tp": "ud",
        "pos": {
        "y": 53.84541,
        "x": 27.4470783333,
        "z": 0,
        "s": 25,
        "c": 285,
        "sc": 255
        },
        "i": 0,
        "o": 0,
        "p": {
        "adc1": 0,
        "pre2": 123,
        "param": 24,
        "param5": 43
        }
            }
        ]Filter example:"filter":"pos.x,p.pre*,p.param?"Filtered response:[
               {
        "t": 1426233861,
        "f": 7,
        "tp": "ud",
        "pos": {
        "x": 27.4470783333
        },
        "i": 0,
        "o": 0,
        "p": {
        "pre2": 123,
        "param5": 43
        }
        }
        ]After filtering we see pos.x value, values for parameters in pos-object with leading “pre” names, values for parameters in pos-object with leading “param” and one-more-following-symbol names (for example 'param1' but 'param' is invalid for search).
        Number of defined parameters using comma as delimiter is unlimited. * – wildcard for 0 or more symbols, ? - wildcard for exactly one symbol.
        Response[/* message array */
        { ... },/* message */
        { ... }/* message */
        ]You can find message formats in the chapter  Data format: Messages.
        """
        params = locals()
        params.pop('self')
        return self.session.call("messages_get_messages", **params)


    def delete_message(self, msgIndex):
        """
                 You can find an example of this request in the sample Messages.
        Parameters
         Name  Description  msgIndex  message index Response{}/* empty object if execution successful, if not - error code */Errors
         Code  Description  4  There is no such message or this message is the last one and thus can't be deleted 
         6  Error deleting message 
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("messages_delete_message", **params)


    def unload(self, ):
        """
                 You can find an example of this request in the sample Messages.
        Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("messages_unload", **params)


    def load_interval(self, itemId, timeFrom, timeTo, flags, flagsMask, loadCount):
        """
                 Сurrent request can't be executed simultaneously with following requests:
         report/exec_report, report/export_result, report/get_result_chart, report/get_result_map, render/create_messages_layer, unit/get_trips, resource/get_driver_bindings, resource/get_trailer_bindings, all requests from chapter Export and import, account/get_account_history. You can find an example of this request in the sample Messages.
        Parameters
         Name  Description  itemId  unit or resource ID (depends on type of message you want to get)
         timeFrom  interval beginning 
         timeTo  interval end 
         flags  flags for loading messages (see below) 
         flagsMask  mask (see below) 
         loadCount  how many messages to return (0xffffffff - all found) Examples of mask and flags usage:
          Mask    Flag   Result   0xFF00    0x0000   all messages with data 
          0xFF10    0x0010   messages with data, which contain alarm bit 
          0xFFF0    0x0010   messages with data, which contain alarm bit(0x10), but dont't contain info about driver code(0x20) 
          0xFFF2    0x0022   messages with data, which contain info about driver code(0x20) and in which input data information is available(0x02), but these messages don't contain alarm bit(0x10) 
          0xFF01    0x0601   events, which are violations 
           0x2000   video usage messages Response{
        "count":<uint>,/* messages count */
        "messages":[/* array of messages */
        {
        ...
        }
        ]
        }You can find message formats in the chapter  Data format: Messages.
        """
        params = locals()
        params.pop('self')
        return self.session.call("messages_load_interval", **params)


    def get_message_file(self, itemId, fileId):
        """
                Parameters
         Name  Description  itemId  unit ID or resource ID*
         fileId  image file ID *To get an image from unit messages, you need to submit the unit ID as itemId. To get an image from a resource, you must submit the resource ID as itemId.
         fileID param you can get from message JSON
        ResponseReturns an image.
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("messages_get_message_file", **params)
