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

    

  def subtitulo(texto):
    conteudo.append(
        Paragraph(texto, estilos["Heading3"])
    )
    conteudo.append(Spacer(1, 8))


  def subtitulo_menor(texto):
    conteudo.append(
        Paragraph(texto, estilos["Normal"])
    )
    conteudo.append(Spacer(1, 6))


  def campo(nome, valor):
    conteudo.append(
        Paragraph(
            f"{nome}: <b>{valor}</b>",
            estilos["Normal"]
        )
    )
    conteudo.append(Spacer(1, 8))


#==================parte inicial==================================
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
#======================================================



#=============CAMPOS 1=================

  conteudo.append(
    Paragraph(
        f"<b>Nome completo:</b>{dados['nome_completo']}",
        estilos["Normal"]
    )
)

  conteudo.append(Spacer(1, 8))

  conteudo.append(
    Paragraph(
        f"<b>RG:</b>{dados['rg']}",
        estilos["Normal"]
    )
   )

  conteudo.append(Spacer(1, 8))

  conteudo.append(
    Paragraph(
        f" <b>CPF:</b>{dados['cpf']}",
        estilos["Normal"]
    )
  )

  conteudo.append(Spacer(1, 8))

  conteudo.append(
    Paragraph(
        f" <b>Cidade/UF:</b>{dados['cidade_uf']}",
        estilos["Normal"]
    )
  )

  conteudo.append(Spacer(1, 8))

  conteudo.append(
    Paragraph(
        f" <b>E-mail:</b>{dados['email']}",
        estilos["Normal"]
    )
)

  conteudo.append(Spacer(1, 8))

  conteudo.append(
    Paragraph(
        f" <b>Telefone/WhatsApp:</b>{dados['contato']}",
        estilos["Normal"]
    )
)
  conteudo.append(Spacer(1, 8))
#================================================================


#=================CAMPOS2============================
  conteudo.append(
           Paragraph(
               "Pessoa Jurídica: ",
               estilos["Heading3"]
           )
       )
   
  conteudo.append(
    Paragraph(
        f" <b>Razão Social:</b>{dados['razao_social']}",
        estilos["Normal"]
    )
)
  conteudo.append(Spacer(1, 8))

  conteudo.append(
    Paragraph(
        f"<b>Nome Fantasia:</b>{dados['nome_fantasia']}",
        estilos["Normal"]
    )
)
  conteudo.append(Spacer(1, 8))

  conteudo.append(
    Paragraph(
        f" <b>CNPJ:</b>{dados['cnpj']}",
        estilos["Normal"]
    )
)
  conteudo.append(Spacer(1, 8))

  conteudo.append(
    Paragraph(
        f"<b>Representante Legal:</b>{dados['representante_legal']}",
        estilos["Normal"]
    )
)
  conteudo.append(Spacer(1, 8))

  conteudo.append(
    Paragraph(
        f" <b>CPF do Representante:</b>{dados['cpf_representante']}",
        estilos["Normal"]
    )
)
  conteudo.append(Spacer(1, 8))

  conteudo.append(
    Paragraph(
        f" <b>RG do Representante:</b>{dados['rg_representante']}",
        estilos["Normal"]
    )
)
  conteudo.append(Spacer(1, 8))

  conteudo.append(
    Paragraph(
        f"<b>Cidade/UF:</b>{dados['cidade_uf2']}",
        estilos["Normal"]
    )
  )
  conteudo.append(Spacer(1, 8))

  conteudo.append(
    Paragraph(
        f" <b>E-mail:</b>{dados['email_juridica']}",
        estilos["Normal"]
    )
)
  conteudo.append(Spacer(1, 8))

  conteudo.append(
    Paragraph(
        f"<b> Telefone/WhatsApp:</b>{dados['telefone_juridica']}",
        estilos["Normal"]
    )
)
#====================================================

  conteudo.append(Spacer(1, 8))
  conteudo.append(Spacer(1, 8))
  

  texto(
     "Doravante denominado simplesmente "
     "<b>ASSOCIADO</b> ou <b>CONTRATANTE</b>."
   )

#====================2.CONTRATADA============================

  subtitulo("2. CONTRATADA")

  texto(
    "CLUBE ALÔ CAMPINAS E REGIÃO, pessoa jurídica de direito privado, "
    "inscrita no CNPJ sob nº "
    "<b>55.633.392/0001-18</b>, "
    "com sede/endereço em "
    "<b>R: Antônio Lapa, 280 - Cambuí, Campinas - SP 13025-240</b>, "
    "neste ato representada na forma de seu Contrato Social/Estatuto, "
    "por seu representante legal, doravante denominada simplesmente "
    "<b>CLUBE</b> ou <b>CONTRATADA</b>."
  )

  texto(
    "CLUBE e ASSOCIADO, quando mencionados conjuntamente, "
    "serão denominados <b>PARTES</b>."
   )

#================================================================



# ==============================
# CLÁUSULA 1ª - DO OBJETO
# ==============================

  titulo("CLÁUSULA 1ª - DO OBJETO")

  texto(
        "1.1. O presente instrumento tem por objeto a adesão do CONTRATANTE "
        "ao Clube <b>Alô Campinas e Região</b>, mediante contratação do "
        "Plano Anual de Associação, compreendendo o acesso aos benefícios, "
        "canais, conteúdos, atividades e serviços descritos neste contrato."
    )

  texto(
        "1.2. A associação tem por finalidade fomentar o desenvolvimento "
        "pessoal e empresarial dos associados por meio de networking estruturado, "
        "acesso a conhecimento, troca de experiências, divulgação institucional, "
        "aproximação entre empresas e profissionais e geração de oportunidades "
        "de relacionamento e negócios."
    )

  texto(
        "1.3. A associação não constitui promessa ou garantia de geração de "
        "negócios, vendas, faturamento, lucro, clientes, contratos ou qualquer "
        "resultado econômico específico."
    )

  texto(
        "1.4. Os resultados eventualmente obtidos pelo ASSOCIADO dependerão, "
        "entre outros fatores, de sua participação, relacionamento, capacidade "
        "comercial, atuação profissional e utilização dos recursos disponibilizados "
        "pelo CLUBE."
    )

  texto(
        "1.5. O CLUBE obriga-se a disponibilizar os benefícios e serviços "
        "previstos neste instrumento, observadas as condições, limitações, "
        "disponibilidade, calendário e regras aplicáveis a cada atividade."
    )
#=================================================================================



