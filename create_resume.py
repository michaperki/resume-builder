# create a resume using reportlab

# Path: create_resume_2.py

# this is a function that will create a resume

# import the canvas from reportlab

from reportlab.pdfgen import canvas

# import the pagesizes from reportlab

from reportlab.lib.pagesizes import letter

# import the units from reportlab

from reportlab.lib.units import inch

from datetime import datetime
import os

margin = inch * 0.75

experience_1 = {
    "job_title": "Data Engineer",
    "company": "Nomi Health",
    "start_date": "May 2022",
    "end_date": "Present",
    "description": {
        "job_detail_1": "• Build ETL pipeline to automate costly manual data wrangling",
        "job_detail_2": "• Optimize member onboarding, improved efficiency by 30%",
        "job_detail_3": "• Develop dashboards to communicate insights to stakeholders"
        }
    }

experience_2 = {
    "job_title": "Founder",
    "company": "eSports Startup",
    "start_date": "Jan 2021",
    "end_date": "April 2022",
    "description": {
        "job_detail_1": "• Lead team in bringing unique product to market for eSports fans",
        "job_detail_2": "• Raised funds to support the enterprise mission",
        "job_detail_3": "• Bootstrap marketing via social media campaigns and influencer outreach"
        }
    }

experience_3 = {
    "job_title": "Data Scientist",
    "company": "Ed Tech Startup",
    "start_date": "June 2018",
    "end_date": "Dec 2020",
    "description": {
        "job_detail_1": "• Built a recommendation engine for personalized learning",
        "job_detail_2": "• Improved data quality by 50% by implementing data validation",
        "job_detail_3": "• Developed a data pipeline to automate data collection"
        }
    }

# define the function
def create_resume():
    create_directory()
    pdf = create_pdf()
    pdf = add_header(pdf)
    pdf = add_contact_details(pdf)
    pdf = add_work_experience(pdf)
    pdf = add_education(pdf)
    pdf = add_skills(pdf)
    pdf = add_projects(pdf)
    pdf = add_interests(pdf)
    pdf  = add_footer(pdf)
    save_pdf(pdf)

def create_directory():
    # create a directory to store the resume
    # get the current date and time
    now = datetime.now()
    # get the current date and time in a string
    now_string = now.strftime("%m-%d-%Y_%H-%M-%S")
    # create the directory name
    directory_name = "resume_" + now_string
    # create the directory within the output directory
    os.mkdir("output/" + directory_name)
    # change the current working directory to the new directory
    os.chdir("output/" + directory_name)

# define the create_pdf function
def create_pdf():
    # Create a new PDF with letter size paper (8.5x11 inches)
    pdf = canvas.Canvas("resume_test.pdf", pagesize=letter)
    return pdf

# define the add_header function
def add_header(pdf):
    # Set the font and font size for the heading
    pdf.setFont("Helvetica-Bold", 18)
    # Write the name in the center of the page
    name = "Michael Perkins"
    pdf.drawCentredString(letter[0] / 2, inch * 10.25, name)
    return pdf

# define the add_contact_details function
def add_contact_details(pdf):
    # Set the font and font size for the contact details
    pdf.setFont("Helvetica", 10)

    # Define the contact details
    email = "mperkins1995@gmail.com"
    phone = "(214) 701-2414"
    address = "3207 Liberty Street #A, Austin, TX 78705"
    github = "github.com/mperkins1995"

    # Concatenate the contact details into a single string with tabs between them
    contact_details = "     ".join([email, phone, address, github])

    pdf.drawCentredString(letter[0] / 2, inch * 9.75, contact_details)

    # Add a line under the contact details
    pdf.line(inch, inch * 9.55, letter[0] - inch, inch * 9.55)

    return pdf

