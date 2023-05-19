What we need:

Linear:

sklearn
    -> linear_models [as l] -> linearRegression [as lr]
    lr.fit(x,y) (y: the to be predicted value)
    lr.ScoreLinLog(x,y)
    lr.PredictDescriptor(x)
    for improved performance: use l.SDGRegressor()

        reg.coef_ -> shows coefficient value (m)
        reg.intercept_ -> b

        m*x+b

        => this is reg.PredictDescriptor(x)!



MatPlotLib


Logistic:

sklearn
    -> linear_models [as l] -> l.logisticRegression [as lr]
    lr.fit(x,y)
    lr.ScoreLinLog(x,y)

    Support Vector Machine:
        sklearn.svm -> SVC

    Decision Tree Classifier:
        sklearn.tree -> DecisionTreeClassifier

    Prevent overfitting: Random Forest Classificator (p.84)
        sklearn.ensemble -> RandomForestClassificator

    Boosted Decision Trees: (p.85)
        sklearn.ensemble -> AddBoostClassifier


