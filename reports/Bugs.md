# Relatórios de bugs — Calculadora Científica

Ambiente comum aos testes: Windows, Python 3.12.14, NumPy 2.5.4 e pytest 7.4.4. Data da identificação: **07/11/2026**. Os bugs não corrigidos podem ser reproduzidos em conjunto com:

```powershell
uv run python scripts/reproduzir_bugs.py
```

## BUG-001 — Adição soma o primeiro operando duas vezes

### Identificação do Bug

- **Título do Bug:** Adição soma o primeiro operando duas vezes.
- **Localização do Bug:** `src/python_calculator/Calculadora.py`, função `adicao`, linha 3 (código original).

### Descrição Detalhada

- **Descrição Clara do Bug:** A expressão original `x + np.add(x, y)` calcula `2x + y`. Toda adição fica incorreta quando `x != 0`.
- **Contexto:** Identificado com entradas escalares positivas, negativas e decimais no ambiente descrito acima.

### Passos para Reproduzir

1. No código original, importar `adicao`.
2. Executar `adicao(2, 3)`.
3. Observar o retorno.
- **Consistência:** Ocorre sempre que o primeiro operando é diferente de zero.

### Resultado Esperado vs. Obtido

- **Resultado Esperado:** `5`.
- **Resultado Obtido:** `7`.

### Evidências

- **Screenshots e Vídeos:** Não aplicável; o comportamento determinístico foi registrado diretamente pela saída do pytest.
- **Logs de Erro:** O teste RED registrou `Obtained: 7` e `Expected: 5 ± 5.0e-06`, com três casos falhando.

### Severidade e Impacto

- **Severidade do Bug:** Alta.
- **Impacto do Bug:** A operação aritmética básica de adição produz resultados não confiáveis.

### Sugestões para Correção (Opcional)

- **Possíveis Soluções:** Retornar somente `np.add(x, y)`.

### Registro e Acompanhamento

- **Data de Identificação:** 07/11/2026.
- **Status do Bug:** Resolvido por TDD.
- **Correção documentada:** Primeiro foi escrito um teste parametrizado para entradas positivas, negativas e decimais. No estágio RED, os três casos falharam (`3 failed, 7 passed`). A correção mínima substituiu `x + np.add(x, y)` por `np.add(x, y)`. Após a inclusão da docstring de contrato e a execução de toda a suíte, o estágio GREEN e a verificação de regressão terminaram com `10 passed`.

## BUG-002 — Fatorial retorna zero para todos os inteiros não negativos

### Identificação do Bug

- **Título do Bug:** Fatorial é zerado na primeira iteração.
- **Localização do Bug:** `src/python_calculator/Calculadora.py`, função `fatorial`, linhas 24–28.

### Descrição Detalhada

- **Descrição Clara do Bug:** O laço começa em zero; logo, `fat *= 0` elimina o acumulador e todo fatorial não negativo retorna zero.
- **Contexto:** Reproduzido com `fatorial(5)`.

### Passos para Reproduzir

1. Executar `uv run python scripts/reproduzir_bugs.py`.
2. Localizar a linha `BUG-002`.
- **Consistência:** Sempre ocorre para inteiros `x >= 0`.

### Resultado Esperado vs. Obtido

- **Resultado Esperado:** `fatorial(5)` retorna `120` (e `fatorial(0)` retorna `1`).
- **Resultado Obtido:** `0`.

### Evidências

- **Screenshots e Vídeos:** Evidência textual reproduzível; captura visual não necessária.
- **Logs de Erro:** `BUG-002 | fatorial(5): 0`.

### Severidade e Impacto

- **Severidade do Bug:** Alta.
- **Impacto do Bug:** A função fatorial não produz um resultado correto para nenhuma entrada válida.

### Sugestões para Correção (Opcional)

- **Possíveis Soluções:** Iterar de `1` até `x`, inclusive, ou usar `math.factorial` após validar a entrada.

### Registro e Acompanhamento

- **Data de Identificação:** 07/11/2026.
- **Status do Bug:** Não resolvido; fora do defeito escolhido para esta aplicação de TDD.

