from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch


def create_resume():
    # Create a new PDF with letter size paper (8.5x11 inches)
    pdf = canvas.Canvas("resume.pdf", pagesize=letter)

    # Set the font and font size for the heading
    pdf.setFont("Helvetica-Bold", 18)

    # Write the name in the center of the page
    name = "Michael Perkins"
    name_width = pdf.stringWidth(name, "Helvetica-Bold", 18)
    pdf.drawCentredString(letter[0] / 2, inch * 10.25, name)

    # Set the font and font size for the contact details
    pdf.setFont("Helvetica", 10)

    # Define the contact details
    email = "mperkins1995@gmail.com"
    phone = "(214) 701-2414"
    address = "3207 Liberty Street #A, Austin, TX 78705"
    github = "github.com/mperkins1995"

    # Concatenate the contact details into a single string with tabs between them
    contact_details = "     ".join([email, phone, address, github])

    pdf.drawCentredString(letter[0] / 2, inch * 10, contact_details)

    # Add a line under the contact details
    pdf.line(inch, inch * 9.95, letter[0] - inch, inch * 9.95)

    # Add a metrics section on the right side of the page
    pdf.setFont("Helvetica-Bold", 14)

    # Write the metrics section heading and underline it
    metrics_heading = "Metrics"
    metrics_heading_width = pdf.stringWidth(metrics_heading, "Helvetica-Bold", 14)
    pdf.drawString(letter[0] - inch * 2.5, inch * 8, metrics_heading)
    pdf.line(letter[0] - inch * 2.5, inch * 7.95, letter[0] - inch * 2.5 + metrics_heading_width, inch * 7.95)

    # Set the font and font size for the metrics details
    pdf.setFont("Helvetica", 12)

    # Write the metrics details
    pdf.drawString(letter[0] - inch * 2.5, inch * 9.5, "Years of Experience: 2")
    pdf.drawString(letter[0] - inch * 2.5, inch * 9.25, "Years of Python Experience: 2")
    pdf.drawString(letter[0] - inch * 2.5, inch * 9, "Years of SQL Experience: 2")
    pdf.drawString(letter[0] - inch * 2.5, inch * 8.75, "Years of Tableau Experience: 1")

    # Set the font and font size for the section headings
    pdf.setFont("Helvetica-Bold", 14)

    # Write the work experience section heading and underline it
    work_heading = "Work Experience"
    work_heading_width = pdf.stringWidth(work_heading, "Helvetica-Bold", 14)
    pdf.drawString(inch, inch * 8.75, work_heading)
    pdf.line(inch, inch * 8.7, inch + work_heading_width, inch * 8.7)

    # Set the font to bold for the job title
    pdf.setFont("Helvetica-Bold", 12)

    job_title_1 = "Data Scientist, Nomi Health"
    job_title_2 = "Data Scientist, Ed Tech Startup"

    # Write the job title
    pdf.drawString(inch, inch * 8.25, job_title_1)

    # Set the font to normal for the job details
    pdf.setFont("Helvetica", 12)

    # Define the job details as a bulleted list of strings
    job_details = [
        "Build and deploy ETL pipelines to process and clean data from various sources.",
        "Automate data collection and analysis using Python and SQL. Reduce manual data collection and analysis time by 70%.",
        "Create data visualizations using Tableau and Domo. Present data to stakeholders and executives.",
        ]
    


    # Write the job details
    for i, detail in enumerate(job_details):
        pdf.drawString(inch * 1.5, inch * (8 - 0.25 * i), detail)


    # Set the font and font size for the section headings
    pdf.setFont("Helvetica-Bold", 14)

    # Write the education section heading and underline it
    edu_heading = "Education"

    edu_heading_width = pdf.stringWidth(edu_heading, "Helvetica-Bold", 14)
    pdf.drawString(inch, inch * 7.25, edu_heading)
    pdf.line(inch, inch * 7.2, inch + edu_heading_width, inch * 7.2)

    # Set the font and font size for the education details
    pdf.setFont("Helvetica", 12)

    # Write the education details
    pdf.drawString(inch, inch * 6.75, "Degree Name, Field of Study, School Name, Year")
    pdf.drawString(inch, inch * 6.5, "Degree Name, Field of Study, School Name, Year")

    # Write the skills section heading
    pdf.drawString(inch, inch * 5.75, "Skills")

    # Set the font and font size for the skills details
    pdf.setFont("Helvetica", 12)

    # Write the skills details
    pdf.drawString(inch, inch * 5.5, "- Skill 1")
    pdf.drawString(inch, inch * 5.2, "- Skill 2")
    pdf.drawString(inch, inch * 4.9, "- Skill 3")

    # Save the PDF
    pdf.save()


if __name__ == '__main__':
    create_resume()
