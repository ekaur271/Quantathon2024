# Create list to keep track of transactions
date <- rep(NA, 100)
action <- rep(NA, 100)
amount <- rep(NA, 100)

transactions <- data.frame(date, action, amount)

capital = 10000


# In real life this would be a while loop to go through every day.
# In this case we want to make a fixed for loop minimum 60 days to end
i = 0 # iteration of for loop, 0 for now


# Model that will be run daily in this case every increment
df <- read.csv("C:\\Users\\david\\Downloads\\DAL_data_1.csv")
df2 <- read.csv("C:\\Users\\david\\Downloads\\CLF_data_1.csv")
CLF <- df %>%
  semi_join(df2, by = "Date")

DAL <- df2 %>%
  semi_join(df, by = "Date")

length(CLF$Close)
length(DAL$Close)

full_df <- data.frame(DAL, CLF)
full_df$combined <- c((DAL$Close + CLF$Close) / 2)
full_df$relative_strength <-((DAL$Close + CLF$Close)/2 - (DAL$Low + CLF$Low)/2) / ((DAL$High + CLF$High) /2 - (DAL$Low + CLF$Low)/2)
full_df <- full_df[(length(full_df$Close) - 60):length(full_df$Close),]
ts <- ts(full_df$combined)
time <- time(ts)
full_df$ts <- ts
full_df$time <- time

null <- lm(ts ~ 1)
full <- lm(ts ~ full_df$time * full_df$Volume + cos(2*pi*time) + sin(2 * pi* time),full_df)
step <- stepAIC(null, scope = list(upper = full), direction="both")

model <- ar.yw(step$fitted.values)
model$x.mean # mean estimate
model$ar # phi1 and phi2 estimates
sqrt(diag(model$asy.var.coef)) # their standard errors
model$var.pred # error variance estimate

# forecast
model_pred <- predict(model, n.ahead = 30)
U <- model_pred$pred + model_pred$se
L <- model_pred$pred - model_pred$se

# Code for buying or selling
# First set up flags
bought_before = F
sold_before = F
bought_first_time = F
sold_first_time = F

# Get Variable data
residual = step$residuals[length(step$residuals)]
total_price_open = full_df$Open[i] + full_df$Open.1[i]

# If Else to buy or sell
if ((sold_before = F) && (residual > 0 && residual <= 1) && (CLF$Open > U && DAL$Open > U)) {
  # Sell for first time or after first time
  if (sold_first_time = F) {
    amt = capital * 0.10 * total_price_open
    # 
    sold_first_time = T
  } else {
    # second amount
  }
  transactions$date[i] <- i
  transactions$action[i] <- 'sold'
  transactions$amount <= amt
  
  # Reset flags
  sold_before = T
  bought_before = F
} else if ((bought_before = F) && (residual < 0 && residual >= 1))
  if (bought_first_time = F) {
    # amount
    amt = 
    bought_first_time = T
  } else {
    # second amount
  }
  transactions$date[i] <- i
  transactions$action[i] <- 'bought'
  transactions$amount <= amt
} else {
  print("ERROR!!!!!!!!!!!!!")
}
  