## BUG-003 — Fatorial aceita números negativos

### Identificação do Bug

- **Título do Bug:** Fatorial negativo retorna valor aparentemente válido.
- **Localização do Bug:** `src/python_calculator/Calculadora.py`, função `fatorial`, linhas 24–28.

### Descrição Detalhada

- **Descrição Clara do Bug:** Não há validação do domínio. Para `-1`, o laço vazio mantém o acumulador em `1`, embora o fatorial não esteja definido para inteiros negativos.
- **Contexto:** Entrada inteira fornecida diretamente à função ou pela opção 7.

### Passos para Reproduzir

1. Executar `uv run python scripts/reproduzir_bugs.py`.
2. Localizar a linha `BUG-003`.
- **Consistência:** Sempre ocorre para inteiros negativos.

### Resultado Esperado vs. Obtido

- **Resultado Esperado:** Rejeição explícita da entrada com mensagem ou `ValueError`.
- **Resultado Obtido:** `fatorial(-1)` retorna `1`.

### Evidências

- **Screenshots e Vídeos:** Evidência textual reproduzível; captura visual não necessária.
- **Logs de Erro:** `BUG-003 | fatorial(-1): 1`.

### Severidade e Impacto

- **Severidade do Bug:** Média.
- **Impacto do Bug:** O programa apresenta como correto um resultado matematicamente indefinido.

### Sugestões para Correção (Opcional)

- **Possíveis Soluções:** Validar `x < 0` antes do cálculo e sinalizar erro claramente.

### Registro e Acompanhamento

- **Data de Identificação:** 07/11/2026.
- **Status do Bug:** Não resolvido.

## BUG-004 — Logaritmo natural chama uma função inexistente

### Identificação do Bug

- **Título do Bug:** `logaritmo_natural` usa `np.ln`, inexistente no NumPy.
- **Localização do Bug:** `src/python_calculator/Calculadora.py`, função `logaritmo_natural`, linhas 30–33.

### Descrição Detalhada

- **Descrição Clara do Bug:** Entradas positivas ultrapassam a validação e chamam `np.ln`, atributo que o NumPy não oferece.
- **Contexto:** NumPy 2.5.4; reproduzido com a entrada `1`.

### Passos para Reproduzir

1. Executar `uv run python scripts/reproduzir_bugs.py`.
2. Localizar a linha `BUG-004`.
- **Consistência:** Sempre ocorre para qualquer entrada positiva.

### Resultado Esperado vs. Obtido

- **Resultado Esperado:** `logaritmo_natural(1)` retorna `0.0`.
- **Resultado Obtido:** `AttributeError: module 'numpy' has no attribute 'ln'`.

### Evidências

- **Screenshots e Vídeos:** Evidência textual reproduzível; captura visual não necessária.
- **Logs de Erro:** A mensagem de `AttributeError` acima é impressa pelo script.

### Severidade e Impacto

- **Severidade do Bug:** Alta.
- **Impacto do Bug:** A opção 8 falha para toda entrada pertencente ao domínio do logaritmo.

### Sugestões para Correção (Opcional)

- **Possíveis Soluções:** Substituir `np.ln(x)` por `np.log(x)`.

### Registro e Acompanhamento

- **Data de Identificação:** 07/11/2026.
- **Status do Bug:** Não resolvido.

## BUG-005 — Logaritmo de base 10 calcula logaritmo natural

### Identificação do Bug

- **Título do Bug:** Função de base 10 usa `np.log`.
- **Localização do Bug:** `src/python_calculator/Calculadora.py`, função `logaritmo_base10`, linhas 35–38.

### Descrição Detalhada

- **Descrição Clara do Bug:** `np.log` calcula o logaritmo natural, não o logaritmo decimal anunciado pelo menu.
- **Contexto:** Reproduzido com `100`, caso cujo resultado decimal é inequívoco.

### Passos para Reproduzir

