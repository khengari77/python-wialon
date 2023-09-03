
class Order:
    def __init__(self, session):
        self.session session

    def list_attachments(self, itemId, id):
        """
                Parameters
         Name  Description  itemId  resource id 
         id  order id within resource Response[
        {
            "n":<text>,/* file name */
            "s":<uint>,/* size, bytes */
            "ct":<uint>,/* creation time */
            "mt":<uint>/* last modification time */
        },
        ...
        ]
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("order/list_attachments", **params)


    def get_attachment(self, itemId, id, path):
        """
                Parameters
         Name  Description   itemId   resource id 
          id    order id within resource 
           path   file name Response
        In case of success the server will return requested file.If failed:Invalid input{"error":3}
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("order/get_attachment", **params)


    def route_update(self, itemId, orders, routeId, callMode):
        """
                Parameters
         Param  Description  itemId  resource ID 
         orders  array JSON orders and “callmode” for every each order 
         routeId  route ID 
         callMode  action: create, update, delete  Result is similar to batch of order/update.
        Response{"orders":[{
        "id":<uint>,/* order id */ 
        "f":<uint>,/* order flags */
        "u":<uint>,/* unit id */
        "uid":<uint>,/* order uid */
        "callMode":<text>
            },
            ...
        ]}
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("order/route_update", **params)


    def attach(self, itemId, id, eventHash):
        """
                Parameters
         Name  Description   itemId   resource id 
          id    order id within resource 
          eventHash   event name which will be generated
        after processing the data  To attach file to order send POST-request. Example is below:Request URL:https://hst-api.wialon.com/wialon/ajax.html?
        """
        params = locals()
        params.pop('self')
        return self.session.call("order/attach", **params)


    def detach(self, itemId, id, path):
        """
                Parameters
          Name    Description    itemId   resource id 
          id    order id within resource 
           path   file name  To get list of files attached to order use order/list_attachments.
        Response{ }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("order/detach", **params)
