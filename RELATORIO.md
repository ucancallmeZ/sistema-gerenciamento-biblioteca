# Relatório de Testes e Feedback

## Testes realizados

### Listar documentos

- Foram incluídos arquivos PDF de exemplo na pasta `documentos`.
- O sistema listou corretamente o nome, tipo e ano de modificação de cada documento.

### Adicionar documento

- Teste com arquivo `Bora_Relembrar.pdf` a partir de um caminho completo.
- Resultado: documento adicionado com sucesso.

### Renomear documento

- Teste com o arquivo `Bora_Relembrar.pdf`, renomeado para `bora_relembrar.pdf`.
- Resultado: documento renomeado com sucesso.
- Teste com nome sem extensão → sistema respondeu com erro adequado.

### Remover documento

- Teste com o arquivo `bora_relembrar.pdf`.
- Resultado: documento removido com sucesso.

## Feedback recebido dos bibliotecários

Após demonstração do sistema, os bibliotecários sugeriram:

- **Feedback**: incluir uma mensagem de confirmação após listar os documentos (opcional).
- **Aplicação**: a interface atual já mostra o resultado da listagem de forma clara; foi considerado adequado manter a abordagem atual.

## Considerações finais

O sistema atende aos requisitos propostos:

- Permite a listagem de documentos organizados.
- Permite adicionar, renomear e remover documentos via CLI.
- Sistema funcional, testado e validado.
