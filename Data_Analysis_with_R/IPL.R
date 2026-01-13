library(dplyr)
library(ggplot2)
library(reshape2)
library(ggcorrplot)
library(corrplot)
library(infotheo)

data <- read.csv("C:/Users/ASUS/Downloads/Orange Cap 2024.csv")

missing_values_count <- data %>%
  summarise(across(everything(), ~ sum(is.na(.))))

# Print missing values count
print(missing_values_count)

# Scatterplot  for Total.runs vs Average
ggplot(data, aes(x = Total.runs, y = Average)) +
  geom_point() +
  labs(title = "Total Runs vs Average", x = "Total Runs", y = "Average")
# Violin plot for Total.runs by Team.Name
ggplot(data, aes(x = Team.Name, y = Total.runs)) +
  geom_violin() +
  labs(title = "Distribution of Total Runs by Team", x = "Team", y = "Total Runs")
# Line graph for Total.runs over Years
ggplot(data, aes(x = Year, y = Total.runs, group = Player.Name, color = Player.Name)) +
  geom_line() +
  labs(title = "Total Runs Over Years", x = "Year", y = "Total Runs")


numeric_data <- data %>%
  select(Total.runs, Average)  


cor_matrix <- cor(numeric_data, use = "complete.obs")


print(cor_matrix)

positive_corr <- cor_matrix
positive_corr[positive_corr < 0] <- NA

negative_corr <- cor_matrix
negative_corr[negative_corr > 0] <- NA


print("Positive Correlations:")
print(positive_corr)

print("Negative Correlations:")
print(negative_corr)

corrplot(cor_matrix, method = "circle", type = "lower", 
         col = colorRampPalette(c("blue", "white", "red"))(200),
         addCoef.col = "black", 
         tl.col = "black", tl.srt = 45, 
         title = "Correlation Matrix (Positive)")

corrplot(cor_matrix, method = "circle", type = "lower", 
         col = colorRampPalette(c("red", "white", "blue"))(200),
         addCoef.col = "black", 
         tl.col = "black", tl.srt = 45, 
         title = "Correlation Matrix (Negative)")


pearson_corr <- cor(numeric_data, method = "pearson", use = "complete.obs")


print(pearson_corr)


spearman_corr <- cor(numeric_data, method = "spearman", use = "complete.obs")


print(spearman_corr)


anova_results <- aov(Total.runs ~ as.factor(Team.Name), data = data)


summary(anova_results)


kendall_corr <- cor(numeric_data, method = "kendall", use = "complete.obs")


print(kendall_corr)

mi <- mutinformation(data$Total.runs, data$Team.Name)  
data

data$Team.Name <- as.factor(data$Team.Name)


data$Team.Name <- as.factor(data$Team.Name)
data$X50 <- as.factor(data$X50)

contingency_table <- table(data$Team.Name, data$X50)


print(contingency_table)


chi_squared_test <- chisq.test(contingency_table)

print(chi_squared_test)

numeric_data <- data[, sapply(data, is.numeric)]


pearson_corr <- cor(numeric_data, method = "pearson")


pearson_corr_melt <- melt(pearson_corr)



ggplot(pearson_corr_melt, aes(x = Var1, y = Var2, fill = value)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1)) +
  theme_minimal() +
  labs(title = "Pearson Correlation Matrix", x = "", y = "")



numeric_data <- data[, sapply(data, is.numeric)]


spearman_corr <- cor(numeric_data, method = "spearman")


spearman_corr_melt <- melt(spearman_corr)


ggplot(spearman_corr_melt, aes(x = Var1, y = Var2, fill = value)) +
  geom_tile() +
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, limit = c(-1, 1)) +
  theme_minimal() +
  labs(title = "Spearman Correlation Matrix", x = "", y = "")