# ==============================
# CLÁUSULA 2ª - DOS PLANOS, BENEFÍCIOS E ACESSOS
# ==============================

  titulo("CLÁUSULA 2ª – DOS PLANOS, BENEFÍCIOS E ACESSOS")

  texto(
    "2.1. O ASSOCIADO declara que, no ato da contratação, escolheu uma "
    "das modalidades de associação abaixo, ficando o plano escolhido "
    "expressamente indicado no Quadro Resumo da Contratação deste instrumento."
)

  texto(
    "<b>PLANO CONEXÃO – R$ 1.490,00</b> "
    "(mil quatrocentos e noventa reais) por ano, ou 12 (doze) parcelas "
    "de R$ 149,00 (cento e quarenta e nove reais), totalizando R$ 1.788,00 "
    "(mil setecentos e oitenta e oito reais) no parcelamento."
)

  texto(
    "Destinado ao associado que deseja ingressar no ecossistema do CLUBE, "
    "ampliar relacionamentos e gerar novas conexões."
)

  texto("<b>Inclui:</b>")

  texto(
    "a) acesso à estrutura digital disponibilizada pelo CLUBE;"
)

  texto(
    "b) acesso ao site oficial do Clube Alô Campinas e Região;"
)

  texto(
    "c) acesso aos canais oficiais de comunicação do CLUBE, inclusive grupos "
    "e canais destinados aos associados, conforme a modalidade disponibilizada;"
)

  texto(
    "d) participação nas ações de networking, encontros e demais atividades "
    "disponibilizadas aos associados, observadas as condições específicas de cada atividade;"
)

  texto(
    "e) certificado de associado;"
)

  texto(
    "f) selo de Empresa Associada, quando aplicável;"
)

  texto(
    "g) acesso aos benefícios gerais do CLUBE que sejam expressamente "
    "disponibilizados a todos os associados;"
)

  texto(
    "h) demais benefícios gerais expressamente divulgados pelo CLUBE durante "
    "a vigência da associação."
)


  texto(
    "<b>2.2. PLANO NETWORKING – R$ 2.490,00</b> "
    "(dois mil quatrocentos e noventa reais) por ano, ou 12 (doze) parcelas "
    "de R$ 249,00 (duzentos e quarenta e nove reais), totalizando R$ 2.988,00 "
    "(dois mil novecentos e oitenta e oito reais) no parcelamento."
)

  texto(
    "Destinado ao associado que busca maior presença, relacionamento "
    "estratégico e oportunidades de negócios."
)

  texto(
    "Além dos benefícios gerais previstos no Plano Conexão, inclui:"
)

  texto(
    "a) 2 (duas) matérias por ano no Portal Alô Campinas e Região, conforme "
    "critérios editoriais, disponibilidade de agenda e materiais fornecidos pelo ASSOCIADO;"
)

  texto(
    "b) 5 (cinco) Stories por ano no perfil oficial @alocampinaseregiao, "
    "mediante fornecimento de material adequado pelo ASSOCIADO;"
)

  texto(
    "c) acesso ao Clube de Desconto Alô Campinas e Região, na condição e "
    "nos termos aplicáveis ao ASSOCIADO;"
)

  texto(
    "d) demais benefícios expressamente previstos na proposta comercial ou neste contrato."
)


  texto(
    "<b>2.3. PLANO ECOSSISTEMA – R$ 4.990,00</b> "
    "(quatro mil novecentos e noventa reais) por ano, ou 12 (doze) parcelas "
    "de R$ 499,00 (quatrocentos e noventa e nove reais), totalizando "
    "R$ 5.988,00 (cinco mil novecentos e oitenta e oito reais) no parcelamento."
)

  texto(
    "Destinado ao associado que deseja maior exposição, proximidade e "
    "participação estratégica dentro do CLUBE."
)

  texto(
    "Além dos benefícios gerais previstos no Plano Conexão, inclui:"
)

  texto(
    "a) 12 (doze) matérias por ano no Portal Alô Campinas e Região, "
    "correspondentes, em regra, a 1 (uma) matéria por mês, conforme critérios "
    "editoriais, disponibilidade de agenda e materiais fornecidos pelo ASSOCIADO;"
)

  texto(
    "b) 3 (três) vídeos profissionais por ano, observadas as condições de "
    "produção, captação, agenda e formato previamente definidos entre as PARTES;"
)

  texto(
    "c) 2 (dois) Reels em formato Collab por ano, sujeitos à disponibilidade "
    "e às regras das respectivas plataformas;"
)

  texto(
    "d) 48 (quarenta e oito) Stories por ano, correspondentes, em regra, a "
    "1 (um) Story por semana, mediante fornecimento de material adequado ou "
    "conforme produção previamente acordada;"
)

  texto(
    "e) 1 (uma) participação em Podcast ou Programa, conforme disponibilidade "
    "de agenda, formato e critérios editoriais do CLUBE;"
)

  texto(
    "f) acesso ao Clube de Desconto Alô Campinas e Região, na condição e "
    "nos termos aplicáveis ao ASSOCIADO;"
)
 
  texto(
    "g) demais benefícios expressamente previstos na proposta comercial ou neste contrato."
)


  texto(
    "2.4. Os benefícios de conteúdo, divulgação e produção previstos nos "
    "Planos Networking e Ecossistema são pessoais e vinculados ao ASSOCIADO, "
    "não podendo ser transferidos, vendidos ou cedidos a terceiros sem "
    "autorização prévia e expressa da CONTRATADA."
)

  texto(
    "2.5. As quantidades de matérias, Stories, vídeos, Reels e participações "
    "previstas em cada plano correspondem ao limite anual contratado e não "
    "representam garantia de resultado, alcance, número de visualizações, "
    "leads, clientes, vendas ou qualquer resultado comercial específico."
)

  texto(
    "2.6. As publicações e produções serão realizadas de acordo com "
    "calendário, disponibilidade de agenda, critérios editoriais, formato "
    "das plataformas, disponibilidade de equipe e recebimento tempestivo "
    "dos materiais e informações necessários pelo ASSOCIADO."
)

  texto(
    "2.7. Caso o ASSOCIADO não forneça, em prazo razoável informado pelo "
    "CLUBE, os materiais, informações, aprovações ou disponibilidade "
    "necessários para execução de determinado benefício, a realização poderá "
    "ser remarcada para data posterior, sem transferência automática para "
    "período contratual seguinte."
)

  texto(
    "2.8. Benefícios não utilizados durante a vigência contratual não serão "
    "convertidos automaticamente em dinheiro, desconto, crédito ou abatimento, "
    "salvo se houver acordo escrito em sentido diverso entre as PARTES."
)

  texto(
    "2.9. A participação em eventos, cursos, treinamentos, experiências ou "
    "programas específicos poderá estar sujeita a inscrição prévia, limite "
    "de vagas, disponibilidade, critérios de participação ou pagamento "
    "adicional, quando assim informado previamente."
)

  texto(
    "2.10. O fato de determinada atividade ser divulgada pelo CLUBE não "
    "significa que seu custo esteja necessariamente incluído no valor do "
    "plano contratado."
)

  texto(
    "2.11. Benefícios, descontos, produtos ou serviços oferecidos por "
    "empresas parceiras são de responsabilidade dos respectivos parceiros, "
    "especialmente quanto a preços, condições comerciais, disponibilidade, "
    "qualidade e execução dos serviços contratados diretamente entre parceiro "
    "e ASSOCIADO."
)
#=====================================================================


