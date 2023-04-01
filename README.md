# projeto_fabrica_de_software

  O conceito do CRUD deste framework é receber informações de uma loja de álbuns, onde você guarda em um banco de dados as informações da loja, o álbum e o cliente.
  
  #Album
    Na aba do álbum, o Nome e o Artista serão utilizados conjutos de caractéres pela modelagem "CharField", enquanto o ano de lançamento utiliza o modelo "InterFields"
    por se tratar de algorismos sem decimais, junto com null=true para não dar o erro "You are trying to add a non-nullable field 'Lancamento' to userprofile without a 
    default;  Por outro lado, o preço utiliza da modelagem "DecimalField" por se tratar de um número que pode estar fora da classificação de números inteiros. A rota
    desses dados já enquadram na área de admin.
 #Loja
    Na aba da Loja, foi usado o endereço, o nome e o número para contato. Ambos em endereço e nome foi utilizado na modelagem "CharFields" por ser tratar de texto string
    enquanto o número foi utilizado o "InterFields" com o código null=true para não dar o mesmo erro que ocorreu antes, com a inserção do Lançamento na aba de álbum.
 #Cliente
    Na aba de clientes foi utilizado o nome, endereço de residência e o e-mail, todos feito pela modelagem "CharField" por se tratar de caracteres que se aplicam em string.
    
    
 As rotas foram definidas no url.py com a base de viewset guiadas pela classes feitas no serializer de cada entidade("Álbum, Loja e Cliente"), as quais, estão, em geral,
 o "id", "nome", "endereço de residência", "e-mail",  "telefone para o contato", "ano do lançamento" e o "preço". Cada rota tem o BaseName auto-explicativo, além de ter
 adicionato o path geral dos urls feitos no rest_framework.
