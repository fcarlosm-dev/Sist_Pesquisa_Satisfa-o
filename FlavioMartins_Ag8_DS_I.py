def pesquisa_atendimento():
    """
    Programa de coleta e exibição de pesquisa de satisfação do cliente.
    Utilizado método de estruturas de repetição para múltiplos registros.
    """
    
    # Listas de armazenamento dos dados coletados
    nomes = []
    idades = []
    opinioes = []
    
    # Contadores de tipo de opinião
    qtd_excelente = 0
    qtd_bom = 0
    qtd_ruim = 0
    
    print("=" * 60)
    print("     PESQUISA DE SATISFAÇÃO DE CLIENTES")
    print("=" * 60)
    print("\nOpiniões disponíveis:")
    print("  1 - EXCELENTE")
    print("  2 - BOM")
    print("  3 - RUIM")
    print("  0 - Encerrar pesquisa\n")
    
    # Estrutura principal de repetição (while)
    while True:
        print("-" * 50)
        
        # Coleta do nome
        nome = input("Digite o nome (somente nome ou 'sair' para encerrar): ").strip()
        
        if nome.lower() == 'sair':
            break
        
        if nome == "":
            print("Campo nome não pode ser vazio! Digite novamente.")
            continue
        
        # Validação da idade
        try:
            idade = int(input(f"Digite a idade de {nome}: "))
            if idade < 0 or idade > 120:
                print("Idade inválida! Digite valor entre 0 e 120")
                continue
        except ValueError:
            print("Idade inválida! Digite SOMENTE números")
            continue
        
        # Validação da opinião
        try:
            opiniao = int(input("Digite sua opinião (1-Excelente, 2-Bom, 3-Ruim): "))
            if opiniao not in [1, 2, 3]:
                print("Opção inválida! Digite apenas o número 1, 2 ou 3")
                continue
        except ValueError:
            print("Opção inválida! Digite apenas os números (1, 2 ou 3).")
            continue
        
        # Armazenamento de dados nas listas
        nomes.append(nome)
        idades.append(idade)
        opinioes.append(opiniao)
        
        # Atualização dos contadores
        if opiniao == 1:
            qtd_excelente += 1
        elif opiniao == 2:
            qtd_bom += 1
        else:
            qtd_ruim += 1
        
        print(f"✅ Resposta de {nome} registrada com sucesso!")
    
    # Exibição dos resultados
    exibir_resultados(nomes, idades, opinioes, qtd_excelente, qtd_bom, qtd_ruim)


def exibir_resultados(nomes, idades, opinioes, qtd_excelente, qtd_bom, qtd_ruim):
    """
    Exibe os resultados consolidados da pesquisa.
    """
    print("\n" + "=" * 50)
    print("            RESULTADO DA PESQUISA")
    print("=" * 50)
    
    total = len(nomes)
    
    if total == 0:
        print("\n Nenhuma resposta foi registrada.")
        return
    
    # Mapeando as opiniões
    descricao = {1: "EXCELENTE", 2: "BOM", 3: "RUIM"}
    
    # Listagem individual dos entrevistados
    print("\n LISTA DE ENTREVISTADOS:")
    print("-" * 50)
    print(f"{'Nome':<20} {'Idade':<10} {'Opinião':<15}")
    print("-" * 50)
    
    for i in range(total):
        print(f"{nomes[i]:<20} {idades[i]:<10} {descricao[opinioes[i]]:<15}")
    
    # Estatísticas gerais
    print("\n" + "=" * 50)
    print("ESTATÍSTICAS GERAIS")
    print("=" * 50)
    print(f"Total de entrevistados: {total}")
    print(f"\nQuantidade por opinião:")
    print(f"  ⭐ EXCELENTE: {qtd_excelente} pessoa(s) "
          f"({(qtd_excelente / total) * 100:.1f}%)")
    print(f"  BOM:       {qtd_bom} pessoa(s) "
          f"({(qtd_bom / total) * 100:.1f}%)")
    print(f"  RUIM:      {qtd_ruim} pessoa(s) "
          f"({(qtd_ruim / total) * 100:.1f}%)")
    
    # Média de idade
    media_idade = sum(idades) / total
    print(f"\nMédia de idade dos entrevistados: {media_idade:.1f} anos")
    
    # Opinião predominante
    print("\n" + "=" * 50)
    if qtd_excelente > qtd_bom and qtd_excelente > qtd_ruim:
        print("🏆 RESULTADO: O atendimento foi avaliado como EXCELENTE!")
    elif qtd_bom > qtd_excelente and qtd_bom > qtd_ruim:
        print("👍 RESULTADO: O atendimento foi avaliado como BOM!")
    elif qtd_ruim > qtd_excelente and qtd_ruim > qtd_bom:
        print("⚠️  RESULTADO: O atendimento foi avaliado como RUIM!")
    else:
        print("RESULTADO: Houve empate entre as opiniões.")
    print("=" * 50)


# Ponto de início do programa
if __name__ == "__main__":
    pesquisa_atendimento()