# ==============================
# CLÁUSULA 3ª – DOS SERVIÇOS DE CONTEÚDO E DIVULGAÇÃO
# ==============================

  titulo("CLÁUSULA 3ª – DOS SERVIÇOS DE CONTEÚDO E DIVULGAÇÃO")

  texto(
    "3.1. Os benefícios de conteúdo e divulgação incluídos nos Planos "
    "Networking e Ecossistema deverão observar o calendário e as condições "
    "de execução definidos pelo CLUBE."
)

  texto(
    "3.2. As matérias do Portal serão produzidas e/ou publicadas conforme "
    "critérios editoriais do Portal Alô Campinas e Região. O ASSOCIADO deverá "
    "fornecer informações, imagens, contatos e demais materiais necessários, "
    "responsabilizando-se pela veracidade e pelos direitos de uso desses conteúdos."
)

  texto(
    "3.3. Os Stories incluídos nos Planos Networking e Ecossistema deverão "
    "ser disponibilizados pelo ASSOCIADO em formato previamente adequado à "
    "publicação, salvo quando houver produção previamente acordada pelo CLUBE."
)

  texto(
    "3.4. Quando o benefício contratado envolver produção de material pelo "
    "CLUBE, a captação, edição, duração, formato, local e demais condições "
    "serão definidos previamente conforme a estrutura e o escopo do plano contratado."
)

  texto(
    "3.5. No Plano Ecossistema, os 3 (três) vídeos profissionais incluídos "
    "correspondem às produções previstas no plano, não abrangendo automaticamente "
    "despesas extraordinárias, tais como deslocamentos especiais, locações, "
    "atores, equipamentos especiais, drone, fotógrafo adicional ou outros "
    "recursos não previstos no escopo originalmente acordado."
)

  texto(
    "3.6. Os 2 (dois) Reels em formato Collab dependem da disponibilidade e "
    "das funcionalidades da plataforma utilizada. O CLUBE não responde por "
    "eventual indisponibilidade, alteração ou limitação técnica da plataforma "
    "de terceiros."
)

  texto(
    "3.7. A participação em Podcast ou Programa prevista no Plano Ecossistema "
    "dependerá de disponibilidade de agenda, formato do programa, critérios "
    "editoriais e condições técnicas da produção."
)

  texto(
    "3.8. Caso o ASSOCIADO solicite produção, adaptação ou criação de materiais "
    "que ultrapassem o escopo expressamente incluído em seu plano, o serviço "
    "adicional poderá ser contratado mediante orçamento e aprovação prévia."
)

  texto(
    "3.9. Na hipótese de contratação adicional de criativo pelo ASSOCIADO, "
    "permanece aplicável o valor de R$ 80,00 (oitenta reais) por criativo "
    "produzido, mediante prévia aprovação."
)

  texto(
    "3.10. Produções de vídeos ou outros serviços que ultrapassem o escopo "
    "do plano poderão ser contratados separadamente, mediante orçamento e "
    "aprovação prévia."
)

  texto(
    "3.11. A publicação de matérias e conteúdos estará sujeita a critérios "
    "editoriais, disponibilidade de agenda e adequação às políticas de "
    "conteúdo do Portal e das plataformas utilizadas."
)

  texto(
    "3.12. O CLUBE poderá recusar material que contenha conteúdo ilícito, "
    "discriminatório, ofensivo, enganoso, difamatório, que viole direitos "
    "de terceiros, propriedade intelectual, normas legais ou políticas das "
    "plataformas."
)
#=====================================================================


# ==============================
#CLÁUSULA 4ª – DAS ATIVIDADES E EVENTOS
# ==============================

  titulo("CLÁUSULA 4ª – DAS ATIVIDADES E EVENTOS")

  texto(
    "4.1. O CLUBE divulgará aos associados os eventos, cursos, treinamentos, "
    "visitas técnicas e demais atividades por meio dos canais oficiais de comunicação."
)

  texto(
    "4.2. A associação não garante a realização de quantidade mínima de eventos, "
    "salvo quando expressamente prevista em proposta comercial, anexo ou instrumento específico."
)

  texto(
    "4.3. Eventos, cursos, treinamentos ou programas poderão ser gratuitos ou "
    "possuir investimento adicional, circunstância que será informada previamente."
)

  texto(
    "4.4. O CLUBE poderá alterar datas, horários, locais, formato ou programação "
    "das atividades por razões operacionais, de segurança, disponibilidade de "
    "palestrantes, parceiros, fornecedores ou circunstâncias alheias à sua vontade, "
    "comunicando os associados pelos canais disponíveis."
)

  texto(
    "4.5. Eventual cancelamento ou alteração de atividade não implica, por si só, "
    "cancelamento da associação ou restituição integral do valor do Plano Anual, "
    "ressalvados os direitos previstos em lei e as condições específicas eventualmente "
    "divulgadas para aquela atividade."
)
#==========================================================================


# ==============================
#CLÁUSULA 5ª – DAS OBRIGAÇÕES DO ASSOCIADO
# ==============================

  titulo("CLÁUSULA 5ª – DAS OBRIGAÇÕES DO ASSOCIADO")

  texto(
    "5.1. Constituem obrigações do ASSOCIADO:"
)

  texto(
    "a) cumprir este contrato e as normas internas do CLUBE;"
)

  texto(
    "b) respeitar as regras de convivência, ética, urbanidade e boa-fé;"
)

  texto(
    "c) manter comportamento compatível com ambiente profissional e de networking;"
)

  texto(
    "d) não praticar atos ofensivos, discriminatórios, fraudulentos, ilícitos "
    "ou que possam causar prejuízo à imagem do CLUBE ou de seus associados;"
)

  texto(
    "e) participar das atividades de forma ética e colaborativa;"
 )

  texto(
    "f) manter seus dados cadastrais atualizados;"
)

  texto(
    "g) preservar seus dados de acesso, senhas e informações de caráter reservado;"
 )

  texto(
    "h) não compartilhar acessos individuais com terceiros;"
)

  texto(
    "i) não utilizar grupos, eventos ou canais do CLUBE para práticas ilícitas, "
    "spam, fraude, divulgação indevida, captação abusiva ou atividades que "
    "contrariem as regras internas;"
)

  texto(
    "j) respeitar a privacidade e os dados pessoais dos demais associados;"
)

  texto(
    "k) responsabilizar-se pela veracidade das informações, imagens, marcas e "
    "conteúdos fornecidos ao CLUBE;"
)

  texto(
    "l) possuir autorização para utilização de conteúdos, imagens, marcas, "
    "textos e demais materiais que encaminhar para publicação."
)

  texto(
    "5.2. O ASSOCIADO responderá pelos prejuízos que causar ao CLUBE ou a "
    "terceiros em razão de conteúdo ilícito ou utilização indevida de materiais "
    "fornecidos por ele, observada a legislação aplicável."
)
#==================================================================

# ==============================
#CLÁUSULA 6ª – DAS OBRIGAÇÕES DO CLUBE
# ==============================

  titulo("CLÁUSULA 6ª – DAS OBRIGAÇÕES DO CLUBE")

  texto(
    "6.1. Constituem obrigações do CLUBE:"
)

  texto(
    "a) disponibilizar os benefícios expressamente previstos neste contrato;"
)

  texto(
    "b) disponibilizar informações sobre eventos e atividades por seus canais oficiais;"
)

  texto(
    "c) liberar os acessos aos grupos e canais destinados aos associados, "
    "observadas as regras de utilização;"
)

  texto(
    "d) manter os canais oficiais de comunicação disponíveis dentro de suas possibilidades técnicas;"
)

  texto(
    "e) prestar informações relativas à associação;"
)

  texto(
    "f) observar a legislação aplicável ao tratamento de dados pessoais;"
)

  texto(
    "g) adotar medidas técnicas e administrativas razoáveis para proteção dos "
    "dados pessoais tratados no âmbito da associação."
)

  texto(
    "6.2. O CLUBE não será responsável por indisponibilidades decorrentes de "
    "falhas de internet, plataformas de terceiros, redes sociais, WhatsApp, "
    "Telegram, serviços de hospedagem, força maior, caso fortuito ou outros "
    "fatores alheios ao seu controle."
 )
