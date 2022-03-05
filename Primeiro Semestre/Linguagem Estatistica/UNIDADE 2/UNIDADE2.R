
var <- "5"

is.numeric(var)
as.numeric(var)

melhorPersonagem <- c("Viper", "Reyna", "Jett", "Astra", "Breach")

for(pos in 1:length(melhorPersonagem)){
  imprima <- print(paste("O melhor personagem de Valorant é: ", melhorPersonagem[pos]))
}