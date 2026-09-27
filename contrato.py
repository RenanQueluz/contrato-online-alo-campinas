import streamlit as st
import pathlib
from gerador_pdf import gerar_pdf

#==============conexão com o css=========================

with open("style.css", "r", encoding="utf-8") as arquivo:
   css = arquivo.read()

st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


#====================CONTRATO=======================================
def contrato():

 #titulo inicial do contrato
    st.write(
     "#### CONTRATO DE ADESÃO E PRESTAÇÃO DE SERVIÇOS DE ASSOCIAÇÃO AO CLUBE ALÔ CAMPINAS E REGIÃO"
    )
    st.write("**Pelo presente instrumento particular, de um lado:**")


#inicio de parte 1 do contratante-associado
    st.write('##### **I - DAS PARTES**')
 
    st.write('##### 1. CONTRATANTE-ASSOCIADO')

    st.markdown(" ##### **Pessoa fisica:**")

    #dados de pessoa fisica.
    with st.container(key="campos1"):
       nome_completo = st.text_input("Nome completo", key="nome_campos1")
       #espaçamento de paragrafos
       st.markdown("<br>", unsafe_allow_html=True)
       rg = st.text_input("RG", key="rg_campos1")

         #espaçamento de paragrafos
       st.markdown("<br>", unsafe_allow_html=True)
       cpf = st.text_input("CPF", key="cpf_campos1")

         #espaçamento de paragrafos
       st.markdown("<br>", unsafe_allow_html=True)
       cidade_Uf = st.text_input("Cidade/UF", key="cidade_campos1")

           #espaçamento de paragrafos
       st.markdown("<br>", unsafe_allow_html=True)
       email = st.text_input("E-mail:", key="email_campos1")

         #espaçamento de paragrafos
       st.markdown("<br>", unsafe_allow_html=True)
       contato = st.text_input("Telefone/WhatsApp:", key="contato_campos1")

       #espaçamento de paragrafos
       st.markdown("<br>", unsafe_allow_html=True)

    #dados de pessoa juridica.
    st.markdown("##### **Pessoa Juridica:**")
    with st.container(key="campos2"):
       
       razao_social = st.text_input("Razão Social:", key="razao_social")
        #espaçamento de paragrafos
       st.markdown("<br>", unsafe_allow_html=True)


       nome_fantasia = st.text_input("Nome fantasia:", key="nome_campos2")
        #espaçamento de paragrafos
       st.markdown("<br>", unsafe_allow_html=True)


       cnpj = st.text_input("CNPJ:", key="cnpj_campos2")
        #espaçamento de paragrafos
       st.markdown("<br>", unsafe_allow_html=True)


       representante_legal = st.text_input("Representante legal", key="representate_campos2")
         #espaçamento de paragrafos
       st.markdown("<br>", unsafe_allow_html=True)


       cpf_representante = st.text_input("CPF do Representante", key="cpf_campos2")
        #espaçamento de paragrafos
       st.markdown("<br>", unsafe_allow_html=True)

       rg_representante = st.text_input("RG do representante:", key="rg_campos2")
         #espaçamento de paragrafos
       st.markdown("<br>", unsafe_allow_html=True)

       email_juridica = st.text_input(
        "E-mail:",
       key="email_juridica"
       )
         #espaçamento de paragrafos
       st.markdown("<br>", unsafe_allow_html=True)

       telefone_juridica = st.text_input(
        "Telefone/WhatsApp:",
       key="telefone_juridica")

        #espaçamento de paragrafos
       st.markdown("<br>", unsafe_allow_html=True)
#======================fim de parte 1, contratante-associado============================

        #espaçamento de paragrafos
       st.markdown("<br>", unsafe_allow_html=True)


#======================inicio de parte 2, contratada============================

       st.write("Doravante denominado simplesmente **ASSOCIADO** ou **CONTRATANTE**.")

       st.write('##### 2. CONTRATADA')

       st.write("**CLUBE ALÔ CAMPINAS E REGIÃO** pessoa juridica de direito privado, inscrita no CNPJ sob n°___________________, com sede/endereço em _____________, neste ato representada na forma de seu Contrato Social/Estatuto, por seu representante legal, doravante denominada simplesmente **CLUBE** ou **CONTRATADA**." )

       st.write("CLUBE e ASSOCIADO, quando mencionados conjuntamente, serão denominados **PARTES**")

#======================inicio cláusula 1============================
       with st.container(key="titulo-clausulas"):
          st.markdown("### **CLÁUSULA 1ª - DO OBJETO**")

       st.write("1.1. O presente instrumento tem por objeto a adesão do CONTRATANTE ao Clube **Alô Campinas e Região**, mediante contratação do Plano Anual de Associação, compreendendo o acesso aos benefícios, canais, conteúdos, atividades e serviços descritos neste contrato. ")

       st.write("1.2. A associação tem por finalidade fomentar o desenvolvimento pessoal e empresarial dos associados por meio de networking estruturado, acesso a conhecimento, troca de experiências, divulgação institucional, aproximação entre empresas e profissionais e geração de oportunidades de relacionamento e negócios. ")

       st.write("1.3. A associação não constitui promessa ou garantia de geração de negócios, vendas, faturamento, lucro, clientes, contratos ou qualquer resultado econômico específico. ")

       st.write("1.4. Os resultados eventualmente obtidos pelo ASSOCIADO dependerão, entre outros fatores, de sua participação, relacionamento, capacidade comercial, atuação profissional e utilização dos recursos disponibilizados pelo CLUBE.")

       st.write("1.5. O CLUBE obriga-se a disponibilizar os benefícios e serviços previstos neste instrumento, observadas as condições, limitações, disponibilidade, calendário e regras aplicáveis a cada atividade. ")


#============fim da cláusula1===============


