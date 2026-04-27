#biblioteca que limpa o terminal
import os #os.system('cls')

pastas = []
pdfs = []

def nome_app():
    print('Challenge JOVI Python - EXPTECH')

def exibir_opcoes():
    print('1- Motivo para as Propostas')
    print('2- Criação de Pastas')
    print('3- Criação de PDF')
    print('4- Sair\n')

def finalizar_app():
    os.system('cls')
    print('finalizando o app...\n')

def opcao_invalida():
    os.system('cls')
    print('Opção inválida, tente novamente\n')
    voltar_app()

def voltar_app():
    input('Pressione Enter para voltar ao menu principal...')
    main()

def motivo_propostas():
    os.system('cls')
    print('O motivo para as propostas de funcionalidades relacionadas à organização de fotos e criação de PDFs a partir de imagens capturadas com a câmera do celular é proporcionar uma experiência mais eficiente e prática para os usuários, neste caso estudantes fulltime. Essas funcionalidades visam facilitar a gestão e o acesso às fotos, especialmente aquelas relacionadas a conteúdos educacionais, como anotações em lousas, exercícios e materiais de estudo.\n')
    print('Ao permitir a criação automática de pastas com base no conteúdo das fotos, os usuários podem organizar suas imagens de forma intuitiva, tornando mais fácil encontrar e acessar as fotos posteriormente. Além disso, a funcionalidade de gerar PDFs a partir das imagens capturadas oferece uma maneira rápida e conveniente de transformar fotos de exercícios ou anotações em documentos editáveis, facilitando o estudo e a revisão do material.\n')
    print('Essas propostas buscam melhorar a experiência do usuário ao lidar com fotos relacionadas à educação, promovendo uma organização eficiente e um acesso mais fácil aos conteúdos capturados, contribuindo para um processo de aprendizado mais fluido e produtivo.\n')
    voltar_app()

#funçao de pastas
def listar_pastas():
    if not pastas:
        print('Nenhuma pasta foi criada ainda.')
    else:
        print('\nPastas criadas:')
        for i, pasta in enumerate(pastas, 1):
            print(f'{i}. {pasta}')
    print()

def criar_pasta():
    #explicação da função de pastas
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

    resposta = input('Deseja criar uma pasta? (s/n): ')
    if resposta.lower() not in ('s', 'sim'):
        print('Operação cancelada.')
        voltar_app()
        return

    while True:
        nome_pasta = input('Digite o nome da pasta: ')
        pastas.append(nome_pasta)
        print(f'Pasta "{nome_pasta}" criada com sucesso!\n')
        
        # pergunta se deseja criar outra pasta
        criar_outra = input('Deseja criar outra pasta? (s/n): ')
        if criar_outra.lower() not in ('s', 'sim'):
            # pergunta se quer listar as pastas criadas
            listar = input('Gostaria de listar as pastas criadas? (s/n): ')
            if listar.lower() in ('s', 'sim'):
                os.system('cls')
                listar_pastas()
            break
    voltar_app()
    
#funcao de pdf
def listar_pdfs():
    if not pdfs:
        print('Nenhum PDF foi criado ainda.')
    else:
        print('\nPDFs criados:')
        for i, pdf in enumerate(pdfs, 1):
            print(f'{i}. {pdf}.pdf')
    print()

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

    resposta = input('Deseja criar um arquivo PDF? (s/n): ')
    if resposta.lower() not in ('s', 'sim'):
        print('Operação cancelada.')
        voltar_app()
        return

    while True:
        nome_pdf = input('Digite o nome do arquivo PDF (sem ".pdf"): ')
        pdfs.append(nome_pdf)
        print(f'Arquivo "{nome_pdf}.pdf" criado com sucesso!\n')
        
        # pergunta se deseja criar outro PDF
        criar_outra = input('Deseja criar outro PDF? (s/n): ')
        if criar_outra.lower() not in ('s', 'sim'):
            # pergunta se quer listar os PDFs criados
            listar = input('Gostaria de listar os PDFs criados? (s/n): ')
            if listar.lower() in ('s', 'sim'):
                os.system('cls')
                listar_pdfs()
            break
    voltar_app()

def escolher_opcao():
    try:
        opcao = int(input('Digite o número da opção desejada: '))

        if opcao == 1:
            motivo_propostas()
        elif opcao == 2:
            criar_pasta()
        elif opcao == 3:
            criar_pdf()
        elif opcao == 4:
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