1. Executar `uv run python scripts/reproduzir_bugs.py`.
2. Localizar a linha `BUG-005`.
- **Consistência:** Sempre ocorre, exceto em valores coincidentemente neutros como `1`.

### Resultado Esperado vs. Obtido

- **Resultado Esperado:** `logaritmo_base10(100)` retorna `2.0`.
- **Resultado Obtido:** `4.605170185988092`.

### Evidências

- **Screenshots e Vídeos:** Evidência textual reproduzível; captura visual não necessária.
- **Logs de Erro:** `BUG-005 | logaritmo_base10(100): np.float64(4.605170185988092)`.

### Severidade e Impacto

- **Severidade do Bug:** Alta.
- **Impacto do Bug:** A opção 9 apresenta resultados de outra operação matemática.

### Sugestões para Correção (Opcional)

- **Possíveis Soluções:** Usar `np.log10(x)`.

### Registro e Acompanhamento

- **Data de Identificação:** 07/11/2026.
- **Status do Bug:** Não resolvido.

## BUG-006 — Logaritmo de zero não é rejeitado

### Identificação do Bug

- **Título do Bug:** Validação de logaritmo base 10 permite zero.
- **Localização do Bug:** `src/python_calculator/Calculadora.py`, função `logaritmo_base10`, linha 36.

### Descrição Detalhada

- **Descrição Clara do Bug:** A condição usa `x < 0`, mas o domínio real exige `x > 0`; zero passa e produz infinito negativo com aviso.
- **Contexto:** NumPy emite `RuntimeWarning: divide by zero encountered in log`.

### Passos para Reproduzir

1. Executar `uv run python scripts/reproduzir_bugs.py`.
2. Localizar o aviso e a linha `BUG-006`.
- **Consistência:** Sempre ocorre com zero.

### Resultado Esperado vs. Obtido

- **Resultado Esperado:** `"Erro: Logaritmo de número não positivo"`.
- **Resultado Obtido:** `-inf` e um `RuntimeWarning`.

### Evidências

- **Screenshots e Vídeos:** Evidência textual reproduzível; captura visual não necessária.
- **Logs de Erro:** `RuntimeWarning: divide by zero encountered in log` e `BUG-006 ... -inf`.

### Severidade e Impacto

- **Severidade do Bug:** Média.
- **Impacto do Bug:** Um valor fora do domínio é tratado como resultado numérico e pode contaminar cálculos posteriores.

### Sugestões para Correção (Opcional)

- **Possíveis Soluções:** Alterar a validação para `x <= 0`.

### Registro e Acompanhamento

- **Data de Identificação:** 07/11/2026.
- **Status do Bug:** Não resolvido.

## BUG-007 — Opção de seno é anunciada, mas não implementada

### Identificação do Bug

- **Título do Bug:** Opção 10 é tratada como operação inválida.
- **Localização do Bug:** `src/python_calculator/Calculadora.py`, `menu` (linha 52) e seleção em `calculadora_cientifica` (linhas 57–103).

### Descrição Detalhada

- **Descrição Clara do Bug:** O menu oferece seno, porém não existe função `seno` nem ramo para a escolha `'10'`.
- **Contexto:** Interface de linha de comando, escolhendo a opção 10.

### Passos para Reproduzir

1. Iniciar a calculadora.
2. Digitar `10`.
3. Observar a mensagem.
- **Consistência:** Sempre ocorre.

### Resultado Esperado vs. Obtido

- **Resultado Esperado:** Solicitar o ângulo em graus e exibir seu seno.
- **Resultado Obtido:** `Operação inválida. Tente novamente.`

### Evidências

- **Screenshots e Vídeos:** O script automatiza a mesma interação; captura visual não necessária.
- **Logs de Erro:** A mensagem acima precede `BUG-007 | opção 10 (seno): None`.

### Severidade e Impacto

- **Severidade do Bug:** Alta.
- **Impacto do Bug:** Uma das três operações trigonométricas anunciadas é totalmente indisponível.

### Sugestões para Correção (Opcional)

- **Possíveis Soluções:** Implementar `seno` com conversão de graus para radianos e incluir o ramo da opção 10.

