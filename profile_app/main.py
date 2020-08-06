import yaml
import pprint
import gspread

gc = gspread.service_account()

sh = gc.open_by_key("1DsLMLkxUQMem5moWIDz2-aVG2rz5BkjgzQ_rSzwUwpc")

worksheet_list = sh.worksheets()


exit

