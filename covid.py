from covid_india import states
from pywebio.input import *
from pywebio.output import *

def find_output():
    yourchoiceState= radio("Choose the state whose covid data you want to know",options = [ "Andhra Pradesh",
                "Arunachal Pradesh",
                "Assam",
                "Bihar",
                "Chhattisgarh",
                "Goa",
                "Gujarat",
                "Haryana",
                "Himachal Pradesh",
                "Jammu and Kashmir",
                "Jharkhand",
                "Karnataka",
                "Kerala",
                "Madhya Pradesh",
                "Maharashtra",
                "Manipur",
                "Meghalaya",
                "Mizoram",
                "Nagaland",
                "Odisha",
                "Punjab",
                "Rajasthan",
                "Sikkim",
                "Tamil Nadu",
                "Telangana",
                "Tripura",
                "Uttarakhand",
                "Uttar Pradesh",
                "West Bengal",
                "Andaman and Nicobar Islands",
                "Chandigarh",
                "Dadra and Nagar Haveli",
                "Daman and Diu",
                "Delhi",
                "Lakshadweep",
                "Puducherry"])
    choiceInfo=radio("choose the covid info about the state that you have selected",options=['Active cases','Cured cases','Number of deaths'])
    if(choiceInfo=='Active cases'):
        output_found=states.getdata(yourchoiceState)['Active']
    elif choiceInfo=='Cured cases':
        output_found = states.getdata(yourchoiceState)['Cured']
    else:
        output_found = states.getdata(yourchoiceState)['Death']
    print(output_found)
    put_text('The option selected is '+yourchoiceState+' and the output is : '+str(output_found))
if __name__=='__main__':
    find_output()