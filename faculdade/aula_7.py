#criando PDF

from reportlab.pdfgen import canvas #biblioteca de uso 

def generatePDF(lista): 
    try:
        nome_pdf = input('informe o nome do pdf: ') # guardando nome na variavel
        pdf =   canvas.Canvas('{}.pdf'.format(nome_pdf)) #criando arquivo em pdf
        pdf = canvas.Canvas(r'C:\Users\second\Desktop\atvFS.pdf') #definindo local de salvar o arquivo
        x = 720
        for nome, idade in lista.items(): #funçao for para colocar o nome e a idade no arquivo
            x -=20
            pdf.drawString(250, x, '{}:{}'.format(nome, idade))# escreva no pdf

        pdf.setTitle(nome_pdf) #------------------------formataçao de texto
        pdf.setFont("Helvetica", 18)#-------------------formataçao de texto
        pdf.drawString(245,750, 'lista clientes')#------formataçao de texto
        pdf.drawString(245,725, "primeiro da lista")#---formataçao de texto
        pdf.save()# salvar arquivo 
        print('{}.pdf criando com sucesso'.format(nome_pdf))#msg se o aquivo foi criado

    except:
        print("chora e reza")# msg se criaçao do arquivo der errado

lista = {'leonardo': '19', 'bruno': '19', 'joao': '20', 'tays': '19', 'arthur': '19'} #lista para usar na funçao

generatePDF(lista) #mandar lista para funçao
