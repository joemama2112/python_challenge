import pandas as pd

#setting up access to the csv and making it into a data frame
file_path = "Instructions/PyPoll/Resources/election_data.csv"

vote_df = pd.read_csv(file_path)

#grouping the data frame by candidate and counting their votes
results_df = vote_df.groupby("Candidate")["Ballot ID"].count().reset_index()

#renaming the columns
results_df.columns = ["Candidate", "Votes"]

#adding a column for and calculating percentages for each candidate
total_votes = results_df["Votes"].sum()
results_df["Percentage"] = round(results_df["Votes"] / total_votes * 100, 3)

#sorting final results to make it easy to determine winner
results_df = results_df.sort_values(by=['Votes'], ascending=False)

winner = results_df.iloc[0, 0]

#outputting results as text file
with open("poll_results.txt", "w") as output_file:
    print(f"""Election Results
-------------------------
Total number of votes: {total_votes}
-------------------------
{results_df}
-------------------------
Winner: {winner}""", file=output_file)

#outputting results to terminal
print(f"""Election Results

-------------------------

Total number of votes: {total_votes}

-------------------------

{results_df}

-------------------------

Winner: {winner}

The results may also be found in poll_results.txt
""")
      


       