# define the add_work_experience function
def add_work_experience(pdf):
    # Set the font and font size for the section headings
    pdf.setFont("Helvetica-Bold", 14)

    # Write the work experience section heading and underline it
    work_heading = "Work Experience"
    work_heading_width = pdf.stringWidth(work_heading, "Helvetica-Bold", 14)
    pdf.drawString(margin, inch * 9.15, work_heading)
    pdf.line(margin, inch * 9.1,margin + work_heading_width, inch * 9.1)
    detail_height = 1.25
    add_work_detail(experience_1, pdf)
    add_work_detail(experience_2, pdf, 8.75 - detail_height)
    add_work_detail(experience_3, pdf, 8.75 - (2*detail_height))
    return pdf

# define the add_work_experience function
def add_work_detail(experience, pdf, start_height=8.75):
    # Set the font and font size for the job title
    pdf.setFont("Helvetica-Bold", 12)

    # Write the job title
    job_title = experience["job_title"]
    job_title_width = pdf.stringWidth(job_title, "Helvetica-Bold", 12)
    pdf.drawString(margin, inch * start_height, job_title)

    # Set the font and font size for the company name
    pdf.setFont("Helvetica", 12)

    # Write the company name
    company = experience["company"]
    pdf.drawString(margin + job_title_width, inch * start_height, ", " + company)

    # Set the font and font size for the dates
    pdf.setFont("Helvetica", 10)

    # Write the dates on the same line as the company name on the right side of the page
    start_date = experience["start_date"]
    end_date = experience["end_date"]
    dates = start_date + " - " + end_date
    dates_width = pdf.stringWidth(dates, "Helvetica", 10)
    pdf.drawString(letter[0] - margin - dates_width, inch * start_height, dates)

    # Set the font and font size for the description
    pdf.setFont("Helvetica", 10)

    # Write the description
    description = experience["description"]
    pdf.drawString(margin, inch * (start_height - .25), description["job_detail_1"])
    pdf.drawString(margin, inch * (start_height - .5), description["job_detail_2"])
    pdf.drawString(margin, inch * (start_height - .75), description["job_detail_3"])

    return pdf


# define the add_education function
def add_education(pdf):
    # Set the font to bold for the education section heading
    pdf.setFont("Helvetica-Bold", 14)

    # Write the education section heading and underline it
    education_heading = "Education"
    education_heading_width = pdf.stringWidth(education_heading, "Helvetica-Bold", 14)
    pdf.drawString(margin, inch * 5, education_heading)
    pdf.line(margin, inch * 4.95,margin + education_heading_width, inch * 4.95)

    # Set the font to normal for the education details
    pdf.setFont("Helvetica", 10)

    # Write the education details
    education_details = "Dartmouth College, B.A. in Quantitative Social Science"
    pdf.drawString(margin, inch * 4.6, education_details)

    # Write the education dates
    education_dates = "July 2014 - June 2018"
    education_dates_width = pdf.stringWidth(education_dates, "Helvetica", 10)
    pdf.drawString(letter[0] - margin - education_dates_width, inch * 4.6, education_dates)

    # Write the coursework details
    coursework_details = "• Coursework in Data Science, Economics, and Statistics"
    pdf.drawString(margin, inch * 4.35, coursework_details)
    # Write the coursework details
    coursework_details = "• Editor for the Dartmouth Review Newspaper"

    return pdf

# define the add_skills function
def add_skills(pdf):
    # Set the font to bold for the skills section heading
    pdf.setFont("Helvetica-Bold", 14)

    # Write the skills section heading and underline it
    skills_heading = "Skills"
    skills_heading_width = pdf.stringWidth(skills_heading, "Helvetica-Bold", 14)
    pdf.drawString(margin, inch * 3.75, skills_heading)
    pdf.line(margin, inch * 3.7,margin + skills_heading_width, inch * 3.7)

    # Set the font to normal for the skills details
    pdf.setFont("Helvetica", 10)

    # Write the skills details
    skills_details = "• Python, R, SQL, Tableau, Git, HTML, CSS, JavaScript, React, Flask, Docker, AWS"
    pdf.drawString(margin, inch * 3.35, skills_details)

    return pdf

