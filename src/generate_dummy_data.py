from reportlab .pdfgen import canvas 
import os 

def generate_dummy_resume (filepath ="data/sample_resume.pdf"):
    if not os .path .exists ("data"):
        os .makedirs ("data")

    c =canvas .Canvas (filepath )


    c .setFont ("Helvetica-Bold",16 )
    c .drawString (50 ,800 ,"John Doe")
    c .setFont ("Helvetica",10 )
    c .drawString (50 ,785 ,"john.doe@example.com | (555) 123-4567 | San Francisco, CA")

    c .line (50 ,775 ,550 ,775 )

    c .setFont ("Helvetica-Bold",12 )
    c .drawString (50 ,750 ,"SUMMARY")
    c .setFont ("Helvetica",10 )
    c .drawString (50 ,735 ,"Experienced Software Engineer with 5+ years of experience in Python and Machine Learning.")

    c .setFont ("Helvetica-Bold",12 )
    c .drawString (50 ,700 ,"SKILLS")
    c .setFont ("Helvetica",10 )
    c .drawString (50 ,685 ,"Python, Java, Pandas, Scikit-learn, Docker, AWS, SQL")

    c .setFont ("Helvetica-Bold",12 )
    c .drawString (50 ,650 ,"EXPERIENCE")
    c .setFont ("Helvetica-Bold",10 )
    c .drawString (50 ,635 ,"Senior Developer | Tech Corp")
    c .setFont ("Helvetica",10 )
    c .drawString (50 ,620 ,"June 2018 - Present")
    c .drawString (50 ,605 ,"- Developed NLP models for sentiment analysis.")
    c .drawString (50 ,590 ,"- Deployed APIs using FastAPI and Docker.")

    c .setFont ("Helvetica-Bold",12 )
    c .drawString (50 ,550 ,"EDUCATION")
    c .setFont ("Helvetica",10 )
    c .drawString (50 ,535 ,"B.Tech in Computer Science | Stanford University | 2014-2018")

    c .save ()
    print (f"Generated dummy resume at {filepath }")

if __name__ =="__main__":
    generate_dummy_resume ()