#==================================================



# ==============================
#CLÁUSULA 7ª – DO PLANO ANUAL
# ==============================

  titulo("CLÁUSULA 7ª – DO PLANO ANUAL")

  texto(
    "7.1. O CLUBE oferece o PLANO ANUAL DE ASSOCIAÇÃO, "
    "com vigência de 12 (doze) meses."
)

  texto(
    "7.2. O ASSOCIADO reconhece que o produto/serviço contratado "
    "é um plano anual de associação, e que eventual pagamento "
    "parcelado constitui apenas forma de pagamento do preço contratado, "
    "não transformando a contratação em mensalidade independente."
)

  texto(
    "7.3. O ASSOCIADO poderá optar pela forma de pagamento indicada "
    "no quadro financeiro deste contrato."
)
#===============================================================


# ==============================
#CLÁUSULA 8ª – DO VALOR E DA FORMA DE PAGAMENTO
# ==============================



  titulo("CLÁUSULA 8ª – DO VALOR E DA FORMA DE PAGAMENTO")

  texto(
    "8.1. O valor devido pelo ASSOCIADO será aquele correspondente ao "
    "plano escolhido e indicado no Quadro Resumo da Contratação."
)

  texto(
    "8.2. PLANO CONEXÃO: valor anual à vista de R$ 1.490,00 "
    "(mil quatrocentos e noventa reais) ou, na modalidade parcelada "
    "prevista nesta contratação, 12 (doze) parcelas de R$ 149,00 "
    "(cento e quarenta e nove reais), totalizando R$ 1.788,00 "
    "(mil setecentos e oitenta e oito reais)."
)

  texto(
    "8.3. PLANO NETWORKING: valor anual à vista de R$ 2.490,00 "
    "(dois mil quatrocentos e noventa reais) ou, na modalidade "
    "parcelada prevista nesta contratação, 12 (doze) parcelas de "
    " R$ 249,00 (duzentos e quarenta e nove reais), totalizando "
    "R$ 2.988,00 (dois mil novecentos e oitenta e oito reais)."
)

  texto(
    "8.4. PLANO ECOSSISTEMA: valor anual à vista de R$ 4.990,00 "
    "(quatro mil novecentos e noventa reais) ou, na modalidade "
    "parcelada prevista nesta contratação, 12 (doze) parcelas de "
    "R$ 499,00 (quatrocentos e noventa e nove reais), totalizando "
    "R$ 5.988,00 (cinco mil novecentos e oitenta e oito reais)."
)

  texto(
    "8.5. A diferença entre o preço à vista e o preço parcelado "
    "deverá ser apresentada ao ASSOCIADO de maneira clara antes "
    "da contratação, quando houver diferença."
)

  texto(
    "8.6. O pagamento poderá ser realizado por:"
)

  texto("a) PIX;")

  texto("b) dinheiro em espécie;")

  texto(
     "c) cartão de crédito, conforme condições da operadora "
    "e modalidade escolhida;"
)

  texto(
    "d) boleto bancário, quando disponibilizado pelo CLUBE."
)

  texto(
    "8.7. Na hipótese de pagamento por cartão de crédito, eventual "
    "acréscimo decorrente exclusivamente da modalidade de parcelamento "
    "deverá ser informado previamente ao ASSOCIADO."
)

  texto(
    "8.8. Na modalidade de boleto bancário, os vencimentos serão "
    "aqueles constantes dos respectivos boletos emitidos pelo CLUBE "
    "ou por instituição responsável pelo processamento do pagamento."
)

  texto(
    "8.9. Salvo disposição diversa expressamente indicada no Quadro "
    "Resumo da Contratação, o primeiro pagamento deverá ocorrer em "
    "até 7 (sete) dias úteis contados da assinatura deste instrumento."
)

  texto(
    "8.10. O ASSOCIADO declara ter recebido informações suficientes "
    "sobre o preço total contratado, quantidade de parcelas, valor "
    "das parcelas e condições de pagamento."
)
#===========================================================


# ==============================
#CLÁUSULA 9ª – DO REAJUSTE
# ==============================

  titulo("CLÁUSULA 9ª – DO REAJUSTE")

  texto(
    "9.1. Na hipótese de renovação do Plano Anual, o valor poderá ser "
    "reajustado anualmente pela variação acumulada do IGP-M/FGV ou, "
    "na sua impossibilidade, por outro índice oficial que legalmente "
    "o substitua."
   )

  texto(
    "9.2. O reajuste será aplicado somente a períodos contratuais "
    "futuros e será informado ao ASSOCIADO por ocasião da renovação."
)

  texto(
    "9.3. O reajuste não será aplicado retroativamente a períodos já pagos."
)
#=====================================================================


# ==============================
#CLÁUSULA 10ª – DA VIGÊNCIA E RENOVAÇÃO
# ==============================


  titulo("CLÁUSULA 10ª – DA VIGÊNCIA E RENOVAÇÃO")

  texto(
    f"10.1. O presente contrato terá vigência de <b>12 (doze) meses</b>, "
    f"iniciando-se em <b>{dados['data_inicio']}</b> "
    f"e encerrando-se em <b>{dados['data_final']}</b>."
)

  texto(
    "10.2. A associação poderá ser renovada automaticamente por novos "
    "períodos de 12 (doze) meses, caso o ASSOCIADO não manifeste "
    "expressamente sua intenção de não renovação."
)

  texto(
    "10.3. Para evitar a renovação, o ASSOCIADO deverá comunicar sua "
    "intenção ao CLUBE com antecedência mínima de 30 (trinta) dias "
    "do término da vigência."
)

  texto(
    "10.4. A ausência de manifestação não será interpretada como "
    "renúncia a direitos previstos em lei."
)

  texto(
    "10.5. Havendo alteração de preço para o período de renovação, "
    "o ASSOCIADO deverá ser informado previamente."
  )
#=====================================================


# =================================================
#CLÁUSULA 11ª – DO CANCELAMENTO ANTECIPADO E DA MULTA COMPENSATÓRIA 
# ================================================

  titulo("CLÁUSULA 11ª – DO CANCELAMENTO ANTECIPADO E DA MULTA COMPENSATÓRIA")

  texto(
    "11.1. Por se tratar de Plano Anual, o período contratado corresponde "
    "a 12 (doze) meses, independentemente da forma de pagamento escolhida."
)

  texto(
    "11.2. O ASSOCIADO poderá solicitar o cancelamento antecipado mediante "
    "comunicação escrita ao CLUBE."
)

  texto(
    "11.3. Ressalvadas as hipóteses de direito de arrependimento, "
    "descumprimento contratual pela CONTRATADA ou outras situações previstas "
    "em lei, o cancelamento antecipado imotivado pelo ASSOCIADO poderá ensejar "
    "<b>multa compensatória correspondente a 10% (dez por cento) do saldo "
    "das parcelas vincendas</b>, calculada na data do pedido de cancelamento."
)

  texto(
    "11.4. A multa prevista nesta cláusula não será calculada sobre parcelas "
    "já vencidas e pagas."
)

  texto(
    "11.5. As parcelas já vencidas e não pagas permanecerão devidas, "
    "acrescidas dos encargos de mora previstos neste contrato."
)

  texto(
    "11.6. Caso o ASSOCIADO tenha realizado pagamento antecipado de valores "
    "referentes a período ainda não usufruído, eventual restituição será "
    "apurada considerando o período efetivamente prestado, os valores já "
    "utilizados, eventuais serviços adicionais efetivamente contratados e a "
    "multa compensatória aplicável, sempre observada a legislação vigente."
)

  texto(
    "11.7. A multa não será aplicada quando o cancelamento decorrer de "
    "descumprimento contratual comprovado da CONTRATADA que justifique a "
    "rescisão, sem prejuízo dos demais direitos legalmente assegurados."
)

  texto(
    "11.8. Quando a contratação ocorrer fora do estabelecimento comercial, "
    "inclusive por meios eletrônicos ou outras hipóteses abrangidas pela "
    "legislação de defesa do consumidor, será respeitado o direito de "
    "arrependimento legalmente previsto."
  )
