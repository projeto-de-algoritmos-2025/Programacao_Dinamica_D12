# Programação Dinamica - LeetCode

**Número da Lista**: 05 

**Conteúdo da Disciplina**: FGA0124 - PROJETO DE ALGORITMOS - T01  


## Alunos


<div align = "center">
<table>
  <tr>
    <td align="center"><a href="https://github.com/CarolinaBarb"><img style="border-radius: 95%;" src=./Documentos/assets/Carolina.jpg width="201"; alt="Carolina"/><br /><sub><b>Carolina Barbosa </b></sub></a><br/></td>
    <td align="center"><a href="https://github.com/JuliaSSouza"><img style="border-radius: 95%;" src=./Documentos/assets/Julia.png width="195"; alt=""/><br /><sub><b>Julia Sant'Anna</b></sub></a><br />
  </tr>
</table>


| Matrícula   | Aluno                             |
| ----------- | ---------------------------------- |
| 211030961 | Carolina Barbosa Brito           |
| 202044144  | Julia Sant'Anna de Souza      |
</div>

## Sobre 

## Exercício 1 - Longest Valid Parentheses
### Descrição
Este exercício envolve um conjunto de trabalhos, cada um com hora de início, hora de término e lucro, e precisa encontrar o maior lucro possível selecionando um subconjunto de trabalhos sem sobreposição de tempo, permitindo iniciar um trabalho exatamente quando outro termina (se um termina em X, outro pode começar em X). O problema é uma versão do Interval Scheduling e pode ser resolvido com programação dinâmica combinada com busca binária, ordenasndo os trabalhos pelo término e, para cada trabalho, some seu lucro ao melhor resultado do último trabalho que termina antes ou em seu início.


- Dificuldade: Difícil
- Link: https://leetcode.com/problems/longest-valid-parentheses/description/?envType=problem-list-v2&envId=dynamic-programming
- Solução: [Código]()

## Exercício 2 - Divide Intervals Into Minimum Number of Groups
### Descrição
Este exercício envolve um conjunto de intervalos inclusivos [left, right], sendo preciso dividi-lós em um ou mais grupos de forma que cada intervalo pertença a exatamente um grupo e nenhum par de intervalos do mesmo grupo se intercepte.
O objetivo é retornar o número mínimo de grupos necessários, esse mínimo equivale ao máximo de intervalos ativos ao mesmo tempo.
Para a solução utilizamos o min-heap para ordenar por início e manter um heap com os finais ativos, removendo finais < início_atual; o tamanho máximo do heap é a resposta.

![](Documentos/screenshots/imagem02.png)

- Dificuldade: Média
- Link:https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/
- Solução: [Código](DivideIntervals.py)


## Exercicio 3 - Non-overlapping Intervals
### Descrição
Dado um vetor (array) de intervalos _intervals_, onde *intervals[i] = [start_i, end_i]*, retorne o número mínimo de intervalos que você precisa remover para que os demais não se sobreponham.
- Dificuldade: Média
- Link: https://leetcode.com/problems/non-overlapping-intervals/description/
- Solução: [Código](NonOverlapping.py)

## Exercicio 4 - Partition Equal Subset Sum
### Descrição
Dado um vetor de inteiros _nums_, retorne _true_ se for possível particioná-lo em dois subconjuntos tais que a soma dos elementos em ambos seja igual; caso contrário, retorne _false_.

- Dificuldade: Média
- Link: https://leetcode.com/problems/partition-equal-subset-sum/description/
- Solução: [Código](PartitionEqual.py)

## Apresentação 
[Vídeo](https://youtu.be/daqUy7FKlzM)

 
 
