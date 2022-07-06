from flask import Blueprint, request, jsonify, render_template
from openpyxl import Workbook
import openpyxl
  

princi= Blueprint('princi',__name__, template_folder='../../templates')

def escribir(iden):
    try:
        hoja = Workbook()
        sheet = hoja.active
        sheet['A1'] = iden      
        hoja.save('C:\\Users\\acer\\Escritorio\\Proyectos-personales\\cineworld\\src\\data\\dato.xlsx')
        return 0
    except Exception as e:
        print(e)
        return -1
       

def leer():
    book = openpyxl.load_workbook('C:\\Users\\acer\\Escritorio\\Proyectos-personales\\cineworld\\src\\data\\dato.xlsx')
    libro = book.active
    usuario = libro['A1']
    return usuario.value


