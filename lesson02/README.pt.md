# Estrutura de Dados #02

Você possui três funções que precisam ser completadas.

A primeira, `get_user_index_by_name`, você receberá uma lista com nomes, e deverá retornar o index que o nome do usuário estiver ou -1.

A segunda, `get_room_index_by_name`, você receberá uma matrix com nomes dos inscritos por sala, e deverá retornar o index da sala que o nome estiver ou -1.

A terceira, `get_room_and_user_indexes_name`, você receberá uma matrix com nomes dos inscritos por sala, e deverá retornar o index da sala e do aluno na sala ou [-1, -1].

## Advanced topics

### Ex.01: Flatten

Dada esta Matriz:

```py
matrix = [
  [1,2,3, [ 3, 4 ] ],
  [5, [ 8, [ 7 ] ] ],
  [ 6 ],
]
```

Crie um algoritmo que converta essa matriz em uma matriz dimensional, como este:

```py
list = [ 1, 2, 3, 3, 4, 5, 8, 7, 6 ]
```

A ordem não importa, mas cada elemento na matriz deve estar na lista final.

### Ex.02: Flatten with reference

Dada esta matriz:

```py
matrix = [
  [1, 3, [ 3 ] ],
  [ 6, [ [ [ [ [ [ [ 7 ] ], 8 ] ] ] ] ] ],
]
```

Crie um algoritmo que converte essa matriz em uma matriz dimensional, mas deve manter a referência para onde estava na matriz:

```py
reference_list = [
  { 'value': 1, 'index': [ 0, 0 ] },
  { 'value': 3, 'index': [ 0, 1 ] },
  { 'value': 3, 'index': [ 0, 2, 0 ] },
  { 'value': 6, 'index': [ 1, 0 ] },
  { 'value': 7, 'index': [ 1, 1, 0, 0, 0, 0, 0, 0, 0 ] },
  { 'value': 8, 'index': [ 1, 1, 0, 0, 0, 0, 1 ] },
]
```

A ordem não importa, mas cada elemento na matriz deve estar na lista final.

### Ex.03: Get in Matrix

Agora, usando o código criado no último exercício, crie uma função que tenha um `index` na lista processada, obtenha o elemento real na matriz.Eu quero o valor da `matrix`, mesmo que você tenha salvado o valor, ele pode mudar na matriz original.

```py
reference_list = [
  { 'value': 1, 'index': [ 0, 0 ] },
  { 'value': 3, 'index': [ 0, 1 ] },
  { 'value': 3, 'index': [ 0, 2, 0 ] },
  { 'value': 6, 'index': [ 1, 0 ] },
]

matrix = [
  [1, 3, [ 3 ] ],
  [ 6 ],
]

get_from_matrix(reference_list, matrix, 3)
#=> Deve retornar matrix[1][0], que é 6
```
