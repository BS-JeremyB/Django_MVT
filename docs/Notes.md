# Création d'un projet Django - Guide de synthèse

Pour créer un projet Django, suivez ces étapes simples :

### Installation de Django
- Utilisez PowerShell pour installer Django en utilisant la commande PIP suivante :
  ```
  pip install django==*version*
  ```
  ou simplement `pip install django` pour obtenir la dernière version.
  ```
  pip install django
  ```
- Vous pouvez vérifier l'installation en exécutant l'une des commandes suivantes :
  ```
  python -m django --version
  ```
  ou
  ```python
  import django
  django.get_version()
  ```

### Création d'un projet
- Pour créer un nouveau projet Django, utilisez la commande suivante dans votre terminal ou PowerShell :
  ```
  django-admin startproject *nom_du_projet*
  ```
  Par exemple :
  ```
  django-admin startproject blog
  ```

### Exécution du projet
- Une fois le projet créé, accédez au dossier du projet dans votre terminal ou PowerShell.
- Pour lancer le serveur de développement, utilisez la commande suivante :
  ```
  python manage.py runserver
  ```
- Vous verrez l'adresse à laquelle le serveur est hébergé localement dans la console.
- Ouvrez cette adresse dans votre navigateur pour accéder à votre projet Django. Une page avec une fusée indiquera le succès de l'opération.

En suivant ces étapes, vous serez en mesure de créer et de lancer un projet Django de base avec succès.

### Fichiers et répertoires générés automatiquement
- **Fichier de base de données SQLite** :
  - Lorsque vous lancez votre projet pour la première fois, Django crée automatiquement un fichier de base de données SQLite par défaut. Ce fichier peut être trouvé dans le répertoire du projet et est généralement nommé `db.sqlite3`.

- **Dossier de mise en cache** :
  - Django crée également un dossier de mise en cache pour l'optimisation des performances. Ce dossier est utilisé pour stocker les fichiers temporaires générés lors de l'exécution de l'application et améliorer les performances en réduisant le temps de chargement des pages. Il est généralement nommé `__pycache__` et est situé dans le répertoire du projet.

### Utilisation du protocole HTTP/HTTPS
- Les requêtes HTTP/HTTPS sont utilisées pour communiquer avec le serveur Django.
- Les requêtes sont gérées par Django via les URL et les vues.

### Utilisation de `urls.py` pour le routage
```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('articles/', views.articles_view, name='articles'),
]
```

### Utilisation de `views.py`
```python
# views.py
from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse('Hello, welcome to the home page!')

def articles_view(request):
    return HttpResponse('Here are all the articles.')
```

### Utilisation de `django.contrib.admin`
- Le module `django.contrib.admin` est importé par défaut pour avoir un panneau de gestion lors de la création du projet.
- Vous pouvez personnaliser l'administration en créant des classes `ModelAdmin`.

### Utilisation des templates
- Les templates permettent de générer du contenu HTML dynamique.
- Créez un dossier `templates` pour stocker vos templates HTML.
- Utilisez la fonction `render` pour afficher les templates dans les vues.
```python
# views.py
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html', {'title': 'Home Page'})

def articles_view(request):
    return render(request, 'articles.html', {'title': 'Articles'})
```

### Meilleures pratiques
- Utilisez un template de base pour la structure HTML commune à toutes les pages.
- Utilisez des tags de template pour rendre les éléments dynamiques.
- Utilisez des URL nommées pour faciliter la gestion des URLs dans vos templates.
```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Django App{% endblock %}</title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```

```html
<!-- home.html -->
{% extends 'base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
<h1>Welcome to the Home Page</h1>
{% endblock %}
```

### Navigation dans Django

Dans votre template HTML, vous avez défini des liens de navigation à l'aide de balises `<a>` avec des attributs `href` utilisant des tags de template Django `{% url 'nom_de_la_vue' %}`. Ces tags de template sont remplacés par les URLs correspondantes définies dans votre fichier `urls.py`.

