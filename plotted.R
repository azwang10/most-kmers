setwd("~/Desktop/most-kmers")
data = read.csv("ranked.csv", header = TRUE)
plot(data[,2], main = 'Do all 6-mers occur at equal frequencies in the E. coli genome?',
     ylab = "6-mer Frequency in Genome", xlab = "6-mers Ranked by Increasing Frequency",
     pch = 20)

ideal = 4641647/4096
abline(h = ideal, col = 'gray', lty = 'dashed', lwd = '4')
text(400, ideal, 'Expected Freq.', pos = 3, cex = 1)