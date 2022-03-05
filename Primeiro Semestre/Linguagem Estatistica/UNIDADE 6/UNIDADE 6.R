
install.packages("quantmod")
library(quantmod)

getSymbols("MSFT", src="yahoo", from = Sys.Date() - 15, to = Sys.Date() - 1)

candleChart(MSFT)