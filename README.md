Atualmente o projeto se encontra arquivado, mas será desenvolvido de forma livre para fins de contribuição geral por mim
- "toda trabalho que envolve dados, sobretudo não-estruturados revelam grandes desafios a se transpor"

- Inspiração de projeto: Meu Querido diário da Open Knowledge, Tesseract
- Requisitado pela Superintendência De Controle Externo

**Resultado final esperado para as partes interessadas:**
- Planilha contemplando informações definitivas sobre as entidades e instrumentos jurídicos extraídos dos Diários Oficiais em seus respectivos sites.
- Com os seguintes segmentos

> Instrumento jurídico (os, osc, oscip, sistema s)
> entidade de contrato(prestadores)
> duração do contrato(de acordo com o acordo firmado)
> início da vigência(quando começou formalmente)

Esboço de tabela:

| Instrumento Jurídico | Entidade de Contrato | Duração | Início da vigência |
| -------------------- | -------------------- | ------- | ------------------ |
|                      |                      |         |                    |
|                      |                      |         |                    |


Sequências básicas do projeto:
- coletar e avaliar: obter arquivos de diários oficiais na fonte, os _sites_ dos municípios 
- processar: aplicar tratamentos sobre os arquivos originais obtidos, elaborando a lógica de captura dos dados desejado
- transformar: Identificação, limpeza e agregação de dados, gerando no final uma estrutura de dados consolidados com pandas
- Aplicar computação paralela com multithreading para processamento em massa

Tecnologias e recursos que serão utilizados: 
> Ocr, ou processamento textual
> Regex
> Algortimos de busca, pesquisa binária
> multitrheading
- Scrapy- para crawling  

Objetos-alvo da coleta
- objetos únicos: diário de cada munícpio
- Objetos agregados: diário com várias munícipios
- objetos fragmentados: vários arqquivos para um munícpio




Categorias a serem usadas que serão pesquisadas nos sites e documentos:
- ano de ínicio
- duração do contrato
- Tipos de instrumento jurídico
	1. oscip ORGANIZAÇÃO DA SOCIEDADE CIVIL DE INTERESSE PÚBLICO
	2. os - ORGANIZAÇÃO SOCIAL
	3. osc -ORGANIZAÇÃO DA SOCIEDADE CIVIL







# Lista de municípios a serem pesquisados (131):
Municipio
ALAGOINHAS
ALCOBACA
AMELIA RODRIGUES
ANTONIO GONCALVES
BAIXA GRANDE
BARRA
BARRA DA ESTIVA
BARREIRAS
BARROCAS
BOA VISTA DO TUPIM
BOM JESUS DA LAPA
BROTAS DE MACAUBAS
BRUMADO
BUERAREMA
CABACEIRAS DO PARAGUACU
CACHOEIRA
CACULE
CAETITE
CAIRU
CALDEIRAO GRANDE
CAMACAN
CAMACARI
CAMAMU
CAMPO FORMOSO
CANARANA
CANDEIAS
CANSANCAO
CARAVELAS
CARINHANHA
CASTRO ALVES
CATU
CICERO DANTAS
CONCEICAO DA FEIRA
CONCEICAO DO COITE
CONCEICAO DO JACUIPE
CORACAO DE MARIA
CORIBE
CORRENTINA
CRUZ DAS ALMAS
DIAS DAVILA
ENTRE RIOS
ESPLANADA
EUCLIDES DA CUNHA
EUNAPOLIS
FEIRA DE SANTANA
GANDU
GLORIA
GOVERNADOR MANGABEIRA
GUANAMBI
IBIRAPITANGA
IBITIARA
IGRAPIUNA
ILHEUS
IPECAETA
IPIAU
IPIRA
IRARA
IRECE
ITABUNA
ITACARE
ITAJUIPE
ITAMARAJU
ITANHEM
ITAPICURU
ITIRUCU
ITIUBA
ITORORO
JACARACI
JACOBINA
JAGUAQUARA
JEQUIE
JIQUIRICA
JOAO DOURADO
JUAZEIRO
LAMARAO
LAPAO
LAURO DE FREITAS
LIVRAMENTO DE NOSSA SENHORA
LUIS EDUARDO MAGALHAES
MADRE DE DEUS
MATA DE SAO JOAO
MILAGRES
MONTE SANTO
MORRO DO CHAPEU
MUCURI
MURITIBA
MUTUIPE
NAZARE
NILO PECANHA
NOVA FATIMA
OLINDINA
OLIVEIRA DOS BREJINHOS
PALMEIRAS
PAULO AFONSO
PILAO ARCADO
POJUCA
PONTO NOVO
PORTO SEGURO
PRADO
PRESIDENTE TANCREDO NEVES
RIACHAO DO JACUIPE
RIACHO DE SANTANA
RIBEIRA DO POMBAL
RODELAS
RUY BARBOSA
SALVADOR
SANTA CRUZ CABRALIA
SANTANOPOLIS
SANTO AMARO
SANTO ANTONIO DE JESUS
SANTO ESTEVAO
SAO DOMINGOS
SAO FRANCISCO DO CONDE
SAO MIGUEL DAS MATAS
SAO SEBASTIAO DO PASSE
SAUBARA
SENHOR DO BONFIM
SERRINHA
SIMOES FILHO
SOBRADINHO
TAPIRAMUTA
TEIXEIRA DE FREITAS
UBAITABA
URUCUCA
VALENCA
VARZEA DA ROCA
VITORIA DA CONQUISTA
WAGNER
WENCESLAU GUIMARAES
XIQUE-XIQUE

