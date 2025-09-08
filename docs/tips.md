# Some tips

```python
flask --help

Commands:
  createdb  Create sqlite database.
  routes    Show the routes for the app.
  run       Run a development server.
  shell     Runs a shell in the app context.
```

## create database
```python
flask createdb
```

## query for insert -< run with CTRL+Shift+P and select the command...
```python
-- SQLite
INSERT INTO 'products' (is, name, price, description)
VALUES(3,"Pretzel", 20, "Pão especial Pretzel");

```