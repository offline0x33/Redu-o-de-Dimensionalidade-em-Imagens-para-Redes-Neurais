from PIL import Image

# Carregando a imagem
imagem = Image.open("lena_color.jpg")

def converter_para_binario(imagem, limiar=128):
    """
    Converte uma imagem para binário usando um limiar.

    Args:
        imagem: Uma imagem PIL.
        limiar: O valor do limiar (0-255).

    Returns:
        Uma nova imagem binária.
    """

    largura, altura = imagem.size
    binaria = Image.new('1', (largura, altura))

    for x in range(largura):
        for y in range(altura):
            pixel = imagem.getpixel((x, y))
            # Assumindo que pixel é uma tupla (R, G, B)
            # Calcular a média dos canais como um valor representativo
            valor = (pixel[0] + pixel[1] + pixel[2]) // 3
            binaria.putpixel((x, y), 1 if valor >= limiar else 0)

    return binaria

def converter_para_cinza(imagem):
    """
    Os números 0.299, 0.587 e 0.114 são chamados de "coeficientes de luminância" ou "pesos". Eles representam a
    contribuição relativa dos canais vermelho, verde e azul, respectivamente, para a percepção da luminosidade por um
    olho humano típico.

    O olho humano é mais sensível ao verde, menos sensível ao azul e possui uma sensibilidade intermediária ao vermelho.
    Esses coeficientes foram determinados experimentalmente para simular a resposta do olho humano à luz.
    Ao aplicar esses pesos, a nova imagem em tons de cinza preservará a percepção visual da luminosidade da imagem
    original da forma mais fiel possível.
    """

    largura, altura = imagem.size
    cinza = Image.new('L', (largura, altura))

    for x in range(largura):
        for y in range(altura):
            r, g, b = imagem.getpixel((x, y))
            cinza.putpixel((x, y), int(0.299 * r + 0.587 * g + 0.114 * b))

    return cinza

# Converter para tons de cinza
imagem_cinza = converter_para_cinza(imagem)

# Converter para binaria
imagem_binario = converter_para_binario(imagem)

# Salva a nova imagem cinza
imagem_cinza.save("lena_cinza.jpg")

# Salva a nova imagem cinza
imagem_binario.save("lena_binario.jpg")