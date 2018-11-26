library(tidyverse)
library(viridis)
library(ggridges)
library(magrittr)
options(pillar.sigfig = 6)

setwd("~/unb/me1")
prova_brasil <- read_rds("dados.rds")

# Função para a frequência experada
table2 <- function(data) {
  exp_data <- data
  for (i in 1:nrow(data)){
    for(j in 1:ncol(data)){
      # Makes row i and column j into the expected value
      exp_data[i,j] <- (sum(data[i,]) * sum(data[,j])) / sum(data)
    }
  }
  return(exp_data)
}

# Função para calcular o Χ²
chisq <- function(data){
  vec <- as.vector(data)
  expec <- as.vector(table2(data))
  chisq = 0
  for(i in 1:length(vec)){
    chisq = chisq + ((vec[i] - expec[i])**2)/expec[i]
  }
  return(chisq)
}

# 2 - Comparar a proficiência média em Matemática segundo o local da escola

ggplot(prova_brasil, aes(LOCAL, NOTA_MT)) +
  geom_boxplot()

ggplot(prova_brasil, aes(NOTA_MT, ..density..,fill = LOCAL)) +
  geom_density()

ggplot(prova_brasil, aes(NOTA_MT, LOCAL)) +
  geom_density_ridges(scale = 4) + theme_ridges() +
  scale_y_discrete(expand = c(0.01, 0)) +
  scale_x_continuous(expand = c(0, 0))

# Você diria que a proficiência em Matemática  é maior  em escolas urbanas? 
# As variâncias são iguais?
prova_brasil %>% 
  spread(key = LOCAL, value = NOTA_MT) %$%
  var.test(Urbana, Rural)

var_mat <- prova_brasil %>% 
  group_by(LOCAL) %>% 
  summarise(Var = var(NOTA_MT), gl = n()-1)

# Região crítica:  0.5669315; 1.763882
qf(.025, df1 = 35, df2 = 163)
qf(.975, df1 = 163, df2 = 35)

# Estatística do Teste: F = S^2_1 / S^2_2: 1.02911
var_mat$Var[1]/var_mat$Var[2]

# Não Rejeitamos H_0: Variâncias iguais

# Comparação entre Médias, variâncias iguais
media_mat <- prova_brasil %>% 
  group_by(LOCAL) %>% 
  summarise(média = mean(NOTA_MT))

#  H_0 : μ_1 - μ_2 = 0
#  H_1 : μ_1 - μ_2 > 0
prova_brasil %>% 
  spread(key = LOCAL, value = NOTA_MT) %$%
  t.test(Urbana, Rural, "greater", var.equal = TRUE)

# Graus de Liberdade: 52
# Região Crítica: 1.674689 /(2.006647)
qt(.95, 52)

# Gruas de Liberdade: 198
# Região Crítica: 1.652586
qt(.95, 198)

# Estatística do Teste: T = 4,526 / 4,483
# p-valor: 0.000006 / 6.223053e-06
(1 - pt(4.483, 198))

# Rejeitamos H_0: Médias diferentes - Profieciência em matemática maior em escolas urbanas

# ========================================= #
# 3 - Comparar a proficiência média em Língua Portuguesa 
# segundo categoria administrativa da escola. 
# ========================================= #

ggplot(prova_brasil, aes(ADM, NOTA_LP)) +
  geom_boxplot()

ggplot(prova_brasil, aes(NOTA_LP, ..density..,fill = ADM)) +
  geom_histogram(position = "identity", bins = 16, alpha = 0.8)

lp <- prova_brasil %>% 
  group_by(ADM) %>% 
  summarise(média = mean(NOTA_LP), Var = var(NOTA_LP), gl = n()-1)

# Existe diferença entre as proficiências?
# As variâncias são iguais?
prova_brasil %>% 
  spread(key = ADM, value = NOTA_LP) %$%
  var.test(Estadual, Municipal)

# Região Crítica: 0.631753; 1.582897
qf(.025, df1 = 158, df2 = 40)
qf(.975, df1 = 40, df2 = 158)

