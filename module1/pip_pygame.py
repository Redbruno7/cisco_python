import pygame

# Executar programa enquanto verdadeiro
run = True

# Tamanho da janela
width = 400
height = 100

# Inicializar ambiente
pygame.init()

# Preparar janela e definir tamanho
screen = pygame.display.set_mode((width, height))

# Criar objeto com tamanho padrão de fonte
font = pygame.font.SysFont(None, 48)

# Criar objeto com texto e cor
text = font.render("Welcome to pygame", True, (255, 255, 255))

# Inserir texto no buffer de tela
screen.blit(
 text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))

# Inverter os buffers de tela
pygame.display.flip()

# Loop principal
while run:
  
  # Listar eventos pendentes
  for event in pygame.event.get():
   
   # Verificar iterações
   if event.type == pygame.QUIT\
   or event.type == pygame.MOUSEBUTTONUP\
   or event.type == pygame.KEYUP:
    
    # Encerrar o código
    run = False