#=============inicio da cláusula 2==============
        
       st.write("### **CLÁUSULA 2ª – DOS BENEFÍCIOS E ACESSOS DO PLANO ANUAL** ")

       st.write("2.1. O Plano Anual contratado pelo ASSOCIADO compreenderá, durante o período de vigência:")

       with st.container(key="clausula_2.1"):
          st.markdown("""

          a) acesso à estrutura digital disponibilizada pelo CLUBE;<br>

          b) acesso ao site oficial do Clube Alô Campinas e Região;

          c) acesso aos canais oficiais de comunicação do CLUBE, inclusive grupo exclusivo de WhatsApp e grupo/canal de Telegram, conforme a modalidade disponibilizada pelo CLUBE; 

          d) acesso ao Clube de Descontos Alô Campinas e Região, na condição de lojista e/ou usuário, conforme as regras específicas do programa; 

          e) participação em eventos, treinamentos, visitas técnicas, cursos, encontros, ações de networking e demais atividades promovidas pelo CLUBE, observadas as condições específicas de cada atividade; 

          f) publicação de até 2 (duas) matérias no Portal Alô Campinas e Região, conforme critérios editoriais, disponibilidade de agenda e materiais fornecidos pelo ASSOCIADO; 

          g) até 5 (cinco) Stories no perfil oficial @alocampinaseregiao, desde que o conteúdo seja fornecido pelo ASSOCIADO em formato adequado para publicação;

          h) certificado de associado; 

          i) selo de Empresa Associada, quando aplicável; 

          j) demais benefícios expressamente divulgados pelo CLUBE durante a vigência da associação. 
    """, unsafe_allow_html=True)
          

          with st.container(key="clausula_2.2"):
             st.markdown("""
             2.2. Os benefícios previstos nesta cláusula são pessoais e vinculados ao ASSOCIADO, sendo vedada a cessão ou transferência a terceiros sem autorização prévia da CONTRATADA.

             2.3. A participação em eventos, cursos, treinamentos, experiências ou programas específicos poderá estar sujeita a inscrição prévia, limite de vagas, disponibilidade, critérios de participação ou pagamento adicional.

             2.4. O fato de determinada atividade ser divulgada pelo CLUBE não significa que seu custo esteja necessariamente incluído no valor da associação. 
             
             2.5. Benefícios, descontos, produtos ou serviços oferecidos por empresas parceiras são de responsabilidade dos respectivos parceiros, especialmente quanto a preços, condições comerciais, disponibilidade, qualidade e execução dos serviços contratados diretamente entre parceiro e ASSOCIADO. 
            """, unsafe_allow_html=True )

#=============fim da cláusula 2 ==================


#=============inicio de cláusula 3================

             st.write(" ### CLÁUSULA 3ª – DOS SERVIÇOS DE CONTEÚDO E DIVULGAÇÃO ")

             with st.container(key="clausula_3.1"):
               st.markdown("""
                 3.1. Os 5 (cinco) Stories previstos no Plano Anual deverão ser disponibilizados pelo ASSOCIADO em formato previamente adequado à publicação. 
                 
                 3.2. Caso o ASSOCIADO necessite que o CLUBE produza ou adapte material criativo, será cobrado valor adicional de **R$ 80,00 (oitenta reais) por criativo produzido**, mediante prévia aprovação do ASSOCIADO. 
                 
                 3.3. A produção de vídeos profissionais não está incluída nos 5 (cinco) Stories do Plano Anual, podendo ser contratada separadamente. 
                 
                 3.4. Quando contratada separadamente, a produção de pacote de até **3 (três) vídeos, incluindo captação e/ou demais recursos previamente acordados, terá valor adicional de R$ 800,00 (oitocentos reais)**, conforme orçamento e condições previamente aprovados pelo ASSOCIADO. 
                 
                 3.5. Eventual utilização de imagem aérea, drone, fotógrafo, equipamento especial, deslocamento ou produção adicional poderá gerar custo adicional, previamente informado e aprovado pelo ASSOCIADO. 
                 
                 3.6. A publicação de matérias e conteúdos estará sujeita a critérios editoriais, disponibilidade de agenda e adequação às políticas de conteúdo do Portal e das plataformas utilizadas. 
                 
                 3.7. O CLUBE poderá recusar material que contenha conteúdo ilícito, discriminatório, ofensivo, enganoso, difamatório, que viole direitos de terceiros, propriedade intelectual, normas legais ou políticas das plataformas. 
                  
        
             """, unsafe_allow_html=True )

#============fim da cláusula 3=================


#==============inicio da cláusula 4

             st.write("### CLÁUSULA 4ª – DAS ATIVIDADES E EVENTOS ")


             with st.container(key="clausula_4.1"):
               st.markdown("""
                4.1. O CLUBE divulgará aos associados os eventos, cursos, treinamentos, visitas técnicas e demais atividades por meio dos canais oficiais de comunicação.

                4.2. A associação não garante a realização de quantidade mínima de eventos, salvo quando expressamente prevista em proposta comercial, anexo ou instrumento específico. 

                4.3. Eventos, cursos, treinamentos ou programas poderão ser gratuitos ou possuir investimento adicional, circunstância que será informada previamente. 

                4.4. O CLUBE poderá alterar datas, horários, locais, formato ou programação das atividades por razões operacionais, de segurança, disponibilidade de palestrantes, parceiros, fornecedores ou circunstâncias alheias à sua vontade, comunicando os associados pelos canais disponíveis.

                4.5. Eventual cancelamento ou alteração de atividade não implica, por si só, cancelamento da associação ou restituição integral do valor do Plano Anual, ressalvados os direitos previstos em lei e as condições específicas eventualmente divulgadas para aquela atividade. 
        
               """, unsafe_allow_html=True  )

#=============fim da cláusula 4=================

