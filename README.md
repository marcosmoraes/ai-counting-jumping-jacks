# Exercício de Contagem de Polichinelos

Este projeto utiliza a biblioteca **MediaPipe** para detectar a pose humana em vídeos e contar automaticamente o número de repetições de um exercício específico. O código processa um vídeo, identifica a posição das mãos e dos pés, e conta as repetições com base na proximidade entre as mãos e a separação dos pés. O vídeo de entrada é processado e a contagem é exibida em tempo real.

## Funcionalidades

- **Detecção de Pose**: Utiliza o modelo de detecção de pose do **MediaPipe** para identificar os marcos do corpo humano, como ombros, mãos e pés.
- **Contagem de Exercícios**: Conta automaticamente as repetições do exercício com base na posição das mãos e pés.
- **Exibição em Tempo Real**: O vídeo de entrada é exibido com a contagem das repetições, atualizada em tempo real.

## Requisitos

Este código utiliza as seguintes bibliotecas:

- **OpenCV**: Para captura e exibição do vídeo.
- **MediaPipe**: Para detecção de pose humana.
- **Math**: Para calcular distâncias e definir limites de contagem.

Você pode instalar as bibliotecas necessárias com o seguinte comando:

```bash
pip install opencv-python mediapipe
