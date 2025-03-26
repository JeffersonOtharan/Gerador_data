from PIL import Image, ImageDraw

# Criar uma imagem 256x256 com fundo branco
size = 256
image = Image.new('RGBA', (size, size), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Desenhar um círculo azul
circle_color = (41, 128, 185)
draw.ellipse([20, 20, size-20, size-20], fill=circle_color)

# Desenhar um símbolo de banco de dados
draw.rectangle([60, 60, size-60, size-60], fill=(255, 255, 255))
draw.rectangle([80, 80, size-80, size-80], fill=circle_color)
draw.rectangle([100, 100, size-100, size-100], fill=(255, 255, 255))

# Salvar como ICO
image.save('icon.ico', format='ICO') 