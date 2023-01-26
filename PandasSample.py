import pandas as pd
from pathlib import Path

def show_rank(csv_path):
    # CsvRead
    df = pd.read_csv(Path(csv_path))

    # Grouping & Aggregate
    df = df.groupby(['player_id']).mean(numeric_only=True)
    df['rank'] = df.rank(numeric_only=True,ascending=False)
    df = df.query('rank <= 10').sort_values('rank')

    # Show(Output)
    print('rank,player_id,mean_score')
    for index, row in df.iterrows() :
        print(row['rank'].astype(int), index, row['score'].astype(int),sep=',')
    
def main():
    show_rank('sample.csv')

if __name__ == '__main__':
    main()