#=============================================================


# =================================================
#CLÁUSULA 12ª – DA INADIMPLÊNCIA
# ================================================


  titulo("CLÁUSULA 12ª – DA INADIMPLÊNCIA")

  texto(
    "12.1. O atraso no pagamento de qualquer parcela sujeitará o ASSOCIADO, "
    "observada a legislação aplicável, ao pagamento de:"
)

  texto(
    "a) multa moratória de <b>2% (dois por cento)</b> sobre o valor da "
    "parcela vencida;"
)

  texto(
    "b) juros de mora de <b>1% (um por cento) ao mês,</b> calculados "
    "proporcionalmente aos dias de atraso, quando juridicamente aplicável;"
)

  texto(
    "c) atualização monetária, quando cabível;"
)

  texto(
    "d) demais encargos legalmente permitidos."
)

  texto(
    "12.2. A multa moratória prevista nesta cláusula será limitada ao "
    "máximo permitido pela legislação aplicável."
)

  texto(
    "12.3. Em caso de inadimplência, o CLUBE poderá, após comunicação ao "
    "ASSOCIADO, suspender temporariamente o acesso a benefícios, grupos, "
    "conteúdos, eventos e demais recursos disponibilizados ao associado "
    "enquanto perdurar o débito."
)

  texto(
    "12.4. A inadimplência superior a 30 (trinta) dias poderá ensejar a "
    "rescisão do contrato pela CONTRATADA, mediante comunicação ao ASSOCIADO."
)

  texto(
    "12.5. A rescisão por inadimplência não prejudicará a cobrança dos "
    "valores vencidos e demais encargos legalmente cabíveis."
)

  texto(
    "12.6. O eventual não exercício imediato de qualquer direito pelo CLUBE "
    "não representará renúncia, novação ou alteração contratual."
)
#============================================================


# =================================================
#CLÁUSULA 13ª – DA RESCISÃO POR DESCUMPRIMENTO
# ================================================

  titulo("CLÁUSULA 13ª – DA RESCISÃO POR DESCUMPRIMENTO")

  texto(
    "13.1. O presente contrato poderá ser rescindido por qualquer das PARTES "
    "em caso de descumprimento relevante de obrigação contratual, desde que "
    "a parte responsável seja previamente comunicada e, quando a natureza "
    "da infração permitir, tenha oportunidade razoável de sanar o descumprimento."
)

  texto(
    "13.2. O CLUBE poderá rescindir imediatamente a associação, observada "
    "a legislação aplicável, em situações graves que envolvam:"
)

  texto("a) prática de ato ilícito;")

  texto("b) fraude;")

  texto("c) ameaça ou violência;")

  texto("d) discriminação;")

  texto("e) assédio;")

  texto("f) uso indevido da marca do CLUBE;")

  texto("g) divulgação não autorizada de informações confidenciais;")

  texto("h) compartilhamento indevido de acessos;")

  texto("i) comportamento reiteradamente incompatível com as normas de convivência;")

  texto(
    "j) utilização dos canais do CLUBE para finalidade ilícita ou prejudicial "
    "aos demais associados."
)

  texto(
    "13.3. A rescisão não prejudicará a apuração de valores eventualmente "
    "devidos ou de danos comprovadamente causados."
)
#=============================================================


# =================================================
#CLÁUSULA 14ª – DO USO DE IMAGEM, VOZ E NOME
# ================================================

  titulo("CLÁUSULA 14ª – DO USO DE IMAGEM, VOZ E NOME")

  texto(
    "14.1. O ASSOCIADO poderá autorizar, mediante manifestação específica, "
    "o uso gratuito de sua imagem, voz e nome pelo CLUBE em materiais "
    "institucionais relacionados às atividades do CLUBE, inclusive site, "
    "redes sociais, fotografias, vídeos, eventos e materiais de divulgação."
)

  texto(
    "14.2. A autorização, quando concedida, será limitada à divulgação "
    "institucional e promocional das atividades do CLUBE, não autorizando "
    "utilização que seja ofensiva, difamatória, ilícita ou incompatível "
    "com a finalidade desta autorização."
)

  texto(
    "14.3. A autorização de uso de imagem não constitui cessão de direitos "
    "patrimoniais sobre a imagem, voz ou nome além da finalidade "
    "expressamente autorizada."
)

  texto(
    "14.4. O ASSOCIADO poderá solicitar a interrupção de novas utilizações "
    "futuras de sua imagem mediante comunicação escrita, ressalvadas as "
    "hipóteses em que a manutenção seja necessária para cumprimento de "
    "obrigação legal, exercício regular de direitos ou situações em que "
    "a retirada seja tecnicamente inviável de materiais já produzidos ou "
    "publicados, observada a legislação aplicável."
)

  subtitulo_menor("AUTORIZAÇÃO ESPECÍFICA DE USO DE IMAGEM")


  if dados["autoriza_imagem"]:
    texto(
        "[X] <b>AUTORIZO</b> o uso gratuito da minha imagem, voz e nome "
        "nos termos desta cláusula."
    )
  else:
    texto(
        "[ ] <b>AUTORIZO</b> o uso gratuito da minha imagem, voz e nome "
        "nos termos desta cláusula."
    )

  if dados["nao_autoriza_imagem"]:
    texto(
        "[X] <b>NÃO AUTORIZO</b> o uso da minha imagem, voz e nome para "
        "fins de divulgação institucional, ressalvadas as hipóteses "
        "legalmente permitidas."
    )
  else:
    texto(
        "[ ] <b>NÃO AUTORIZO</b> o uso da minha imagem, voz e nome para "
        "fins de divulgação institucional, ressalvadas as hipóteses "
        "legalmente permitidas."
    )

    texto(
    f"Nome: <b>{dados['nome_cl14']}</b>"
)

  texto(
    "Assinatura: _________________________________________________"
)

  texto(
    f"Data: <b>{dados['data_imagem']}</b>"
  )

#===================================================



