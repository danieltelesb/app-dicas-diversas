# --- Dados do Aplicativo ---
# Este arquivo contém a lista de dicas.

tips_data = [
    {
        "topic": "python",
        "title": "Iteração com enumerate()",
        "tip": "Use `enumerate()` para iterar sobre uma lista e obter o índice e o valor de cada item simultaneamente. Exemplo: `for i, item in enumerate(lista):`"
    },
    {
        "topic": "python",
        "title": "Formatação de Strings com f-strings",
        "tip": "As f-strings (`f\"Olá, {nome}!\"`) são a maneira mais moderna e legível de formatar strings em Python. São mais rápidas que `.format()` e `%s`."
    },
    {
        "topic": "sql",
        "title": "Contagem de Registros Únicos",
        "tip": "Para contar o número de valores únicos em uma coluna, use `COUNT(DISTINCT coluna)`. Isso é mais eficiente do que carregar todos os dados."
    },
    {
        "topic": "sql",
        "title": "Alias de Tabela",
        "tip": "Use aliases para encurtar nomes de tabelas, o que é útil em JOINs e consultas complexas. Exemplo: `SELECT * FROM clientes AS c JOIN pedidos AS p ON c.id = p.cliente_id`"
    },
    {
        "topic": "python",
        "title": "Compreensão de Lista",
        "tip": "Use a compreensão de lista para criar uma nova lista de forma concisa e eficiente. Exemplo: `quadrados = [x*x for x in range(10)]`"
    },
    {
        "topic": "sql",
        "title": "Cláusula HAVING",
        "tip": "Use a cláusula `HAVING` para filtrar resultados após a agregação, enquanto `WHERE` filtra antes. Exemplo: `GROUP BY categoria HAVING COUNT(*) > 5`"
    },
    {
        "topic": "python",
        "title": "Dicionários Padrão",
        "tip": "O `defaultdict` do módulo `collections` é útil para criar dicionários com valores padrão para chaves que não existem, evitando erros de `KeyError`."
    },
    {
        "topic": "sql",
        "title": "Usando o comando EXISTS",
        "tip": "O `EXISTS` é um comando booleano para verificar se um subconjunto de linhas existe, o que pode ser mais rápido que `IN` ou `JOIN` em grandes conjuntos de dados."
    },
]
