# Atividade Prática - Banco de Dados II

**Aluno:** Gustavo Romão
**Disciplina:** Banco de Dados II

## Descrição

Este script em Python demonstra algumas operações básicas do sistema operacional utilizando as bibliotecas `os` e `subprocess`:

- Exibe o diretório atual de execução do script;
- Exibe o ID (PID) do processo em execução;
- Abre o aplicativo Bloco de Notas (Notepad) através de um subprocesso;
- Cria um arquivo de texto (`Arquivo_aula.txt`) e escreve uma frase nele.

## Como executar

```bash
python aula.py
```

> Obs: o comando `subprocess.run("notepad")` funciona apenas em sistemas Windows.

## Saída esperada

Ao executar o script, será impresso no terminal o diretório atual e o PID do processo, o Bloco de Notas será aberto, e um arquivo `Arquivo_aula.txt` será criado na mesma pasta do script.