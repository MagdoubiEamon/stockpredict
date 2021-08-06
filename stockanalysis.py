from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import io

class TextAnalyzer:
    def positiveNegativeNeutralStock(fileStock):
        df = pd.read_csv("excel/"+fileStock+'.csv', encoding='cp1252',  error_bad_lines=False)
        #print(df.head())
        analyzer = SentimentIntensityAnalyzer()
        negative = []
        neutral = []
        positive = []
        for n in range(df.shape[0]):
            title = df.iloc[n,0]
            description = df.iloc[n, 2]
            title_analyzed = analyzer.polarity_scores(title)
            description_analyzed = analyzer.polarity_scores(description)
            #print(title_analyzed)
            negative.append((title_analyzed['neg'])+ (description_analyzed['neg'])/2)
            neutral.append((title_analyzed['neu']) + (description_analyzed['neu']) / 2)
            positive.append((title_analyzed['pos']) + (description_analyzed['pos']) / 2)
        df['Negative'] = negative
        df['Neutral'] = neutral
        df['Positive'] = positive
        pd.set_option('display.max_columns', None)
        #print(df.nlargest(5,['Positive']))
        print("Negative: "+str(df['Negative'].mean()))
        print("Positive: "+str(df['Positive'].mean()))
        dfTwo = io.open("excel/"+'finalResult.csv', 'a')
        dfTwo.write("{}, {}, {}, {} \n".format(fileStock, df['Positive'].mean(), df['Neutral'].mean(), df['Negative']
                                               .mean()))
        dfTwo.close()