#### Template HTML :
```html
<nav>
    <a href="{% url 'home' %}">Home</a>
    <a href="{% url 'article' %}">Article 1</a>
    <

a href="{% url 'contact' %}">Contact</a>
</nav>
```

Dans votre fichier `urls.py`, vous avez défini les URLs correspondantes pour ces vues.

#### Fichier urls.py :
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('article/', views.article_view, name='article'),
]
```

Lorsque vous cliquez sur un lien dans votre navigation, Django utilise le nom de la vue défini dans `urls.py` pour générer l'URL correspondant à cette vue. Cela permet de rendre votre code HTML plus modulaire et de faciliter la gestion des URLs.

### Importation de valeurs dans la vue via le contexte dans `render`

Dans votre vue `article_view`, vous utilisez la fonction `render` pour afficher le template `article.html` en passant un contexte contenant les articles. Le contexte est un dictionnaire Python qui contient des données que vous souhaitez passer au template pour les afficher dynamiquement.

#### Vue `article_view` :
```python
def article_view(request):
    return render(request, 'article.html', context={'articles': articles})
```

Dans votre template `article.html`, vous pouvez accéder aux articles à l'aide de la variable `articles` qui a été passée dans le contexte.

#### Template article.html :
```html
{% for article in articles %}
    <h1>{{ article.titre }}</h1>
    <p>{{ article.contenu }}</p>
    <span>{{ article.date }}</span>
{% endfor %}
```

En utilisant cette méthode, vous pouvez rendre votre page HTML dynamique en affichant les articles stockés dans votre "fausse" base de données.

### Applications Django

Les applications Django correspondent aux différents composants de notre application.

- Les modèles nous permettront d'interagir avec la base de données.
- Les applications sont des packages et peuvent être importées depuis Internet.
- Ce sont des modules indépendants pouvant être réutilisés dans d'autres projets Django.

### Création d'une application

- Utilisez la commande `python manage.py startapp *nomApp*` pour créer une nouvelle application Django.
- Cela crée un dossier avec une structure de fichiers prête à l'emploi, y compris un dossier `migrations` qui sera utilisé pour gérer les modifications de la base de données.
- Dans le fichier principal de l'application, `settings.py`, ajoutez le nom de l'application à la liste `INSTALLED_APPS` pour que Django sache qu'il doit charger/utiliser cette application.

### Gestion des URLs de l'application

- Créez un nouveau fichier `urls.py` dans le dossier de l'application pour gérer les URLs spécifiques à cette application/module.
- Utilisez la fonction `path` pour définir les routes URL dans le fichier `urls.py` de l'application.
- Assurez-vous d'importer le module `include` en plus de `path` dans le fichier `urls.py` principal de l'application.

Exemple :
```python
# urls.py (application principale)
from django.urls import path, include

urlpatterns = [
    path('utilisateurs/', include('utilisateurs.urls')),
]
```

- Importez les URLs de l'application dans le fichier `urls.py` principal de l'application pour les inclure dans le routage global de l'application.

### Utilisation de templates avec les applications

- Créez un nouveau dossier `templates` dans le dossier racine de votre projet, puis un sous-dossier avec le nom de l'application afin d'éviter les ambiguïtés avec d'autres dossiers de templates.
- Dans `settings.py`, assurez-vous que `app_dirs: true` est activé pour permettre à Django de rechercher dans chaque dossier de templates.
- Lorsque vous utilisez la fonction `render` pour renvoyer une vue, spécifiez le nom du dossier qui contient les templates de l'application.
  
Exemple :
```python
# views.py
from django.shortcuts import render

def my_view(request):
    return render(request, 'utilisateurs/list.html')
