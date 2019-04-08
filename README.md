# PythonBmpGreenColors

Repositório para o trabalho de faculdade de Python - Uniasselvi Famemblu Campus I.

Classe Python que lê cores Verdes em imagem .bmp e grava um log.txt 

## Como Usar

Basta clonar o repositório para o diretório onde desejar usando `git clone`, colocar as imagens na pasta **\images** e executar o arquivo `read_images.py`. 

Será lido todas imagens do formato `.bmp`, e será gravado as informações no arquivo de log, com o nome *log_dia_atual.txt*.

## Justificativa

Fiz essa classe pensando em facilitar o estudo de regiões de mapas, para uma melhor acurácia na medição de áreas verdes, e de forma simples, apenas colocando as imagens em uma pasta específica.

## Objetivos

**O que se espera com essa classe?**

Ler uma quantidade de arquivos e verificar a quantidade de pixels em tons de verde em cada um destes arquivos, com base nas cores RGB, e gravar um log com as informações dos arquivos.

**Os Resultados que se pretende alcançar**

Ler uma determinada região do mapa, e dizer quanto % daquela região possui área verde. Útil para estudos de mapas.

**As soluções que se pretende dar com esta classe**

-Ler uma quantidade qualquer de arquivos de forma simples
-Ter a informação de área verde do mapa de forma rápida e prática
-Realizar estudos na região do mapa de acordo com o resultado da análise que a classe faz

## Conclusão

A classe lê as imagens e grava um arquivo de log com as informações de: 

*Data e Hora da Leitura*

*Nome do Arquivo*

*Largura e Altura*

*Quantidade total de Pixels*

*Quantidade total de Pixels Verdes*

*% de pixels verdes em relação a quantidade total*
