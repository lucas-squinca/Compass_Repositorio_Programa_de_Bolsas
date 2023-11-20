Diretório Sprint #7
===================
Diretório destinado para os conteúdos trabalhados durante a Sprint 7 do programa de bolsas D&A CompassUOL

## Resumo

# Hadoop MapReduce

O **Hadoop MapReduce** é um componente chave do ecossistema Hadoop, projetado para processar grandes volumes de dados distribuídos em clusters de computadores. Ele segue um modelo de programação paralela e escalável para realizar tarefas de processamento e análise de dados de forma eficiente.

## Funcionamento

O processo do Hadoop MapReduce é dividido em duas etapas principais:

1. **Map**: Nesta fase, os dados de entrada são divididos em pedaços menores chamados "splits". Em seguida, uma função de mapeamento é aplicada a cada split, transformando os dados brutos em pares chave-valor intermediários.

2. **Reduce**: Na etapa de redução, os pares chave-valor intermediários são agrupados e processados com base na chave. Uma função de redução é aplicada a cada grupo de chaves, permitindo a agregação, filtragem ou qualquer outra operação necessária.

## Vantagens

- Escalabilidade: O MapReduce pode ser dimensionado horizontalmente para lidar com grandes conjuntos de dados.

- Tolerância a falhas: O Hadoop MapReduce é robusto e lida com falhas de hardware ou software automaticamente.

- Processamento distribuído: Ele aproveita a capacidade de vários nós de um cluster para acelerar o processamento.

## Exemplo

Aqui está um exemplo simples de código MapReduce em Java para contar a ocorrência de palavras em um conjunto de documentos:

```java
public class WordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
  public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
    String line = value.toString();
    String[] words = line.split(" ");
    for (String word : words) {
      context.write(new Text(word), new IntWritable(1));
    }
  }
}

public class WordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
  public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
    int sum = 0;
    for (IntWritable value : values) {
      sum += value.get();
    }
    context.write(key, new IntWritable(sum));
  }
}
```
# Apache Spark

O **Apache Spark** é um poderoso framework de código aberto projetado para processamento rápido e eficiente de dados em grande escala. Ele é altamente flexível e oferece suporte a várias linguagens de programação, incluindo Python, Scala e Java.

## Principais Conceitos

- **Resilient Distributed Datasets (RDDs)**: RDDs são a estrutura de dados fundamental no Spark. Eles representam conjuntos de dados distribuídos em várias máquinas e podem ser transformados e processados em paralelo.

- **Transformações**: As transformações no Spark são operações que são aplicadas a RDDs para criar um novo conjunto de dados. Exemplos incluem `map`, `filter`, `reduceByKey`, etc.

- **Ações**: As ações são operações que retornam resultados ou enviam dados de volta para o driver. Exemplos de ações são `count`, `collect`, `saveAsTextFile`, entre outros.

## PySpark

**PySpark** é a biblioteca Python que permite interagir com o Apache Spark. Ele oferece uma API Python para acessar as funcionalidades do Spark, tornando-o uma escolha popular para desenvolvedores Python.

### Exemplo PySpark:

```python
from pyspark import SparkContext

# Cria um contexto Spark
sc = SparkContext("local", "PySpark Example")

# Cria um RDD a partir de uma lista
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# Realiza uma transformação e ação simples
filtered_rdd = rdd.filter(lambda x: x % 2 == 0)
result = filtered_rdd.collect()

# Exibe o resultado
print(result)

# Encerra o contexto Spark
sc.stop()
```

## SparkSQL
O **Spark SQL** é um módulo do Apache Spark que permite a execução de consultas SQL em dados estruturados, proporcionando uma integração perfeita entre o processamento SQL e os recursos de Big Data do Spark. Isso facilita a análise de dados estruturados usando a linguagem familiar do SQL.

### Principais Recursos:

1. **Processamento Distribuído:** Aproveita a capacidade de processamento distribuído do Apache Spark para consultas SQL em grande escala.

2. **Integração com Dados Estruturados:** Permite a execução de consultas SQL em DataFrames do Spark, que representam dados estruturados em formato tabular.

3. **Suporte a Fontes de Dados Diversificadas:** Pode ser utilizado para consultar uma variedade de fontes de dados, incluindo arquivos Parquet, JSON, Hive, e bancos de dados externos.

4. **Extensibilidade:** Possui suporte para funções SQL personalizadas e extensões, permitindo a personalização de consultas.

### Exemplo de Código:

A seguir, um exemplo simples de utilização do Spark SQL em PySpark:

```python
from pyspark.sql import SparkSession

# Inicializa uma sessão Spark
spark = SparkSession.builder.appName("ExemploSparkSQL").getOrCreate()

# Cria um DataFrame de exemplo
data = [("Alice", 25), ("Bob", 30), ("Catherine", 28)]
columns = ["Nome", "Idade"]
df = spark.createDataFrame(data, columns)

# Registra o DataFrame como uma tabela temporária
df.createOrReplaceTempView("pessoas")

# Executa uma consulta SQL
resultado = spark.sql("SELECT * FROM pessoas WHERE Idade >= 28")

# Exibe o resultado
resultado.show()
```
