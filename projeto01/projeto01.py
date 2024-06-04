from fpdf import FPDF

projeto = input("Digite a descrição do projeto: ")
horas_estimadas = input("Digite quantas horas vc preve pra terminar: ")
valor_hora = input("Qual preço da hora de trabalho?: ")
prazo = input("Qual prazo estimado pra finalizar?: ")

valor_total = int(horas_estimadas) * int(valor_hora)

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")

pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)




pdf.output("Orçamenmto.pdf")