#=============inicio da cláusula5===============

               st.write("### CLÁUSULA 5ª – DAS OBRIGAÇÕES DO ASSOCIADO", )

               st.write("5.1. Constituem obrigações do ASSOCIADO: ")

               with st.container(key="clausula_5.1"):
                st.markdown("""
                    a) cumprir este contrato e as normas internas do CLUBE;

                     b) respeitar as regras de convivência, ética, urbanidade e boa-fé; 

                     c) manter comportamento compatível com ambiente profissional e de networking;

                     d) não praticar atos ofensivos, discriminatórios, fraudulentos, ilícitos ou que possam causar prejuízo à imagem do CLUBE ou de seus associados;

                    e) participar das atividades de forma ética e colaborativa;

                    f) manter seus dados cadastrais atualizados; 

                    g) preservar seus dados de acesso, senhas e informações de caráter reservado; 

                    h) não compartilhar acessos individuais com terceiros; 

                    i) não utilizar grupos, eventos ou canais do CLUBE para práticas ilícitas, spam, fraude, divulgação indevida, captação abusiva ou atividades que contrariem as regras internas; 

                    j) respeitar a privacidade e os dados pessoais dos demais associados; 

                    k) responsabilizar-se pela veracidade das informações, imagens, marcas e conteúdos fornecidos ao CLUBE; 

                    l) possuir autorização para utilização de conteúdos, imagens, marcas, textos e demais materiais que encaminhar para publicação. 
        
               """, unsafe_allow_html=True  )

                st.write("5.2. O ASSOCIADO responderá pelos prejuízos que causar ao CLUBE ou a terceiros em razão de conteúdo ilícito ou utilização indevida de materiais fornecidos por ele, observada a legislação aplicável. ")

#============fim da cláusula 5==================


#===========inicio da clausula 6============
          st.write("###  CLÁUSULA 6ª – DAS OBRIGAÇÕES DO CLUBE")

          st.write("6.1. Constituem obrigações do CLUBE")

          with st.container(key="clausula_6.1"):
             st.markdown("""

             a) disponibilizar os benefícios expressamente previstos neste contrato; 

             b) disponibilizar informações sobre eventos e atividades por seus canais oficiais;

             c) liberar os acessos aos grupos e canais destinados aos associados, observadas as regras de utilização; 

             d) manter os canais oficiais de comunicação disponíveis dentro de suas possibilidades técnicas; e) prestar informações relativas à associação; 

             f) observar a legislação aplicável ao tratamento de dados pessoais; 
             
             g) adotar medidas técnicas e administrativas razoáveis para proteção dos dados pessoais tratados no âmbito da associação. 
             
             6.2. O CLUBE não será responsável por indisponibilidades decorrentes de falhas de internet, plataformas de terceiros, redes sociais, WhatsApp, Telegram, serviços de hospedagem, força maior, caso fortuito ou outros fatores alheios ao seu controle. 
            
  """, unsafe_allow_html=True  )

#============fim da cláusula 6==============



#============inicio da cláusula 7==============

       st.write(" ### CLÁUSULA 7ª – DO PLANO ANUAL")

       with st.container(key="clausula_7.1"):
            st.markdown("""

           7.1. O CLUBE oferece o PLANO ANUAL DE ASSOCIAÇÃO, com vigência de 12 (doze) meses. 

           7.2. O ASSOCIADO reconhece que o produto/serviço contratado é um plano anual de associação, e que eventual pagamento parcelado constitui apenas forma de pagamento do preço contratado, não transformando a contratação em mensalidade independente.
          
           7.3. O ASSOCIADO poderá optar pela forma de pagamento indicada no quadro financeiro deste contrato. 
        
       """, unsafe_allow_html=True  )
#=============fim da cláusula7 ================

#=============inico da cláusula 8==============
    st.write(" ### CLÁUSULA 8ª – DO VALOR E DA FORMA DE PAGAMENTO ")

    st.write("8.1. O valor do Plano Anual à vista é de: ")

    st.write("**R$ 1.490,00 (mil quatrocentos e noventa reais).** ")

    st.write("8.2. Caso seja escolhida a modalidade de pagamento parcelado por boleto bancário, o preço contratado será de: ")

    st.text("**12 (doze) parcelas de R$ 149,90 (cento e quarenta e nove reais e noventa centavos), totalizando R$ 1.798,80 (mil setecentos e noventa e oito reais e oitenta centavos).** ")

    st.write("8.3. A diferença entre o preço à vista e o preço parcelado deverá ser apresentada ao ASSOCIADO de maneira clara antes da contratação. ")

    st.write("8.4. O pagamento poderá ser realizado por: ")

    with st.container(key="clausula_8.1"):
       st.markdown("""
        a) PIX; 

        b) dinheiro em espécie;

        c) cartão de crédito, conforme condições da operadora e modalidade escolhida; 

        d) boleto bancário, quando disponibilizado pelo CLUBE. 
        
        8.5. Na hipótese de pagamento por cartão de crédito, eventual acréscimo decorrente exclusivamente da modalidade de parcelamento deverá ser informado previamente ao ASSOCIADO. 
        
        8.6. Na modalidade de boleto bancário, os vencimentos serão aqueles constantes dos respectivos boletos emitidos pelo CLUBE ou por instituição responsável pelo processamento do pagamento. 
        
        8.7. Salvo disposição diversa expressamente indicada no quadro financeiro, o primeiro pagamento deverá ocorrer em até 7 (sete) dias úteis contados da assinatura deste instrumento.
         
        8.8. O ASSOCIADO declara ter recebido informações suficientes sobre o preço total contratado, quantidade de parcelas, valor das parcelas e condições de pagamento.        
  """, unsafe_allow_html=True  )

#=============fim da cláusula 8 ===============


#=============incio da clausula 9=============

    st.write("### CLÁUSULA 9ª – DO REAJUSTE  ")

    with st.container(key="clausula_9.1"):
       st.markdown("""
       9.1. Na hipótese de renovação do Plano Anual, o valor poderá ser reajustado anualmente pela variação acumulada do IGP-M/FGV ou, na sua impossibilidade, por outro índice oficial que legalmente o substitua. 
       
       9.2. O reajuste será aplicado somente a períodos contratuais futuros e será informado ao ASSOCIADO por ocasião da renovação. 
       
       9.3. O reajuste não será aplicado retroativamente a períodos já pagos. 

        
  """, unsafe_allow_html=True  )
#============fim da cláusula 9 =====================