```

En suivant ces étapes, vous pourrez créer et intégrer des applications dans votre projet Django, tout en organisant proprement les URLs et les templates.

### Gestion des URLs paramétrées

Les URLs paramétrées permettent de rendre l'accès à une page dynamique en fonction du paramètre passé dans l'URL.

#### Exemple :
```
mon_site/article/1
```
Cela permettra d'atteindre le premier article de mon site.

Pour ce faire, nous allons utiliser dans les URLs un paramètre à la place ou en plus du nom de notre route. Afin d'éviter d'accepter n'importe quoi dans cette URL, nous pourrons typé le paramètre attendu :

- `str` : chaîne de caractères
- `int` : nombre entier
- `slug` : chaîne de caractères, mais acceptant également les caractères `_` et `-`
- `regex` : une expression régulière

Nous utiliserons donc ici un identifiant (`id`). Il faudra d'abord mettre à jour la "fausse" base de données avec un ID par article, puis utiliser ce paramètre dans les patterns d'URLs.

#### Exemple dans `urls.py` :
```python
path('<int:id>/', views.detail_view.html, name='article')
```

Dans notre vue, en plus de récupérer une requête, nous allons avoir le nom de notre paramètre (ici, entre chevrons, je l'ai appelé `id`).

#### Exemple dans la vue (`views.py`) :
```python
def detail_view(request, id):
    article = next((article for article in articles if article['id'] == id), None)
    if article:
        return render(request, 'articles/detail.html', context={'article': article})
    else:
        return HttpResponse(f"Il n'y a pas d'article avec l'ID {id}")
```

Comme je ne fournis qu'un seul article dans mon contexte, il me suffit de l'utiliser directement dans ma page `detail.html`, en n'oubliant pas de remettre tous les tags de template nécessaires.

Pour ensuite créer des liens sur chaque titre dans notre `list.html`, il faudra ajouter un template tag `url`.

#### Exemple dans le template (`list.html`) :
```html
<a href="{% url 'article' id=article.id %}">{{ article.title }}</a>
```

Afin d'éviter des problèmes d'ambiguïté, il est conseillé d'utiliser un namespace. Dans notre cas, nous utilisons un article de blog, mais peut-être que plus tard nous vendrons des produits sur notre blog et les objets seront également des articles. C'est pourquoi dans `urls.py` de l'application "article", je vais ajouter un namespace.

#### Exemple dans `urls.py` de l'application "article" :
```python
app_name = 'nom_souhaite'
```

Mais attention, cela devra être pris en compte dans tous nos appels d'URLs, par exemple ceux de `list.html` ou notre navigation dans le template de base. Pour cela, il faudra le mentionner juste avant le nom de l'URL.

#### Exemple dans le template (`base.html`) :
```html
<a href="{% url 'nom_souhaite:article' %}">Articles</a>
```

### Modèles et Bases de Données

Les modèles dans Django permettent de créer des tables pour stocker des données telles que des articles, des utilisateurs, etc. Django facilite l'utilisation des bases de données en offrant une interface simple pour la manipulation des données.

Pour commencer, il faut créer des modèles dans le fichier `models.py` de votre application. Les modèles doivent hériter de la classe `Model` de l'import `models`.

```python
from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
```

Ensuite, pour utiliser PostgreSQL, installez les pilotes nécessaires avec la commande :

```
pip install psycopg2
```

Puis, configurez les paramètres de connexion à la base de données dans le fichier `settings.py` :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nom_de_votre_base_de_données',
        'USER': 'votre_utilisateur',
        'PASSWORD': 'votre_mot_de_passe',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Après avoir créé la base de données PostgreSQL et configuré les paramètres de connexion, exécutez la commande pour migrer les changements vers la base de données :

```
python manage.py migrate
```

Utilisez la commande `makemigrations` pour créer un fichier de migration pour votre application :

```
python manage.py makemigrations article
```

Ensuite, appliquez les modifications à la base de données avec la commande `migrate` :

```
python manage.py migrate
```

Désormais, vous pouvez interagir avec la base de données en utilisant l'ORM de Django. Plus besoin d'écrire des requêtes SQL à la main. Vous pouvez accéder directement aux données de la base de données via vos modèles.

```python
from .models import Article
from django.shortcuts import render, get_object_or_404

