highest_temp = 72
lowest_temp = 51
gap = highest_temp - lowest_temp
print("the gap between the highest and lowest temperature in 10 days is", gap)
noon1 = 63
noon2 = 59
noon3 = 59
noon4 = 63
noon5 = 60
noon6 = 64
noon7 = 66
noon8 = 63
noon9 = 62
noon10 = 63
average = (
    noon1 + noon2 + noon3 + noon4 + noon5 + noon6 + noon7 + noon8 + noon9 + noon10
) / 10
print("The average noon temperatrue is", average)
TEMP_PRECISION = 2
celsius_high = (highest_temp - 32) / 1.8
print("The highest temperature in celsius is", round(celsius_high, TEMP_PRECISION))
