CONTRATO ONLINE — CLUBE ALÔ CAMPINAS E REGIÃO

Este projeto foi desenvolvido para facilitar e digitalizar o processo de contratação do Clube Alô Campinas e Região.

O sistema permite que o associado preencha seus dados diretamente pela página do contrato, escolha o plano, informe as condições de pagamento e preencha as demais informações necessárias para a contratação.

Depois que o formulário é finalizado, os dados preenchidos são utilizados para gerar automaticamente o contrato em formato PDF. Após a geração do documento, o sistema também realiza o envio do contrato por e-mail.

O objetivo principal é deixar o processo mais rápido e organizado, evitando que o contrato precise ser preenchido manualmente e reduzindo a necessidade de inserir novamente as mesmas informações.


INSTALÇÃO DAS FERRAMENTAS:

nesse projeto foi utilizado as principais ferramentas:
streamli
reportlab
python-dotenv

para instalr tudo: pip install streamlit reportlab python-dotenv



TECNOLOGIAS UTILIZADAS

Python

Python é a linguagem principal utilizada no projeto. 
Ela é responsável pela lógica do sistema, tratamento dos dados preenchidos no formulário, geração do PDF e envio do contrato por e-mail.


Streamlit

Streamlit é utilizado para criar a interface web do sistema.

Com ele foram criados os campos de preenchimento, títulos, textos, opções de planos, formas de pagamento, caixas de seleção, botões e mensagens apresentadas ao usuário.

O Streamlit também é responsável por executar a aplicação e disponibilizá-la no navegador.

PARA RODAR O PROJETO: streamlit run contrato.py (esse comando vai rodar a parte principal aonde sera exibido no navegador com as cláusulas textos e campos para preencher)



ReportLab

ReportLab é utilizado para gerar o contrato em PDF.

Os dados preenchidos no formulário são enviados para a função responsável pela geração do documento, que utiliza o ReportLab para montar o contrato com suas cláusulas, informações do associado e demais dados da contratação.




python-dotenv

A biblioteca python-dotenv é utilizada para trabalhar com as variáveis de ambiente do projeto.

Ela permite manter informações sensíveis, principalmente as credenciais utilizadas para o envio de e-mails, fora do código principal.


SMTP / Gmail

O sistema utiliza SMTP para realizar o envio dos contratos por e-mail.

A conta utilizada para o envio possui suas informações configuradas através das variáveis de ambiente, evitando que as credenciais fiquem diretamente escritas no código.


ESTRUTURA DO PROJETO

O projeto possui a seguinte estrutura:

contrato-online/

contrato.py

gerar_pdf.py

email_service.py

css/

estilo.css

.env

.env.example

.gitignore

requirements.txt

README.md


CONTRATO.PY

Este é o arquivo principal da aplicação.

Nele fica a maior parte da interface do contrato e os campos que serão preenchidos pelo associado.

Também ficam neste arquivo as opções de plano, datas, formas de pagamento, autorizações, informações de pessoa física e pessoa jurídica e o botão responsável por finalizar o contrato.

Depois que o formulário é preenchido, as informações são organizadas em um dicionário chamado "dados". Esse dicionário é utilizado pelas outras partes do sistema.


GERADOR_PDF.PY

Este arquivo é responsável pela geração do contrato em PDF.

A função principal deste arquivo é "gerar_pdf(dados)".

Ela recebe as informações preenchidas no formulário e utiliza o ReportLab para montar o documento final.

A separação da geração do PDF em um arquivo próprio facilita futuras alterações no layout ou no conteúdo do contrato sem precisar modificar toda a aplicação principal.


GERAR_EMAIL.PY

Este arquivo é responsável pelo envio do contrato por e-mail.

A função principal é "enviar_email(dados)".

Ela recebe os dados necessários, acessa as configurações de e-mail definidas nas variáveis de ambiente, monta a mensagem e adiciona o PDF gerado como anexo.

A separação do envio de e-mail em um arquivo próprio também facilita futuras alterações nessa parte do sistema.



