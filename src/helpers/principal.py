from flask import Blueprint, request, jsonify, render_template
from openpyxl import Workbook
import openpyxl
  

princi= Blueprint('princi',__name__, template_folder='../../templates')

def escribir(iden):
    try:
        hoja = Workbook()
        sheet = hoja.active
        sheet['A1'] = iden      
        hoja.save('src/data/dato.xlsx')
        return 0
    except Exception as e:
        print(e)
        return -1
       

def leer():
    book = openpyxl.load_workbook('src/data/dato.xlsx')
    libro = book.active
    usuario = libro['A1']
    return usuario.value

def delete():
    try:
        hoja = Workbook()
        sheet = hoja.active
        sheet.delete_cols(1)     
        hoja.save('src/data/dato.xlsx')
        return 0
    except Exception as e:
        print(e, "Intento fallido")
        return -1

