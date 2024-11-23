import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Título del juego
pygame.display.set_caption("Tower Defense")

# Reloj para controlar los FPS
clock = pygame.time.Clock()

# Dimensiones de los objetos
ENEMY_WIDTH = 140  # Ancho deseado para los enemigos
ENEMY_HEIGHT = 100  # Alto deseado para los enemigos
ENEMY2_WIDTH = 140  # Ancho deseado para los enemigos
ENEMY2_HEIGHT = 100  # Alto deseado para los enemigos
ENEMY3_WIDTH = 140  # Ancho deseado para los enemigos
ENEMY3_HEIGHT = 100  # Alto deseado para los enemigos
BULLET_WIDTH = 30  # Ancho deseado para los disparos
BULLET_HEIGHT = 40  # Alto deseado para los disparos
CLOUD_WIDTH = 150  # Ancho deseado para la nube
CLOUD_HEIGHT = 100  # Alto deseado para la nube
TOWER_WIDTH = 200  # Ancho deseado para la torre
TOWER_HEIGHT = 600  # Alto deseado para la torre

# Cargar imágenes
background_image = pygame.image.load('fondo.png').convert()  # Cargar imagen de fondo
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Redimensionar fondo

tower_image = pygame.image.load('tower.png').convert_alpha()  # Cargar imagen de la torre
tower_image = pygame.transform.scale(tower_image, (TOWER_WIDTH, TOWER_HEIGHT))  # Redimensionar imagen de la torre

# Clase para los enemigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('enemy.png').convert_alpha()  # Cargar imagen
        self.image = pygame.transform.scale(self.image, (ENEMY_WIDTH, ENEMY_HEIGHT))  # Redimensionar imagen
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 50)
        self.health = 3 
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.x += self.speed
        # Si el enemigo llega al final de la pantalla, se descuenta salud de la torre
        if self.rect.x > SCREEN_WIDTH:
            global tower_health  # Hacer la variable accesible
            tower_health -= 5  # Descontar 5%
            if tower_health < 0:  # Asegurarse de que no baje de 0
                tower_health = 0
            self.kill()

class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('enemy2.png').convert_alpha()  # Cargar imagen
        self.image = pygame.transform.scale(self.image, (ENEMY_WIDTH, ENEMY_HEIGHT))  # Redimensionar imagen
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 50)
        self.speed = random.randint(1, 3)
        self.health = 2 
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.x += self.speed
        # Si el enemigo llega al final de la pantalla, se descuenta salud de la torre
        if self.rect.x > SCREEN_WIDTH:
            global tower_health  # Hacer la variable accesible
            tower_health -= 5  # Descontar 5%
            if tower_health < 0:  # Asegurarse de que no baje de 0
                tower_health = 0
            self.kill()

class Enemy3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('enemy3.png').convert_alpha()  # Cargar imagen
        self.image = pygame.transform.scale(self.image, (ENEMY_WIDTH, ENEMY_HEIGHT))  # Redimensionar imagen
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 50)
        self.speed = random.randint(1, 3)
        self.health = 4   
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.x += self.speed
        # Si el enemigo llega al final de la pantalla, se descuenta salud de la torre
        if self.rect.x > SCREEN_WIDTH:
            global tower_health  # Hacer la variable accesible
            tower_health -= 5  # Descontar 5%
            if tower_health < 0:  # Asegurarse de que no baje de 0
                tower_health = 0
            self.kill()            

# Clase para los disparos
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('bullet.png').convert_alpha()  # Cargar imagen
        self.image = pygame.transform.scale(self.image, (BULLET_WIDTH, BULLET_HEIGHT))  # Redimensionar imagen
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

    def update(self):
        self.rect.y += self.speed  # Los disparos ahora se mueven hacia abajo
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()

# Clase para la nube
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('nube.png').convert_alpha()  # Cargar imagen
        self.image = pygame.transform.scale(self.image, (CLOUD_WIDTH, CLOUD_HEIGHT))  # Redimensionar imagen
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = 20

    def move(self, dx):
        self.rect.x += dx
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH - self.rect.width

