# Bug Hunter & TDD Calculator

Atividade prática de identificação de defeitos e aplicação de TDD em uma calculadora científica escrita em Python.

## Preparação

```powershell
uv sync
```

## Testes

```powershell
uv run pytest -q
```

## Relatório

- [Relatórios detalhados dos bugs](reports/Bugs.md)

Os defeitos ainda abertos podem ser reproduzidos sem interação manual:

```powershell
uv run python scripts/reproduzir_bugs.py
```
