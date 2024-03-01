# Projeto-pygame

# O jogo que vocês implementarão é o jogo da memória composto por quadrados com cores diversas. Os quadrados começam com as cores escondidas e o jogador deve clicar em dois quadrados para revelar a cor. Se as cores forem iguais, o jogador ganha pontos e os quadrados desaparecem. Se as cores forem diferentes, os quadrados voltam a ficar escondidos. O jogo termina quando todos os quadrados forem revelados.


# Items para o desenvolvimento do jogo
# Etapa 1
# Implemente uma função que recebe como argumento um número inteiro N e retorna N**2 elementos. A função deve retornar uma lista de dicionários, cada dicionário deve representar um quadrado do jogo da memória. 
# Cada cor deve aparecer na lista exatamente duas vezes.
# Os quadrados devem ser posicionados de forma a formarem um quadrado de lado N na tela.
# Ou seja, para N=4 teremos um quadrado de 4x4 quadrados.
# Etapa 2
# No arquivo principal do jogo, utilize a função desenvolvida na etapa 1 para criar uma lista de quadrados, utilize o N inicialmente como 4.
# Desenhe os quadrados na tela.
# Etapa 3
# Faça com que clicar no quadrado alterne a cor dele entre branca e a cor sorteada.
# Etapa 4
# Agora devemos verificar se o jogador clicou em dois quadrados.
# Quando o jogador clicar no segundo quadrado, devemos verificar se as cores dos quadrados são iguais. Caso sejam cores iguais, apague os dois quadrados. Caso sejam cores diferentes, altere a cor dos quadrados para branca.
# Etapa 5
# Caso não hajam quadrados restantes, significa que o jogador ganhou o jogo. O jogo deve acabar.
# Etapa 6
# Centralize os quadrados na tela.
# Entrega
# Envie no BlackBoard o endereço do seu repositório GitHub (faça isso logo no início do projeto para não perder o prazo).

# O professor irá clonar o código presente no GitHub ao final do dia de entrega (assim, se o repositório for privado, adicione o professor como colaborador). -->

# Nota
# A nota do projeto será dada pelo menor conceito entre os dois objetivos abaixo:

# Objetivo 1: Desenvolver programas de computador e dentificar e programar estratégias computacionais de resolução de problemas práticos
# Conceito I
# Não entregou ou o código não pode ser executado (dá erro ao tentar executar).

# Conceito D
# Código funciona, mas não atingiu o conceito C ou ocorre um erro em uma parte essencial do jogo.

# Conceito C
# Implementou os 6 primeiros passos descritos acima.
# Conceito B
# Atingiu o conceito C; - Quando o jogador acertar dois quadrados, o jogo deve emitir um som; (Caso queiram, existem um som disponível no projeto em assets/snd) - Quando o jogador errar dois quadrados, o jogo deve emitir um som; (Caso queiram, existem um som disponível no projeto em assets/snd) - Quando o jogador clicar no segundo quadrado, o jogo deve esperar 1 segundo antes de verificar se as cores são iguais ou diferentes;

# Conceitos A
# Implementar a pontuação do jogador. A pontuacão deve ser o tempo que o jogador levour para finalizar o jogo. Quanto menor o tempo, maior a pontuação.
# Renderize na tela do jogo os segundos.
# Implemente uma tela pós jogo mostrando a pontuação do jogador e um botão para voltar para a tela inicial.
# Implementou um tela que mostra o ranking dos 10 melhores jogadores. O ranking deve ser salvo em um arquivo texto.
# Conceitos A+
# Utilize classes para representar as telas e cada quadrado.
# Altere a funcionalidade do jogo para revelar as cores dos quadrados ao inicio do jogo e esconder as cores após 3 segundos.
# Implemente uma tela de configuração do jogo. O jogador deve poder escolher o tamanho do jogo (4x4, 6x6, 8x8, 10x10);
# Objetivo 2: Atuar em uma equipe de desenvolvimento de software
# O conceito do projeto ficará limitado a C, caso um dos itens abaixo ocorra. - Não entregou o jogo pelo GitHub ou enviou poucos commits. - Caso não haja evidências no github da participação de todos os integrantes.

# Caso o aluno não tenha evidências de participação no projeto e não participou adequadamente das aulas estúdio o conceito deste aluno ficará em I.