# Crear grupos de sprites
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Crear la nube
cloud = Cloud()
all_sprites.add(cloud)

# Variables de salud
tower_health = 100  # Salud inicial de la torre (100%)
running = True
spawn_timer = 0  # Controla el tiempo de aparición de enemigos
score = 0
bullet_cooldown = 250  # Cooldown entre disparos (en milisegundos)
last_shot_time = 0  # Tiempo desde el último disparo

def game_over_screen():
    """Función para mostrar la pantalla de Game Over."""
    font = pygame.font.SysFont(None, 74)
    game_over_text = font.render("GAME OVER", True, WHITE)
    restart_text = font.render("Press any key to restart", True, WHITE)

    screen.fill(BLACK)
    screen.blit(game_over_text, ((SCREEN_WIDTH - game_over_text.get_width()) // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(restart_text, ((SCREEN_WIDTH - restart_text.get_width()) // 2, SCREEN_HEIGHT // 2 + 50))
    pygame.display.flip()

    # Esperar hasta que se presione una tecla
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.KEYDOWN:
                # Reiniciar el juego
                reset_game()
                waiting = False

def reset_game():
    """Función para reiniciar el juego."""
    global tower_health, score, spawn_timer, running, cloud  # Agrega cloud a las globales
    tower_health = 100
    score = 0
    spawn_timer = 0
    all_sprites.empty()
    enemies.empty()
    bullets.empty()
    cloud = Cloud()  # Crear una nueva nube
    all_sprites.add(cloud)  # Añadir la nube de nuevo al grupo de sprites
    running = True

while running:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mover la nube con las teclas A (izquierda) y D (derecha)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  # Mover a la izquierda con 'A'
        cloud.move(-5)
    if keys[pygame.K_d]:  # Mover a la derecha con 'D'
        cloud.move(5)

    # Disparo con cooldown (barra espaciadora)
    current_time = pygame.time.get_ticks()  # Tiempo actual
    if keys[pygame.K_SPACE] and current_time - last_shot_time > bullet_cooldown:
        bullet = Bullet(cloud.rect.centerx, cloud.rect.bottom)
        all_sprites.add(bullet)
        bullets.add(bullet)
        last_shot_time = current_time  # Actualizar el tiempo del último disparo
    # Crear nuevos enemigos
    spawn_timer += 1
    if spawn_timer > 100:  # Ajusta este valor para cambiar la frecuencia de aparición
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
        spawn_timer = 0

        enemy2 = Enemy2()
        all_sprites.add(enemy2)
        enemies.add(enemy2)
        spawn_timer = 0

        enemy3 = Enemy3()
        all_sprites.add(enemy3)
        enemies.add(enemy3)
        spawn_timer = 0
    # Actualizar sprites
    all_sprites.update()

    # Detectar colisiones entre disparos y enemigos
    hits = pygame.sprite.groupcollide(bullets, enemies, True, False)
    for bullet in hits:
        for enemy in hits[bullet]:
            enemy.health -= 2
            if enemy.health <= 0:
                enemy.kill()
                score += 1

    # Dibujar fondo
    screen.blit(background_image, (0, 0))

    # Dibujar la torre en la posición deseada
    tower_x = SCREEN_WIDTH - TOWER_WIDTH + 80 # A 20 píxeles del borde derecho
    tower_y = (SCREEN_HEIGHT - TOWER_HEIGHT) // 2  # Centrado verticalmente
    screen.blit(tower_image, (tower_x, tower_y))

    # Dibujar todos los sprites
    all_sprites.draw(screen)

    # Mostrar la puntuación
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)  # Cambiar a blanco
    screen.blit(score_text, (10, 10))

    # Mostrar salud de la torre
    health_text = font.render(f"Tower Health: {tower_health}%", True, BLACK)  # Cambiar a blanco
    screen.blit(health_text, (10, 40))

    # Verificar si la salud de la torre es 0
    if tower_health <= 0:
        running = False
        game_over_screen()  # Mostrar pantalla de Game Over

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar los FPS
    clock.tick(60)

# Salir de Pygame
pygame.quit()