# =================================================
#CLÁUSULA 15ª – DA MARCA, PROPRIEDADE INTELECTUAL E MATERIAIS DO CLUBE
# ================================================

  titulo("CLÁUSULA 15ª – DA MARCA, PROPRIEDADE INTELECTUAL E MATERIAIS DO CLUBE")

  texto(
    "15.1. A marca, nome empresarial, logotipo, identidade visual, materiais, "
    "conteúdos, metodologias, textos, apresentações, cursos, treinamentos, "
    "vídeos, fotografias e demais materiais produzidos ou disponibilizados "
    "pelo CLUBE pertencem à CONTRATADA ou a terceiros que tenham autorizado "
    "sua utilização."
)

  texto(
    "15.2. O ASSOCIADO não poderá reproduzir, modificar, comercializar, "
    "distribuir, sublicenciar, publicar ou utilizar os materiais do CLUBE "
    "para finalidade diversa daquela expressamente autorizada."
)

  texto(
    "15.3. O uso do selo, logotipo, placa, identidade visual ou qualquer "
    "elemento que indique a condição de Empresa Associada somente poderá "
    "ocorrer durante a vigência da associação e nos termos autorizados pelo CLUBE."
)

  texto(
    "15.4. Encerrada a associação, por qualquer motivo, o ASSOCIADO deverá "
    "cessar o uso da marca, logotipo, selo, placa e demais elementos que "
    "indiquem vínculo atual com o CLUBE."
)

  texto(
    "15.5. O ASSOCIADO não poderá utilizar a marca do CLUBE de forma que "
    "gere aparência de representação, sociedade, franquia, parceria comercial, "
    "patrocínio ou vínculo que não esteja expressamente autorizado."
)

#================================================================




# =================================================
#CLÁUSULA 16ª – DA CONFIDENCIALIDADE
# ================================================
  titulo("CLÁUSULA 16ª – DA CONFIDENCIALIDADE")

  texto(
    "16.1. As PARTES comprometem-se a preservar informações confidenciais "
    "às quais tenham acesso em razão da associação."
)

  texto(
    "16.2. O ASSOCIADO deverá respeitar a confidencialidade de informações "
    "comerciais, estratégicas, financeiras, pessoais ou profissionais de "
    "outros associados que sejam compartilhadas em ambiente de networking "
    "ou em atividades do CLUBE."
)

  texto(
    "16.3. A obrigação de confidencialidade não se aplica às informações que:"
)

  texto(
    "a) sejam públicas sem violação deste contrato;"
)

  texto(
    "b) já fossem legitimamente conhecidas pela parte;"
)

  texto(
    "c) devam ser divulgadas por determinação legal ou judicial;"
)

  texto(
    "d) sejam divulgadas com autorização de seu titular."
)

  texto(
    "16.4. A obrigação de confidencialidade permanecerá aplicável mesmo "
    "após o encerramento da associação, enquanto a informação mantiver "
    "caráter confidencial."
)
#=================================================================



# =================================================
#CLÁUSULA 17ª – DA PROTEÇÃO DE DADOS PESSOAIS – LGPD
# ================================================

  titulo("CLÁUSULA 17ª – DA PROTEÇÃO DE DADOS PESSOAIS – LGPD")

  texto(
    "17.1. A CONTRATADA compromete-se a tratar os dados pessoais do "
    "ASSOCIADO em conformidade com a Lei nº 13.709/2018 – Lei Geral de "
    "Proteção de Dados Pessoais (LGPD), observando os princípios e bases "
    "legais aplicáveis."
)

  texto(
    "17.2. O tratamento dos dados poderá ocorrer, conforme a finalidade, para:"
)

  texto(
    "a) execução e administração da associação;"
)

  texto(
    "b) cadastro e identificação do ASSOCIADO;"
)

  texto(
    "c) comunicação relacionada ao contrato;"
)

  texto(
    "d) envio de informações sobre eventos, atividades e benefícios;"
)

  texto(
    "e) cumprimento de obrigações legais e regulatórias;"
)

  texto(
    "f) exercício regular de direitos;"
)

  texto(
    "g) proteção do crédito, quando legalmente aplicável;"
)

  texto(
    "h) realização de ações de relacionamento e networking, observada "
    "a base legal correspondente."
)

  texto(
    "17.3. Os dados pessoais poderão ser compartilhados com fornecedores "
    "e operadores que auxiliem o CLUBE na execução de suas atividades, "
    "tais como plataformas de comunicação, sistemas de gestão, hospedagem, "
    "serviços administrativos e tecnológicos, observada a legislação aplicável."
)

  texto(
    "17.4. O compartilhamento de dados pessoais com outros associados ou "
    "parceiros comerciais para finalidade de networking será realizado "
    "somente quando houver base legal adequada e, quando necessário, "
    "autorização específica do titular."
)

  texto(
    "17.5. Sempre que necessário ao atendimento da LGPD, o ASSOCIADO será "
    "informado sobre as categorias de dados compartilhados, finalidade e "
    "forma de utilização."
)

  texto(
    "17.6. O ASSOCIADO poderá exercer os direitos previstos na LGPD, "
    "observadas as hipóteses e limitações legais, incluindo:"
)

  texto(
    "a) confirmação da existência de tratamento;"
)

  texto(
    "b) acesso aos dados;"
)

  texto(
    "c) correção de dados incompletos, inexatos ou desatualizados;"
)

  texto(
    "d) eliminação dos dados tratados com base no consentimento, quando aplicável;"
)

  texto(
    "e) informação sobre compartilhamento;"
)

  texto(
    "f) revogação do consentimento, quando essa for a base legal utilizada;"
)

  texto(
    "g) demais direitos previstos no art. 18 da LGPD."
)

  texto(
    "17.7. A revogação do consentimento não prejudicará os tratamentos "
    "realizados anteriormente de forma legítima nem aqueles que possuam "
    "outra base legal autorizadora."
)

  texto(
    "17.8. Os dados serão armazenados pelo período necessário ao cumprimento "
    "das finalidades previstas neste contrato e/ou pelo período exigido para "
    "cumprimento de obrigações legais, regulatórias e exercício regular de direitos."
)

  texto(
    "17.9. A CONTRATADA adotará medidas técnicas e administrativas "
    "compatíveis com a natureza dos dados e riscos envolvidos para proteção "
    "contra acessos não autorizados, perda, destruição, alteração, comunicação "
    "ou tratamento inadequado."
)

  texto(
    "17.10. Solicitações relacionadas à privacidade e proteção de dados "
    "poderão ser encaminhadas para:"
)

  texto(
    "weldersaba@clubealocampinaseregiao.com.br"
)

  texto(
    "17.11. A Política de Privacidade do CLUBE integra este contrato para "
    "todos os fins e deverá estar disponível ao ASSOCIADO em local de fácil acesso."
)
#================================================================



# =================================================
#CLÁUSULA 18ª – DO COMPARTILHAMENTO DE DADOS PARA NETWORKING
# ================================================

  titulo("CLÁUSULA 18ª – DO COMPARTILHAMENTO DE DADOS PARA NETWORKING")

  texto(
    "18.1. O ASSOCIADO declara estar ciente de que a finalidade do CLUBE "
    "inclui a aproximação entre profissionais, empresários e empresas."
)

  texto(
    "18.2. Quando houver necessidade de divulgação de dados pessoais do "
    "ASSOCIADO a outros membros para viabilizar networking, serão "
    "compartilhados apenas os dados necessários à finalidade pretendida, "
    "observada a legislação aplicável."
)

  texto(
    "18.3. Sempre que o tratamento depender de consentimento, a autorização "
    "será obtida de forma específica, informada e destacada."
)

  texto(
    "18.4. A autorização para compartilhamento de dados para networking "
    "poderá ser revogada quando essa for a base legal aplicável, sem prejuízo "
    "dos tratamentos realizados anteriormente de forma legítima."
)

