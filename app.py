#biblioteca que limpa o terminal
import os #os.system('cls')
import json

#leitura dos arquivos JSON, caso nao exista, cria um arquivo vazio
def carregar_dados(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados if isinstance(dados, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
#carregamento no json para informaçoes novas
def salvar_dados(caminho, dados):
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

#funcao que vinha se repetindo, para pedir quantidade de fotos ou paginas
def pedir_quantidade(mensagem, padrao):
    while True:
        try:
            quantidade = int(input(mensagem).strip() or padrao)
            if quantidade < 0:
                raise ValueError
            return quantidade
        except ValueError:
            print('Erro: informe um número inteiro não negativo.\n')

#funçao para listar, serve para pastas e pdfs, recebe o arquivo, mensagem de erro, titulo e a funçao de formataçao
def listar(arquivo, mensagem_vazia, titulo, formatar):
    if not arquivo:
        print(mensagem_vazia)
        voltar_app()
        return

    os.system('cls')
    print(f'\n{titulo}:')
    print('---------------------------------------------')
    for indice, registro in enumerate(arquivo, start=1):
        print(f'{indice}. {formatar(registro)}')
    print('---------------------------------------------\n')
    voltar_app()

#carrega os dados de pastas e pdfs dos arquivos JSON, para posterior manipulação
pastas = carregar_dados('pastas.json')
pdfs = carregar_dados('pdfs.json')


#funçao que passa o nome do app
def nome_app():
    print('Challenge JOVI Python - EXPTECH')
    print('============================================\n')

#funcao que exibe opçoes
def exibir_opcoes():
    print('1- Motivo para as Propostas')
    print('2- Criação de Pastas')
    print('3- Listar Pastas')
    print('4- Apagar Pastas')
    print('5- Criação de PDF')
    print('6- Listar PDFs')
    print('7- Apagar PDFs')
    print('8- Sair\n')

#funcao que finaliza o app
def finalizar_app():
    os.system('cls')
    print('finalizando o app...\n')

#funçao de opçao invalida, quando a resposta nao é esperada
def opcao_invalida():
    os.system('cls')
    print('Opção inválida, tente novamente\n')
    voltar_app()

def voltar_app():
    input('Pressione Enter para voltar ao menu principal...')
    main()

#funcao da primeira escolhas
def motivo_propostas():
    os.system('cls')
    print('O motivo para as propostas de funcionalidades relacionadas à organização de fotos e criação de PDFs a partir de imagens capturadas com a câmera do celular é proporcionar uma experiência mais eficiente e prática para os usuários, neste caso estudantes fulltime. Essas funcionalidades visam facilitar a gestão e o acesso às fotos, especialmente aquelas relacionadas a conteúdos educacionais, como anotações em lousas, exercícios e materiais de estudo.\n')
    print('Ao permitir a criação automática de pastas com base no conteúdo das fotos, os usuários podem organizar suas imagens de forma intuitiva, tornando mais fácil encontrar e acessar as fotos posteriormente. Além disso, a funcionalidade de gerar PDFs a partir das imagens capturadas oferece uma maneira rápida e conveniente de transformar fotos de exercícios ou anotações em documentos editáveis, facilitando o estudo e a revisão do material.\n')
    print('Essas propostas buscam melhorar a experiência do usuário ao lidar com fotos relacionadas à educação, promovendo uma organização eficiente e um acesso mais fácil aos conteúdos capturados, contribuindo para um processo de aprendizado mais fluido e produtivo.\n')
    voltar_app()
            
def criar_pasta(pastas):
    # Explicação das etapas mantida
    os.system('cls')
    print('Imagine que Você tirou uma foto de uma lousa com uma materia especifica, porem anteriormente você já tinha tirado uma foto a um tempo atras da mesma materia, e agora você quer organizar suas fotos, para isso você pode criar uma pasta com o nome da matéria e colocar as fotos dentro dela ou deixar que o aparelho faça isso automaticamente, assim fica mais fácil de encontrar as fotos depois.\n')
    input('Pressione Enter para continuar...')
    os.system('cls')
    print('Ao utilizar a câmera do celular, um ícone aparece no canto inferior da tela quando o sistema detecta conteúdo legível (como textos em lousas, documentos ou anotações). Ao clicar nesse ícone, a foto é capturada e processada, abrindo um menu de ações.\n')
    input('Pressione Enter para continuar...')
    os.system('cls')
    
    print('Vamos para uma pequena atividade: criar uma pasta para organizar suas fotos!')
    print('============================================================================\n')

    #interação com o usuário para criar pasta
    resposta = input('Deseja criar uma pasta? (s/n): ')
    if resposta.lower() not in ('s', 'sim'):
        print('Operação cancelada.')
        voltar_app()
        return

    while True:
        nome_pasta = input('Digite o nome da pasta: ').strip()
        if not nome_pasta:
            print('Erro: O nome da pasta não pode estar vazio.\n')
            continue
        #verifica se já existe um dicionário com esse mesmo nome na lista 'pastas'
        if any(pasta['nome'].lower() == nome_pasta.lower() for pasta in pastas):
            print(f'Erro: Uma pasta com o nome "{nome_pasta}" já existe. Escolha um nome diferente.\n')
            continue
        #pede informações adicionais para compor o dicionário
        categoria = input('Digite a categoria/matéria (ou deixe em branco para "Geral"): ').strip() or 'Geral'
        fotos = pedir_quantidade(
            'Digite a quantidade de fotos (ou deixe em branco para 0): ',
            0
        )
        #cria a estrutura do dicionário
        nova_pasta = {
            'nome': nome_pasta,
            'categoria': categoria,
            'qtd_fotos': fotos
        }
        pastas.append(nova_pasta)#adiciona a nova pasta à lista de pastas
        salvar_dados('pastas.json', pastas)

        print(f'\nPasta "{nome_pasta}" [{categoria}] criada com sucesso!\n')

        #criar outra pasta se quiser
        criar_outra = input('Deseja criar outra pasta? (s/n): ')
        if criar_outra.lower() not in ('s', 'sim'):
            break

    voltar_app()

#funçao de apagar pastas
def apagar_pasta(pastas):
    if not pastas:
        print('Nenhuma pasta foi criada ainda.')
        voltar_app()
    else:
        os.system('cls')
        for pasta in pastas:
            print(f'Pasta: {pasta["nome"]} | Categoria: {pasta["categoria"]} | {pasta["qtd_fotos"]} foto(s)')

    #pergunta ao usuário qual pasta deseja apagar, entao percorre as pastas e deleta a pasta correspondente
        remocao = input('Digite o nome da pasta que deseja apagar (ou deixe em branco para cancelar): ').strip()
        if not remocao:
            print('Operação cancelada.')
            voltar_app()
            return
        else:
            for pasta in pastas:
                if pasta['nome'] == remocao:
                    del pastas[pastas.index(pasta)]
                    salvar_dados('pastas.json', pastas)

                    print(f'Pasta "{remocao}" apagada com sucesso!')
                    voltar_app()
                    return
            print(f'Erro: A pasta "{remocao}" não foi encontrada.')
            voltar_app()
            return


def criar_pdf(pdfs):
    #explicação da função de pdf
    os.system('cls')
    print('Imagine que Você tirou uma foto de um exercicio ou ate mesmo de materias, e agora você quer criar um arquivo PDF para organizar suas fotos!\n')
    input('Pressione Enter para continuar...')
    os.system('cls')
    print('Após capturar a imagem e acessar o menu de opções, o usuário pode selecionar a função “gerar PDF”.\n')
    print('Isso permite, por exemplo, transformar instantaneamente uma foto de exercícios ou anotações em um documento editável e organizado, facilitando o uso posterior, como leitura, estudo ou resposta das atividades\n')
    input('Pressione Enter para continuar...')
    os.system('cls')

    print('Vamos para uma pequena atividade: criar um arquivo PDF!')
    print('=========================================================\n')

    #interaçao com o usuario, para criaçao de pasta
    resposta = input('Deseja criar um arquivo PDF? (s/n): ')
    if resposta.lower() not in ('s', 'sim'):
        print('Operação cancelada.')
        voltar_app()
        return

    while True:
        nome_pdf = input('Digite o nome do arquivo PDF (sem ".pdf"): ').strip()
        if not nome_pdf:
            print('Erro: O nome do arquivo PDF não pode estar vazio.\n')
            continue
        #pega os nomes dos PDFs usados para tratar duplicados
        nomes_existentes = [p['nome'] for p in pdfs]
        #ajusta o nome com sufixo se já existir um pdf com aquele nome
        if nome_pdf in nomes_existentes:
            contador = 1
            sufixo = f"{nome_pdf}_{contador}"
            while sufixo in nomes_existentes:
                contador += 1
                sufixo = f"{nome_pdf}_{contador}"
            nome_pdf = sufixo
        #pede quantidade de páginas para simular o PDF gerado
        paginas = pedir_quantidade(
            'Quantidade de fotos/páginas convertidas (ou nada para uma): ',
            1
        )
        #cria a estrutura do dicionário
        novo_pdf = {
            'nome': nome_pdf,
            'paginas': paginas
        }
        pdfs.append(novo_pdf) #adiciona o novo PDF à lista de PDFs
        salvar_dados('pdfs.json', pdfs)
        print(f'\nArquivo "{nome_pdf}.pdf" criado com sucesso com {paginas} página(s)!\n')

        #criar outro pdf se quiser
        criar_outra = input('Deseja criar outro PDF? (s/n): ')
        if criar_outra.lower() not in ('s', 'sim'):
            break

    voltar_app()


def apagar_pdf(pdfs):
    if not pdfs:
        print('Nenhum PDF foi criado ainda.')
        voltar_app()
    else:
        os.system('cls')
        for pdf in pdfs:
            print(f'PDF: {pdf["nome"]} | Páginas: {pdf["paginas"]}')

    #pergunta ao usuário qual PDF deseja apagar, entao percorre os PDFs e deleta o PDF correspondente
        remocao = input('Digite o nome do PDF que deseja apagar (ou deixe em branco para cancelar): ').strip()
        if not remocao:
            print('Operação cancelada.')
            voltar_app()
            return
        else:
            for pdf in pdfs:
                if pdf['nome'] == remocao:
                    del pdfs[pdfs.index(pdf)]
                    with open('pdfs.json', 'w', encoding='utf-8') as f:
                                json.dump(pdfs, f, ensure_ascii=False, indent=4)
                    print(f'PDF "{remocao}" apagado com sucesso!')
                    voltar_app()
                    return
            print(f'Erro: O PDF "{remocao}" não foi encontrado.')
            voltar_app()
            return

#funçao para escolher a opçao
def escolher_opcao():
    print('=============================================')
    try:
        opcao = int(input('Digite o número da opção desejada: '))

        #cada opcao ativa uma funçao
        if opcao == 1:
            motivo_propostas()
        elif opcao == 2:
            criar_pasta(pastas)
        elif opcao == 3:
            listar(pastas,'Nenhuma pasta foi criada ainda.','Pastas criadas',
                    lambda pasta: f'{pasta["nome"]} | Categoria: {pasta["categoria"]} | {pasta["qtd_fotos"]} foto(s)' #lambda funciona como uma função anônima para formatar a saída das pastas 
                    #(anotação pessoal, se quiser pule) usamos lambda para criar uma função simples e rápida que recebe um dicionário de pasta e retorna uma string formatada com as informações da pasta, precisei usar lambda porque a função listar espera uma função de formatação como argumento, e lambda é uma maneira conveniente de criar funções pequenas e específicas para esse propósito.
                )
        elif opcao == 4:
            apagar_pasta(pastas)
        elif opcao == 5:
            criar_pdf(pdfs)
        elif opcao == 6:
            listar(pdfs,'Nenhum PDF foi criado ainda.','PDFs criados',
                    lambda pdf: f'{pdf["nome"]}.pdf ({pdf["paginas"]} página(s))' #lambda funciona como uma função anônima para formatar a saída dos PDFs
                    #(anotação pessoal, se quiser pule) usamos lambda para criar uma função simples e rápida que recebe um dicionário de PDF e retorna uma string formatada com as informações do PDF, precisei usar lambda porque a função listar espera uma função de formatação como argumento, e lambda é uma maneira conveniente de criar funções pequenas e específicas para esse propósito.
                )
        elif opcao == 7:
            apagar_pdf(pdfs)
        elif opcao == 8:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

#criei a ordem
def main():
    os.system('cls')
    nome_app()
    exibir_opcoes()
    escolher_opcao()

main()