#==========inico da cláusula 10 =================

    st.write("### CLÁUSULA 10ª – DA VIGÊNCIA E RENOVAÇÃO ")
    

    st.write("10.1. O presente contrato terá vigência de **12 (doze) meses**, iniciando-se no:")

    with st.container(key="datas"):
      data_inicio = st.text_input("**Inicio:**", key="campos_data")
      data_final = st.text_input("**Término:**", key="campos_data2")

     #espaçamento de paragrafos
    st.markdown("<br>", unsafe_allow_html=True)

    with st.container(key="clausula_10.1"):
        st.markdown("""

      10.2. A associação poderá ser renovada automaticamente por novos períodos de 12 (doze) meses, caso o ASSOCIADO não manifeste expressamente sua intenção de não renovação. 

      10.3. Para evitar a renovação, o ASSOCIADO deverá comunicar sua intenção ao CLUBE com antecedência mínima de 30 (trinta) dias do término da vigência.
     
      10.4. A ausência de manifestação não será interpretada como renúncia a direitos previstos em lei.
      
      10.5. Havendo alteração de preço para o período de renovação, o ASSOCIADO deverá ser informado previamente. 
        
  """, unsafe_allow_html=True  )
#==============fim da cláusula 10=====================


#==============inicio da clásula 11 ===================

    st.write("### CLÁUSULA 11ª – DO CANCELAMENTO ANTECIPADO E DA MULTA COMPENSATÓRIA ")

    with st.container(key="clausula_11.1"):
     st.markdown("""

     11.1. Por se tratar de Plano Anual, o período contratado corresponde a 12 (doze) meses, independentemente da forma de pagamento escolhida. 
     
     11.2. O ASSOCIADO poderá solicitar o cancelamento antecipado mediante comunicação escrita ao CLUBE. 
     
     11.3. Ressalvadas as hipóteses de direito de arrependimento, descumprimento contratual pela CONTRATADA ou outras situações previstas em lei, o cancelamento antecipado imotivado pelo ASSOCIADO poderá ensejar **multa compensatória correspondente a 10% (dez por cento) do saldo das parcelas vincendas**, calculada na data do pedido de cancelamento. 
     
     11.4. A multa prevista nesta cláusula não será calculada sobre parcelas já vencidas e pagas. 
     
     11.5. As parcelas já vencidas e não pagas permanecerão devidas, acrescidas dos encargos de mora previstos neste contrato. 
     
     11.6. Caso o ASSOCIADO tenha realizado pagamento antecipado de valores referentes a período ainda não usufruído, eventual restituição será apurada considerando o período efetivamente prestado, os valores já utilizados, eventuais serviços adicionais efetivamente contratados e a multa compensatória aplicável, sempre observada a legislação vigente. 
     
     11.7. A multa não será aplicada quando o cancelamento decorrer de descumprimento contratual comprovado da CONTRATADA que justifique a rescisão, sem prejuízo dos demais direitos legalmente assegurados. 
     
     11.8. Quando a contratação ocorrer fora do estabelecimento comercial, inclusive por meios eletrônicos ou outras hipóteses abrangidas pela legislação de defesa do consumidor, será respeitado o direito de arrependimento legalmente previsto. 
  """, unsafe_allow_html=True  )
#===============fim da cláusula 11 =================

#================inicio da cláusula 12===============
  
     st.write("### CLÁUSULA 12ª – DA INADIMPLÊNCIA ")

     with st.container(key="clausula_12.1"):
      st.markdown("""
      12.1. O atraso no pagamento de qualquer parcela sujeitará o ASSOCIADO, observada a legislação aplicável, ao pagamento de:
      
      a) multa moratória de **2% (dois por cento)** sobre o valor da parcela vencida; 
     
      b) juros de mora de **1% (um por cento) ao mês,** calculados proporcionalmente aos dias de atraso, quando juridicamente aplicável; 
      
      c) atualização monetária, quando cabível; 
      
      d) demais encargos legalmente permitidos. 

      12.2. A multa moratória prevista nesta cláusula será limitada ao máximo permitido pela legislação aplicável. 

      12.3. Em caso de inadimplência, o CLUBE poderá, após comunicação ao ASSOCIADO, suspender temporariamente o acesso a benefícios, grupos, conteúdos, eventos e demais recursos disponibilizados ao associado enquanto perdurar o débito. 

      12.4. A inadimplência superior a 30 (trinta) dias poderá ensejar a rescisão do contrato pela CONTRATADA, mediante comunicação ao ASSOCIADO.

      12.5. A rescisão por inadimplência não prejudicará a cobrança dos valores vencidos e demais encargos legalmente cabíveis. 12.6. O eventual não exercício imediato de qualquer direito pelo CLUBE não representará renúncia, novação ou alteração contratual. 
        
  """, unsafe_allow_html=True  )

#================== fim da cláusula 12 ======================

#================== inico da cláusula 13 ====================

      st.write("### CLÁUSULA 13ª – DA RESCISÃO POR DESCUMPRIMENTO ")

      with st.container(key="clausula_13.1"):
       st.markdown("""

       13.1. O presente contrato poderá ser rescindido por qualquer das PARTES em caso de descumprimento relevante de obrigação contratual, desde que a parte responsável seja previamente comunicada e, quando a natureza da infração permitir, tenha oportunidade razoável de sanar o descumprimento. 

       13.2. O CLUBE poderá rescindir imediatamente a associação, observada a legislação aplicável, em situações graves que envolvam: 

       a) prática de ato ilícito; 

       b) fraude; 

       c) ameaça ou violência; 

       d) discriminação; 

       e) assédio; 

       f) uso indevido da marca do CLUBE;

       g) divulgação não autorizada de informações confidenciais; 

       h) compartilhamento indevido de acessos; i) comportamento reiteradamente incompatível com as normas de convivência; 

       j) utilização dos canais do CLUBE para finalidade ilícita ou prejudicial aos demais associados. 
       
       13.3. A rescisão não prejudicará a apuração de valores eventualmente devidos ou de danos comprovadamente causados. 
        
  """, unsafe_allow_html=True  )

#============== fim da cláusula 13 ====================

