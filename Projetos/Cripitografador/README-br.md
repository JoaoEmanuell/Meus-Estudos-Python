# Projeto Encrypt
Esse projeto se trata de um cripitografador de mensagens, nos teclados de telefones antigos, temos que teclar mais de uma vez uma tecla para que a letra desejada apareça, cada tecla possui um número, portanto o criptiografador ira fazer a conversão da string desejada para o número que corresponde a ela.

A formula da conversão é _N * Conjunto_, isso irá determinar o valor que a letra irá receber, ou seja depedendo do número e do conjunto, a letra irá receber um valor, começando a partir da letra A e do Número 2.

Os Números 7 e 9 são os únicos números que recebem o quarto conjunto, uma vez que os teclados de telefones antigos recebiam quatro letras ao invés das três letras que todos os outros números apresentam.

Imagem de um teclado antigo:

<p align="center">
  <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F7%2F73%2FTelephone-keypad2.svg%2F300px-Telephone-keypad2.svg.png&f=1&nofb=1" alt="Foto de um teclado de telefone antigo, a foto pertence ao site da wikipédia"/>
</p>

## Objetivos:

- [x] Criptografador.
- [x] Descriptografador.
- [x] Facilitação da entrega do código criptografado.
- [x] Interface Gráfica.

## Tabela de conversão:

Número|Letra 1|Conversão 1|Letra 2|Conversão 2|Letra 3|Conversão 3|Letra 4|Conversão 4
:---: | :---: | :---: | :---: | :---:| :---:| :---:| :---:| :---:
2 |A|2|B|22|C|222||
3 |D|3|E|33|F|333||
4 |G|4|H|44|I|444||
5 |J|5|K|55|L|555||
6 |M|6|N|66|O|666||
7 |P|7|Q|77|R|777|S|7777
8 |T|8|U|88|V|888||
9 |W|9|X|99|Y|999|Z|9999
