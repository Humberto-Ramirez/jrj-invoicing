import os

from jrj_invoicing.core.config import settings
from jrj_invoicing.utils.PDF import PDF


def is_odd(no_row: int) -> int:
    #  if (num % 2) == 0: print (“The number is even”) else: print (“The provided number is odd”)
    if (no_row % 2) == 0:
        # The number is even
        return 0
    else:
        # The number is odd
        return 1


class Reporting:

    async def create_invoice_report(self, invoice_id: int) -> str:
        path = f'{settings.REPORTS_DIR}/invoice_{invoice_id}.pdf'
        pdf = PDF()
        # pdf.add_page()
        pdf.set_title("JRJ-INVOICING!")
        pdf.print_header(str(invoice_id))
        # Table Header
        self.create_table_block(pdf, 0)
        self.create_table_block(pdf, 1)
        self.create_table_block(pdf, 0)
        self.create_table_block(pdf, 1)
        self.create_table_block(pdf, 0)
        pdf.ln(10)
        # two blank lines
        pdf.cell(0, 6, '', 0, 1, 'C', 1)
        pdf.cell(0, 6, '', 0, 1, 'C', 0)
        # Grand total
        pdf.set_font('Arial', size=22)
        # pdf.set_text_color(102, 102, 102)
        pdf.cell(91, 10, 'GRAND TOTAL: ', 0, 0, 'R', 1)
        pdf.cell(56, 10, '', 0, 1, 'L', 1)

        pdf.output(path, 'F')
        return path

    @staticmethod
    def create_table_block(pdf, first_row: int):
        fill_row = is_odd(first_row)
        # Table Header
        pdf.set_text_color(42, 57, 144)
        pdf.set_font('Arial', 'B', 11.5)
        pdf.cell(69.5, 6, 'Address:', 0, 0, 'L', fill_row)
        pdf.cell(21.5, 6, 'Amount', 0, 0, 'R', fill_row)
        pdf.cell(28, 6, 'Unit price', 0, 0, 'R', fill_row)
        pdf.cell(28, 6, 'Total price', 0, 1, 'R', fill_row)

        # SKU 001
        pdf.set_font('Arial', size=10)
        pdf.set_fill_color(243, 243, 243)
        pdf.set_text_color(0, 0, 0)
        pdf.set_draw_color(0, 0, 0)
        pdf.set_line_width(0.3)
        fill_row = is_odd(first_row + 1)
        pdf.cell(69.5, 6, '6/12 pitch and under', 0, 0, 'L', fill_row)
        pdf.cell(21.5, 6, '', 1, 0, 'R', fill_row)
        pdf.set_text_color(102, 102, 102)
        pdf.cell(28, 6, '$75.00', 0, 0, 'R', fill_row)
        pdf.cell(28, 6, '$0.00', 0, 1, 'R', fill_row)
        pdf.set_text_color(0, 0, 0)

        # SKU 002
        fill_row = is_odd(first_row + 2)
        pdf.cell(69.5, 6, '7/12 - 8/12 pitch', 0, 0, 'L', fill_row)
        pdf.cell(21.5, 6, '', 1, 0, 'R', fill_row)
        pdf.set_text_color(102, 102, 102)
        pdf.cell(28, 6, '$80.00', 0, 0, 'R', fill_row)
        pdf.cell(28, 6, '$0.00', 0, 1, 'R', fill_row)
        pdf.set_text_color(0, 0, 0)

        # SKU 003
        fill_row = is_odd(first_row + 3)
        pdf.cell(69.5, 6, '9/12 - 10/12 pitch', 0, 0, 'L', fill_row)
        pdf.cell(21.5, 6, '', 1, 0, 'R', fill_row)
        pdf.set_text_color(102, 102, 102)
        pdf.cell(28, 6, '$85.00', 0, 0, 'R', fill_row)
        pdf.cell(28, 6, '$0.00', 0, 1, 'R', fill_row)

        # SKI 004
        fill_row = is_odd(first_row + 4)
        pdf.cell(69.5, 6, '11/12 - 12/12 pitch', 0, 0, 'L', fill_row)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(21.5, 6, '', 1, 0, 'R', fill_row)
        pdf.set_text_color(102, 102, 102)
        pdf.cell(28, 6, '$90.00', 0, 0, 'R', fill_row)
        pdf.cell(28, 6, '$0.00', 0, 1, 'R', fill_row)

        # SKU 005
        fill_row = is_odd(first_row + 5)
        pdf.cell(69.5, 6, '13/12 +', 0, 0, 'L', fill_row)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(21.5, 6, '', 1, 0, 'R', fill_row)
        pdf.set_text_color(102, 102, 102)
        pdf.cell(28, 6, 'negotiable', 0, 0, 'R', fill_row)
        pdf.cell(28, 6, '', 0, 1, 'R', fill_row)
        pdf.set_text_color(0, 0, 0)

        # SKU 006
        fill_row = is_odd(first_row + 6)
        pdf.cell(69.5, 6, 'OSB', 0, 0, 'L', fill_row)
        pdf.cell(21.5, 6, '', 1, 0, 'R', fill_row)
        pdf.set_text_color(102, 102, 102)
        pdf.cell(28, 6, '$20.00', 0, 0, 'R', fill_row)
        pdf.cell(28, 6, '$0.00', 0, 1, 'R', fill_row)
        pdf.set_text_color(0, 0, 0)

        # SKU 007
        fill_row = is_odd(first_row + 7)
        pdf.cell(69.5, 6, 'Chimney (Small)', 0, 0, 'L', fill_row)
        pdf.cell(21.5, 6, '', 1, 0, 'R', fill_row)
        pdf.set_text_color(102, 102, 102)
        pdf.cell(28, 6, '$75.00', 0, 0, 'R', fill_row)
        pdf.cell(28, 6, '$0.00', 0, 1, 'R', fill_row)
        pdf.set_text_color(0, 0, 0)

        # SKU 008
        fill_row = is_odd(first_row + 8)
        pdf.cell(69.5, 6, 'Chimney (Large)', 0, 0, 'L', fill_row)
        pdf.cell(21.5, 6, '', 1, 0, 'R', fill_row)
        pdf.set_text_color(102, 102, 102)
        pdf.cell(28, 6, '$125.00', 0, 0, 'R', fill_row)
        pdf.cell(28, 6, '$0.00', 0, 1, 'R', fill_row)
        pdf.set_text_color(0, 0, 0)

        # SKU 009
        fill_row = is_odd(first_row + 9)
        pdf.cell(69.5, 6, 'Step Flashing @ $3 per foot', 0, 0, 'L', fill_row)
        pdf.cell(21.5, 6, '', 1, 0, 'R', fill_row)
        pdf.set_text_color(102, 102, 102)
        pdf.cell(28, 6, '$3.00', 0, 0, 'R', fill_row)
        pdf.cell(28, 6, '$0.00', 0, 1, 'R', fill_row)
        pdf.set_text_color(0, 0, 0)

        # SKU 010
        fill_row = is_odd(first_row + 10)
        pdf.cell(69.5, 6, 'Cricket', 0, 0, 'L', fill_row)
        pdf.cell(21.5, 6, '', 1, 0, 'R', fill_row)
        pdf.set_text_color(102, 102, 102)
        pdf.cell(28, 6, '$85.00', 0, 0, 'R', fill_row)
        pdf.cell(28, 6, '$0.00', 0, 1, 'R', fill_row)
        pdf.set_text_color(0, 0, 0)

        # Line ending
        fill_row = is_odd(first_row + 11)
        pdf.set_font('Arial', size=11.5)
        pdf.cell(0, 6, '_____________________________________________________________', 0, 1, 'C', fill_row)

        # Total
        fill_row = is_odd(first_row + 12)
        pdf.cell(69.5, 6, '', 0, 0, 'L', fill_row)
        pdf.cell(21.5, 6, '', 0, 0, 'R', fill_row)
        pdf.set_text_color(102, 102, 102)
        pdf.set_font('Arial', style='B', size=11.5)
        pdf.cell(28, 6, 'TOTAL:', 0, 0, 'L', fill_row)
        pdf.set_font('Arial', size=10)
        pdf.cell(28, 6, '$0.00', 0, 1, 'R', fill_row)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Arial', style='B', size=11.5)

        # two blank lines
        fill_row = is_odd(first_row + 13)
        pdf.cell(0, 6, '', 0, 1, 'C', fill_row)
        fill_row = is_odd(first_row + 14)
        pdf.cell(0, 6, '', 0, 1, 'C', fill_row)

    @staticmethod
    def create_path(path: str) -> None:
        """
        Crea una ruta si no existe
        :param path: Ruta a crear
        """
        os.makedirs(path, exist_ok=True)
