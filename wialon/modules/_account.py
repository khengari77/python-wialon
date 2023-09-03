
class Account:
    def __init__(self, session):
        self.session session

    def update_min_days(self, itemId, minDays):
        """
                Parameters
         Name  Description  itemId  resource (account) ID 
         minDays  minimum days counter value, days Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("account/update_min_days", **params)


    def trash(self, callMode, guids):
        """
                Parameters
         Param  Description  callMode  action: list, restore 
         guids  item guids for restoring
        (actual for restore callmode)  Attention: deleted item cannot be restored earlier than 20 mins of being in trash bin.
        Response
        While listing trash bin items:{
            "code":<uint>,
            "items": [
                        {
                            "guid":<text>,      /* guid */
                            "name":<text>,      /* item name */
                            "tm":<uint>,        /* time if deletion */
                            "type":<text>       /* type (ex. "avl_resource") */
                        },
                        ...
            ]
        }After restore callmode:{
            "code":<uint>,
            "items": [
                        {
                            "name":<text>,        /* item name */
                            "result":<bool>,      /* result: 1 - success, 0 - failure */
                            "type":<text>         /* item type */
                        },
                        ...
            ]
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("account/trash", **params)


    def update_sub_plans(self, itemId, plans):
        """
                 Attention!
        Current user can assign only available for him subordinate plans. To assign a billing plan to an account, the current user must have the right to manage this account (see  Access flags: Resources). Besides, the current user must be a direct or indirect parent of the account.This command is available to execute if the account already has dealer rights (you may use account/update_dealer_rights command).
        Parameters
         Name  Description  itemId  resource (account) ID 
         plans  list of subplans Response{}/* empty object if execution successful, if not - error code */Error codes
         Error code  Possible reason   7    no dealer rights  
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("account/update_sub_plans", **params)


    def enable_account(self, itemId, enable):
        """
                Parameters
         Name  Description  itemId  resource (account) ID 
         enable  mode: 0 - disable, 1 - enable Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("account/enable_account", **params)


    def get_account_history(self, itemId, days, tz):
        """
                 Current request can't be executed simultaneously with following requests:
         report/exec_report, report/export_result, report/get_result_chart, report/get_result_map, messages/load_interval, render/create_messages_layer, unit/get_trips, resource/get_driver_bindings, resource/get_trailer_bindings, all requests from chapter Export and import.Parameters
         Name  Description  itemId  resource (account) ID
         days  time to request statistics (days) 
         tz  timezone Response
        Service list with type PERIODIC and cost table (or counter or days_count). 
        Please note the following services have the other names in JSON response. "days_counter"-> "cnt"
         "email_report"-> "erp"
         "email_notification"-> "enf"
        [
        [
        <uint>,/* action type: 1 - payment, 0 - write off */
        <text>,/* date */
        <text>,/* service */
        <text>,/* cost */
        <uint>,/* quantity */
        <text>/* information */
        ]
        ]
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("account/get_account_history", **params)


    def change_account(self, itemId, resourceId):
        """
                Parameters
         Param  Description  itemId  unit id 
         resourceId  account id  In order to migrate a unit into the child account this account creator user should have some rights:
        1. On his account:
         ACL name  ACL flag   Manage account  0x100000000 2. On migrated unit:
         ACL name  ACL flag   View item and its basic properties  0x000001 
         Manage access to this item   0x000004 
         Delete item   0x000008 
         Edit connectivity settings (device type, UID, phone, access password, messages filter)  0x100000 
         Delete messages   0x800000 Response
        If migration ended successfully then:{}If some errors occured:{
            "error":<uint>
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("account/change_account", **params)


    def get_billing_plans(self, ):
        """
                Response{
        "plan":{/* own billing plan */
                "parent": <text>,/* parent plan name */
                "name": <text>,/* billing plan name */
                "servicesModCounter": <uint>,/* services modification counter */
                "historyPeriod": <int>,/* period of time to store unit messages */
                "flags": <uint>,/* flags */
                "denyBalance": <double>,/* operatons block appears below this balance value */
                "minDaysCounter": <int>,/* block occurs below this number of days */
                "blockBalance": <double>,/* block occurs below this balance value */
                "currencyFormat": <text>,/* currency format */ 
                "descr": <text>,/* billing plan description */
                "email": <text>,/* email */
                "hwTypes":{/* hardware object */
        "<hw_id>":/* hardware id */
             { 
                     "name": <text>/* hardware name */
             },
        ...
        },
                "personal":
                        {
                        "services": <object>/* services object (see below) */
                        },
                "combined":
                        {
                        "services": <object>/* services object (see below) */
                        }
        },
        "subPlans":[/* list of child billing plans */
        {
            "parent": <text>,/* parent plan name */
                "name": <text>,/* billing plan name */
                "servicesModCounter": <uint>,/* services modification counter */
                "historyPeriod": <int>,/* period of time to store unit messages */
                "flags": <uint>,/* flags */
                "denyBalance": <double>,/* operatons block appears below this balance value */
                "minDaysCounter": <int>,/* block occurs below this number of days */
                "blockBalance": <double>,/* block occurs below this balance value */
                "currencyFormat": <text>,/* currency format */ 
                "descr": <text>,/* billing plan description */
                "email": <text>,/* email */
                "hwTypes":{/* hardware object */
        "<hw_id>":/* hardware id */
             { 
                     "name": <text>/* hardware name */
             },
        ...
        },
                "personal":
                        {
                        "services": <object>/* services object (see below) */
                        },
                "combined":
                        {
                        "services": <object>/* services object (see below) */
                        }
        },
        ...
        ]
        }Services"services":{                          /* service object where keys are correct service names */
                        "<service_name>":{                  /* put correct service name instead of <service_name> */
                                        "type": <uint>,
                                        "maxUsage": <int>,
                                        "cost": <text>,
                                        "interval": <uint>,
                                        "descr": <text>,
                                        "flags": <uint>
                        },
                        ...
        }Please go here to see services list.
        """
        params = locals()
        params.pop('self')
        return self.session.call("account/get_billing_plans", **params)


    def update_flags(self, itemId, flags, blockBalance, denyBalance):
        """
                Parameters
         Name  Description  itemId  resource (account) ID 
         flags  account settings flags (see  Detailed information about account) 
         blockBalance  block balance value 
         denyBalance  deny balance value  You can get additional info about kinds of balances in Account flags section.
        Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("account/update_flags", **params)


    def get_account_data(self, itemId, type):
        """
                or the 2nd signature for some accounts:
        """
        params = locals()
        params.pop('self')
        return self.session.call("account/get_account_data", **params)


    def delete_account(self, itemId):
        """
                Parameters
         Name  Description  itemId  resource (account) ID Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("account/delete_account", **params)


    def update_dealer_rights(self, itemId, enable):
        """
                Parameters
         Name  Description  itemId  resource (account) ID 
         enable  enable/disable dealer rights Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("account/update_dealer_rights", **params)


    def create_account(self, itemId, plan):
        """
                Parameters
         Name  Description  itemId  resource ID 
         plan  billing plan Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("account/create_account", **params)


    def do_payment(self, itemId, balanceUpdate, daysUpdate, description):
        """
                Parameters
         Name  Description  itemId  resource (account) ID 
         balanceUpdate  sum of payment (can be negative) 
         daysUpdate  quantity of days added (can be negative) 
         description  description (required parameter) Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("account/do_payment", **params)


    def update_plan(self, itemId, plan):
        """
                 Attention!
        To assign a billing plan to an account, the current user must have the right to manage this account (see  Access flags: Resources). Besides, the current user must be a direct or indirect parent of the account.
        Parameters
         Name  Description  itemId  resource (account) ID 
         plan  billing plan name Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("account/update_plan", **params)


    def list_change_accounts(self, units):
        """
                Параметры
         Name  Description  units  unit id array Response
        Got results[
            {
        "id":<long>,/* account id */
        "name":<text>/* account name */
            },
            .../* other valid accounts (if any) */
        ]No results[]
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("account/list_change_accounts", **params)


    def update_billing_service(self, itemId, name, type, intervalType, costTable):
        """
                Parameters
         Name  Description  itemId  resource (account) ID
         name  service name (complete list of services is given in the chapter Detailed information about account) 
         type  service type (see below) 
         intervalType  interval type (see below) 
         costTable  cost table Service types:
         1 – on demand (for example, SMS). IntervalType defines frequency of service usage counter reset.  2 – periodic services, payments for them must be performed in specified time interval. Interval types:
         0 – never; 1 – hourly; 2 – daily; 3 – weekly; 4 – monthly. Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("account/update_billing_service", **params)


    def update_history_period(self, itemId, historyPeriod):
        """
                Parameters
         Name  Description  itemId  resource (account) ID 
         historyPeriod  history period value, days Response{}/* empty object if execution successful, if not - error code */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("account/update_history_period", **params)
