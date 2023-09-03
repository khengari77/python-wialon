
class Apps:
    def __init__(self, session):
        self.session session

    def list(self, ):
        """
                Parameters
         Name  Description  manageMode 1 -  flag to billing data, optional
         filterLang  filter by language, optionalResponse{"name":<text>, /* app name */
        "description":<text>, /* app description */
        "url":<text>, /* app url */
        "flags":<uint>,/*flags */
        "sortOrder":<uint>, /*sort type */
        "serviceName":<text>, /* service name*/
        "id":<uint>, /* app id */
        "langs":<text>, /* app languages*/
        "requiredServicesList":<text>, /* required services */
        "billingPlans":<text>, /* required billing plans*/}
        
        """
        params = locals()
        params.pop('self')
        return self.session.call("apps/list", **params)
