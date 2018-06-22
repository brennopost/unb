library(tidyverse)

# 2
fluxo_lotacao <- read_csv('fluxo-lotacao-port.csv')

# 4
fluxo <- fluxo_lotacao %>% 
  select(Date_Time_AMPM, Faixa1_Fluxo, Faixa2_Fluxo, Faixa3_Fluxo)

lotacao <- fluxo_lotacao %>% 
  select(Date_Time_AMPM, Faixa1_Lotação, Faixa2_Lotação, Faixa3_Lotação)


# 5
fluxo <- fluxo %>%
  gather(Faixa1_Fluxo:Faixa3_Fluxo, key = faixa, value = fluxo)

lotacao <- lotacao %>% 
  gather(Faixa1_Lotação:Faixa3_Lotação, key = faixa, value = lotacao)

# 6
fluxo$faixa <- as.factor(fluxo$faixa)
levels(fluxo$faixa) <- c(1,2,3)

lotacao$faixa <- as.factor(lotacao$faixa)
levels(lotacao$faixa) <- c(1,2,3)

fluxo_lotacao_joined <- left_join(fluxo, lotacao)

# 7
fluxo_lot <- fluxo_lotacao_joined %>% 
  separate(Date_Time_AMPM, into = c("date", "time"), sep = " ") %>% 
  mutate(date = parse_date(date, "%m/%d/%Y"),
         time = parse_time(time))