# Estatística do Teste: F = S^2_1 / S^2_2: 1.056026
lp$Var[1]/lp$Var[2]

# Não Rejeitamos H_0: Variâncias Iguais

# Comparação entre Médias, variâncias iguais

#  H_0 : μ_1 - μ_2 = 0
#  H_1 : μ_1 - μ_2 ≠ 0
prova_brasil %>% 
  spread(key = ADM, value = NOTA_LP) %$%
  t.test(Estadual, Municipal, var.equal = TRUE)

# Região Crítica: ± 1.972017
qt(0.975, 198)

# Estatística do Teste: 2.479
# p-valor: 0.01401
2*(1-pt(2.479, 198))

# Rejeitamos H_0: Médias Diferentes - Existe diferença entre as proficiências


# ========================================= #
# 4 - Verificar se existe diferença significativa  
# entre as notas de Língua Portuguesa e Matemática. 
# ========================================= #

notas <- prova_brasil %>% 
  gather('NOTA_LP', 'NOTA_MT', key = "mod", value = "nota") %>% 
  group_by(mod) %>% 
  summarise(Média = mean(nota), Variância = var(nota), "G.L." = n() - 1)

prova_brasil %>% 
  gather('NOTA_LP', 'NOTA_MT', key = "mod", value = "nota") %>% 
  ggplot() +
    geom_histogram(aes(nota, fill = mod))

# As variâncias são iguais?
prova_brasil %$%
 var.test(NOTA_LP, NOTA_MT)

# Região Crítica: 0.7567866; 1.321376
qf(.025, df1 = 199, df2 = 199)
qf(.975, df1 = 199, df2 = 199)


# Estatística do Teste: F = S^2_1 / S^2_2: 0.7395368
var(prova_brasil$NOTA_LP) / var(prova_brasil$NOTA_MT)

# Rejeitamos H_0: Variâncias diferentes

# Comparação de médias - variâncias diferentes

#  H_0 : μ_1 - μ_2 = 0
#  H_1 : μ_1 - μ_2 ≠ 0
prova_brasil %$% 
  t.test(NOTA_LP, NOTA_MT)

# Graus de Liberdade: 392 ?? ~ NORMAL
# Região Crítica: 1.966034
qt(0.975, 392)

# Estatística do Teste: -7.37 ; -7.3707
# p-valor:  1.015632e-12
2*(1 - pt(7.3707, 392))

# REJEITA MUITO PELAMOR


# ========================================= #
# 5 - Comparar a proporção de escolas que menos de 75% de  
# seus estudantes participaram da Prova Brasil em 2011 segundo:
# ========================================= #

# a - Local da Escola
prova_brasil %>% 
  mutate(lt75 = ifelse(PARTICIPACAO < 75, 'menor', 'maior')) %>% 
  ggplot(aes(LOCAL, PARTICIPACAO, fill = lt75)) +
  geom_dotplot(binaxis = 'y', stackdir = 'center', dotsize = 0.5)

prova_brasil %>% 
  mutate(lt75 = ifelse(PARTICIPACAO < 75, 'menor', 'maior')) %>% 
  ggplot(aes(PARTICIPACAO)) +
  geom_dotplot(aes(fill = lt75)) +
  facet_wrap(~ LOCAL)


part_local <- prova_brasil %>% 
  group_by(LOCAL) %>% 
  summarise("Menor que 75%" = sum(PARTICIPACAO < 75), "Maior que 75%" = sum(PARTICIPACAO >= 75))

# Teste de Homogeneidade

# H_0: p_11 = p_21; p_21 = p_22
# H_1: p_ij ≠ p_ik
chisq.test(part_local[2:3], correct = FALSE)

# Estatística do Teste: 4,8444
# p-valor: 0,02773604
1 - pchisq(4.8444, 1)

# Região Crítica: 0.00393214
qchisq(0.05, 1)

# Rejeitamos H_0: A proporção de participação varia conforme o local

#b.Região de localização da escola.

prova_brasil %>% 
  mutate(lt75 = ifelse(PARTICIPACAO < 75, 'menor', 'maior')) %>% 
  ggplot(aes(PARTICIPACAO)) +
  geom_dotplot(aes(fill = lt75)) +
  facet_wrap(~ ADM)

