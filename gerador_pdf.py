from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT


#====================gerador de dpf=========================================
def gerar_pdf(dados):
  arquivo = "Contrato.pdf"

  documento = SimpleDocTemplate(
    arquivo,
    pagesize=A4,
    rightMargin=57,
    leftMargin=50,
    topMargin=50,
    bottomMargin=50
  )

  estilos =getSampleStyleSheet()

  for estilo in estilos.byName.values():
    estilo.alignment = TA_LEFT


  conteudo = []


  def texto(texto):
        conteudo.append(
            Paragraph(texto, estilos["Normal"])
        )
        conteudo.append(Spacer(1, 8))

  def titulo(texto):
        conteudo.append(
            Paragraph(texto, estilos["Heading2"])
        )
        conteudo.append(Spacer(1, 10))


   
  conteudo.append(
        Paragraph(
            "CONTRATO DE ADESÃO E PRESTAÇÃO DE SERVIÇOS DE ASSOCIAÇÃO AO CLUBE ALÔ CAMPINAS E REGIÃO",
            estilos["Title"]
        )
    )


  conteudo.append(
        Paragraph(
            "Pelo presente instrumento particular, de um lado:",
            estilos["Normal"]
        )
    )
  
  conteudo.append(Spacer(1, 8))


  conteudo.append(
        Paragraph(
            "I - DAS PARTES",
            estilos["Heading2"]
        )
    )

  conteudo.append(Spacer(1, 8))

  conteudo.append(
        Paragraph(
            "1. CONTRATANTE-ASSOCIADO",
            estilos["Heading3"]
        )
    )

  conteudo.append(Spacer(1, 8))

  conteudo.append(
      Paragraph(
          "Pessoa física:",
          estilos["Heading3"]
        )
  )

#=============CAMPOS 1=================

  conteudo.append(
    Paragraph(
        f"Nome completo: <b>{dados['nome_completo']}</b>",
        estilos["Normal"]
    )
)

  conteudo.append(Spacer(1, 8))

  conteudo.append(
    Paragraph(
        f"RG: <b>{dados['rg']}</b>",
        estilos["Normal"]
    )
   )

  conteudo.append(Spacer(1, 8))

  conteudo.append(
    Paragraph(
        f"CPF: <b>{dados['cpf']}</b>",
        estilos["Normal"]
    )
  )

  conteudo.append(Spacer(1, 8))

  conteudo.append(
    Paragraph(
        f"Cidade/UF: <b>{dados['cidade_uf']}</b>",
        estilos["Normal"]
    )
  )

  conteudo.append(Spacer(1, 8))

  conteudo.append(
    Paragraph(
        f"E-mail: <b>{dados['email']}</b>",
        estilos["Normal"]
    )
)

  conteudo.append(Spacer(1, 8))

  conteudo.append(
    Paragraph(
        f"Telefone/WhatsApp: <b>{dados['contato']}</b>",
        estilos["Normal"]
    )
)
#================================================================


  documento.build(conteudo)
