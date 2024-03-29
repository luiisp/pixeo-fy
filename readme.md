## Pixeo-fy API



A API Pixeo é uma Rest API baseada em **Django Rest Framework** que oferece funcionalidades para armazenar e gerenciar imagens. Ela fornece endpoints para fazer upload de imagens, obter detalhes das imagens e realizar diversas operações com imagens, como otimização e remoção de fundo.

---
> Voce pode acessar a documentação completa acessando o endpoint **/docs**

> Os endpoints **/api/** são protegidos pela autenticação JWT


*  **/admin/**  Fornece acesso à interface administrativa

*  **/token/**  Gera um JSON Web Token (JWT) para autenticação (Isto so pode ser feito com credenciais administrativas).

*  **/token/refresh/**  Renova um JWT mediante a um Token válido

*  **/api/** Inclui as rotas da Pixeo Api 

*  **/api/images** Todas as imagens já registradas pelos users devem ser apresentadas. **(GET)**

*  **/api/images** Um novo Upload pode ser feito incluindo os paramêtros do novo upload de Imagem **(POST)**

*  **/api/images/UUID** O upload feito pode ser acessado, modificado ou deletado.  **(GET/PUT/DELETE)**

## Image 

_Cada imagem podem/devem possuir os seguintes atributos antes do upload_


*  **title (String)**: Titulo para a imagem. **(Required)**

*  **image (Image)**: Arquivo de imagem **(Required)**

*  **description (String)**: Uma descrição da imagem. **(Not Required)**

*  **optimized (Bool)**: Indica se a imagem deve/foi otimizada ou não. **(Not Required | Default = False)**

*  **remove_bg (Bool)**: Indica se o fundo da imagem deve/foi removido ou não. **(Not Required | Default = False)**

## Dependencies

> Para maior compatibilidade é recomendado usar as dependencias nas versões presentes em requirements.txt. Isso pode ser feito com ```pip install -r requirements.txt```


- Django
- Django REST Framework
- uritemplate
- django-rest-framework-simplejwt
- Pillow 
- rembg


## Start Using 

* Clone este repo com ```git clone https://github.com/luiisp/pixeo-fy```

* Instale as dependências necessárias usando ```pip install -r requirements.txt```.

* Execute as migrações com ```python manage.py migrate```.

* Inicie o servidor com ```python manage.py runserver```.


*Acesse os endpoints da API usando um navegador da web ou cliente HTTP. em ```http://127.0.0.1:8000/```*

**Para documentação detalhada consulte o endpoint ```/docs```** 