#==============inicio da clásula 14 ====================

    st.write("### CLÁUSULA 14ª – DO USO DE IMAGEM, VOZ E NOME ")

    with st.container(key="clausula_14.1"):
     st.markdown("""
        14.1. O ASSOCIADO poderá autorizar, mediante manifestação específica, o uso gratuito de sua imagem, voz e nome pelo CLUBE em materiais institucionais relacionados às atividades do CLUBE, inclusive site, redes sociais, fotografias, vídeos, eventos e materiais de divulgação. 
        
        14.2. A autorização, quando concedida, será limitada à divulgação institucional e promocional das atividades do CLUBE, não autorizando utilização que seja ofensiva, difamatória, ilícita ou incompatível com a finalidade desta autorização. 
        
        14.3. A autorização de uso de imagem não constitui cessão de direitos patrimoniais sobre a imagem, voz ou nome além da finalidade expressamente autorizada. 
        
        14.4. O ASSOCIADO poderá solicitar a interrupção de novas utilizações futuras de sua imagem mediante comunicação escrita, ressalvadas as hipóteses em que a manutenção seja necessária para cumprimento de obrigação legal, exercício regular de direitos ou situações em que a retirada seja tecnicamente inviável de materiais já produzidos ou publicados, observada a legislação aplicável. 
        
  """, unsafe_allow_html=True  )

     st.write(" ##### AUTORIZAÇÃO ESPECÍFICA DE USO DE IMAGEM ")

    autoriza = st.checkbox(
    "**AUTORIZO** O uso gratuito da minha imagem, voz e   nome nos termos desta cláusula. ", key="autorizo")

    nao_autoriza = st.checkbox(
      "**NÃO AUTORIZO** O uso da minha imagem, voz e nome para fins de divulgação institucional, ressalvadas as hipóteses legalmente permitidas. ",
      disabled=autoriza, key="não_autorizo")

    nome_cl14 = st.text_input("Nome:", key="campos3")

     #espaçamento de paragrafos
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.write("**Assinatura:**_________________________________________")
         
    data = st.text_input("Data:", key="campo_data3")


#==================fim da cláusula 14 =====================


#====================inicio da cláusula 15 =====================

    st.write("### CLÁUSULA 15ª – DA MARCA, PROPRIEDADE INTELECTUAL E MATERIAIS DO CLUBE ")


    with st.container(key="clausula_15.1"):
     st.markdown("""
      
       15.1. A marca, nome empresarial, logotipo, identidade visual, materiais, conteúdos, metodologias, textos, apresentações, cursos, treinamentos, vídeos, fotografias e demais materiais produzidos ou disponibilizados pelo CLUBE pertencem à CONTRATADA ou a terceiros que tenham autorizado sua utilização. 
       
       15.2. O ASSOCIADO não poderá reproduzir, modificar, comercializar, distribuir, sublicenciar, publicar ou utilizar os materiais do CLUBE para finalidade diversa daquela expressamente autorizada. 
       
       15.3. O uso do selo, logotipo, placa, identidade visual ou qualquer elemento que indique a condição de Empresa Associada somente poderá ocorrer durante a vigência da associação e nos termos autorizados pelo CLUBE. 
       
       15.4. Encerrada a associação, por qualquer motivo, o ASSOCIADO deverá cessar o uso da marca, logotipo, selo, placa e demais elementos que indiquem vínculo atual com o CLUBE. 
       
       15.5. O ASSOCIADO não poderá utilizar a marca do CLUBE de forma que gere aparência de representação, sociedade, franquia, parceria comercial, patrocínio ou vínculo que não esteja expressamente autorizado. 
   
  """, unsafe_allow_html=True  )
#==================fim da cláusula 15 ========================


#=======================inicio da clásula 16 ======================


    st.write("### CLÁUSULA 16ª – DA CONFIDENCIALIDADE ")

    with st.container(key="clausula_16.1"):
     st.markdown("""
     16.1. As PARTES comprometem-se a preservar informações confidenciais às quais tenham acesso em razão da associação. 
   
     16.2. O ASSOCIADO deverá respeitar a confidencialidade de informações comerciais, estratégicas, financeiras, pessoais ou profissionais de outros associados que sejam compartilhadas em ambiente de networking ou em atividades do CLUBE. 

     16.3. A obrigação de confidencialidade não se aplica às informações que: 

     a) sejam públicas sem violação deste contrato;

     b) já fossem legitimamente conhecidas pela parte; 
  
     c) devam ser divulgadas por determinação legal ou judicial; d) sejam divulgadas com autorização de seu titular. 
   
     16.4. A obrigação de confidencialidade permanecerá aplicável mesmo após o encerramento da associação, enquanto a informação mantiver caráter confidencial. 
        
  """, unsafe_allow_html=True  )
#=================== fim da cláusula 16 ====================