def list_view(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', context={'articles': articles})

def detail_view(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'articles/detail.html', context={'article': article})
```

Ces fonctions récupèrent respectivement tous les articles de la base de données et affichent les détails d'un article spécifique en utilisant l'identifiant de l'article.


### Utilisation du Panneau d'Administration

Pour commencer à utiliser le panneau d'administration de Django, nous devons créer un superutilisateur. Cela se fait en ouvrant PowerShell et en exécutant la commande suivante :

```
python manage.py createsuperuser
```

Vous devrez fournir un nom d'utilisateur, une adresse e-mail (optionnelle), un mot de passe et une confirmation du mot de passe.

Une fois que le superutilisateur est créé, nous pouvons nous connecter à l'interface d'administration en utilisant ces identifiants.

Par défaut, l'interface d'administration affiche les utilisateurs existants. Actuellement, vous devriez voir l'utilisateur que vous venez de créer. Depuis ce menu, nous avons la possibilité de gérer un petit CRUD (Create, Read, Update, Delete) pour les utilisateurs.

Il est également possible, si nous le souhaitons, d'intégrer notre modèle `Article` au panneau administratif. Pour ce faire, dans le fichier `admin.py` de notre application, nous importons le modèle `Article` et l'enregistrons dans l'interface d'administration :

```python
from .models import Article

admin.site.register(Article)
```

Une fois cela fait, l'interface d'administration affichera également la section `Articles`. Nous pouvons maintenant voir que le panneau intègre directement des fonctionnalités pour consulter, éditer, supprimer et créer des articles. Tous les changements effectués dans le panneau d'administration sont reflétés dans la base de données.

### Gestion des Fichiers Statiques et Utilisation de Bootstrap

Lorsque nous souhaitons utiliser des fichiers de style ou des fichiers de script dans Django, nous devons les déclarer en tant qu'éléments statiques. Pour ce faire, nous modifions le fichier `settings.py` comme suit :

```python
STATIC_URL = '/static/' 
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
```

Ensuite, nous créons un dossier `static`, à l'intérieur duquel nous pouvons organiser des sous-dossiers selon nos besoins, tels que `css` pour les feuilles de style et `js` pour les scripts. 

Pour charger les fichiers de style dans notre template, nous utilisons des tags de template. Tout d'abord, nous chargeons le dossier `static` en haut du template :

```html
{% load static %}
```

Puis, nous pouvons inclure le fichier CSS de la manière suivante :

```html
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
```

Il est également possible d'ajouter des bibliothèques telles que Bootstrap. Pour cela, nous utilisons la méthode CDN en ajoutant les liens suivants dans la balise `<head>` de notre template :

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
```

### Création de Formulaires pour les Modèles

Nous pouvons désormais récupérer des pages de manière dynamique et utiliser des feuilles de style pour la mise en page. Cependant, pour interagir avec le contenu et ajouter des éléments tels que des articles ou des utilisateurs, nous avons besoin de formulaires.

Pour créer un bouton "Créer un article" dans notre page `list.html`, nous utilisons Bootstrap pour cela.

Ensuite, nous créons des formulaires de modèle pour interagir avec notre base de données. Dans le dossier `forms.py` de notre application, nous définissons une classe de formulaire qui hérite de `ModelForm` et spécifions les champs que nous voulons voir dans notre formulaire :

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu']
```

Nous importons ce formulaire dans notre fichier `views.py` et l'instancions dans notre vue :

```python
from .forms import ArticleForm

def create_view(request):
    form = ArticleForm()
    return render(request, 'articles/create.html', context={'form': form})
```

Dans notre fichier HTML, nous utilisons le formulaire de la manière suivante :

```html
<form action="{% url 'article:create' %}" method="POST">
    {% csrf_token %}
    {{ form }}
    <button type="submit" class="btn btn-primary">Créer</button>
</form>
```

Ensuite, dans la vue, nous traitons les méthodes GET et POST différemment :

```python
def create_view(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article:articles')
    else:
        form = ArticleForm()
    return render(request, 'articles/create.html', context={'form': form})
```

En utilisant cette méthode, nous pouvons créer des formulaires pour interagir avec notre base de données de manière simple et efficace.