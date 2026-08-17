import pandas as pd

def main():

    Datapath = "student_performance_ml.csv"

    df = pd.read_csv(Datapath)

    print("Dataset loaded Successfully")

    percentage = df.FinalResult.value_counts(normalize=True)
    #"normalize = True" here does this :- 

    #Proportion = COunt of that category / Total number of rows

    #  Old Method - percentage["Pass"]
    #  New Method - percentage.get("What to look for","Default value if not found in CSV")
    print("Percentage of students passed is : ",percentage.get(1,0)*100)
    print("Percentage of students failed is : ",percentage.get(0,0)*100)
    
    
if __name__ == "__main__":
    main()

# Justification 

# The Dataset is not balanced Because percentage of passed students is more tha fail
