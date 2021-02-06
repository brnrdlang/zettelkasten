
Before any zettel can be filed, we have to set up the database in Django first.
```
$ python manage.py makemigrations
$ python manage.py migrate
```

The following command creates database entries from all markdown files in `zettel_dir/` and all subdirectories.
```
$ python manage.py file_zettel zettel_dir/
```

The following command starts the web server.
```
$ python manage.py runserver
```
E.g. the content of the markdown file `some-zettel.md` will be displayed under `127.0.0.1:8000/some-zettel/`. Each block corresponds to a zettel and will be identified by their block position. E.g. the second block/zettel can be displayed under `127.0.0.1:8000/some-zettel/1/
