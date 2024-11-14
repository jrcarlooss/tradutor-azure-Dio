# Tradutor-Azure-Dio

Desafio da DIO , no qual aprendemos a desenvolver um tradutor usando conta na Azure , utilizando a sua chave key  e  API  Endpoint URL.

# Como funciona:
Requisição HTTP : O código faz uma requisição HTTP POST para o endpoint da API do Translator.

Chave de acesso : Ele usa uma chave de API e região para autenticar uma solicitação.

Parâmetros de tradução : O texto, idioma de origem e destino são enviados no corpo da requisição.

Resposta da API : A API retorna o texto traduzido em formato JSON.

Índices de que uma API está sendo usada:
Endpoint URL : Uma URL ( https://api.cognitive.microsofttranslator.com/translate) é de um serviço externo.
Autenticação : Uso de uma chave de API no cabeçalho.
Requisição/Resposta : Envio de dados (texto a ser traduzido) e coleta de uma resposta JSON.
