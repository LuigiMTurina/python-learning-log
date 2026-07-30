# 📅 Task Tracker - Rastreador de Tarefas CLI
## Task Tracker - CLI tracker

**[PT]** Esse repositório apresenta meu segundo projeto prático desenvolvido em Python, um rastreador de tarefas exacutado na linha de comando.
O usuário consegue realizar ações no programa pelo bash, sendo capaz de:
- Adicionar tarefas
- Deletar tarefas
- Atualizar a descrição
- Atualizar o status (to-do, em progresso, feita)
- Listar as tarefas de acordo com o status

Todas as tarefas são registradas em um arquivo JSON, que é salvo no mesmo diretório no qual o programa é executado, garantindo a persistência dos dados.


**[EN]** This reposiroty presents my second practical project developed in Python, a task tracker executed on the CLI.
The user can perform actions on the program using the bash, being able to:
- Add tasks
- Delete tasks
- Update the description
- Update the status (to-do, in progress, done)
- List the tasks based on status

All of the tasks are registred in a JSON file, that is saved on the same directory where the program is executed, ensuring the data persistence.

---
## Development History

**[PT]** O programa foi desenvolvido como um desafio proposto pelo Roadmap.sh, que se encontra no link abaixo.

A ideia é que fosse um desafio particular para mim, para avaliar o meu nível de conhecimento na linguagem e o nível da minha capacidade lógica.
Da mesma forma, o propósito do repositório é apresentar projetos feitos inteiramente sem a IA, portanto, eu a utilizei somente como material de consulta
para estudar o funcionamento das funções e bibliotecas utilizadas, tendo escrito cada linha de código por conta própria
- [Link do projeto proposto](https://roadmap.sh/projects/task-tracker)

**[EN]** The program was developed as a challenge suggested by Roadmap.sh, that can be found on the link below.

The idea was that it be an particular challenge for me, to evaluate my language knowledge level and my logical capacities.
On the same way, the proposite of the repo is present projects made entirely without AI, so I used it only as consult material
to study the funtions operation and library used, writing each code line by my own
- [Link of the project suggested](https://roadmap.sh/projects/task-tracker)

---
# How to use it

**[PT]** 
### Pré-Requisitos
Verifique se você tem o [Python 3.x](https://www.python.org/downloads/) instalado no seu sistema

### Configuração
1. Clone o repositório para a sua máquina local:
    ```bash
   git clone [https://github.com/LuigiMTurina/python-learning-log.git](https://github.com/LuigiMTurina/python-learning-log.git)

2. Navegue para o diretório do projeto:
   ```bash
   cd python-learning-log/02-task-tracker-cli

### Exemplos de uso
Você pode executar a aplicação através da linha de comando chamando o script com o Python

Alguns exemplos de comando:
1. Adicionando uma tarefa
   ```bash
   py task-cli.py add "Comprar comida"

2. Atualizando a descrição de uma tarefa pelo ID
   ```bash
   py task-cli.py update 1 "Comprar leite"

3. Apagando uma tarefa pelo ID:
   ```bash
   py task-cli.py delete 1

4. Listando todas as tarefas:
   ```bash
   py task-cli.py list

5. Listando por status:
   ```bash
   py task-cli.py list in-progress


**[EN]**
### Prerequisites
Ensure you have [Python 3.x](https://www.python.org/downloads/) installed on your system

### Setup
1. Clone the repository to your local machine:
   ```bash
   git clone [https://github.com/LuigiMTurina/python-learning-log.git](https://github.com/LuigiMTurina/python-learning-log.git)

2. Navigate to the project directory:
   ```bash
   cd python-learning-log/02-task-tracker-cli

### Usage examples
You can run the application through the command line by calling the main script with Python

Some command examples:
1. Adding a task
   ```bash
   py task-cli.py add "Buy groceries"

2. Updating the description by the ID:
   ```bash
   py task-cli.py update 1 "Buy milk"

3. Deleting a task by the ID:
   ```bash
   py task-cli.py delete 1

4. Listing all the tasks:
   ```bash
   py task-cli.py list

5. Listing by status:
   ```bash
   py task-cli.py list in-progress
