from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
     cgpa = float(request.form['cgpa'])
     n = int(request.form['n'])
     if cgpa>8.0:
      result= "you have good cgpa already"
     else:
      result= "you need more sgpa"
      Required_sgpa = 8*(n+1) - (cgpa*n)
     if Required_sgpa<=10:
      result= f"you need {round(Required_sgpa)} for next 1 sem"
      
     else:       
         result="you need 2 sem "
         Required_sgpa_for_2nd_sem = (8*(n+2) - (cgpa*n))/2
         if Required_sgpa_for_2nd_sem<=10:
          result=f"you need {round(Required_sgpa_for_2nd_sem)} for next 2 sem"
          
         else:       
             result="you need 3 sem "
             Required_sgpa_for_3rd_sem = (8*(n+3) - (cgpa*n))/3
             if Required_sgpa_for_3rd_sem<=10:
              result=f"you need {round(Required_sgpa_for_3rd_sem)} for next 3 sem"
               
             else:       
              result="you need 4 sem "
              Required_sgpa_for_4th_sem = (8*(n+4) - (cgpa*n))/4
              if Required_sgpa_for_4th_sem<=10:
               result=f"You need 4 sem {round(Required_sgpa_for_4th_sem)} for next 4sem"
              else:
               result="You need more than 4 sem to reach 8 cgpa , YOU ARE COOKED BRO" 

    return f'''
    <h2>Welcome to  genz CGPA calculator </h2>
    <form method ="post">
    CGPA <input name = "cgpa"><br><br>
    NUMBER OF SEMESTERS STUDENT COMPLETED <input name = "n"><br><br>
    <button type="submit"> CALCULATE </button>
    </form>  
    <h3>{result}</h3>
    '''

if __name__ == "__main__":
     app.run()
    
