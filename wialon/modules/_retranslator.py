
class Retranslator:
    def __init__(self, session):
        self.session session

    def get_stats(self, itemId):
        """
                Parameters
         Name  Description  itemId  retranslator ID Response
        Parameter “au” - the number of objects, which have been added/deleted to/from retranslator directly.{
        "au": <long>, /* the number of objects in the retranslator */
        "ru": <long>, /* the number of objects in the queue for history retranslation */
        "hf": <long>, /* time 'from' */
        "ht": <long>  /* time 'to' */
        "hc": <uint>, /* current retranlation messages time */
        "hms": <uint>, /* current queue of historical messages */
        "hp": <uint>, /* progress percent */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("retranslator/get_stats", **params)


    def update_operating(self, itemId, operate, stopTime, timeFrom, timeTo, callMode):
        """
                Parameters
         Name  Description  itemId  retranslator ID 
         operate  true - start, false - stop 
         stopTime  time, when retranslation will be stopped (optional parameter) 
         timeFrom  interval beginning of history retranslation, UNIX - time (only for history) 
         timeTo  interval end of history retranslation, UNIX - time (only for history) 
         callMode  switch - start/stop retranslator, history - start/stop history retranslation Response{
        "rtro":<int>/* 0 - stopped, 1 - started */
                "rtrst":<uint>  /* time, when retranslation will be stopped */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("retranslator/update_operating", **params)
