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