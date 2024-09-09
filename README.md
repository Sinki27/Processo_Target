## Desafios

Este repositório contém a minha resolução para diversos desafios de programação. Os desafios foram realizados em Python.

### Desafio: Verificar Números na Sequência de Fibonacci

**Descrição:**
Este desafio consiste: 

Função pertence_fibonacci(num):

a, b = 0, 1: Inicializa as duas primeiras variáveis da sequência.
while b <= num: Enquanto o valor atual (b) for menor ou igual ao número informado, o loop continua.
if b == num: Se o valor atual for igual ao número informado, o número pertence à sequência.
a, b = b, a + b: Atualiza os valores de a e b para os próximos termos da sequência.
Entrada do Usuário:

numero = int(input("Digite um número: ")): Lê o número informado pelo usuário e converte para inteiro.
Verificação e Saída:

if pertence_fibonacci(numero): Chama a função para verificar se o número pertence à sequência.
print(...) Imprime a mensagem correspondente ao resultado.

**Código:**
```python
def pertence_fibonacci(num):
  """Verifica se um número pertence à sequência de Fibonacci.
  Args:
    num: O número a ser verificado.
  Returns:
    True se o número pertence à sequência, False caso contrário.
  """
  a, b = 0, 1
  while b <= num:
    if b == num:
      return True
    a, b = b, a + b
  return False
# Entrada do usuário
numero = int(input("Digite um número: "))
# Verificação e saída
if pertence_fibonacci(numero):
  print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
  print(f"O número {numero} não pertence à sequência de Fibonacci.")
```

### Desafio: Contar Ocorrências da Letra 'a' em uma String

**Descrição:**
O usuário digita uma frase.
A frase é convertida para minúsculas.
A função count() conta quantas vezes a letra 'a' aparece na frase convertida.
O resultado é exibido para o usuário.

**Código:**
```python
def contar_as(frase):
  """Conta a quantidade de vezes que a letra 'a' (maiúscula ou minúscula) aparece em uma string.
  Args:
    frase: A string a ser analisada.
  Returns:
    O número de ocorrências da letra 'a'.
  """
  # Converte toda a string para minúsculas para facilitar a contagem
  frase_minuscula = frase.lower()
  # Conta as ocorrências da letra 'a'
  contador = frase_minuscula.count('a')
  return contador
# Solicita a entrada do usuário
texto = input("Digite uma frase: ")
# Chama a função e exibe o resultado
quantidade_as = contar_as(texto)
print(f"A letra 'a' aparece {quantidade_as} vezes na frase.")
```

### Desafio: Analisando o Código e Calculando o Valor Final de SOMA

**Descrição:**
Declaração de variáveis:

INDICE: Define o valor limite da soma (12).
SOMA: Inicializa a variável que irá armazenar o resultado da soma (0).
K: Um contador que inicia em 1 e será incrementado a cada iteração do loop.
Laço enquanto:

Condição: O loop continua enquanto K for menor que INDICE.
Corpo do loop:
K = K + 1: Incrementa o valor de K em 1 a cada iteração.
SOMA = SOMA + K: Adiciona o valor atual de K à variável SOMA.
Impressão:

imprimir(SOMA): Após o término do loop, o valor final de SOMA é impresso.

**Código:**
```python
INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)
#Resultado = 77
```

### Desafio: Analisando a logica da sequencia de elementos 

**Descrição:**
As sequências a), b), c), d) e e) possuem padrões matemáticos claros. A sequência f) não apresenta um padrão numérico óbvio.

**Solução:**
```txt
Questões
a) 1,3,5,7, __
b) 2,4,8,16,32,64, __
c) 0,1,4,9,16,25,36, __
d) 4,16,36,64, __
e) 1,1,2,3,5,8, __
f) 2,10,12,16,17,18,19, __

Respostas 
a) 9
b) 128
c) 49
d) 100
e) 13
f) Não parece ter um padrão.
```

### Desafio: Desvendando o Mistério dos Interruptores: Uma Solução em Duas Visitas

**O Problema:**

Você está em uma sala com três interruptores, cada um ligado a uma lâmpada em salas diferentes. Sua missão é descobrir qual interruptor controla qual lâmpada, fazendo apenas duas idas até as salas das lâmpadas.

**Solução:**

Eu ligaria o primeiro interruptor e o deixaria ligado para a lampada aquecer, depois de um tempo ligado eu desligaria e agora sim o segundo eu ligaria. Ao chegar na primeira sala, se eu encontra a lâmpada apagada e quente quer dizer que é o interruptor 1, caso ela esteja ligada essa é o interruptor 2, e se estiver apagada é fria é a terceira opção que não mexida ainda. Isso significa que na primeira vista eu descubro uma opção. Exemplo caso a lampada esteja apaguada e fria na primeira, na segunda visita eu vou ligar deixar ligado o segundo interruptor e vou para a segunda sala. Se a lâmpada estiver acesa, o segundo interruptor a controla, e o restante controla a primeira lâmpada.

Desse jeito, você pode determinar qual interruptor controla cada lâmpada em apenas duas idas, utilizando o calor como indicador e a lógica de eliminação.

