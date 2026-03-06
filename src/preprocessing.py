import re 

def clean_text (text ):
    """
    Cleans and normalizes text.
    """
    if not text :
        return ""


    text =text .encode ('ascii','ignore').decode ()





    lines =[line .strip ()for line in text .split ('\n')if line .strip ()]
    text ='\n'.join (lines )

    return text 
