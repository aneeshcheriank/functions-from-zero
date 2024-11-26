# functions-from-zero
create a function and push to cloud

[![Python application test with GitHub Actions](https://github.com/aneeshcheriank/functions-from-zero/actions/workflows/makefile.yml/badge.svg)](https://github.com/aneeshcheriank/functions-from-zero/actions/workflows/makefile.yml)

## Python scafolding
- Makefile (linux)
- requirement file
- test file

## Functional Programming vs Object Oriented Programming

## mis
- change ~/.bashrc
- add last line as `source ~/.venv/bin/activate`
- `which python`
- `which pip`
- run a python script file
    - hedder of the file: `# !user/bin/env python` 
    - set the file executable: `chmod +x`
    - run the file `./<filename>.py`

## call microservice
```
curl -X 'POST' \
  'https://refactored-memory-6v5qv46xgxj2x6vw-8000.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Facebook"
}'
```