#=====================inicio da cláusula 17 ======================

    st.write("### CLÁUSULA 17ª – DA PROTEÇÃO DE DADOS PESSOAIS – LGPD ")


    with st.container(key="clausula_ 17.1"):
      st.markdown("""
         17.1. A CONTRATADA compromete-se a tratar os dados pessoais do ASSOCIADO em conformidade com a Lei nº 13.709/2018 – Lei Geral de Proteção de Dados Pessoais (LGPD), observando os princípios e bases legais aplicáveis. 
         
         17.2. O tratamento dos dados poderá ocorrer, conforme a finalidade, para: 
         
         a) execução e administração da associação; 
         
         b) cadastro e identificação do ASSOCIADO; 
         
         c) comunicação relacionada ao contrato; 
         
         d) envio de informações sobre eventos, atividades e benefícios; 
         
         e) cumprimento de obrigações legais e regulatórias; f) exercício regular de direitos; 
         
         g) proteção do crédito, quando legalmente aplicável; 
         
         h) realização de ações de relacionamento e networking, observada a base legal correspondente. 
         
         17.3. Os dados pessoais poderão ser compartilhados com fornecedores e operadores que auxiliem o CLUBE na execução de suas atividades, tais como plataformas de comunicação, sistemas de gestão, hospedagem, serviços administrativos e tecnológicos, observada a legislação aplicável. 
         
         17.4. O compartilhamento de dados pessoais com outros associados ou parceiros comerciais para finalidade de networking será realizado somente quando houver base legal adequada e, quando necessário, autorização específica do titular.

         17.5. Sempre que necessário ao atendimento da LGPD, o ASSOCIADO será informado sobre as categorias de dados compartilhados, finalidade e forma de utilização. 
         
         17.6. O ASSOCIADO poderá exercer os direitos previstos na LGPD, observadas as hipóteses e limitações legais, incluindo: 
         
         a) confirmação da existência de tratamento;
         
         b) acesso aos dados; 
         
         c) correção de dados incompletos, inexatos ou desatualizados; 
         
         d) eliminação dos dados tratados com base no consentimento, quando aplicável; 
         
         e) informação sobre compartilhamento; 
         
         f) revogação do consentimento, quando essa for a base legal utilizada; 
         
         g) demais direitos previstos no art. 18 da LGPD. 17.7. A revogação do consentimento não prejudicará os tratamentos realizados anteriormente de forma legítima nem aqueles que possuam outra base legal autorizadora. 
         
         17.8. Os dados serão armazenados pelo período necessário ao cumprimento das finalidades previstas neste contrato e/ou pelo período exigido para cumprimento de obrigações legais, regulatórias e exercício regular de direitos. 
         
         17.9. A CONTRATADA adotará medidas técnicas e administrativas compatíveis com a natureza dos dados e riscos envolvidos para proteção contra acessos não autorizados, perda, destruição, alteração, comunicação ou tratamento inadequado. 
         
         17.10. Solicitações relacionadas à privacidade e proteção de dados poderão ser encaminhadas para: 
         
         juridico@clubealocampinaseregiao.com.br 

         17.11. A Política de Privacidade do CLUBE integra este contrato para todos os fins e deverá estar disponível ao ASSOCIADO em local de fácil acesso. 
        
  """, unsafe_allow_html=True  )
#=======================fim da cláusula 17 =======================


#=======================inicio da clásula 18 =====================


    st.write("### CLÁUSULA 18ª – DO COMPARTILHAMENTO DE DADOS PARA NETWORKING ")

    with st.container(key="clausula_ 18.1"):
      st.markdown("""
     18.1. O ASSOCIADO declara estar ciente de que a finalidade do CLUBE inclui a aproximação entre profissionais, empresários e empresas. 
     
     18.2. Quando houver necessidade de divulgação de dados pessoais do ASSOCIADO a outros membros para viabilizar networking, serão compartilhados apenas os dados necessários à finalidade pretendida, observada a legislação aplicável. 
     
     18.3. Sempre que o tratamento depender de consentimento, a autorização será obtida de forma específica, informada e destacada. 
     
     18.4. A autorização para compartilhamento de dados para networking poderá ser revogada quando essa for a base legal aplicável, sem prejuízo dos tratamentos realizados anteriormente de forma legítima. 
        
  """, unsafe_allow_html=True  )
#================= fim da cláusula 18 =====================

#==================inicio da cláusula 19 ====================


    st.write("### CLÁUSULA 19ª – DA POLÍTICA DE PRIVACIDADE ")

    with st.container(key="clausula_ 19.1"):
     st.markdown("""

   19.1. A Política de Privacidade do Clube Alô Campinas e Região constitui documento complementar a este contrato e estabelece, entre outros aspectos: 
   
   a) quais dados pessoais são coletados; 
   
   b) as finalidades de tratamento; 
   
   c) as bases legais utilizadas; 
   
   d) como os dados são armazenados e protegidos; 
   
   e) com quem os dados podem ser compartilhados; 
   
   f) os direitos dos titulares; 
   
   g) os canais de atendimento relacionados à privacidade. 
   
   19.2. A Política de Privacidade estará disponível na plataforma de associados e/ou em endereço eletrônico indicado pelo CLUBE. 
   
   19.3. O ASSOCIADO declara que teve acesso à Política de Privacidade e que poderá consultá-la durante a vigência da associação. 
        
  """, unsafe_allow_html=True  )

#=================fim da clásula 19 ======================

#==================== Clausula 20 =======================

     st.write("### CLÁUSULA 20ª – DOS PARCEIROS E DAS RELAÇÕES COMERCIAIS ")

     with st.container(key="clausula_ 20.1"):
       st.markdown("""
        20.1. O CLUBE poderá apresentar aos associados empresas, profissionais e parceiros comerciais.
        
        20.2. A apresentação, indicação ou disponibilização de contato não representa recomendação, garantia, certificação ou responsabilidade do CLUBE pela contratação realizada entre ASSOCIADO e terceiro. 
        
        20.3. O ASSOCIADO deverá realizar sua própria avaliação antes de contratar produtos ou serviços de terceiros. 
        
        20.4. O CLUBE não garante preço, qualidade, prazo, resultado, disponibilidade ou cumprimento de obrigações assumidas por parceiros ou outros associados. 
        
        20.5. Eventuais conflitos comerciais entre ASSOCIADO e terceiro serão, em regra, tratados diretamente entre os envolvidos, sem prejuízo da colaboração do CLUBE quando razoavelmente cabível. 
  """, unsafe_allow_html=True  ) 
#======================fim da cláusula 20 ==================

#===================cláusula 21===========================

     st.write("### CLÁUSULA 21ª – DAS REGRAS DOS GRUPOS DE WHATSAPP E TELEGRAM ")

     with st.container(key="clausula_ 21.1"):
        st.markdown("""
       21.1. Os grupos e canais de WhatsApp e Telegram são instrumentos de comunicação e networking entre associados. 
       
       21.2. É vedado utilizar os grupos para: 
       
       a) conteúdo ilegal;
      
       b) discurso de ódio, discriminação ou ameaça; 
       
       c) assédio; 
       
       d) spam excessivo; 
       
       e) divulgação repetitiva não autorizada; 
       
       f) compartilhamento de dados pessoais de terceiros sem autorização; 
       
       g) conteúdo que viole direitos autorais ou de imagem; 
       
       h) qualquer atividade que prejudique o funcionamento do grupo ou a convivência entre os associados. 
       
       21.3. O CLUBE poderá advertir, restringir ou remover o ASSOCIADO dos grupos quando houver descumprimento das regras, sem prejuízo das demais medidas contratuais cabíveis. 
       
       21.4. A remoção de grupo de comunicação em razão de violação das regras não implica automaticamente cancelamento da associação, salvo se a conduta também caracterizar hipótese de rescisão. 
        
  """, unsafe_allow_html=True  )

