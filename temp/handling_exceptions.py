

#temperature - 120
temp = None

# fire sprinkler automation
try:
    if (temp > 94):
        print("Turn on the sprinkler, set off the alarms")
    else:
        print("The temperature is normal, we don't have to worry about anything")
except Exception as err:
    print(f"Error with the fire sprinklers, call the fire dept. The error is: {err}")
    


