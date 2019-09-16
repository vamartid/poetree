# Poetree

Poetree is a django project, written with python, pugjs, sass.

  - It is a simple website for friends to write/read poems.
# Features!

  - Home page
  - Register/Login
  - Poem Creation/Edit/Delete
  - Poem ListView/User Poem ListView

### Tech

Poetree uses a number of open source projects to work properly:

* [Django](https://www.djangoproject.com/) - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [Pugjs](https://pugjs.org/api/getting-started.html) - Pug is a high-performance template engine heavily influenced by Haml and implemented with JavaScript for Node.js and browsers.
* [Sass](https://sass-lang.com/) - Sass is the most mature, stable, and powerful professional grade CSS extension language in the world.
* [Materialize](https://materializecss.com/) - A modern responsive front-end framework based on Material Design
* [Animate](https://daneden.github.io/animate.css/) - A cross-browser library of CSS animations. As easy to use as an easy thing.

And of course Poetree itself is open source.

### Installation

Poetree requires Django, pypugjs, django-sass-processor, libsass take a look [here](https://github.com/mjun/dj-pug-sass).
Extract poetree/static.tar.gz to poetree/poetree_blog/static and you are good to go.
Install the dependencies and devDependencies and start the local server.

```sh
$ python manage.py runserver
```

### Development

Want to contribute? Great!

Do not upload sqlite.db file and static, migrations, cache dirs.

### Todos

 - Docker
 - Ui changes

License
----

MIT
