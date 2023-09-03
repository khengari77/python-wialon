
class File:
    def __init__(self, session):
        self.session session

    def write(self, itemId, storageType, path, content, writeType, contentType):
        """
                Params
         Parameter  Description  itemId  item id 
         storageType  storage type:
        1 - public (all users may see/download
        files ),
        2 - protected (that users may see/down-
        load files who being grant rights) 
         path  relative path from root folder to the file included  
         content  content being written 
         writeType  write type:
        0 - rewrite a file,
        1 - append to a file,
        2 - do not rewrite if the file exists 
         contentType  content type; the content is returned as:
        0 - text,
        1 - hex string, 
        2 - base64 string Response
        After write success:{}Errors{
            "error":<uint>/* error code */
        }  Error code   Description   1  you are not authorized 
         3  file not found 
         4  wrong id inputted (not digits) 
         5  file already exists (if 'do not rewrite existed file' option chosen)
         7  'id' not found 
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("file/write", **params)


    def rm(self, itemId, storageType, path):
        """
                Params
         Param  Description  itemId  element id 
         storageType  storage type:
        1 - public(all users may see/download
        files ),
        2 - protected (that users may see/down-
        load files who being grant rights) 
         path  relative path from root folder to the file   If you want to clear public/protected storage totally please use    "path":"/"in your request.
        Response
        If succeed to delete a file then:{}Errors{
        "error":<uint>/* error code */
        }  Error
        code   Description   1  not authorized 
         4  incorrect id stated (not digits) 
         5  file not found for deleting
         7  there is no element with that 'id' 
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("file/rm", **params)


    def library(self, type, flags):
        """
                Parameters
        NameDescription type  library name; default values: unit, group, poi 
         flags  0 - list files from default library only (valid are default
        type values);
        1 - list files from all available hierarchy libraries recur-
        sively (this account, parent, parent's parent etc) How to create custom library and find it?
        1. Create “library” directory in the account public file storage (<account_id>/1/library);2. Put custom library in “library” folder (put assumed “cust_lib” library  – <account_id>/1/library/cust_lib);3. To list library content we type library name as type value (so we will search type:'cust_lib' from the example above).
        Response{
            "<account_id>": [        /* account id, 0 - default library */
                              {
                                  "n":<text>,      /* file name */
                                  "s":<uint>,      /* file size (bytes) */
                                  "ct":<uint>,     /* file creation time, UNIX-time */
                                  "mt":<uint>      /* file last modification time, UNIX-time */
                              },
                              ...
            ],
            ...                      /* other account ids (if any) */
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("file/library", **params)


    def type_library(self, text):
        """
                Parameters
         Name  Description  lang  lang 2-letters code, optional, by default the language from current sessionResponse
        JSON with the list of types - {“key”:key1, “name”:value1}. See the full description below.
        Unit type list
        Category "Personal GPS tracker"
        ValueNameempty_person Person
        empty_animalAnimal
        empty_personal_otherOtherCategory "Stationary object"
         Value  Name empty_cameraCamera
        empty_compressorCompressor
        empty_containerContainer
        empty_electric generatorElectric generator
        empty_filling_stationFilling station
        empty_machine_toolMachine-tool
        empty_stationary_otherOther
        empty_roomRoom
        empty_vending_machineVending machineCategory "Cargo transport"
        ValueNamepickupPick-up
        vanVan
        truckTruck
        heavy_truckHeavy Truck
        dump_truckDump truck
        logging_truckLogging Truck
        tractor_unitTractor unit
        trailers_semiTrailer and semi-trailers
        tanker_trailerTanker trailer 
        tank_trailerTank truck
        refrigerator_vanRefrigerator van
        other_cargoOtherCategory "Passenger transport"
         Value  Name kick_scooterKick scooter
        bicycleBicycle
        motorcycleMotorcycle
        passenger_carPassenger car
        minibusMinibus
        busBus
        trolleybusTrolleybus
        tramTram
        other_passengerOtherCategory 'Agricultural machinery"
         Value Name tractorTractor
        combineCombine
        sprayerSprayer
        balerBaler
        agricultural_spreaderAgricultural spreader
        mowerMowerCategory "Construction equipment"
         Value  Name bulldozerBulldozer
        excavatorExcavator
        backhoe_loaderBackhoe loader
        loaderLoader
        skid_steer_loaderSkid-steer loader
        forkliftForklift
        hookliftHooklift
        craneCran
        manipulatorManipulator
        bucket_truckBucket truck
        concrete_mixerConcrete mixer
        concrete_pumpConcrete pump
        piling_drilling_rigPiling and drilling rig
        crusherCrusher
        trencherTrencher
        pipelayerPipelayer
        road_rollerRoad roller
        road_graderRoad grader
        paverPaver
        scraperScraperCategory "Special vehicles"
         Value  Name ambulanceAmbulance
        garbage_truckGarbage Truck
        fire_truckFire truck
        street_cleaning_machineStreet cleaning machine
        tow_truckTow truck
        other_specialOther
        store_on_wheelsStore on wheelsCategory "Others"
         Value  Name air_transportAir transport
        off_road_vehicleOff-road vehicle
        all_terrain_vehicleAll-terrain vehicle
        snowmobileSnowmobile
        snowcatSnowcat
        rail_transportRail transport
        water_transportWater transport
        recreational_vehicleRecreational vehicle
        other_vehicleOther
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("file/type_library", **params)


    def get(self, itemId, storageType, path, format):
        """
                Params
         Param  Description  itemId  element id 
         storageType  storage type:
        1 - public(all users may see/download
        files ),
        2 - protected (that users may see/down-
        load files who being grant rights) 
         path  relative path from root folder to the file  
         format  for .ddd files, get file in VDO format (“format”:1) Response
        Returns the file.
        If there is no file according to path specified then:Invalid input{"error":3}
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("file/get", **params)


    def list(self, itemId, storageType, path, mask, recursive, fullPath):
        """
                Params
         Param  Description  itemId  element id 
         storageType  storage type:
        1 - public(all users may see/download files ),
        2 - protected (that users may see/download files who being grant rights) 
         path  relative path from root folder to the file  
         mask  name mask; you may use '*':
        it can wildcard 0, 1, …, namy symbols 
         recursive  flag, whether you want content be shown recursively 
         fullPath  flag, whether you want elements fullpath be shown   Only element creator may put and remove files.
        Response
         'n/c'-signature means that hierarchy element is 'folder', 'n/s'-signature states that element is 'file'.[
        {
        "n": <text>,/* path to the folder being chosen, starts with "public" or "protected" */
        "c": [/* root folder content, inside may be files and/or folders */
        {
        "n": <text> /* folder name */
        "c": [...]/* folder content, inside may be files and/or folders */
        },
         
        {
        "n": <text>, /* file name */
        "s": <text> /* file size (bytes) */
        },
        ...
        ]
        }
        ]IF the path does not exist then:{
            "error": 5
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("file/list", **params)


    def read(self, itemId, storageType, path, contentType):
        """
                Parameters
         Param  Description  itemId  item id 
         storageType  storage type:
        1 - public (all users may see/download
        files ),
        2 - protected (that users may see/down-
        load files who being grant rights) 
         path  relative path from root folder to the file  
         contentType  content type; the content is returned as:
        0 - text,
        1 - hex string, 
        2 - base64 string Response
        After read success:{
            "content": <content>
        }where <content> – file content as string.
        If there is no such file then:{
            "error": 3
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("file/read", **params)


    def put(self, itemId, storageType, path, writeType, eventHash):
        """
                Parameters
         Parameter  Description  itemId  element id 
         storageType  storage type:
        1 - public(all users may see/download
        files ),
        2 - protected (that users may see/down-
        load files who being grant rights) 
         path  relative path from root folder to the file  
         writeType  write type:
        0 - overwrite a file,
        1 - append to a file content,
        2 - do not overwrite if file exists 
         eventHash  event name which will be generated af-
        ter processing the data   There is no way for 'file' and 'folder' to coexist with the same names (e.g. text file 'readme' and 'readme'-folder) because Linux treats them as the same entity though with different attributes.
        In order to upload some files, put them using POST-request with some params (multipart/form-data), e.g.:Request URL: https://hst-api.wialon.com/wialon/ajax.html?
        """
        params = locals()
        params.pop('self')
        return self.session.call("file/put", **params)


    def mkdir(self, itemId, storageType, path):
        """
                Params
         Param  Description  itemId  element id 
         storageType  storage type:
        1 - public(all users may see/download
        files ),
        2 - protected (that users may see/down-
        load files who being grant rights) 
         path  relative path from root folder to the file  Response{} /* empty object if execution successful, if not - error code */IF the path does not exist then:{
            "error": 5
        }
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("file/mkdir", **params)
