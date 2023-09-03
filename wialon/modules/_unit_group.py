
class Unit_group:
    def __init__(self, session):
        self.session session

    def update_units(self, itemId, units):
        """
                Parameters
         Name  Description  itemId  unit group ID 
         units  array of units IDs Note: The units parameter must contain IDs of both objects already added and that should be added. In the case of deletion, you must list the IDs of the objects that should remain in the group.
        Response{
        "u":[<long>]/* array of units IDs */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("unit_group/update_units", **params)