#=================== fim da clásula 21 ===================

#===================== Cláusula 22 ========================

    st.write("### CLÁUSULA 22ª – DA AUSÊNCIA DE VÍNCULO ")

    with st.container(key="clausula_ 22.1"):
     st.markdown("""
    22.1. Este contrato não cria entre as PARTES vínculo empregatício, societário, representação comercial, franquia, mandato, agência, associação societária ou qualquer outra relação além daquela expressamente prevista neste instrumento. 
    
    22.2. O ASSOCIADO não está autorizado a assumir obrigações, realizar negócios ou representar o CLUBE perante terceiros sem autorização expressa e por escrito. 
       
         
  """, unsafe_allow_html=True  )

#=================== fim da clásula 22 ===================

#===================== Cláusula 23 ========================

    st.write("###  CLÁUSULA 23ª – DAS COMUNICAÇÕES ")

    with st.container(key="clausula_ 23.1"):
     st.markdown("""
      23.1. As comunicações relacionadas ao contrato poderão ser realizadas por e-mail, WhatsApp, plataforma do CLUBE ou outro canal eletrônico previamente informado pelo ASSOCIADO. 
      
      23.2. O ASSOCIADO é responsável por manter seus dados de contato atualizados. 
      
      23.3. Para comunicações formais relacionadas a cancelamento, rescisão ou exercício de direitos, recomenda-se a utilização de meio que permita comprovação do envio e recebimento. 
      
      23.4. O e-mail indicado no cadastro será considerado canal oficial de comunicação contratual, sem prejuízo de outros meios legalmente admitidos. 
        
  """, unsafe_allow_html=True  )



     
#=================== fim da clásula 23 ===================

#===================== Cláusula 24 ========================

    st.write("###   CLÁUSULA 24ª – DA ASSINATURA ELETRÔNICA ")

    with st.container(key="clausula_ 24.1"):
     st.markdown("""
      24.1. As PARTES reconhecem como válidas as assinaturas eletrônicas realizadas por plataforma ou mecanismo que permita identificar o signatário e demonstrar sua manifestação de vontade. 
      
      24.2. O contrato poderá ser assinado fisicamente ou por meio eletrônico, produzindo os mesmos efeitos jurídicos, observada a legislação aplicável.
     
      24.3. Cada parte poderá manter cópia física ou digital deste instrumento e de seus anexos. 
  """, unsafe_allow_html=True  )

         
#=================== fim da clásula 24===================
    
#===================== Cláusula 25=========================
     
    st.write("###   CLÁUSULA 25ª – DA INTEGRIDADE DO CONTRATO ")
     
    with st.container(key="clausula_ 25.1"):
      st.markdown("""
       
         25.1. Este instrumento, juntamente com seus anexos e documentos expressamente incorporados, representa o acordo entre as PARTES quanto ao objeto contratado. 
         
         25.2. Eventual tolerância de uma das PARTES quanto ao descumprimento de determinada obrigação não constituirá renúncia, novação ou alteração contratual. 
         
         25.3. Caso qualquer disposição deste contrato seja considerada inválida ou inexigível, as demais disposições permanecerão em vigor, na máxima extensão permitida pela legislação. 

         25.4. Qualquer alteração relevante deste contrato deverá ser formalizada por escrito, ressalvadas as atualizações permitidas pela legislação e pelas regras específicas de renovação.      
     """, unsafe_allow_html=True)


         
  #=================== fim da clásula 25===================
      
  #===================== Cláusula 26=========================
       
      st.write("### CLÁUSULA 26ª – DO FORO  ")
       
      with st.container(key="clausula_ 26.1"):
        st.markdown("""
         26.1. As PARTES buscarão solucionar amigavelmente eventuais divergências decorrentes deste contrato. 
         
         26.2. Nas relações que não estejam sujeitas a regra legal específica de competência, fica eleito o foro da Comarca de ______________________________, Estado de ____________, para dirimir questões decorrentes deste contrato. 
         
         26.3. Caso seja aplicável legislação de proteção ao consumidor que estabeleça foro diverso ou mais favorável ao consumidor, será respeitada a competência legalmente prevista.
       """, unsafe_allow_html=True)
     
  #=================== fim da clásula 26===================
      
  #===================== Cláusula 27=========================
       
      st.write("###  CLÁUSULA 27ª – DA DECLARAÇÃO DE CIÊNCIA E ACEITE ")
       
      with st.container(key="clausula_ 27.1"):
        st.markdown("""
         27.1. O ASSOCIADO declara que: 
         a) recebeu informações suficientes sobre o objeto da contratação; 
         
         b) teve oportunidade de conhecer previamente este contrato; 
         
         c) compreendeu que se trata de Plano Anual com vigência de 12 (doze) meses; 
         
         d) compreendeu a diferença entre o preço à vista e o preço parcelado, quando aplicável; 
         
         e) está ciente de que determinados eventos, cursos ou programas poderão exigir pagamento adicional; 
         
         f) está ciente de que o CLUBE não garante resultados comerciais ou financeiros; 
         
         g) está ciente das regras de cancelamento e da eventual multa compensatória; 
         
         h) teve acesso à Política de Privacidade; 
         
         i) compromete-se a observar as normas de convivência do CLUBE. 
         
         27.2. As cláusulas que estabelecem vigência anual, cancelamento antecipado, multa, inadimplência, uso de imagem, propriedade intelectual e tratamento de dados deverão ser apresentadas ao ASSOCIADO de forma clara e destacada. 
       """, unsafe_allow_html=True)
 #=================== fim da clásula 27===================
      
