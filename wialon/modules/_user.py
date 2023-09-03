
class User:
    def __init__(self, session):
        self.session session

    def update_auth_params(self, userId, type, phone):
        """
                Parameters
         Name  Description  userId  user ID 
         type  type ( 0 - none, 1 - email, 2 - SMS ) 
         phone  phone number (if type:2) Response{
            "type":<uint>,
            "phone":<text>
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("user/update_auth_params", **params)


    def verify_auth(self, userId, type, destination):
        """
                Parameters
         Name  Description  userId  user ID 
         type  address type (0 - sms, 1 - email) 
         destination  email or phone number Response{
        "code":<text>/* code */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("user/verify_auth", **params)


    def send_sms(self, phoneNumber, smsText):
        """
                Parameters
         Name  Description  phoneNumber  phone number 
         smsText  message text Response{}/* empty object if execution successful, if not - error code */Errors
         Code  Value  6  error sending SMS 
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("user/send_sms", **params)


    def update_item_access(self, userId, itemId, accessMask):
        """
                Parameters
         Name  Description  userId  user ID 
         itemId  item ID 
         accessMask  access mask (see  Access flags: General and  Access flags: Units and unit groups)Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("user/update_item_access", **params)


    def get_items_access(self, userId, directAccess, itemSuperclass, flags):
        """
                Parameters
         Name  Description  userId  user ID 
         directAccess  return only items to which the user has direct access rights 
         itemSuperclass  item type (the list of all types see in the chapter Search items by property) 
         flags  flags (return: 0x1 - combined access level, 0x2 - direct access level), optional, default value = 1 Response{
        <text>: /* item ID */
        {
        "cacl":<long>,/* combined access level */
        "dacl":<long>/* direct access level */
        }
        }
         
        /* "directAccess":1 there is received only combined access level */
         
        {
        "<text>":<long> /* "element ID":"calc" */
         
        }Access rights are described in chapter Items access rights check.
        """
        params = locals()
        params.pop('self')
        return self.session.call("user/get_items_access", **params)


    def get_locale(self, userId):
        """
                Parameters
         Param  Description  userId  user id Response
        If settings never changed via user/update_locale then blank object returned:{}If settings changed then response will be the following:{
            "fd":<text>,   /* date and fime format */
            "wd":<uint>    /* the 1st week day: 1 - Monday, 7 - Sunday */
        } More info about date and time format may be get from here.
        """
        params = locals()
        params.pop('self')
        return self.session.call("user/get_locale", **params)


    def update_user_flags(self, userId, flags, flagsMask):
        """
                Parameters
         Name  Description  userId  user ID 
         flags  settings flags 
         flagsMask  mask that determines which bits will be changed User settings flags:
          Value   Description   0x01   User disabled 
          0x02   Can't change password 
          0x04   Can create items 
          0x10   Can't change settings 
          0x20   Can send SMS 
        The example of using mask and user settings flags:
        We need to allow user changing password (0x02), to forbid changing settings(0x10), and to leave all the other flags without changes. In such case mask will be 0x2 + 0x10 = 0x12. Flag 0x02 must be removed, and flag 0x10 must be set, therefore parameter flag will be 0x10.
        Response{
        "fl":<uint>/* flags */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("user/update_user_flags", **params)


    def update_password(self, userId, oldPassword, newPassword):
        """
                Parameters
         Name  Description  userId  user ID 
         oldPassword  old password 
         newPassword  new password Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("user/update_password", **params)


    def get_dst_time(self, timeFrom, timeTo, tz):
        """
                Params
         Name  Description  timeFrom  time from, UNIX time 
         timeTo  time to, UNIX time 
         tz   time zone (optional) Response{
        <text>: 1, /* DST start, UNIX time */ 
        <text>: 0, .../* DST end, UNIX time */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("user/get_dst_time", **params)


    def update_hosts_mask(self, userId, hostsMask):
        """
                Parameters
         Name  Description  userId  user ID 
         hostsMask  host mask Response{
        "hm":<text>/* host mask */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("user/update_hosts_mask", **params)
