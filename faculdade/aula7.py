from reportlab.pdfgen import canvas

def generatePDF(lista):
    try:
        nome_pdf = input('informe o nome do pdf: ')
        pdf =   canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 720
        for nome, idade in lista.items():
            x -=20
            pdf.drawString(250, x, '{}:{}'.format(nome, idade))

        pdf.setTitle(nome_pdf)
        #pdf.setFont("Helvetica", 18)
        #pdf.drawString(245,750, 'lista clientes')
        #pdf.setFont("Helvetica-bold", 20)
        #pdf.drawString(245,725, "primeiro da lista")
        pdf.save()
        print('{}.pdf criando com sucesso'.format(nome_pdf))

    except:
        print("chora e reza")

lista = {'leonardo': '19', 'bruno': '19', 'joao': '20', 'tays': '19'}

generatePDF(lista)
