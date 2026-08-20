#biblioteca que limpa o terminal
import os #os.system('cls')

pastas = []
pdfs = []

#funçao que passa o nome do app
def nome_app():
    print('Challenge JOVI Python - EXPTECH')
    print('============================================\n')

#funcao que exibe opçoes
def exibir_opcoes():
    print('1- Motivo para as Propostas')
    print('2- Criação de Pastas')
    print('3- Listar Pastas')
    print('4- Criação de PDF')
    print('5- Listar PDFs')
    print('6- Sair\n')

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

#funçao de listar as pastas que vai estar presente na funcao criar_pasta 
def listar_pastas(pastas):
    if not pastas:
        print('Nenhuma pasta foi criada ainda.')
        voltar_app()
    else:
        os.system('cls')
        print('\nPastas criadas:')
        print('---------------------------------------------')
        for i, pasta in enumerate(pastas, start=1):
            #acessa as chaves do dicionário
            nome = pasta['nome']
            categoria = pasta['categoria']
            fotos = pasta['qtd_fotos']
            print(f'{i}. {nome} | Categoria: {categoria} | {fotos} foto(s)')
        print('---------------------------------------------\n')
        
    voltar_app()
def criar_pasta():
    # Explicação das etapas mantida
    os.system('cls')
    print('Imagine que Você tirou uma foto de uma lousa com uma materia especifica, porem anteriormente você já tinha tirado uma foto a um tempo atras da mesma materia, e agora você quer organizar suas fotos, para isso você pode criar uma pasta com o nome da matéria e colocar as fotos dentro dela ou deixar que o aparelho faça isso automaticamente, assim fica mais fácil de encontrar as fotos depois.\n')
    input('Pressione Enter para continuar...')
    os.system('cls')
    print('Ao utilizar a câmera do celular, um ícone aparece no canto inferior da tela quando o sistema detecta conteúdo legível (como textos em lousas, documentos ou anotações). Ao clicar nesse ícone, a foto é capturada e processada, abrindo um menu de ações.\n')
    print('A principal funcionalidade é a opção de criar uma pasta com fotos relacionadas. A partir da imagem capturada, o sistema realiza OCR para identificar o tema principal do conteúdo (por exemplo, “derivadas”) e busca automaticamente na galeria outras imagens com o mesmo contexto. Em seguida, cria uma pasta nomeada de forma correspondente (ex: “Pasta sobre Derivadas”) e organiza todas essas fotos encontradas dentro dela.\n')
    print('Esse processo acontece de forma automática e integrada à galeria, sem a necessidade de busca e organização manual, funcionando de maneira semelhante à pesquisa inteligente, mas com organização real através da criação da pasta.\n')
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
        fotos = int(input('Digite a quantidade de fotos (ou deixe em branco para 0): ').strip() or 0)
        if fotos < 0: #verificaçao das entradas do usuario para fotos
            print('Erro: A quantidade de fotos não pode ser negativa.\n')
            continue
        elif type(fotos) != int:
            print('Erro: A quantidade de fotos deve ser um número inteiro não negativo.\n')
            continue
        #cria a estrutura do dicionário
        nova_pasta = {
            'nome': nome_pasta,
            'categoria': categoria,
            'qtd_fotos': fotos
        }
        pastas.append(nova_pasta)#adiciona a nova pasta à lista de pastas
        print(f'\nPasta "{nome_pasta}" [{categoria}] criada com sucesso!\n')

        #criar outra pasta se quiser
        criar_outra = input('Deseja criar outra pasta? (s/n): ')
        if criar_outra.lower() not in ('s', 'sim'):
            break

    voltar_app()
    
#funcao de listar pdfs, que vai estar presente na funcao criar_pdf
def listar_pdfs(pdfs):
    if not pdfs:
        print('Nenhum PDF foi criado ainda.')
        voltar_app()
    else:
        os.system('cls')
        print('\nPDFs criados:')
        print('---------------------------------------------')
        for i, pdf in enumerate(pdfs, start=1):
            #acesso as chaves do dicionário
            nome = pdf['nome']
            paginas = pdf['paginas']
            
            print(f'{i}. {nome}.pdf ({paginas} página(s))')
        print('---------------------------------------------\n')
        
    voltar_app()
    
def criar_pdf():
    #explicação da função de pdf
    os.system('cls')
    print('Imagine que Você tirou uma foto de um exercicio ou ate mesmo de materias, e agora você quer criar um arquivo PDF para organizar suas fotos!\n')
    input('Pressione Enter para continuar...')
    os.system('cls')
    print('Após capturar a imagem e acessar o menu de opções, o usuário pode selecionar a função “gerar PDF”.\n')
    print('Nessa opção, o sistema utiliza reconhecimento de texto (OCR) para identificar e transcrever todo o conteúdo legível presente na imagem. Em seguida, gera automaticamente um arquivo em PDF com o texto digitalizado, preservando a estrutura original, como quebras de linha e organização do conteúdo.\n')
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
        paginas = int(input('Quantidade de fotos/páginas convertidas(ou nada para um): ') or 1)
        if paginas < 0: #verificaçao das entradas do usuario para paginas
            print('Erro: A quantidade de páginas deve ser um número inteiro não negativo.\n')
            continue
        elif type(paginas) != int:
            print('Erro: A quantidade de páginas deve ser um número inteiro não negativo.\n')
            continue
        #cria a estrutura do dicionário
        novo_pdf = {
            'nome': nome_pdf,
            'paginas': paginas
        }
        pdfs.append(novo_pdf) #adiciona o novo PDF à lista de PDFs
        print(f'\nArquivo "{nome_pdf}.pdf" criado com sucesso com {paginas} página(s)!\n')

        #criar outro pdf se quiser
        criar_outra = input('Deseja criar outro PDF? (s/n): ')
        if criar_outra.lower() not in ('s', 'sim'):
            break

    voltar_app()

#funçao para escolher a opçao
def escolher_opcao():
    print('=============================================')
    try:
        opcao = int(input('Digite o número da opção desejada: '))

        #cada opcao ativa uma funçao
        if opcao == 1:
            motivo_propostas()
        elif opcao == 2:
            criar_pasta()
        elif opcao == 3:
            listar_pastas(pastas)
        elif opcao == 4:
            criar_pdf()
        elif opcao == 5:
            listar_pdfs(pdfs)
        elif opcao == 6:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

#criei a ordem
def main():
    os.system('cls')
    nome_app()
    exibir_opcoes()
    escolher_opcao()

#chamei a ordem
if __name__ == "__main__":
    main()
