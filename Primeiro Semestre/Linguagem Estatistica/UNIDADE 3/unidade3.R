
diaSemana <- c(1,2,3,4,5,6,7)
diaSemana[5]

nomeSemana <- c("Domingo","Segunda","Ter�a","Quarta","Quinta","Sexta","S�bado")
nomeSemana[2]

##****** Atribuindo valores aos vetores 
names(diaSemana) <- nomeSemana
diaSemana

##****** Acrescentando mais valores aos vetores
nomes <- c("Israel Kessler","Amauri Lucas")
nomes

nomes[length(nomes)+1] <- "Vitor Monte Alto"

nomes

##****** Crianco fun��es na l�nguagem R
soma <- function(valor1, valor2){
  resultado <- valor1 + valor2
  return(resultado)
}
soma(25,1)

multiplicacao <- function(valor1, valor2){
  resultado <- valor1 * valor2
  return(resultado)
}

multiplicacao(25,4)