#============================================================



# =================================================
#CLÁUSULA 19ª – DA POLÍTICA DE PRIVACIDADE
# ================================================
  
  titulo("CLÁUSULA 19ª – DA POLÍTICA DE PRIVACIDADE")

  texto(
    "19.1. A Política de Privacidade do Clube Alô Campinas e Região "
    "constitui documento complementar a este contrato e estabelece, "
    "entre outros aspectos:"
)

  texto(
    "a) quais dados pessoais são coletados;"
)

  texto(
    "b) as finalidades de tratamento;"
)

  texto(
    "c) as bases legais utilizadas;"
)

  texto(
    "d) como os dados são armazenados e protegidos;"
)

  texto(
    "e) com quem os dados podem ser compartilhados;"
)

  texto(
    "f) os direitos dos titulares;"
)

  texto(
    "g) os canais de atendimento relacionados à privacidade."
)

  texto(
    "19.2. A Política de Privacidade estará disponível na plataforma "
    "de associados e/ou em endereço eletrônico indicado pelo CLUBE."
)

  texto(
    "19.3. O ASSOCIADO declara que teve acesso à Política de Privacidade "
    "e que poderá consultá-la durante a vigência da associação."
)
#=====================================================



# =================================================
#CLÁUSULA 20ª – DOS PARCEIROS E DAS RELAÇÕES COMERCIAIS
# ================================================

  titulo("CLÁUSULA 20ª – DOS PARCEIROS E DAS RELAÇÕES COMERCIAIS")

  texto(
    "20.1. O CLUBE poderá apresentar aos associados empresas, profissionais "
    "e parceiros comerciais."
)

  texto(
    "20.2. A apresentação, indicação ou disponibilização de contato não "
    "representa recomendação, garantia, certificação ou responsabilidade "
    "do CLUBE pela contratação realizada entre ASSOCIADO e terceiro."
)

  texto(
    "20.3. O ASSOCIADO deverá realizar sua própria avaliação antes de "
    "contratar produtos ou serviços de terceiros."
)

  texto(
    "20.4. O CLUBE não garante preço, qualidade, prazo, resultado, "
    "disponibilidade ou cumprimento de obrigações assumidas por parceiros "
    "ou outros associados."
)

  texto(
    "20.5. Eventuais conflitos comerciais entre ASSOCIADO e terceiro serão, "
    "em regra, tratados diretamente entre os envolvidos, sem prejuízo da "
    "colaboração do CLUBE quando razoavelmente cabível."
)
#========================================================================

# =================================================
#CLÁUSULA 21ª – DAS REGRAS DOS GRUPOS DE WHATSAPP E TELEGRAM
# ================================================

  titulo("CLÁUSULA 21ª – DAS REGRAS DOS GRUPOS DE WHATSAPP E TELEGRAM")

  texto(
     "21.1. Os grupos e canais de WhatsApp e Telegram são instrumentos "
    "de comunicação e networking entre associados."
)

  texto(
    "21.2. É vedado utilizar os grupos para:"
)

  texto("a) conteúdo ilegal;")

  texto("b) discurso de ódio, discriminação ou ameaça;")

  texto("c) assédio;")

  texto("d) spam excessivo;")

  texto("e) divulgação repetitiva não autorizada;")

  texto(
    "f) compartilhamento de dados pessoais de terceiros sem autorização;"
 )

  texto(
    "g) conteúdo que viole direitos autorais ou de imagem;"
 )

  texto(
    "h) qualquer atividade que prejudique o funcionamento do grupo "
    "ou a convivência entre os associados."
 )

  texto(
    "21.3. O CLUBE poderá advertir, restringir ou remover o ASSOCIADO "
    "dos grupos quando houver descumprimento das regras, sem prejuízo "
    "das demais medidas contratuais cabíveis."
)

  texto(
    "21.4. A remoção de grupo de comunicação em razão de violação "
    "das regras não implica automaticamente cancelamento da associação, "
    "salvo se a conduta também caracterizar hipótese de rescisão."
 )
  #==========================================================
  
# =================================================
#CLÁUSULA 22ª – DA AUSÊNCIA DE VÍNCULO
# ================================================


  titulo("CLÁUSULA 22ª – DA AUSÊNCIA DE VÍNCULO")

  texto(
    "22.1. Este contrato não cria entre as PARTES vínculo empregatício, "
    "societário, representação comercial, franquia, mandato, agência, "
    "associação societária ou qualquer outra relação além daquela "
    "expressamente prevista neste instrumento."
)

  texto(
    "22.2. O ASSOCIADO não está autorizado a assumir obrigações, "
    "realizar negócios ou representar o CLUBE perante terceiros sem "
    "autorização expressa e por escrito."
  )


#==============================================================

 
# =================================================
#CLÁUSULA 23ª – DAS COMUNICAÇÕES
# ================================================

  titulo("CLÁUSULA 23ª – DAS COMUNICAÇÕES")

  texto(
    "23.1. As comunicações relacionadas ao contrato poderão ser realizadas "
    "por e-mail, WhatsApp, plataforma do CLUBE ou outro canal eletrônico "
    "previamente informado pelo ASSOCIADO."
)

  texto(
    "23.2. O ASSOCIADO é responsável por manter seus dados de contato "
    "atualizados."
)

  texto(
    "23.3. Para comunicações formais relacionadas a cancelamento, rescisão "
    "ou exercício de direitos, recomenda-se a utilização de meio que permita "
    "comprovação do envio e recebimento."
)

  texto(
    "23.4. O e-mail indicado no cadastro será considerado canal oficial "
    "de comunicação contratual, sem prejuízo de outros meios legalmente "
    "admitidos."
)
#============================================================

# =================================================
#CLÁUSULA 24ª – DA ASSINATURA ELETRÔNICA
# ================================================

  titulo("CLÁUSULA 24ª – DA ASSINATURA ELETRÔNICA")

  texto(
    "24.1. As PARTES reconhecem como válidas as assinaturas eletrônicas "
    "realizadas por plataforma ou mecanismo que permita identificar o "
    "signatário e demonstrar sua manifestação de vontade."
  )

  texto(
    "24.2. O contrato poderá ser assinado fisicamente ou por meio "
    "eletrônico, produzindo os mesmos efeitos jurídicos, observada "
    "a legislação aplicável."
 )

  texto(
    "24.3. Cada parte poderá manter cópia física ou digital deste "
    "instrumento e de seus anexos."
 )


# =================================================
#CLÁUSULA 25ª – DA INTEGRIDADE DO CONTRATO
# ================================================

  titulo("CLÁUSULA 25ª – DA INTEGRIDADE DO CONTRATO")

  texto(
    "25.1. Este instrumento, juntamente com seus anexos e documentos "
    "expressamente incorporados, representa o acordo entre as PARTES "
    "quanto ao objeto contratado."
)

  texto(
    "25.2. Eventual tolerância de uma das PARTES quanto ao descumprimento "
    "de determinada obrigação não constituirá renúncia, novação ou "
    "alteração contratual."
)

  texto(
    "25.3. Caso qualquer disposição deste contrato seja considerada "
    "inválida ou inexigível, as demais disposições permanecerão em vigor, "
    "na máxima extensão permitida pela legislação."
  )

  texto(
    "25.4. Qualquer alteração relevante deste contrato deverá ser "
    "formalizada por escrito, ressalvadas as atualizações permitidas "
    "pela legislação e pelas regras específicas de renovação."
  )
  