part_adm <- prova_brasil %>% 
  group_by(ADM) %>% 
  summarise("Menor que 75%" = sum(PARTICIPACAO < 75), "Maior que 75%" = sum(PARTICIPACAO >= 75))

# Teste de Homogeneidade

# H_0: p_11 = p_21; p_21 = p_22
# H_1: p_ij ≠ p_ik
chisq.test(part_adm[2:3], correct = FALSE)

# Estatística do Teste: 0,1151
# p-valor: 0.7344109
1 - pchisq(0.1151, 1)

# Região Crítica: 3.841459
qchisq(0.95, 1)

# Não Rejeitamos H_0: A proporção de participação...

# ========================================= #
# 6 - Verificar-se:
# ========================================= #

# a - Região e categoria administrativa estão associadas;

reg_adm <- table(prova_brasil$ADM, prova_brasil$REG)

prova_brasil %>% 
  count(REG, ADM) %>% 
  ggplot(aes(REG, ADM)) +
  geom_tile(aes(fill = n)) +
  scale_fill_viridis(option = "A")

# Teste de Independência
chisq.test(reg_adm)

# H_0: p_ij = p_i+ * p_+j

# Frequência Experada:
table2(reg_adm)

# Estatística do Teste: 11.24391
chisq(reg_adm)

# p-valor: 0.02395535
1 - pchisq(chisq(reg_adm), 4)

# Região Crítica: 9.487729
qchisq(0.95, 4)

# Rejeitamos H_0: Região e Categoria Administrativas não são independentes

# b - Tamanho da escola e tamanho do município estão associados.

tam <- table(prova_brasil$TAM_ESCOLA, prova_brasil$TAM_MUN)

prova_brasil %>% 
  count(TAM_ESCOLA, TAM_MUN) %>% 
  ggplot(aes(TAM_ESCOLA, TAM_MUN)) +
  geom_tile(aes(fill = n)) +
  scale_fill_viridis(option = "E") +
  coord_flip()

prova_brasil %>%
  group_by(TAM_MUN, TAM_ESCOLA) %>% 
  summarise(n =  n()) %>% 
  mutate( freq = n / sum(n)) %>% 
  ggplot(aes(TAM_ESCOLA, TAM_MUN)) +
  geom_tile(aes(fill = freq)) +
  scale_fill_viridis(option = "E") +
  coord_flip()

prova_brasil %>%
  ggplot(aes(TAM_ESCOLA, TAM_MUN))+
  geom_count(aes(color = ..n..)) +
  scale_color_viridis(option = "A")

prova_brasil %>% 
  ggplot(aes(TAM_MUN)) +
   geom_bar(aes(fill = TAM_ESCOLA), position = "dodge")+
   scale_fill_viridis_d()


# Teste de Independência
chisq.test(tam)

# Frequências Relativas:
table2(tam)

# Estatística do Teste: 61.20021 ~ gl = 12
chisq(tam)
# p-valor: 1.362776e-08 ; 0,0000000136
1 - pchisq(chisq(tam), 12)

# Região Crítica: 21.02607
qchisq(0.95, 12)

# Rejeitamos H_0: Tamanho da Escola e Tamanho do Município não são independentes

# ========================================= #
# Verificar se a nota em Língua Portuguesa é um bom indicador para
# predizer a nota existe em Matemática, ou seja se estão associadas.
# ========================================= # 

prova_brasil %>% 
  ggplot(aes(NOTA_LP, NOTA_MT)) +
  geom_point(alpha = 0.8) +
  geom_smooth(method = "lm", se = FALSE, color = "darkgray")

# Teste de Correlação
prova_brasil %$%
  cor.test(NOTA_LP, NOTA_MT)

# H_0: ro = 0
# H_1: ro ≠ 0

# Região Crítica:
qt(0.975, 198)

# Estatística do Teste: 49,37196
# p-valor: menor que 2,2x10^-16

# Rejeitamos H_0: Amostra idependente
