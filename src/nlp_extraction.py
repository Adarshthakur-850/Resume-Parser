import spacy 
import re 


SKILL_DB =[
'Python','Java','C++','SQL','HTML','CSS','JavaScript',
'React','Node.js','Machine Learning','Deep Learning','NLP',
'Pandas','NumPy','Scikit-learn','TensorFlow','PyTorch',
'AWS','Azure','Docker','Kubernetes','Git','Agile'
]

def load_nlp_model ():
    try :
        return spacy .load ("en_core_web_sm")
    except OSError :
        print ("Downloading spaCy model...")
        from spacy .cli import download 
        download ("en_core_web_sm")
        return spacy .load ("en_core_web_sm")

nlp =load_nlp_model ()

def extract_entities (text ):
    doc =nlp (text )
    data ={
    "name":extract_name (doc ,text ),
    "email":extract_email (text ),
    "phone":extract_phone (text ),
    "skills":extract_skills (doc ,text ),
    "education":extract_education (text ),
    "experience":[],
    "projects":[],
    "certifications":[]
    }
    return data 

def extract_name (doc ,text ):

    for ent in doc .ents :
        if ent .label_ =="PERSON":
            return ent .text 

    lines =text .split ('\n')
    if lines :
        return lines [0 ][:50 ]
    return ""

def extract_email (text ):
    pattern =r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    match =re .search (pattern ,text )
    return match .group (0 )if match else ""

def extract_phone (text ):

    pattern =r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    match =re .search (pattern ,text )
    return match .group (0 )if match else ""

def extract_skills (doc ,text ):
    skills =[]

    text_lower =text .lower ()
    for skill in SKILL_DB :
        if re .search (r'\b'+re .escape (skill .lower ())+r'\b',text_lower ):
            skills .append (skill )


    return list (set (skills ))

def extract_education (text ):
    edu_keywords =['B.Tech','M.Tech','B.Sc','M.Sc','Ph.D','Bachelor','Master','University','College','Institute']
    education =[]
    lines =text .split ('\n')
    for line in lines :
        if any (keyword .lower ()in line .lower ()for keyword in edu_keywords ):
            education .append (line )
    return education 
