#questao 5.6.7 - 4
by_day <- flights %>% 
  group_by(year, month, day) %>%
  summarise(delay = mean(dep_delay, na.rm = TRUE),n = sum(is.na(dep_time)))


ggplot(by_day, aes(delay, n)) +
  geom_point() +
  geom_smooth(se = FALSE)

#questao 5.6.7 - 5
by_carrier <- flights %>%
  group_by(carrier) %>%
  summarise(delay = mean(dep_delay, na.rm = TRUE)) %>%
  arrange(desc(delay))

flights %>% group_by(carrier, dest) %>% summarize(n())

by_carrier <- flights %>%
  group_by(carrier) %>%
  summarise(delay = mean(dep_delay, na.rm = TRUE)) %>%
  arrange(desc(delay))

#questao 5.7.1 - 4
