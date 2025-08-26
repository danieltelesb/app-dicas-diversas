# --- Funções Auxiliares ---
# Este arquivo contém a lógica de filtragem das dicas.

def filter_tips(tips, selected_topics, search_term):
    """
    Filtra a lista de dicas com base no tópico e termo de pesquisa.
    
    Args:
        tips (list): A lista de dicionários de dicas.
        selected_topics (list): Uma lista de tópicos selecionados (ex: ['python', 'sql']).
        search_term (str): O termo para pesquisar em títulos e dicas.
        
    Returns:
        list: Uma nova lista de dicas filtradas.
    """
    filtered_tips = []
    # Remove espaços extras no início e no fim do termo de pesquisa
    cleaned_search_term = search_term.strip().lower()
    
    for tip in tips:
        # A dica só é exibida se o tópico dela estiver na lista de tópicos selecionados
        topic_match = tip["topic"] in selected_topics
        
        # O filtro de pesquisa é o mesmo
        search_match = cleaned_search_term in tip["title"].lower() or \
                       cleaned_search_term in tip["tip"].lower()
        if topic_match and search_match:
            filtered_tips.append(tip)
    return filtered_tips
