import re 

def parse_experience_years (text ):

    pattern =r'(\d+(\.\d+)?)(\+)?\s*(years|yrs)'
    matches =re .findall (pattern ,text .lower ())
    if matches :

        years =[float (m [0 ])for m in matches ]
        return max (years )
    return 0 

def post_process_data (data ,raw_text ):
    """
    Refines extracted data and calculates derived fields.
    """


    total_exp =parse_experience_years (raw_text )
    data ['total_experience_years']=total_exp 


    if data ['name']:
        data ['name']=data ['name'].title ()

    return data 
