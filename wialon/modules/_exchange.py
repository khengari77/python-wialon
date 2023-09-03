
class Exchange:
    def __init__(self, session):
        self.session session

    def import_json(self, eventHash):
        """
                 Current request can't be executed simultaneously with any request from this chapter and following requests:
         report/exec_report, report/export_result, report/get_result_chart, report/get_result_map, messages/load_interval, render/create_messages_layer, unit/get_trips, resource/get_driver_bindings, resource/get_trailer_bindings, account/get_account_history.Parameters
         Name  Description  eventHash  event name, which will be generated after reading data (optional parameter) To load a WLP file, use a POST request with multiple contents (multipart/form-data).
        For example:Request URL: https://hst-api.wialon.com/wialon/ajax.html?
        """
        params = locals()
        params.pop('self')
        return self.session.call("exchange/import_json", **params)


    def import_zones_read(self, eventHash):
        """
                 Current request can't be executed simultaneously with any request from this chapter and following requests:
         report/exec_report, report/export_result, report/get_result_chart, report/get_result_map, messages/load_interval, render/create_messages_layer, unit/get_trips, resource/get_driver_bindings, resource/get_trailer_bindings, account/get_account_history.Parameters
         Name  Description  eventHash  event name, which will be generated after reading geofences (optional parameter) To upload a file with geofences, use a POST request with multiple contents (multipart/form-data).
        For example:Request URL: https://hst-api.wialon.com/wialon/ajax.html?
        """
        params = locals()
        params.pop('self')
        return self.session.call("exchange/import_zones_read", **params)


    def import_messages(self, itemId, eventHash):
        """
                 Current request can't be executed simultaneously with any request from this chapter and following requests:
         report/exec_report, report/export_result, report/get_result_chart, report/get_result_map, messages/load_interval, render/create_messages_layer, unit/get_trips, resource/get_driver_bindings, resource/get_trailer_bindings, account/get_account_history.Parameters
         Name  Description  itemId  item ID 
         eventHash  event name, which will be generated after messages will be imported (optional parameter) To load a file, use a POST request with multiple contents (multipart/form-data).
        For example:Request URL: https://hst-api.wialon.com/wialon/ajax.html?
        """
        params = locals()
        params.pop('self')
        return self.session.call("exchange/import_messages", **params)


    def export_messages(self, layerName, format, itemId, timeFrom, timeTo, compress):
        """
                 Current request can't be executed simultaneously with any request from this chapter and following requests:
         report/exec_report, report/export_result, report/get_result_chart, report/get_result_map, messages/load_interval, render/create_messages_layer, unit/get_trips, resource/get_driver_bindings, resource/get_trailer_bindings, account/get_account_history.Parameters
         Name  Description  layerName  message layer name (optional), to export from layer
         itemId  unit ID (optional),to export directly for time (not from layer)
         format  file format: txt, kml, plt, wln, wlb 
         timeFrom  time from(optional), to export directly 
         timeTo  time to(optional), to export directly 
         compress  compress file: 0 - no, 1 - yes Response
        Returns a file of specified format.
        """
        params = locals()
        params.pop('self')
        return self.session.call("exchange/export_messages", **params)


    def import_pois_read(self, eventHash):
        """
                 Current request can't be executed simultaneously with any request from this chapter and following requests:
         report/exec_report, report/export_result, report/get_result_chart, report/get_result_map, messages/load_interval, render/create_messages_layer, unit/get_trips, resource/get_driver_bindings, resource/get_trailer_bindings, account/get_account_history.Parameters
         Name  Description  eventHash  event name, which will be generated after reading POIs (optional parameter) To upload a file containing POIs, use a POST request with multiple contents (multipart/form-data).
        For example:Request URL: https://hst-api.wialon.com/wialon/ajax.html?
        """
        params = locals()
        params.pop('self')
        return self.session.call("exchange/import_pois_read", **params)
