
class Token:
    def __init__(self, session):
        self.session session

    def update(self, callMode, userId, h, app, at, dur, fl, p, items, deleteAll):
        """
                Parameters
         Name  Description  callMode  action: creation, editing, deletion (create, update, delete) 
         userId  subuser id (optional, for managing other user tokens) 
         h  token name - 72 symbols (while update, delete) 
         app  application name 
         at  token activation time, UNIX-time:
        0 - now 
         dur  token duration after activation, seconds:
        max value = 8640000 (100 days) if 0 – duration is infinite 
         fl  access flags 
         p  custom parameters, value must be object or an array of objects
        p:{} is minimal 
         items  list of item ids with token granted access, optional 
         deleteAll  actual for callMode:delete; values: 1 or true - delete all created tokens   Token is deleted automatically through 100 days of inaction ( even with dur:0)!
        Object example for p-param:"p":"{\"paramA\":\"valueB\"}"Array of objects example for p-param:"p":"[{\"paramA\":\"valueB\"},{\"paramB\":\"valueD\"}]"Access flags
         Value  Description   0x100   online tracking 
          0x200   view access to most data 
          0x400   modification of non-sensitive data 
          0x800   modification of sensitive data 
          0x1000   modification of critical data, including messages deletion 
          0x2000   communication 
          -1   unlimited operation as authorizated user
        (allows to manage user tokens)  More info you can get here.
        Response{
        "h":<text>,/* unique token name, 72 symbols */
        "app":<text>,/* application name */
        "at":<uint>,/* token activation time, UNIX-time */
        "ct":<uint>,/* token creation time, UNIX-time */
        "dur":<uint>,/* token duration after activation, секунды */
        "fl":<uint>,/* access flags */
        "items":[<long>],/* list of item ids with token granted access */
        "p":<text>/* custom parameters, value must be object or an array of objects */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("token/update", **params)


    def list(self, userId):
        """
                Parameters
        Param DescriptionCommentsuserId subuser id optional Response[
            {
        "h":<text>,/* unique token name, 72 symbols */
        "app":<text>,/* application name */
        "at":<uint>,/* token activation time, UNIX-time */
        "ct":<uint>,/* token creation time, UNIX-time */
        "dur":<uint>,/* token duration after activation, секунды */
        "fl":<uint>,/* access flags */
        "ll":<uint>,/* last time of using */
        "ttl":<uint>,/* not actual parameter */
        "items":[<long>],/* list of item ids with token granted access */
        "p":<text>/* custom parameters, value must be object or an array of objects */
            },
            .../* other tokens (if any) */
        ]
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("token/list", **params)


    def login(self, token, operateAs, fl):
        """
                Parameters
         Name  Description  token  unique token name, 72 symbols 
         operateAs  subuser name to login (optional parameter) 
         fl  response flags  Flag HEX  Flag DEC  Description  0x1  1  basic info 
         0x2  2  user info 
         0x4  4  token info 
         0x8  8  items info 
         0x10  16  billing services info 
         0x20  32  user CustomProperties  How to get token name?
        - create new token (token/update command, callmode:create);- execute token/list command (if tokens already created).
        You cannot login under non-activated token (refer to at-param in token parameters). After login session is created, you can execute some requests within it. If server haven't received any requests for 5 minutes the session will be killed. To prevent such behaviour you can send a request every 5 minutes, for example  requests/avl_evts.
        Response{
        "eid":<text>,/* session ID */
        "gis_sid":<text>,/* session ID for gis services */
        "host":<text>,/* host */
        "hw_gw_ip":<text>,/* hardware gateway ip */
        "au":<text>,/* user name */
        "pi":<int>,/* ping interval */
        "tm":<uint>,/* current time (UTC) */
                "wsdk_version":<text>           /* sdk version */
        "user":{/* user from whose behalf you want to perform login */
        "nm":<text>,/* name  */
        "cls":<uint>,/* ID of superclass "user" */
        "id":<long>,/* ID */
        "prp":{/* custom properties, for example: */
        "dst":<text>,/* daylight savings time */
        "language":<text>,/* language (two-lettered code) */
        "msakey":<text>,/* access key to mobile site */
        "pcal":<text>,/* Iranian calendar */
        "tz":<text>,/* time zone */
        "us_units":<text>,/* US metrics (miles and gallons) */
        ...
        },
        "crt":<uint>,/* creator ID */
        "bact":<uint>,/* account ID */
        "fl":<uint>,/* user flags */
        "hm":<text>,/* host mask */
        "uacl":<uint>,/* user access to himself */
        "mu": <uint>,/* Measurement system */
        "ct": <uint>,/* User creation date */
        "ftp": {<text>},/* FTP settings */
        "ld": <uint>,/* Last login date */
        "pfl": <uint>,/* Creators flag */
        "ap": {/* Two-factor authentication settings */
            "type":<uint>,/* authentication type ( 0 - none, 1 - email, 2 - SMS ) */
            "phone":<text>/* Phone number */
        },    
        "mapps": {<text>},/* Mobile apps list */
        "mappsmax": <int>/* Restrictions on mobile applications specified in the billing plan */
        },
        "classes":{/* superclasses available for current user (key - superclass name, value - superclass ID): */
        "avl_hw":<uint>,/* hardware type */
        "avl_resource":<uint>,/* resource */
        "avl_retranslator":<uint>,/* retranslator */
        "avl_unit":<uint>,/* unit */
        "avl_unit_group":<uint>,/* unit group */
        "user":<uint>,/* user */
        "avl_route":<uint>/* route */
        }
        "features":{
        "unlim":<bool>,/* billing plan type: 0 - regular, 1 - special (for development/testing) */
        "svcs":{/* hash-collection of allwed services, if service not mentioned here means it is forbidden */
        "<service_name>":<bool>,/* key - service name, value: 0 - service available, but limit reached, 1 - service available and can be used */
        ...
        }
        }
         
        ...,/* core/login response */
         
        "token":"{\"app\":\"<text>\",\"ct\":<uint>\"at\":<uint>,\"dur\":<uint>,\"fl\":<uint>\"p\":\"<text>\",\"items\":[<long>]}",
        /* all token settings as escaped json */
        .../* core/login response */
        } Clarification for <service_name>: for additional info please refer to  services list.
        User flags are described in the chapter Set user settings flags.
        More about FTP setting here - Custom FTP settings.
        """
        params = locals()
        params.pop('self')
        return self.session.call("token/login", **params)
