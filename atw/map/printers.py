from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from atw.map.models import TripStage, Trip
# Pour la classe NumberedCanvas
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
	def __init__(self, *args, **kwargs):
		canvas.Canvas.__init__(self, *args, **kwargs)
		self._saved_page_states = []

	def showPage(self):
		self._saved_page_states.append(dict(self.__dict__))
		self._startPage()

	def save(self):
		"""add page info to each page (page x of y)"""
		num_pages = len(self._saved_page_states)
		for state in self._saved_page_states:
			self.__dict__.update(state)
			self.draw_page_number(num_pages)
			canvas.Canvas.showPage(self)
		canvas.Canvas.save(self)

	def draw_page_number(self, page_count):
		# Change the position of this to wherever you want the page number to be
		self.drawRightString(105 * mm, 20 * mm, "%d / %d" % (self._pageNumber, page_count))

class PrinterTripStages:
	def __init__(self, buffer, pagesize):
		self.buffer = buffer
		if pagesize == 'A4':
			self.pagesize = A4
		elif pagesize == 'Letter':
			self.pagesize = letter
		elif pagesize == 'Landscape':
			self.pagesize = landscape

	@staticmethod
	def _header_footer(canvas, doc):
		# Save the state of our canvas so we can draw on it
		canvas.saveState()
		style = getSampleStyleSheet()
		style.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

		# Header
		header = Paragraph('List of Trip Stages', style['centered'])
		w, h = header.wrap(doc.width, doc.topMargin)
		header.drawOn(canvas, doc.leftMargin, doc.height + doc.bottomMargin + doc.topMargin - h * 2)

		# Footer
		footer = Paragraph('', style['Normal'])
		w, h = footer.wrap(doc.width, doc.bottomMargin)
		footer.drawOn(canvas, doc.leftMargin, h)

		# Release the canvas
		canvas.restoreState()

	def print_db(self):
		buffer = self.buffer
		doc = SimpleDocTemplate(buffer,
								rightMargin= 20 * mm,
								leftMargin= 20 * mm,
								topMargin= 20 * mm,
								bottomMargin= 30 * mm,
								pagesize=self.pagesize)
		
		# Container for 'Flowable' objects
		elements = []

		# A large collection of style sheets pre-made for us
		style = getSampleStyleSheet()
		style.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

		# Draw things on the PDF. Here's where the PDF generation happens.
		elements.append(Paragraph('Trip Stages', style['Heading1']))
		for o in TripStage.objects.all():
			elements.append(Paragraph(o.stage_name, style['Normal']))

		headings = ('Stage', 'Massif', 'Distance', 'Duration', 'Localisation')
		trip_stages = []
		for o in TripStage.objects.order_by('distance','massif'):
			# Add a row to the table
			trip_stages.append([o.stage_name, o.massif, o.distance, o.duration, str(o.geom.coords)])
		# Create the table
		trip_stages_table = Table([headings] + trip_stages)
		trip_stages_table.setStyle(TableStyle([
			('BACKGROUND', (0, 0), (-1, 0), colors.black),
			('TEXTCOLOR',(0,0),(-1,0), colors.white),
			('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
			('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
		elements.append(trip_stages_table)

		doc.build(elements, onFirstPage=self._header_footer, onLaterPages=self._header_footer, canvasmaker=NumberedCanvas)

		# Get the value of the BytesIO buffer and write it to the response.
		pdf = buffer.getvalue()
		buffer.close()
		return pdf


class PrinterTrips:
	def __init__(self, buffer, pagesize):
		self.buffer = buffer
		if pagesize == 'A4':
			self.pagesize = A4
		elif pagesize == 'Letter':
			self.pagesize = letter
		elif pagesize == 'Landscape':
			self.pagesize = landscape

	@staticmethod
	def _header_footer(canvas, doc):
		# Save the state of our canvas so we can draw on it
		canvas.saveState()
		style = getSampleStyleSheet()
		style.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

		# Header
		header = Paragraph('List of Trips', style['centered'])
		w, h = header.wrap(doc.width, doc.topMargin)
		header.drawOn(canvas, doc.leftMargin, doc.height + doc.bottomMargin + doc.topMargin - h * 2)

		# Footer
		footer = Paragraph('', style['Normal'])
		w, h = footer.wrap(doc.width, doc.bottomMargin)
		footer.drawOn(canvas, doc.leftMargin, h)

		# Release the canvas
		canvas.restoreState()

	def print_db(self):
		buffer = self.buffer
		doc = SimpleDocTemplate(buffer,
								rightMargin= 20 * mm,
								leftMargin= 20 * mm,
								topMargin= 20 * mm,
								bottomMargin= 30 * mm,
								pagesize=self.pagesize)

		# Container for 'Flowable' objects
		elements = []

		# A large collection of style sheets pre-made for us
		style = getSampleStyleSheet()
		style.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

		# Draw things on the PDF. Here's where the PDF generation happens.
		elements.append(Paragraph('Trips', style['Heading1']))
		for o in Trip.objects.all():
			elements.append(Paragraph(o.trip_name, style['Normal']))

		headings = ('Trip', 'Duration', 'Start date', 'End date', 'Stages','Localisation')
		trips = []
		for o in Trip.objects.order_by('start_date'):
			# Add a row to the table
			trips.append([o.trip_name, o.nbr_of_days(), o.start_date, o.end_date, o.tripstage_set.all(), str(o.geom.coords)])
		# Create the table
		trips_table = Table([headings] + trips)
		trips_table.setStyle(TableStyle([
			('BACKGROUND', (0, 0), (-1, 0), colors.black),
			('TEXTCOLOR',(0,0),(-1,0), colors.white),
			('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
			('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
		elements.append(trips_table)

		doc.build(elements, onFirstPage=self._header_footer, onLaterPages=self._header_footer, canvasmaker=NumberedCanvas)

		# Get the value of the BytesIO buffer and write it to the response.
		pdf = buffer.getvalue()
		buffer.close()
		return pdf