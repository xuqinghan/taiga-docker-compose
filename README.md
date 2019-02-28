# deploy taiga in docker via one command:

```bash
pip3 install jinja2
python3 setup.py
```

inspired by https://github.com/douglasmiranda/docker-taiga

-change the docker-compose.yml to  v3

-generate install scripts via rendering template

-remove "python /home/taiga/taiga-back/manage.py loaddata initial_role"  follow offical answer 

3.1.0 Install : CommandError: No fixture named 'initial_role' found.
https://github.com/taigaio/taiga-back/issues/958





and src taiga-back need fix:

add "from . import celery_local" @ taiga-back/settings/__init__.py
