
library(dplyr)

resultado <- pagamento %>% select(Valor, Regiao) %>% filter(Valor>1000)
View(resultado)

resultado <- pagamento %>% select(Valor, Regiao) %>% filter(Valor>1000 & Regiao =='RIO DE JANEIRO')
View(resultado)

###****** Abaixo vemos um código usado para acrescentar em uma tabela,
###*mais uma coluna, usando outra como parametro *****
resultado <- pagamento %>% select(Valor, Regiao) %>% mutate(pix = (Valor * 0.135))


resultado <- pagamento %>% select(NumeroNota, Valor, Prestador, Regiao) %>% group_by(Regiao) %>%
  summarise((Total = mean (Valor)))
View(resultado)

resultado <- pagamento %>% select(NumeroNota, Valor, Prestador, Regiao) %>% count(Regiao)
View(resultado)

pagamento %>% arrange(desc(Prestador)) ## ORDEM DECRESCENTE
pagamento %>% arrange(Prestador) ## ORDEM CRESCENTE

