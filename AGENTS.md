# AGENTS

## Contexto operacional
- Este reposit?rio deve ser tratado como workspace Linux/WSL-first.
- Prefira leitura, escrita, valida??o e testes pelo lado Linux do WSL.
- Se houver diverg?ncia entre Windows e WSL, considere o WSL como fonte operacional principal.
- N?o use PowerShell como caminho principal de edi??o neste repo.
- O Git do Windows pode ser usado apenas como fallback de transporte remoto quando o Git no WSL n?o tiver credenciais HTTPS prontas.

## Regras de mudan?a
- Preserve contratos existentes, especialmente na CLI.
- Fa?a mudan?as m?nimas e de alta confian?a.
- N?o altere `docs/` sem solicita??o expl?cita.
- Evite mudan?as cosm?ticas desnecess?rias, especialmente de whitespace e line endings.

## Regra arquitetural
- `npt_prep` ? uma camada de pr?-ingest?o revis?vel.
- `npt_prep` n?o substitui a ingest?o oficial no NPT.
- Ao integrar `npt_prep`, preserve o formato anterior do resultado e acrescente apenas a nova chave/sa?da necess?ria.

## Testes
- Rode nesta ordem:
- `pytest tests/test_npt_prep.py`
- `pytest tests/test_pipeline.py`
- `pytest tests/test_cli_main.py`
- Depois rode `pytest`

## Observa??es de ambiente
- `tests/conftest.py` garante a raiz do projeto no `sys.path` durante o `pytest` no Linux.
- Se o `git push` no WSL falhar por credenciais HTTPS ausentes, use o Git do Windows apenas para transporte remoto.
