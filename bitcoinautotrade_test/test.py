import pyupbit

access  =  "lGMDCfqhWbvKOJXl4Nun9xROXkF8xxxi4axDBK7r"           
secret  =  "Bh1Xe7QLlfN3rxCt7WwKqAsiiBB1Z6f6lml1sK2S"           
upbit =  pyupbit.Upbit ( access , secret )

print ( upbit . get_balance ( "KRW-BTT" ))   
print ( upbit . get_balance ( "KRW" ))         
