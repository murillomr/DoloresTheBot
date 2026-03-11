# DoloresTheBot - Bot para Cartola FC
DoloresTheBot é um bot que escala automaticamente um time para o fantasy game Cartola FC, da Globo.com. O bot utiliza uma série de critérios para analisar e pontuar os jogadores disponíveis no mercado, montando o time com a melhor relação custo-benefício.

## Como funciona

O bot opera em uma série de etapas para escalar o melhor time possível:

1.  **Busca de Dados:** Coleta dados atualizados da API do Cartola FC, incluindo informações sobre jogadores, partidas e status do mercado.
2.  **Filtragem:** Filtra os jogadores para considerar apenas os que estão com status "provável" para a rodada.
3.  **Pontuação de Jogadores (`score_robot`):** Cada jogador recebe uma pontuação (`score_robot`) com base em um algoritmo que considera diversas variáveis:
    *   Média de pontos do jogador
    *   Quantidade de jogos disputados
    *   Valorização na última rodada
    *   Gols, assistências e desarmes
    *   Cartões amarelos e vermelhos recebidos
    *   Faltas cometidas
    *   Finalizações
    *   Mando de campo
    *   Classificação do time do jogador e do time adversário no campeonato.
4.  **Orquestração:** O bot classifica os jogadores de cada posição (goleiro, lateral, zagueiro, meia, atacante e técnico) com base no `score_robot`.
5.  **Montagem do Time:** Com os jogadores ranqueados, o bot monta diversas combinações de times, verifica o custo de cada um e escala a opção mais cara que se encaixe no patrimônio do usuário.

## Arquivos do Projeto

*   `main.py`: Ponto de entrada da aplicação. Verifica o status do mercado e inicia o processo de escalação.
*   `BuscaDados.py`: Responsável por toda a comunicação com a API do Cartola FC.
*   `Filtragem.py`: Contém as classes para filtrar jogadores e jogos.
*   `Esteira_clubes.py`: Analisa e classifica os clubes com base na sua posição na tabela.
*   `Esteira_jogador.py`: Onde a mágica acontece. Calcula o `score_robot` para cada jogador.
*   `Orquestrador.py`: Orquestra a filtragem e a pontuação dos jogadores.
*   `Monta_time.py`: Monta as combinações de times e seleciona a melhor opção para escalar.

## Como usar

1.  **Instale as dependências:**
    ```bash
    pip install requests
    ```
2.  **Configure suas credenciais:** Adicione suas credenciais do Cartola FC no arquivo `BuscaDados.py` para que o bot possa escalar seu time.
3.  **Execute o bot:**
    ```bash
    python main.py
    ```

**Aviso:** Este bot utiliza um token de autenticação que precisa ser gerado a partir do login no site do Cartola FC. O processo de obtenção e uso desse token deve ser feito com cuidado.
