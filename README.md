# Sistema de Envio de E-mails Automático

Aplicação desktop em Python para envio de e-mails em massa com interface gráfica amigável. Perfeita para campanhas de marketing, comunicação com clientes ou qualquer situação que exija envio de e-mails para múltiplos destinatários.

## Funcionalidades

- **Gerenciamento de Lista de E-mails**
  - Importação de listas de e-mails de arquivos CSV e TXT
  - Adição manual de e-mails
  - Verificação de validade de e-mails
  - Exportação de listas

- **Configurações SMTP**
  - Suporte a diferentes servidores SMTP
  - Opções de segurança (SSL/TLS, STARTTLS)
  - Suporte a autenticação
  - Teste de conexão

- **Suporte a Proxy**
  - Compatível com SOCKS4, SOCKS5 e HTTP
  - Suporte a autenticação de proxy

- **Gerenciamento de Anexos**
  - Adição de múltiplos anexos
  - Visualização de anexos
  - Suporte a diferentes tipos de arquivos

- **Envio de E-mails**
  - Suporte a HTML e texto simples
  - Carregamento de templates
  - Controle de intervalo entre envios
  - Log detalhado de envio
  - Estatísticas de envio

## Requisitos

- Python 3.6 ou superior
- Bibliotecas Python (instaladas automaticamente):
  - email-validator>=1.1.3
  - PySocks>=1.7.1
  - chardet>=4.0.0
  - Pillow>=9.0.0
  - customtkinter>=5.2.0

## Instalação

### Instalação Fácil (Windows)

1. Clone o repositório ou baixe o código-fonte:
```
git clone https://github.com/Hencheo/envio-emails-automatico.git
cd envio-emails-automatico
```

2. Execute o arquivo `instalar_e_executar.bat` para instalar as dependências e iniciar o programa.
   - Basta clicar duas vezes sobre o arquivo

### Instalação Manual

1. Clone o repositório ou baixe o código-fonte:
```
git clone https://github.com/Hencheo/envio-emails-automatico.git
cd envio-emails-automatico
```

2. Instale as dependências:
```
pip install -r requirements.txt
```

3. Execute o aplicativo:
```
python run.py
```

## Guia de Uso

### 1. Aba "Lista de E-mails"

Esta aba permite gerenciar os destinatários dos seus e-mails.

- **Importar CSV**: Permite carregar uma lista de e-mails a partir de um arquivo CSV.
- **Adicionar E-mail**: Adiciona um e-mail individual à lista.
- **Remover Selecionados**: Remove os e-mails selecionados da lista.
- **Verificar E-mails**: Verifica a validade do formato dos e-mails na lista.

Os e-mails válidos serão destacados em verde, enquanto os inválidos serão marcados em vermelho.

### 2. Aba "Configurações"

Configure os parâmetros de conexão com o servidor de e-mail:

#### Configurações SMTP:
- **Servidor SMTP**: Endereço do servidor de envio de e-mails
  - Gmail: smtp.gmail.com
  - Hotmail/Outlook: smtp.office365.com
  - Yahoo: smtp.mail.yahoo.com
- **Porta**: Normalmente 587 (com TLS) ou 465 (com SSL)
- **E-mail**: Seu endereço de e-mail completo
- **Senha**: 
  - Se usar Gmail com verificação em duas etapas: use uma senha de app
  - Caso contrário: sua senha normal

#### Configurações de Proxy (opcional):
- **Usar Proxy**: Ative esta opção se precisar usar um servidor proxy.
- **Tipo**: Selecione entre HTTP, SOCKS4 ou SOCKS5.
- **Servidor**: Endereço do servidor proxy.
- **Porta**: Porta do servidor proxy.

### 3. Aba "Anexos"

Esta aba permite gerenciar os arquivos que serão anexados aos e-mails.

### 4. Aba "Envio"

Esta aba permite compor e enviar sua mensagem:

- **Assunto**: Título do e-mail.
- **Mensagem**: Corpo do e-mail.
- **Usar HTML**: Ative esta opção se quiser formatar sua mensagem com HTML.

## Dicas Importantes

1. **Para contas Gmail**:
   - Ative a verificação em duas etapas
   - Crie uma senha de app específica para este programa

2. **Evite enviar muitos e-mails de uma vez** para não ser marcado como spam.

3. **Intervalo entre envios**:
   - Gmail: pelo menos 5 segundos
   - Outros provedores: 8-10 segundos

## Solução de Problemas

Os logs de erro são salvos na pasta `logs/error.log` para ajudar na solução de problemas.

- **Falha na autenticação SMTP**: Verifique se o usuário e senha estão corretos. Para Gmail, use uma senha de aplicativo.
- **Conexão recusada**: Verifique se o servidor SMTP e a porta estão corretos e se não há bloqueio de firewall.
- **Limite de envio excedido**: Muitos provedores têm limites diários de envio. Aumente o intervalo entre envios.
- **Erro de proxy**: Verifique se as configurações do proxy estão corretas e se o proxy está ativo.

## Licença

Este projeto está licenciado sob a licença MIT.