# define the add_projects function
def add_projects(pdf):
    # Set the font to bold for the projects section heading
    pdf.setFont("Helvetica-Bold", 14)

    # Write the projects section heading and underline it
    projects_heading = "Projects"
    projects_heading_width = pdf.stringWidth(projects_heading, "Helvetica-Bold", 14)
    pdf.drawString(margin, inch * 2.75, projects_heading)
    pdf.line(margin, inch * 2.7,margin + projects_heading_width, inch * 2.7)

    # Set the font to normal for the projects details
    pdf.setFont("Helvetica", 10)

    # Write the projects details
    project_1 = {
        "employer": "Nomi Health",
        "date": "2022",
        "description": "Built \"the most important financial dashboard in the company\" by automating Excel-based models from 3rd party consultants"
    }
    project_2 = {
        "employer": "Dartmouth College",
        "date": "2018",
        "description": "Develop resume generator for Mentorship program using Python."
    }

    projects_details = "• " + project_1["employer"] + ", " + project_1["date"] + ": " + project_1["description"]
    # if the project description is too long, split it into two strings and then use the drawString function twice. But don't split the string in the middle of a word.

    # get the width of "• "
    bullet_width = pdf.stringWidth("• " + project_1["employer"] + ", " + project_1["date"] + ": ", "Helvetica", 10)

    if len(projects_details) > 100:
        projects_details_1 = projects_details[:projects_details.rfind(" ", 0, 90)]
        projects_details_2 = projects_details[projects_details.rfind(" ", 0, 90):]
        pdf.drawString(margin, inch * 2.35, projects_details_1)
        pdf.drawString(margin + bullet_width, inch * 2.1, projects_details_2)
    else:
        pdf.drawString(margin, inch * 2.35, projects_details)

    projects_details = "• " + project_2["employer"] + ", " + project_2["date"] + ": " + project_2["description"]
    # if the project description is too long, split it into two strings and then use the drawString function twice. But don't split the string in the middle of a word.
    
    # get the width of "• "
    bullet_width = pdf.stringWidth("• " + project_2["employer"] + ", " + project_2["date"] + ": ", "Helvetica", 10)

    if len(projects_details) > 100:
        projects_details_1 = projects_details[:projects_details.rfind(" ", 0, 90)]
        projects_details_2 = projects_details[projects_details.rfind(" ", 0, 90):]
        pdf.drawString(margin, inch * 1.75, projects_details_1)
        pdf.drawString(margin + bullet_width, inch * 1.6, projects_details_2)
    else:
        pdf.drawString(margin, inch * 1.75, projects_details)
    
    return pdf


# define the add_interests function
def add_interests(pdf):
    # Set the font to bold for the interests section heading
    pdf.setFont("Helvetica-Bold", 14)

    # Write the interests section heading and underline it
    interests_heading = "Interests"
    interests_heading_width = pdf.stringWidth(interests_heading, "Helvetica-Bold", 14)
    pdf.drawString(margin, inch * 1.25, interests_heading)
    pdf.line(margin, inch * 1.2,margin + interests_heading_width, inch * 1.2)

    # Set the font to normal for the interests details
    pdf.setFont("Helvetica", 10)

    # Write the interests details
    interests_details = "• Soccer, skiing, chess, poker, reading, and traveling"
    pdf.drawString(margin, inch * 0.85, interests_details)

    return pdf


# define the add_footer function
def add_footer(pdf):
    # Set the font to normal for the footer
    pdf.setFont("Helvetica", 8)

    # Write the footer
    # get the date
    date = datetime.now().strftime("%B %d, %Y")
    
    footer = "Generated on " + date + " using Python"

    # draw in the bottom right corner
    footer_width = pdf.stringWidth(footer, "Helvetica", 8)
    pdf.drawString(letter[0] - margin - footer_width, margin, footer)

    return pdf
    

# define the save_pdf function
def save_pdf(pdf):
    pdf.save()


if __name__ == "__main__":
    create_resume()