### Registro e Acompanhamento

- **Data de Identificação:** 07/11/2026.
- **Status do Bug:** Não resolvido.

## BUG-008 — Opção de cosseno chama função inexistente

### Identificação do Bug

- **Título do Bug:** Cosseno encerra a aplicação com `NameError`.
- **Localização do Bug:** `src/python_calculator/Calculadora.py`, opção 11, linhas 94–96.

### Descrição Detalhada

- **Descrição Clara do Bug:** O fluxo tenta chamar `cosseno(x)`, mas essa função não foi definida.
- **Contexto:** Reproduzido com ângulo de 60 graus.

### Passos para Reproduzir

1. Iniciar a calculadora.
2. Escolher `11` e informar `60`.
- **Consistência:** Sempre ocorre.

### Resultado Esperado vs. Obtido

- **Resultado Esperado:** Resultado `0.5` (aproximadamente).
- **Resultado Obtido:** `NameError: name 'cosseno' is not defined`.

### Evidências

- **Screenshots e Vídeos:** Evidência textual reproduzível; captura visual não necessária.
- **Logs de Erro:** A exceção acima é registrada como `BUG-008` pelo script.

### Severidade e Impacto

- **Severidade do Bug:** Alta.
- **Impacto do Bug:** A opção 11 interrompe a aplicação sem resultado nem recuperação.

### Sugestões para Correção (Opcional)

- **Possíveis Soluções:** Definir `cosseno(x)` usando `np.cos(np.radians(x))`.

### Registro e Acompanhamento

- **Data de Identificação:** 07/11/2026.
- **Status do Bug:** Não resolvido.

## BUG-009 — Opção de tangente chama função inexistente

### Identificação do Bug

- **Título do Bug:** Tangente encerra a aplicação com `NameError`.
- **Localização do Bug:** `src/python_calculator/Calculadora.py`, opção 12, linhas 98–100.

### Descrição Detalhada

- **Descrição Clara do Bug:** O fluxo chama `tangente(x, radianos=False)`, mas nenhuma função `tangente` foi definida.
- **Contexto:** Reproduzido com ângulo de 45 graus.

### Passos para Reproduzir

1. Iniciar a calculadora.
2. Escolher `12` e informar `45`.
- **Consistência:** Sempre ocorre.

### Resultado Esperado vs. Obtido

- **Resultado Esperado:** Resultado `1.0` (aproximadamente).
- **Resultado Obtido:** `NameError: name 'tangente' is not defined`.

### Evidências

- **Screenshots e Vídeos:** Evidência textual reproduzível; captura visual não necessária.
- **Logs de Erro:** A exceção acima é registrada como `BUG-009` pelo script.

### Severidade e Impacto

- **Severidade do Bug:** Alta.
- **Impacto do Bug:** A opção 12 interrompe a aplicação sem resultado nem recuperação.

### Sugestões para Correção (Opcional)

- **Possíveis Soluções:** Definir uma interface coerente para `tangente` e converter graus para radianos antes de usar `np.tan`.

### Registro e Acompanhamento

- **Data de Identificação:** 07/11/2026.
- **Status do Bug:** Não resolvido.

## BUG-010 — Importar o módulo inicia a interface interativa

### Identificação do Bug

- **Título do Bug:** Módulo executa a calculadora durante a importação.
- **Localização do Bug:** `src/python_calculator/Calculadora.py`, chamada global na linha 109.

### Descrição Detalhada

- **Descrição Clara do Bug:** A chamada incondicional a `calculadora_cientifica()` causa efeitos colaterais, solicita entrada e dificulta reutilização e testes.
- **Contexto:** Visível ao importar o módulo; os testes precisam simular a entrada `0` somente para concluir a importação.

### Passos para Reproduzir

1. Executar `uv run python -c "import python_calculator.Calculadora"`.
2. Observar que o menu aparece e aguarda entrada.
- **Consistência:** Sempre ocorre na primeira importação do processo.

### Resultado Esperado vs. Obtido

