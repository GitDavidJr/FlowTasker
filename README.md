# FlowTasker

FlowTasker é uma base de funções desenvolvidas em Python utilizando a biblioteca **PyAutoGUI**, projetada para facilitar a automação de tarefas repetitivas em sistemas operacionais. O projeto é voltado para automatizar interações com a interface gráfica, podendo simular cliques, digitação, espera de eventos baseados em imagens, e muito mais.

Além disso, o FlowTasker se integra ao **Google Sheets**, permitindo que as automações sejam baseadas em dados armazenados em planilhas, o que possibilita a criação de loops para a execução de tarefas complexas. Para aumentar ainda mais a flexibilidade, o projeto também pode ser combinado com o **VirtualBox** para escalar a velocidade das automações ou executar múltiplas funções de forma paralela, simulando comportamento humano de maneira mais eficiente.

## Estrutura do Projeto

A estrutura do projeto é simples e composta por três arquivos principais:

- **`automatization.py`**: Contém funções para realizar ações de automação, como clicar em botões, escrever textos e esperar eventos baseados em imagens. Através de PyAutoGUI, estas funções permitem automatizar interações com a interface gráfica.
  
- **`flow.py`**: Este arquivo lida com a criação de fluxos de automação, permitindo que você organize e execute sequências de tarefas com base nas funções definidas em `automatization.py`. É aqui que a mágica de automação realmente acontece.

- **`mapCoor.py`**: Utilitário para mapear coordenadas na tela, caso seja necessário para certas automações. Esse arquivo permite que você identifique as posições específicas onde as ações precisam ser realizadas.

## Funcionalidades

- **Automação com PyAutoGUI**: Use funções simples para clicar, digitar, mover o mouse e esperar por eventos.
  
- **Integração com Google Sheets**: Conecte-se a planilhas Google e utilize os dados nelas contidos para gerar loops automatizados. Ideal para tarefas como preenchimento de formulários, envio de e-mails em massa, ou qualquer outro processo repetitivo que envolva dados estruturados.

- **VirtualBox para Escala de Velocidade**: Integre o FlowTasker ao VirtualBox para rodar as automações em múltiplas instâncias de máquinas virtuais. Isso aumenta a capacidade de processamento e a velocidade de execução, permitindo automatizar grandes volumes de tarefas simultaneamente.

- **Simulação de Comportamento Humano**: Além de realizar tarefas repetitivas, o FlowTasker pode ser configurado para simular o comportamento humano no PC, o que é útil em cenários de testes automatizados ou quando é necessário evitar padrões muito óbvios de automação.

## Como Funciona

O FlowTasker permite que o usuário crie seus próprios fluxos de automação diretamente no arquivo `flow.py`. No exemplo abaixo, você verá como o fluxo de uma tarefa pode ser criado e personalizado.

### Criando um Fluxo

1. No arquivo `flow.py`, você pode definir um fluxo de automação onde você especifica uma sequência de ações a serem executadas.

Exemplo básico:

```python

# Defina o fluxo/loop
espera("tela_cadastro")
clica("imput1")
pa.write(texto_para_digitar2)
pa.press("tap") # entrar no imput2
pa.write(texto_para_digitar2)
clicar("buton_cadastrar")
esperar("tela_final")

```

### Detalhes sobre o Fluxo

- **Ação "clicar"**: Realiza um clique do mouse baseado em uma imagem da interface.
- **Ação "esperar"**: Aguarda até que uma imagem específica apareça na tela, simulando a espera por um evento.
- **Ação "digitar"**: Preenche campos de texto com o conteúdo especificado.

O fluxo pode ser adaptado para qualquer tarefa repetitiva que você deseje automatizar.

### Mapeamento de Coordenadas

Em alguns casos, pode ser necessário mapear a coordenada de um ponto específico na tela para realizar a automação de maneira mais precisa. O arquivo `mapCoor.py` foi criado para esse propósito, ajudando a identificar posições exatas para cliques ou outras interações.

Exemplo de Mapeamento de Coordenadas:

```python
import pyautogui

# Mapeia as coordenadas de um ponto
x, y = pyautogui.position()
print(f"A coordenada do ponto é: X={x}, Y={y}")
```

Após obter as coordenadas, você pode usá-las em seu fluxo de automação para cliques mais precisos.

## Requisitos

- Python 3.x
- PyAutoGUI
- Google API Client (para integração com Google Sheets)
- VirtualBox (opcional, para escalar a execução)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/FlowTasker.git
cd FlowTasker
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure a integração com o Google Sheets (siga a documentação da API Google Sheets para configurar as credenciais).

4. Execute o script para testar suas automações!

## Contribuições

Sinta-se à vontade para contribuir com o projeto! Se você tiver sugestões de melhorias ou quiser adicionar novos recursos, basta criar um pull request.

## Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.