style.CSS

Esta pasta contém o arquivo responsável pela aparência visual do formulário.

O arquivo "estilo.css" possui as regras de CSS utilizadas para personalizar os elementos do Streamlit.

Ele foi utilizado principalmente para modificar a aparência dos campos, títulos, espaçamentos e outros elementos da página, deixando o formulário mais próximo da aparência de um documento de contrato.


.ENV

O arquivo ".env" é utilizado para armazenar informações sensíveis utilizadas pelo sistema.

Entre essas informações estão os dados da conta responsável pelo envio dos e-mails e o endereço que receberá os contratos.

Esse arquivo não deve ser enviado para o GitHub, pois contém informações privadas.




.ENV.EXAMPLE

O arquivo ".env.example" serve como modelo das variáveis que o sistema precisa.

Ele não contém as informações reais da conta de e-mail.

Sua função é apenas mostrar quais variáveis precisam existir quando o sistema for configurado em outro ambiente.


.GITIGNORE

O ".gitignore" informa ao Git quais arquivos não devem ser enviados para o GitHub.

No projeto ele é utilizado principalmente para impedir que o arquivo ".env", arquivos temporários e arquivos gerados pelo sistema sejam publicados junto com o código.


REQUIREMENTS.TXT

O arquivo "requirements.txt" contém as bibliotecas externas utilizadas pelo projeto.

Entre elas estão:

streamlit

reportlab

python-dotenv

requests

Esse arquivo facilita a identificação das dependências necessárias para executar a aplicação.



COMO RODAR O STREAMLIT

Para executar o sistema localmente, é necessário estar dentro da pasta do projeto.

Com o ambiente Python configurado e as dependências instaladas, o Streamlit pode ser iniciado utilizando o comando:

streamlit run contrato.py

Depois de executar o comando, o Streamlit inicia a aplicação e disponibiliza o endereço para acesso pelo navegador.

Normalmente o endereço local será:

http://localhost:8501

ou:

http://127.0.0.1:8501



FUNCIONAMENTO DO SISTEMA

A aplicação começa pelo arquivo "contrato.py", onde o associado preenche todas as informações necessárias.

Os valores preenchidos são armazenados pelo Streamlit e posteriormente reunidos no dicionário "dados".

Esse dicionário contém as informações necessárias para gerar o contrato e realizar o envio.

A função "gerar_pdf(dados)" utiliza essas informações para criar o contrato em PDF.

Depois da geração do documento, a função "enviar_email(dados)" utiliza o PDF gerado e realiza o envio através do serviço de e-mail configurado.

Ao final do processo, o sistema apresenta uma mensagem informando se o contrato foi finalizado corretamente ou se ocorreu algum problema.


OBSERVAÇÃO 

O projeto foi separado em diferentes arquivos para facilitar sua manutenção.

O arquivo "contrato.py" concentra a aplicação e o formulário.

O arquivo "gerar_pdf.py" concentra a geração do contrato.

O arquivo "email_service.py" concentra o envio dos e-mails.

A pasta "css" concentra a parte visual.

Dessa forma, cada parte principal do sistema possui sua própria responsabilidade, facilitando futuras alterações e manutenção do projeto.


CUIDADOS:

Por preferência, evite rodar o sistema no navegador Microsoft Edge, pois durante os testes ele apresentou alguns problemas no envio das informações dos campos, fazendo com que alguns dados chegassem vazios. Fora isso, outros navegadores podem acessar normalmente, o mais recomendado principalmente é o Google Chrome.


Os campos do formulário não possuem preenchimento obrigatório e o sistema não avisa quando algum campo fica vazio. Isso foi feito porque pode haver situações em que o associado não tenha algum dado necessário no momento ou não queira informar determinado dado, então para não preujudicar a continuação associado ao preenchimento do contrato foi tomado essa decisão.

Por isso, é recomendado conferir todos os campos antes de finalizar e enviar o contrato, verificando se todas as informações necessárias foram preenchidas corretamente.
