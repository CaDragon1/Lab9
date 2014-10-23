############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.


# Asking for temperature

print 'Hello, welcome to Silent Hill General Hospital. May I please have your temperature?'
temp = int(raw_input())
if temp > 100:
    if temp > 102:
        if temp > 105:
            print 'You can go down to room 103, the doctor will be with you shortly.'
        if temp <= 105:
            print 'Have you been sick in the last 24 hours?'
            sickHr = raw_input()
            if sickHr == 'yes' or sickHr == 'y' or sickHr == 'Yes':
                print 'Room 78 is down the hall to your left.'
            else:
                print 'Come back if you start feeling worse.'
    
            
    
else:
    if temp > 102:
        
    else:
        if temp > 100:
            print 'Have you been sick in the last 24 hours?'
            sickHr = raw_input()
            if sickHr == 'yes' or sickHr == 'y' or sickHr == 'Yes':
                print 'Have you recently been to West Africa?'
                wA = raw_input()
                if wA == 'yes' or sickHr == 'y' or sickHr == 'Yes':
                    print 'Go into the quarantine room, the ebola specialists will join you soon.'
            elif sickHr == 'no' or sickHr == 'No' or sickHr == 'n':
                print 'Have you recently been to West Africa?'
                wA = raw_input()
                if wA == 'yes' or sickHr == 'y' or sickHr == 'Yes':
                    print 'Go into the quarantine room, the ebola specialists will join you soon.' 
#elif temp > 105
    
    
#    print 'Come back if you start feeling worse.'