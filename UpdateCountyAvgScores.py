import csv


def avg_scores():
    with open("public/U.S.-Elections-and-their-Voting-Methods-2020-U.S.-Elections.csv") as elections_file:
        csv_elections_file = list(csv.reader(elections_file))
    with open("public/voting-method-by-county-2020-avg-scores.csv") as scores_file:
        scores_elections_file = list(csv.reader(scores_file))

    #for row in scores_elections_file:
    #    print(row[1])
    #for elections_row in csv_elections_file:
    #    print(elections_row[5])

    for scores_row in scores_elections_file:
        #print(scores_row[1])
        int score = scores_row[5]
        for elections_row in csv_elections_file:
            #print(elections_row[5])
            if (scores_row[1] in elections_row[5]):
                print("Found ", scores_row[1], " in ", elections_row[5])


#    with open(input, "r") as file, open(tmpFile, "w") as outFile:
#        reader = csv.reader(file, delimiter=',')
#        writer = csv.writer(outFile, delimiter=',')
#        header = next(reader)
#        writer.writerow(header)
#        for row in reader:
#            colValues = []
#            for col in row:
#                colValues.append(col.lower())
#            writer.writerow(colValues)
#    os.rename(tmpFile, input)


if __name__ == "__main__":
    avg_scores();
