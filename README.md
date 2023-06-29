# Pytest

Um repositório criado para eu estudar e brincar com o `Pytest`.

![image](https://user-images.githubusercontent.com/69183396/231850691-c84005a3-1dee-4e26-b32c-e29484dd7e46.png)

# Ativando o venv

Ative o `venv` dentro do repositório usando: `source venv/bin/activate`.

# Como usar

No arquivo `Makefile` vai ter alguns comandos para não quebrar os tests.

Exemplo: `make all_tests` vai rodar todos os tests fora os que precisa de uma resposta pra rodar.

O test_imc vai precisar de uma resposta para calcular o imc, usando o `make test_imc` vai rodar esse test, que vai perguntar seu peso e altura.
