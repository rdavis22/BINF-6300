#Acetaminophen
dose_mg=raw_input('What is your dose in mg?\n')
new_dose=int(dose_mg)
print new_dose
fq_day=raw_input('How many times a day do you take your Acetaminophen?\n')
new_fq=int(fq_day)
print new_fq
age_yrs=raw_input('What is your age in years?\n')
new_age=int(age_yrs)
print new_age
if new_age < 12:
    wt_kg=raw_input('What is your weight in kg?\n')
    new_wt=int(wt_kg)
    ch_dose=new_dose/new_wt
    if ch_dose <40: #dose is in mg/kg
        print 'Warning! The dose is too low!'
    elif ch_dose>90:
        print 'Warning! The dose is too high!'
    else:
        print 'The dose is within normal range.'
else:
    if new_dose <1300: #dose is in mg
        print 'Warning! The dose is too low!'
    elif new_dose>3250:
        print 'Warning! The dose is too high!'
    else:
        print 'The dose is within normal range.'