- **Resultado Esperado:** A importação apenas disponibiliza funções, sem interação.
- **Resultado Obtido:** O menu é exibido e `input()` é chamado.

### Evidências

- **Screenshots e Vídeos:** A abertura do menu antes das linhas `BUG-*` no script demonstra o efeito.
- **Logs de Erro:** Em ambiente sem entrada, pode terminar em `EOFError`.

### Severidade e Impacto

- **Severidade do Bug:** Média.
- **Impacto do Bug:** Prejudica automação, testes e uso do arquivo como biblioteca.

### Sugestões para Correção (Opcional)

- **Possíveis Soluções:** Proteger a chamada com `if __name__ == "__main__":`.

### Registro e Acompanhamento

- **Data de Identificação:** 07/11/2026.
- **Status do Bug:** Não resolvido; contornado exclusivamente no teste.

## BUG-011 — Divisão por zero encerra a aplicação

### Identificação do Bug

- **Título do Bug:** Divisão por zero não possui tratamento.
- **Localização do Bug:** `src/python_calculator/Calculadora.py`, função `divisao`, linhas 13–14.

### Descrição Detalhada

- **Descrição Clara do Bug:** O divisor não é validado e a exceção atravessa a camada de interface.
- **Contexto:** Reproduzido com `divisao(1, 0)`.

### Passos para Reproduzir

1. Executar `uv run python scripts/reproduzir_bugs.py`.
2. Localizar a linha `BUG-011`.
- **Consistência:** Sempre ocorre quando o divisor escalar é zero.

### Resultado Esperado vs. Obtido

- **Resultado Esperado:** Mensagem controlada informando que não existe divisão por zero.
- **Resultado Obtido:** `ZeroDivisionError: division by zero`.

### Evidências

- **Screenshots e Vídeos:** Evidência textual reproduzível; captura visual não necessária.
- **Logs de Erro:** A exceção acima é impressa pelo script.

### Severidade e Impacto

- **Severidade do Bug:** Alta.
- **Impacto do Bug:** Uma entrada comum encerra a sessão e perde o fluxo atual.

### Sugestões para Correção (Opcional)

- **Possíveis Soluções:** Validar o divisor e retornar mensagem consistente ou lançar `ValueError` tratado pela interface.

### Registro e Acompanhamento

- **Data de Identificação:** 07/11/2026.
- **Status do Bug:** Não resolvido.

## BUG-012 — Entrada não numérica encerra a aplicação

### Identificação do Bug

- **Título do Bug:** Conversão de entrada não trata texto inválido.
- **Localização do Bug:** `src/python_calculator/Calculadora.py`, conversões `float(input(...))` e `int(input(...))`, linhas 65–99.

### Descrição Detalhada

- **Descrição Clara do Bug:** Entradas não numéricas são convertidas diretamente, sem validação nem tratamento de `ValueError`.
- **Contexto:** Reproduzido na opção 1 digitando `abc` como primeiro número.

### Passos para Reproduzir

1. Iniciar a calculadora e escolher `1`.
2. Digitar `abc` no primeiro operando.
- **Consistência:** Sempre ocorre com texto que não representa o tipo esperado.

### Resultado Esperado vs. Obtido

- **Resultado Esperado:** Informar entrada inválida e permitir nova tentativa.
- **Resultado Obtido:** `ValueError: could not convert string to float: 'abc'` e encerramento.

### Evidências

- **Screenshots e Vídeos:** O script automatiza a interação; captura visual não necessária.
- **Logs de Erro:** A exceção acima é registrada como `BUG-012`.

### Severidade e Impacto

- **Severidade do Bug:** Média.
- **Impacto do Bug:** Um erro de digitação encerra o programa e degrada a experiência do usuário.

### Sugestões para Correção (Opcional)

- **Possíveis Soluções:** Centralizar a leitura em função com `try/except ValueError` e repetição controlada.

### Registro e Acompanhamento

- **Data de Identificação:** 07/11/2026.
- **Status do Bug:** Não resolvido.
