import xlwings as xw

wb = xw.Book()  # Ouvre un nouveau fichier Excel
sheet = wb.sheets[0]
sheet.range("A1").value = "Hello depuis Python 🚀"

print("✅ xlwings fonctionne !")
