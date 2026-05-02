# Projeto: Estruturas Lineares em Python

Atividade prática da disciplina de Programação de Computadores — 1º Semestre 2026.  
Professor: Marco Antonio

---

## Desafio 1 — Sistema de Votação de Representantes

### Qual problema resolve?
Simula uma eleição entre três candidatos: Ana, Bruno e Carlos. O programa registra os votos informados pelo usuário e, ao final, apura o resultado — anunciando o vencedor ou informando se houve empate.

### Estruturas utilizadas
- **Lista** para armazenar os votos
- **Loop while** para coletar os votos repetidamente
- **Loop for** para contar os votos de cada candidato
- **Condicionais (if/elif/else)** para validar entradas e identificar o vencedor

### Como executar
```bash
python desafio_01_votacao.py
```

### Exemplo de entrada e saída
```
Digite o nome do candidato (fim para encerrar): Ana
Digite o nome do candidato (fim para encerrar): Bruno
Digite o nome do candidato (fim para encerrar): Ana
Digite o nome do candidato (fim para encerrar): fim

Resultado da votação:
Ana: 2 votos
Bruno: 1 votos
Carlos: 0 votos
O vencedor é: Ana
```

---

## Desafio 2 — Editor de Texto com Pilha (Desfazer)

### Qual problema resolve?
Simula um editor de texto simples com a funcionalidade de desfazer. O usuário pode digitar palavras, desfazer a última palavra digitada, visualizar o texto atual ou sair do programa.

### Estruturas utilizadas
- **Lista usada como Pilha (Stack)** com comportamento LIFO (Last In, First Out)
- **append()** para adicionar palavras no topo da pilha
- **pop()** para remover a última palavra adicionada
- **Loop while** para manter o menu ativo
- **Condicionais (if/elif)** para tratar cada opção do menu

### Como executar
```bash
python desafio_02_editor_pilha.py
```

### Exemplo de entrada e saída
```
EDITOR DE TEXTO
[1] - Digitar palavra
[2] - Desfazer última palavra
[3] - Mostrar texto
[4] - Sair
Escolha uma opção: 1
Digite uma palavra: minha
Palavra adicionada: minha

Escolha uma opção: 1
Digite uma palavra: terra
Palavra adicionada: terra

Escolha uma opção: 3
Texto atual: minha terra

Escolha uma opção: 2
Palavra removida: terra

Escolha uma opção: 3
Texto atual: minha
```

---

## Desafio 3 — Fila de Atendimento Universitário

### Qual problema resolve?
Simula o sistema de atendimento da secretaria de uma universidade. Os alunos retiram uma senha conforme a ordem de chegada e são atendidos na mesma ordem — o primeiro a chegar é o primeiro a ser atendido.

### Estruturas utilizadas
- **Lista usada como Fila (Queue)** com comportamento FIFO (First In, First Out)
- **append()** para adicionar alunos no final da fila
- **pop(0)** para chamar o primeiro aluno da fila
- **Loop while** para manter o menu ativo
- **Condicionais (if/elif)** para tratar cada opção do menu

### Como executar
```bash
python desafio_03_fila_atendimento.py
```

### Exemplo de entrada e saída
```
SECRETARIA ACADÊMICA
[1] - Retirar senha
[2] - Chamar próximo aluno
[3] - Mostrar fila
[4] - Sair
Escolha uma opção: 1
Nome do aluno: Ana
Ana entrou na fila de atendimento.

Escolha uma opção: 1
Nome do aluno: João
João entrou na fila de atendimento.

Escolha uma opção: 3
Fila atual:
1º - Ana
2º - João

Escolha uma opção: 2
Chamando aluno: Ana

Escolha uma opção: 3
Fila atual:
1º - João
```
