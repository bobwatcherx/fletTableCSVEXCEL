from flet import *

# NOW IMPORT EXCEL TO DATATBEL EASY
from simpledt import ExcelDataTable,CSVDataTable,SQLDataTable

def main(page:Page):
	page.scroll = "auto"

	# FIRST GET EXCEL TABLE THEN INSERT TOTABLE
	df = ExcelDataTable("percontohan2.xlsx")
	# YOU FILE EXCEL NAME
	myexcel = df.datatable
	# THIS SCRIPT FOR SCROLL HORIZONTAL THE TABLE 
	excel_res = Row([myexcel],scroll="always")

	# ===========================================
	# CSV
	csv = CSVDataTable("dataset.csv")
	xx = csv.datatable
	csv_res = Row([xx],scroll="always")

	# =============================================
	# SQLITE
	sql = SQLDataTable("sqlite","db/dbfood.db",statement="select * from mainan")
	mytable = sql.datatable
	sql_res = Row([mytable],scroll="always")



	page.add(
	Column([
	Text("GET FROM EXCEL FILE",size=30),
	excel_res,

	# NOW GET FROM CSV FILE AND INSERT TO datatable
	# I WANT TO DOWNLOAD THE FILE CSV
	Text("GET FROM CSV FILE",size=30),
	csv_res,

	# NOW I WANT GET DATA FROM SQLITE TABLE AND PUSH 
	# ALL DATA FROM TABLE TO DATATTABLE

	# NOW I CREATE TABLE SQLITE 
	Text("GET FROM SQLITE FILE",size=30),
	sql_res,

		])

	)

flet.app(target=main)
