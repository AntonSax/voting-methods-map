import csv


def max_scores():
    with open("public/U.S.-Elections-and-their-Voting-Methods-2020-U.S.-Elections.csv", "r", newline='') as elections_file, open("public/voting-method-by-county-2020-max-scores.csv", "r") as scores_file:
        csv_elections_file = list(csv.reader(elections_file))
        scores_elections_file = list(csv.reader(scores_file))

        #for row in scores_elections_file:
        #    print(row[1])
        #for elections_row in csv_elections_file:
        #    print(elections_row[5])

        # Clean the info in case there are empty lists.
        csv_elections_file = [x for x in csv_elections_file if x != []]

        # There should be no more than 3220 rows.
        print("There are", len(scores_elections_file), " rows of data.")

        # Loop through the Counties
        for count, scores_row in enumerate(scores_elections_file):
            string_score = "0.0"
            score = 0.0
            if (scores_row):
                if (scores_row[4] is not ""):
                    string_score = scores_row[4]
                    try:
                        score = float(string_score)
                    except ValueError:
                        print("The error is in the data on row", count)
                        print(scores_row)
                        print("This is the string_score:", string_score)
                else:
                    print(scores_row) # will print in case we are missing data. e.g. D.c. not having a cell for state

            #print("string", string_score)
            #print("float", score)
            #print(scores_row)

            # With one county chosen, loop through the elections file to find
            #  any lines with a matching county
            if (len(csv_elections_file) == 0):
                print("The csv_elections_file has 0 data.")
                print("len(csv_elections_file):", len(csv_elections_file))
                break
            for elections_row in csv_elections_file:
                #print("Looking for", scores_row[1], "in", elections_row[5])

                # Set a score to that county according to the best
                #   voting method that it uses.
                if (scores_row[1] in elections_row[5]):
                    #print("Found ", scores_row[1], " in ", elections_row[5])
                    if elections_row[8] == "?":
                        score = max(score,0.0)
                    elif elections_row[8] == "Varies":
                        score = max(score,0.0)
                    elif elections_row[8] == "Appointed":
                        score = max(score,0.0)
                    elif elections_row[8] == "Retention":
                        score = max(score,0.0)
                    elif elections_row[8] == "Appointed + Retention":
                        score = max(score,0.0)
                    elif elections_row[8] == "Plurality":
                        score = max(score,1.0)
                    elif elections_row[8] == "Plurality + Retention":
                        score = max(score,1.0)
                    elif elections_row[8] == "Borda":
                        score = max(score,1.0)
                    elif elections_row[8] == "Plurality + Top 2 Runoff (Nonpartisan Primary)":
                        score = max(score,2.0)
                    elif elections_row[8] == "Plurality + Top 3 Runoff (Nonpartisan Primary)":
                        score = max(score,2.0)
                    elif elections_row[8] == "Majority":
                        score = max(score,2.0)
                    elif elections_row[8] == "Majority or Top 2 Runoff (Nonpartisan Primary)":
                        score = max(score,2.0)
                    elif elections_row[8] == "RCV":
                        score = max(score,3.0)
                    elif elections_row[8] == "Block":
                        score = max(score,4.0)
                    elif elections_row[8] == "Approval":
                        score = max(score,4.0)
                    elif elections_row[8] == "Score":
                        score = max(score,5.0)
                    elif elections_row[8] == "Approval + Top 2 Runoff":
                        score = max(score,5.0)
                    elif elections_row[8] == "STAR":
                        score = max(score,6.0)
                    scores_row[4] = score
                    scores_elections_file[count][4] = score

        # Test print to see if can use indices with the created eleciton files
        #print(scores_elections_file[2][2])

        # Print out rows with a score better than 2.0
        for scores_row in scores_elections_file:
            if (scores_row):
                if (scores_row[4] != ""):
                    if (float(scores_row[4]) > 1.0):
                        #print(scores_row)
                        continue

        # Convert the list of lists to the format used by React-Simple-Maps
        for scores_row in scores_elections_file:
            # Append a space in front of the state acronym
            scores_row[2] = ' ' + scores_row[2]
            # Add quotation marks around the county,state name to combine the county and state cell into one cell
            scores_row[1] = "'" + scores_row[1]
            scores_row[2] = scores_row[2] + "'"

    with open("public/voting-method-by-county-2020-max-scores.csv", "w", newline='') as old_scores_file:
        writer = csv.writer(old_scores_file)
        # Overwrite the old scores file
        writer.writerows(scores_elections_file)


if __name__ == "__main__":
    max_scores();
