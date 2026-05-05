from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("report.pdf")
styles = getSampleStyleSheet()

content = []
content.append(Paragraph("Demographic Decline in Bulgaria", styles["Title"]))
content.append(Paragraph("Advanced statistical analysis of population trends.", styles["BodyText"]))

doc.build(content)