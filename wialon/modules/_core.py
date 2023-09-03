
class Core:
    def __init__(self, session):
        self.session = session

    def search_item(self, id, flags):
        """
                 You can find an example of this request in the sample Item search.
        Parameters
         Name  Description  id  item ID 
         flags  data flags for the response (the value of this parameter depends on item type; data formats of all item types and their flags are described in the chapter Data format)Response{
        "item":{/* found item */
        ...
        },
        "flags":<uint>/* applied data flags */
        }The format of “item” depends on item type. All formats are described in the chapter Data format.
        """
        params = locals()
        params.pop('self')
        return self.session.call("core_search_item", **params)


    def create_resource(self, creatorId, name, dataFlags, skipCreatorCheck):
        """
                Parameters
         Name  Description  creatorId  ID of a user who will be assigned a creator for a new resource 
         name  name of a new resource (at least 4 characters) 
         dataFlags  data flags for the response (see Data format: Resources)
         skipCreatorCheck  special flag (see below), 1 - enable Clarification for skipCreatorCheck: if non-account user created items then it is impossible to create account for such user later; in order to create resource for such user please use skipCreatorCheck=1. The flag is used for that case only. Such limitation exists to protect one's hierarchy.
        Response{
        "item":{/* resource created */
        ...
        },
        "flags":<uint>/* applied data flags */
        }You can find the format of “item” in the chapter Data format: Resources.
        """
        params = locals()
        params.pop('self')
        return self.session.call("core_create_resource", **params)


    def use_auth_hash(self, authHash, operateAs, checkService):
        """
                Parameters
         Name  Description  authHash  authorization hash that you can get using core/create_auth_hash request 
         operateAs  subuser name to log in 
         checkService  you can check on  service Response
        Response format is be the same as in the command login.
        """
        params = locals()
        params.pop('self')
        return self.session.call("core_use_auth_hash", **params)


    def create_route(self, creatorId, name, dataFlags):
        """
                Parameters
         Name  Description  creatorId  ID of a user who will be assigned a creator for a new route 
         name  new route name (at least 4 characters) 
         dataFlags  data flags for the response (see Data format: Routes)Response{
        "item":{/* route created */
        ...
        },
        "flags":<uint>/* applied data flags */
        }You can find the format of “item” in the chapter Data format: Routes.
        """
        params = locals()
        params.pop('self')
        return self.session.call("core_create_route", **params)


    def create_unit_group(self, creatorId, name, dataFlags):
        """
                Parameters
         Name  Description  creatorId  ID of a user who will be assigned a creator for a new unit group 
         name  new unit group name (at least 4 characters) 
         dataFlags  data flags for the response (see Data format: Unit group)Response{
        "item":{/* unit group created */
        ...
        },
        "flags":<uint>/* applied data flags */
        }You can find the format of “item” in the chapter Data format: Unit group.
        """
        params = locals()
        params.pop('self')
        return self.session.call("core_create_unit_group", **params)


    def get_account_data(self, type):
        """
                Parameters
         Name  Description  type  type of result JSON Types of response:
         1 – minimal information, usually required to estimate the state of logged user; 2 – detailed information with combined, personal and billing plan settings.Response
        Minimal information:{
        "plan":<text>,/* billing plan name */
        "enabled":<int>,/* state: 0 - blocked, 1 - active */
        "​created":<​uint>,​/​* creation time (unix time) */
        "flags":<uint>,/* billing plan flags */
        "balance":<text>,/* balance (with currency) */
        "daysCounter":<int>,/* days counter */
        "services":{/* services list */
        <text>:{/* name */
        "type":<int>,/* type: 1 - on demand; 2 - periodic */
        "usage":<uint>,/* quantity of active resources of current service */
        "maxUsage":<int>/* maximal quantity of resources */
        },
        ...
        },
        "dealerRights":<int>,/* allow using dealer rights for current billing plan: 0 - no, 1 - yes */
        "subPlans":[<text>],/* array of subplans */
        "​switchTime":​<uint>​/​* time of switch "​enabled" param​ */ 
        }Detailed information:{
        "plan":<text>,/* billing plan name */
        "enabled":<int>,/* state: 0 - blocked, 1 - active */
        "flags":<uint>,/* flags - duplicates the same flags from billing plan settings (see the "plan" field below) */
        "balance":<text>,/* balance (with currency) */
        "daysCounter":<int>,/* days counter */
        "settings":{
        "balance":<double>,/* balance */
        "plan":{/* billing plan settings */
        "flags":<uint>,/* billing plan flags */
        "blockBalance":<int>,/* block balance */
        "denyBalance":<int>,/* deny balance */
        "minDaysCounter":<int>,/* minimum days counter */
        "historyPeriod":<int>,/* history period to store messages, in days (if 0 - unlimited) */
        "services":{/* services list */
        <text>:{/* name */
        "type":<int>,/* type: 1 - on demand; 2 - periodic */
        "usage":<uint>,/* count of used items of a type */
        "maxUsage":<int>/* maximum allowed items of a type */
        "cost":<text>,/* cost table */
        "interval":<int>/* reset interval: 0 - none, 1 - hourly, 2 - daily, 3 - weekly, 4 - monthly*/
        },
        ...
        }
        },
        "personal":{/* personal (account) settings */
        .../* has the same format as billing plan settings */
        },
        "combined":{/* combined settings (overlapping billing plan and account settings) */
        .../* has the same format as billing plan settings */
        }
        },
        "siteAccess":{
        "<service_name>":"<dns_name>",/* where key is service name and value is dns-name */
        ...
        },
        "dealerRights":<int>,/* allow using dealer rights for current billing plan: 0 - no, 1 - yes */
        "subPlans":[<text>]/* array of subplans */
        }You can find available values of billing plan and account flags, as well as list of services in the chapter Detailed information about account.
        """
        params = locals()
        params.pop('self')
        return self.session.call("core_get_account_data", **params)


    def get_hw_cmds(self, deviceTypeId, unitId, template, lang):
        """
                Parameters
         Name  Description  Comments  deviceTypeId  hardware type ID  
         unitId  unit ID  
         template  flag, respond with com-
        mand template data:
        1 - on  optional 
         lang  flag, translates “title”,“label” values  optional You can set either one of the parameters or both. The procedure begins with the search by hardware type ID, and if it fails, the search by unit ID proceeds. If you want to omit one of the parameters, set it to 0.
        Response
        Returns the list of available commands (if template:0 or missing):{
        <text>:[/* link type: gsm, tcp, udp, vrt */
        <text>,/* command type */
        ...
        ],
        ...
        }Returns command templates (example json is below; in real templates it might be custom set of fields below):{
          "<cmd_template_name>": {   /* name */
            "icon": <text>,          /* icon */
            "props": [               /* properties */
              {
                "label":<text>,      /* property label */
                "type":<text>,       /* type */
                "validate":<text>,   /* validation rule */
                "value": [           /* key-value array */
                  {
                    "n":<text>,      /* key */
                    "v":<text>       /* value */
                  },
                  ...
                ],
                "default":<text>,    /* some dafault value (for example port of IP-address ) */
                "title":<text>,      /* title */
                "maxlength":<uint>   /* max length */
              },
              ...      
            ]
          },
          ...  
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("core_get_hw_cmds", **params)


    def check_accessors(self, items, flags):
        """
                Parameters
         Name  Description  items  unit id array 
         flags  flag for adding “dact” param in response:
        1 - add param,
        0 - don't add Response{
           "<unit_id>": {/* unit id */
        "<acc_id>": {/* user id */
        "acl": <uint>,/* inherited unit access rights, they are put as mask on direct access rights,
           if inherited access rights prohibit -- result access right prohibit */
        "dacl": <uint>/* if flags:1 set; direct unit access rights  (set by unit owner) */
        },
        .../* other user ids (if any) */
            },
            .../* other unit ids (if requested) */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("core_check_accessors", **params)


    def check_items_billing(self, items, accessFlags, serviceName):
        """
                While processing a request, available services and access rights on items are checked. For example, a user has a right to create POIs in some resource, however, according to service's cost table, the limit of allowed POIs has been reached, so this resource will not be present in the result array.
        Parameters
         Name  Description  items  array of item IDs 
         accessFlags  access flags (described below) 
         serviceName  service name (see Detailed information about account)Response[
        <long>/* array of items that the user can access */
        ]Access flags
        General
         Flag  Description  0x0001  View item and its basic properties 
         0x0002  View detailed item properties 
         0x0004  Manage access to this item 
         0x0008  Delete item 
         0x0010  Rename item 
         0x0020  View custom fields 
         0x0040  Manage custom fields 
         0x0080  Edit not mentioned properties 
         0x0100  Change icon 
         0x0200  Query reports or messages 
         0x0400  Edit ACL propagated items 
         0x0800  Manage item log 
         0x1000  View administrative fields 
         0x2000  Edit administrative fields 
         0x4000  View attached files 
         0x8000  Edit attached files Units and unit groups
         Flag  Description  0x0000100000  Edit connectivity settings (device type, UID, phone, access password, messages filter) 
         0x0000200000  Create, edit, and delete sensors 
         0x0000400000  Edit counters 
         0x0000800000  Delete messages 
         0x0001000000  Execute commands 
         0x0002000000  Register events 
         0x0004000000  View connectivity settings (device type, UID, phone, access password, messages filter) 
         0x0010000000  View service intervals 
         0x0020000000  Create, edit, and delete service intervals 
         0x0040000000  Import messages 
         0x0080000000  Export messages 
         0x0400000000  View commands 
         0x0800000000  Create, edit, and delete commands 
         0x4000000000  Edit trip detector and fuel consumption 
         0x8000000000  Use unit in jobs, notifications, routes, retranslators Users
         Flag  Description  0x100000  Manage user`s access rights 
         0x200000  Act as given user (create items, login, etc.) 
         0x400000  Change flags for given user 
         0x800000  View push messages for mobile app
         0x1000000  Edit push messages Retranslators
         Flag  Description  0x100000  Edit retranslator properties including start/stop 
         0x200000  Add or remove units from retranslator, change their UIDs Resources (Accounts)
         Flag  Description  0x0000000100000  View notifications 
         0x0000000200000  Create, edit, and delete notifications 
         0x0000000400000  View POIs 
         0x0000000800000  Create, edit, and delete POIs 
         0x0000001000000  View geofences 
         0x0000002000000  Create, edit, and delete geofences 
         0x0000004000000  View jobs 
         0x0000008000000  Create, edit, and delete jobs 
         0x0000010000000  View report templates 
         0x0000020000000  Create, edit, and delete report templates 
         0x0000040000000  View drivers and driver groups 
         0x0000080000000  Create, edit, and delete drivers and driver groups
         0x0000100000000  Manage account 
         0x0000200000000  View orders 
         0x0000400000000  Create, edit, and delete orders 
         0x0000800000000  View passengers and passengers groups 
         0x0001000000000  Create, edit, and delete passengers and passengers groups
         0x0100000000000  View trailers and trailer groups 
         0x0200000000000  Create, edit, and delete trailers and trailer groups Routes
         Flag  Description  0x0000000100000  Edit route properties Other
         Flag  Description  0xfffffffffffffff  Sets all possible access flags to an item 
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("core_check_items_billing", **params)


    def logout(self, ):
        """
                 You can find an example of this request in the sample Login/logout.
        Response{
        "error":<int>/* error code */
        }Errors
          Code   Value   0   exit successful 
          1   server connection error 
          4   user not authorized 
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("core_logout", **params)


    def create_unit(self, creatorId, name, hwTypeId, dataFlags):
        """
                 You can find an example of this request in the sample Creating, editing and deleting items.
        Parameters
         Name  Description  creatorId  ID of a user who will be assigned a creator for a new unit 
         name  new unit name (at least 4 characters) 
         hwTypeId  device (hardware) ID 
         dataFlags  data flags for the response (see Data format: Units)Response{
        "item":{/* unit created */
        ...
        },
        "flags":<uint>/* applied data flags */
        }You can find the format of “item” in the chapter Data format: Units.
        """
        params = locals()
        params.pop('self')
        return self.session.call("core_create_unit", **params)


    def reset_password_perform(self, user, code):
        """
                Parameters
        After executing reset_password_request, an e-mail with link will be sent to the user. The link will lead to the URL indicated in the request and will contain two more parameters needed to finalize password reset:
         Name  Description  user  user name 
         code  code generated by reset_password_request and sent to the user by e-mail Response{
        "newPassword":<text>/* new password */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("core_reset_password_perform", **params)


    def reset_password_request(self, user, url, email):
        """
                Request execution is 1 time per 1 minute, in other case returns “error”:11 - reason: “REQUEST_TOO_OFTEN”
        Parameters
         Name  Description  user  user name 
         url  URL contained in the letter that will be sent to the user at password reset request: <url>?user=<login>&passcode=<passcode> (the value of passcode see in Password reset)
         email  user e-mail Response{
        "error":0/* successful request */
        }Other types of errors may occur. See the full list in the chapter Errors.
        """
        params = locals()
        params.pop('self')
        return self.session.call("core_reset_password_request", **params)


    def create_user(self, creatorId, name, password, dataFlags):
        """
                Parameters
         Name  Description  creatorId  ID of a user who will be assigned a creator for a new user 
         name  new user name (at least 4 characters) 
         password  new user password 
         dataFlags  data flags for the response (see Data format: Users)Response{
        "item":{/* user created */
        ...
        },
        "flags":<uint>/* applied data flags */
        }You can find the format of “item” in the chapter Data format: Users.
        """
        params = locals()
        params.pop('self')
        return self.session.call("core_create_user", **params)


    def set_session_property(self, prop_value):
        """
                
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("core_set_session_property", **params)


    def duplicate(self, operateAs, continueCurrentSession):
        """
                It duplicates the active session.
        Parameters
         Name  Description  operateAs  name of a user you want to operate as (must be empty if you want to operate as the main user) 
         continueCurrentSession  defines whether to continue the previous session (false by default, if true - both sid's remain valid) Response
        Response format is be the same as in the command Token login
        """
        params = locals()
        params.pop('self')
        return self.session.call("core_duplicate", **params)


    def check_unique(self, type, value):
        """
                Params
         Name  Description  type  item type (user, avl_resource) 
         value  item name Response{"result":0}     /* if unique  */
        {"result":1}     /* if exist  */
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("core_check_unique", **params)


    def create_auth_hash(self, ):
        """
                 Generated hash is valid from creation moment to first usage during 2 minutes!
        Response{
        "authHash":<text> /* authorization hash value */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("core_create_auth_hash", **params)


    def get_hw_types(self, filterType, filterValue, includeType, ignoreRename):
        """
                Parameters
        All params are optional.
         Name  Description  filterType  filter type, may be:
        -name,
        -id,
        -type,
        -feature 
         filterValue  filter value array (delimiter is comma), for different 'filterType'
        values may be as follows::
        name – full device name(s),
        id – device id(s),
        type – values: auto, tracker, mobile, soft ,
        feature – values: wifi_pos
         includeType  flag, whether to show device type
        in response or not 
         ignoreRename  flag, whether to ignore device type rename or not Response[/* hardware types */
        {
            "id":<uint>,/* ID */
            "uid2":<uint>,/* second ID */
            "name":<text>,/* name */
            "hw_category":<text>,/* hardware type */
            "tp":<text>,/* TCP port */
            "up":<text> /* UDP port */
        },
        ...
        ]
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("core_get_hw_types", **params)