#======================================================================


# =================================================
#CLÁUSULA 26ª – DO FORO
# ================================================

  titulo("CLÁUSULA 26ª – DO FORO")

  texto(
    "26.1. As PARTES buscarão solucionar amigavelmente eventuais "
    "divergências decorrentes deste contrato."
  )

  texto(
    "26.2. Nas relações que não estejam sujeitas a regra legal específica "
    "de competência, fica eleito o foro da Comarca de "
    "<b>Campinas</b>, "
    "Estado de <b>São Paulo</b>, para dirimir questões "
    "decorrentes deste contrato."
  )

  texto(
    "26.3. Caso seja aplicável legislação de proteção ao consumidor que "
    "estabeleça foro diverso ou mais favorável ao consumidor, será "
    "respeitada a competência legalmente prevista."
  )
#========================================================


# =================================================
#CLÁUSULA 27ª – DA DECLARAÇÃO DE CIÊNCIA E ACEITE
# ================================================

  titulo("CLÁUSULA 27ª – DA DECLARAÇÃO DE CIÊNCIA E ACEITE")

  texto(
    "27.1. O ASSOCIADO declara que:"
)

  texto(
    "a) recebeu informações suficientes sobre o objeto da contratação;"
)

  texto(
    "b) teve oportunidade de conhecer previamente este contrato;"
)

  texto(
    "c) compreendeu que se trata de Plano Anual com vigência de "
    "12 (doze) meses;"
)

  texto(
    "d) compreendeu a diferença entre o preço à vista e o preço "
    "parcelado, quando aplicável;"
)

  texto(
    "e) está ciente de que determinados eventos, cursos ou programas "
    "poderão exigir pagamento adicional;"
)

  texto(
    "f) está ciente de que o CLUBE não garante resultados comerciais "
    "ou financeiros;"
)

  texto(
    "g) está ciente das regras de cancelamento e da eventual multa "
    "compensatória;"
)

  texto(
    "h) teve acesso à Política de Privacidade;"
)

  texto(
    "i) compromete-se a observar as normas de convivência do CLUBE."
)

  texto(
    "27.2. As cláusulas que estabelecem vigência anual, cancelamento "
    "antecipado, multa, inadimplência, uso de imagem, propriedade "
    "intelectual e tratamento de dados deverão ser apresentadas ao "
    "ASSOCIADO de forma clara e destacada."
  )


# =================================================
#CLÁUSULA 28ª – DOS ANEXOS
# ================================================

  titulo("CLÁUSULA 28ª – DOS ANEXOS")

  texto(
    "8.1. Integram este contrato, quando aplicáveis:"
)

  texto(
    "<b>ANEXO I – Política de Privacidade;</b>"
)

  texto(
    "<b>ANEXO II – Regulamento de Convivência e Uso dos Grupos;</b>"
)

  texto(
    "<b>ANEXO III – Tabela de Benefícios e Serviços Adicionais;</b>"
)

  texto(
    "<b>ANEXO IV – Termo de Autorização de Uso de Imagem, Voz e Nome;</b>"
)

  texto(
    "<b>ANEXO V – Termo de Autorização de Compartilhamento de Dados "
    "para Networking.</b>"
)

  texto(
    "28.2. Em caso de divergência entre este contrato e material "
    "publicitário ou mensagem comercial, prevalecerão as condições "
    "expressamente formalizadas neste instrumento, sem prejuízo dos "
    "direitos legalmente assegurados ao ASSOCIADO."
)
#===========================================================

   
  # =================================================
  #QUADRO RESUMO DA CONTRATAÇÃO
  # ================================================
  
  titulo("QUADRO RESUMO DA CONTRATAÇÃO")

  texto(
    f"<b>Plano contratado:</b> {dados['plano']}"
)

  texto(
    f"<b>Data de início:</b> {dados['data_de_inicio']}"
)

  texto(
    f"<b>Data de término:</b> {dados['data_de_termino']}"
)

  texto(
    f"<b>Forma de pagamento:</b> {dados['forma_pagamento']}"
)

  texto(
    f"<b>Data do primeiro vencimento:</b> {dados['data_vencimento']}"
)

  texto(
    f"<b>Quantidade de parcelas:</b> {dados['quantidade_parcelas']}"
)

  texto(
    f"<b>Valor da parcela:</b> R$ {dados['valor_parcela']}"
)

  texto(
    "Declaração de ciência do plano: O ASSOCIADO declara que recebeu "
    "informações sobre o plano selecionado, seus respectivos benefícios, "
    "limitações, valores e condições de pagamento, reconhecendo que os "
    "benefícios variam conforme a modalidade contratada."
  )

   
 # =================================================
 # DECLARAÇÃO FINAL
 # ================================================

  titulo("DECLARAÇÃO FINAL")

  texto(
    "E, por estarem de acordo com as condições estabelecidas neste "
    "instrumento, as PARTES declaram que leram, compreenderam e aceitaram "
    "suas disposições, firmando o presente contrato para todos os fins "
    "de direito."
 )

  texto(
    f"<b>Local:</b> {dados['local']}"
  )

  texto(
    f"<b>Data:</b> {dados['data_final_contrato']}"
  )

  titulo("CONTRATANTE – ASSOCIADO")

  texto(
    f"<b>Nome/Razão Social:</b> {dados['nome_associado']}"
)

  texto(
    f"<b>CPF/CNPJ:</b> {dados['cpf_associado']}"
)
  conteudo.append(Spacer(1, 8))
  

  texto(
    "Assinatura: _________________________________________________"
)

# =================================================
 # DECLARAÇÃO FINAL
 # ================================================

  titulo("CONTRATADA – CLUBE ALÔ CAMPINAS E REGIÃO")

  texto(
    "<b>Razão Social:</b>ALÔ CAMPINAS E REGIÃO "
 )

  texto(
    "<b>CNPJ:</b>55.633.392/0001-18  "
)

  texto(
    "<b> Representante Legal:</b> WELDER SABAINI DOS SANTOS "
)

  texto(
    "<b>CPF:</b>357.691.718-71  "
)
  conteudo.append(Spacer(1, 8))

  texto(
    "Assinatura:_____________________________________________ "
)



  titulo("TESTEMUNHAS")

  texto("<b>1. Testemunha</b>")

  texto(
    f"<b>Nome:</b> {dados['nome_testemunha1']}"
  )

  texto(
    f"<b>CPF:</b> {dados['cpf_testemunha1']}"
  )

  texto(
    "Assinatura: _________________________________________________"
  )

  conteudo.append(Spacer(1, 8))
  

  texto("<b>2. Testemunha</b>")

  texto(
    f"<b>Nome:</b> {dados['nome_testemunha2']}"
  )

  texto(
    f"<b>CPF:</b> {dados['cpf_testemunha2']}"
  )

  texto(
    "Assinatura: _________________________________________________"
  )


  documento.build(conteudo)
