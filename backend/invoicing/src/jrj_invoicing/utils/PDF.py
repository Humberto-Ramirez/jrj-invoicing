from fpdf import FPDF
from loguru import logger

title = "JRJ Invoicing"


class PDF(FPDF):
	def chapter_title(self, num:str):
		mlw = 2
		sw_border = 0
		# sw_border = 1
		self.set_margins(25.4, 20, 37)
		self.set_font("Arial", size=13.5)
		self.set_draw_color(40, 50, 162)
		self.set_text_color(109, 100, 232)
		self.set_line_width(2.3)
		self.line(18.5, 19, self.w - 18.5, 19)
		self.ln(15)
		ibc = "Integrity Building Companies"
		logger.info(f"X: {self.get_x()}")
		logger.info(f"Y: {self.get_y()}")
		ibc_w = self.get_string_width(ibc)
		# Company Name
		self.cell((ibc_w + mlw), 6, ibc, sw_border, 1, 'L')
		ibc_address = "1213 Culbreth Drive #444"
		self.set_text_color(102, 102, 102)
		self.set_font_size(9.5)
		ibc_address_w = self.get_string_width(ibc_address)
		# Address
		self.cell((ibc_address_w + mlw), 5, ibc_address, sw_border, 1, 'L')
		ibc_city = "Wilmington, NC 28405"
		ibc_city_w = self.get_string_width(ibc_city)
		# City
		self.cell((ibc_city_w + mlw), 5, ibc_city, sw_border, 1, 'L')
		# self.cell(0, 6, '', 0, 1, 'C', 0)
		ivc_no = "Invoice #"
		ivc_no_w = self.get_string_width(ivc_no)
		self.set_line_width(0.3)
		self.ln(8)
		self.set_x((105 + ivc_no_w))
		self.set_draw_color(0, 0, 0)
		# Invoice No Label
		self.cell((ivc_no_w * 2), 6.6, ivc_no, 0, ln=0, align='L')
		# Invoice No Frame
		self.cell(28, 6.6, num, 1, 1, 'C')
		self.ln(10)
		self.cell(0, 6, '', 0, 1, 'C', 0)

	def print_header(self, num):
		self.add_page()
		self.chapter_title(num)





