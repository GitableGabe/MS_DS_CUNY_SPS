# quiz1 solution -- there are often many different for each problem
# I've left some "scaffolding" in place to show how I set up and/or verify my solutions
# 1. Create a vector that contains 20 numbers.
# (You may choose whatever numbers you like,
# but make sure there are some duplicates.)
numVec <- c(1:8,7:14,7:10)
numVec

# 2. Use R to convert the vector from question 1 into a character vector.
charVec <- as.character(numVec)
charVec

# 3. Use R to convert the vector from question 1 into a vector of factors.
numFactors <- as.factor(numVec)
numFactors

# 4. Use R to show how many levels the vector in the previous question has.
nlevels(numFactors)

# alternative solution
length(unique(numFactors))

#5 Use R to create a vector that takes the vector from
# question 1 and performs on it the formula 3x^2 - 4x + 1
numVec <- 3 * numVec ^ 2 - 4 * numVec + 1
numVec

#6. Create a named list. That is, create a list with several elements
# that are each able to be referenced by name.
namedlist <- list(rank = 1:5, players = c("Ada Lovelace", "Grace Hopper"))
namedlist$players[2]

# 7. Create a data frame with four columns - one each character,
# factor (with three levels), numeric, and date.
# Your data frame should have at least 10 observations (rows).
# source: http://www.buzzfeed.com/kateaurthur/all-85-best-picture-oscar-winners-ranked#1gjwibh
# I took a lot of liberties in classifying genres
title <- as.character(c("Unforgiven","The Deer Hunter", "It Happened One Night","The Bridge on the River Kwai","Lawrence of Arabia","The Silence of the Lambs", "The Godfather Part II", "Casablanca","The Godfather", "All about Eve"))
genre <- c("Western", "Drama", "Comedy","Drama", "Drama", "Drama", "Drama", "Drama", "Drama", "Drama")
wins <- as.numeric(c(4, 8, 5, 7, 7, 5, 6, 3, 3, 6))
release <- as.Date(c("1992-1-1", "1978-1-1", "1934-1-1", "1957-1-1", "1962-1-1","1991-1-1", "1974-1-1", "1943-1-1", "1972-1-1", "1950-1-1"))
df <- data.frame(title, genre, wins, release)
df$title <- as.character(df$title)
str(df)

# 8. Illustrate how to add a row with a value for the factor column that isn't already in the list of levels.
# (Note: You do not need to accomplish this with a single line of code.)
# Task: Add "West Side Story", "Musical", 10, "1961-1-1"
dfnew <- data.frame(title="West Side Story", genre="Musical",wins=10, release="1961-1-1")
str(dfnew)
dfnew$release <- as.Date(dfnew$release)
dfnew$title <- as.character(dfnew$title)
str(dfnew)
dfnew$title
str(dfnew)
df <- rbind(df, dfnew)
df
str(df)