#===================== Cláusula  28=========================
       
      st.write("###  CLÁUSULA 28ª – DOS ANEXOS ")
       
      with st.container(key="clausula_ 28.1"):
        st.markdown("""
         8.1. Integram este contrato, quando aplicáveis:
         
         **ANEXO I – Política de Privacidade;**

         **ANEXO II – Regulamento de Convivência e Uso dos Grupos;**

         **ANEXO III – Tabela de Benefícios e Serviços Adicionais;**

         **ANEXO IV – Termo de Autorização de Uso de Imagem, Voz e Nome;**

         **ANEXO V – Termo de Autorização de Compartilhamento de Dados para Networking.** 
         
         28.2. Em caso de divergência entre este contrato e material publicitário ou mensagem comercial, prevalecerão as condições expressamente formalizadas neste instrumento, sem prejuízo dos direitos legalmente assegurados ao ASSOCIADO.

       """, unsafe_allow_html=True)

#=================fim da cláusula 28 =====================


#====================Quadro de resumo do contrato==============


    st.write("### QUADRO RESUMO DA CONTRATAÇÃO ")

    with st.container(key="campos_4"):

      st.write("**Plano contratado:** PLANO ANUAL ")

      with st.container(key="datas_resumo"):
        data_de_incio = st.text_input("**Data de inicio:**", key="data_inicio")
        data_de_termino = st.text_input("**Data de término:**", key="data_final")



      st.write("**Valor à vista:** R$ 1.490,00 ")
      st.write("**Valor à vista:** R$ 1.490,00 ")
      st.write("**Total no parcelamento:** R$ 1.798,80 ")

    forma_pagamento = st.radio(
    " **Forma de pagamento:**",
    [
        "PIX",
        "DINHEIRO",
        "CARTÃO DE CRÉDITO",
        "BOLETO BANCÁRIO"
    ], 
)

    with st.container(key="data_vencimento"):
      data_vencimento = st.text_input("**data do primeiro vencimento:**", key="data_de_vencimento")


    with st.container(key="parcela"):
      quantidade_parcelas = st.text_input("**Quantidade de parcelas:**", key="quantidade_parcela")

      valor_parcela = st.text_input("**Valor da parcela: R$**", key="valor_parcela")


#=====================declaração final =========================
    st.write("### DECLARAÇÃO FINAL ")

    st.text("E, por estarem de acordo com as condições estabelecidas neste instrumento, as PARTES declaram que leram, compreenderam e aceitaram suas disposições, firmando o presente contrato para todos os fins de direito. ")

    with st.container(key="declaracao_final_local"):
      local = st.text_input("Local:", key="local")

    with st.container(key="declaracao_final_data"):
      data4 = st.text_input("Data:", key="data4")

#=====================contratante-associado=======================

    st.write("### CONTRATANTE – ASSOCIADO ")

    with st.container(key="contratante_associado"):
      nome_associado = st.text_input("**Nome/Razão Social:**", key="nome_associado")
      cpf_associado = st.text_input("**CPF/CNPJ:**", key="cpf_associado")

     #espaçamento de paragrafos
    st.markdown("<br>", unsafe_allow_html=True)

    st.write("Assinatura:_____________________________________")

#=====================contratada=================================

    st.write("### CONTRATADA – CLUBE ALÔ CAMPINAS E REGIÃO ")

    with st.container(key="clausula_ .1"):
     st.markdown("""
      Razão Social:

      CNPJ:

      Representant Legal:

      CPF:

      Assinatura
        
  """, unsafe_allow_html=True  )

#=====================testemunhas===============================

    st.write("### TESTEMUNHAS ")

    st.write("**1. Testemunha**")

    nome_testemunha1 = st.text_input(
      "Nome:",
       key="nome_testemunha1"
     )

    cpf_testemunha1 = st.text_input(
      "CPF:",
      key="cpf_testemunha1"
   )

    
    #espaçamento de paragrafos
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.write(" Assinatura:__________________________________________________")

    #espaçamento de paragrafos
    st.markdown("<br>", unsafe_allow_html=True)

    st.write("**2. Testemunha**")

    nome_testemunha2 = st.text_input(
      "Nome:",
      key="nome_testemunha2"
    )

    cpf_testemunha2 = st.text_input(
      "CPF:",
      key="cpf_testemunha2"
    )
        
        #espaçamento de paragrafos
    st.markdown("<br>", unsafe_allow_html=True)
        
    st.write(" Assinatura:__________________________________________________")

     #espaçamento de paragrafos
    st.markdown("<br>", unsafe_allow_html=True)


    dados = {
    "nome_completo": nome_completo,
    "rg": rg,
    "cpf": cpf,
    "cidade_uf": cidade_Uf,
    "email": email,
    "contato": contato,

    "razao_social": razao_social,
    "nome_fantasia": nome_fantasia,
    "cnpj": cnpj,
    "representante_legal": representante_legal,
    "cpf_representante": cpf_representante,
    "rg_representante": rg_representante,
    "email_juridica": email_juridica,
    "telefone_juridica": telefone_juridica,

    "data_inicio": data_inicio,
    "data_final": data_final,

    "autoriza_imagem": autoriza,
    "nao_autoriza_imagem": nao_autoriza,
    "nome_cl14": nome_cl14,
    "data_imagem": data,

    "forma_pagamento": forma_pagamento,

    "data_vencimento": data_vencimento,
    "quantidade_parcelas": quantidade_parcelas,
    "valor_parcela": valor_parcela,

    "local": local,
    "data_final_contrato": data4,

    "nome_associado": nome_associado,
    "cpf_associado": cpf_associado,

    "nome_testemunha1": nome_testemunha1,
    "cpf_testemunha1": cpf_testemunha1,

    "nome_testemunha2": nome_testemunha2,
    "cpf_testemunha2": cpf_testemunha2
}
    

    if st.button("Finaliza e enviar ", key="botao"):
       gerar_pdf(dados)

contrato()
