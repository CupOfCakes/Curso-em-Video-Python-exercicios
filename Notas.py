'''
======MODULO======
import _: importa uma biblioteca / https://docs.python.org/3/library/index.html
from _ import _: importa um comando especifico de uma biblioteca

======MATEMATICA======
procedencia = (); **; * / // %; + -
** = potencia
// = divisão sem virgula
% = resto da divisão
raiz = x**(1/2)
abs(): inverte o sinal do numero

=======MANIPULADOR DE PRINT======
\n = quebra linha ; end= =adiciona algo ao final da linha e não quebra a linha
{:._f} numero de numeros apos a virgula em numeros floats, usando o format

=======MODULO MATH======
raiz = math.sqrt(_)
math.ceil = arredondar para cima
math.floor = ar redondar para baixo

======MODULO RANDOM======
random.choice() escolhe uma coisa aleatoria em uma lista
random.shuffle() embaralha uma lista
random.randint(_,_) escolhe um numero aleatorio de _ ate _

======MODULO DATETIME======
datetime.date.today().year : da o ano atual no calendario do pc

======MODULO TIME======
sleep(_) o computador "dorme" por segundos

======MODULO OPERATOR======
itemgetter(1): pega os valores em um dicionario
itemgetter(0): pega os nomes dos valores em um dicionario

======ANALISE DE STRING======
_[_:_:_:] começa, termina -1, pula
len() quantidade de letras
_.count(_,_,_) contata a quantidade de alguma coisa, começo, termina
_.find(_) encontra a onde começa alguma coisa na frase, se não tiver retorna -1
_ in _ verifica se existe
_.replace(_,_) troca
_.upper() transforma em maiusculo
_.lower() transforma em minusculo
_.capitalize transforma a 1 letra em maiusculo e o resto em minusculo
_.title transforma a 1 letra de cada palavra em maiusculo, se baseando nos espaços
_.strip() remove espaços em branco no começo e fim
_.rstrip() remove os espaços em branco do final
_.lstrip() remove os espaços em brancos do começo
_.split() divide a frase em palavras sem ligação e junta em um lista ex: (come churros) 1 frase === (come) (churros) 2 palavras
' ' .join(_) junta palavras em uma frase, o espaço no começo e o caractere q ira unilos

======CONDICIONAIS======
if_: se
else: senão

======CORES======
\33[_:_:_m style, text, background
style: 0 padrão, 1 negrito, 4 underline, 7 invertido
text: 30 a 37 adiciona cor ao texto [branco, vermelho, verde, amarelo, azul, roxo, ciano, cinza]
background: 40 a 47 o mesmo do text

======VARIAVEIS COMPOSTAS   ======
max(_): da o maior valor da lista
min(_): da o menor valor da lista
_.sort(); sorted(): ordena em ordem crescente
_.sort(reverse=True): ordena em ordem decrescente
[:]: cria uma copia da lista
.index(_): mostra a posição de um valor na lista a 1 vez que ele aparece

======REPETIÇÃO======
for _ in range(_,_,_): repeti começa, termina, tipo de interação
while ___: repeti algo com uma condição

======(TUPLAS)======
*tuplas são imutaveis

======[LISTAS]======
_.append(_): adiciona um valor ao final da lista
_.insert(_,_): adiciona um valor a uma lugar da lista e empurra pra frente os valores a frente
del; _pop(); _.remove('_'); _.clear(): deleta um valor e reposiciona o resto
list(): cria uma lista

======{DICIONARIOS}======
*da nome aos valores de listas
_=dict(): cria um dicionario
_= ("_":_) denomina um nome e valor no dicionario
print(_.values()): pega o valor na lista
print(_.keys()): pega o nome do dicionario do item
print(_.items()): pega ambos nome e valor
.copy(): faz uma copia

======FUNÇÕES======
def _(_): cria uma função
*_: a quantidade de paremetros e indefinida
"""___""": cria uma descrição para a função
help(): mostra a descrição da função
print(_.__doc__): mostra a descrição da função, doc e escrito com 2 underline antes e depois
return _: colocar o valor de uma variavel da função dentro de uma variavel global

======ERROS======
try:: tenta rodar o codigo dentro
except:: roda se o try der erro
except exception as error:: torna possivel mostrar o tipo de erro ocorrido
else:: roda se o try funcionar sem erro
finally:: roda independente de try ou except

======ARQUIVO======
_.close(): fecha um arquivo
open(_,"*codigos abaixo*"): abri um arquivo
wt+: cria o arquivo
rt: le o arquivo
at: escreve no arquivo
'''


