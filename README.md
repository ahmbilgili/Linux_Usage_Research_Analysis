<h1>Linux Usage Trend and End of Lifetime of Windows Versions</h1>

<h2>Overview</h2>
With the discontinuation of Windows 10 support from Microsoft, the current users of Windows 10 (excluding LTSC and IoT versions) will not be able to receive support, including security updates. This raises concerns amongst users, primarily due to security. Some believe that there will be a noticeable shift towards linux systems, resulting in changes among OS market shares, while some believe that there won't be any noticeable shift. My research aims to come up with a satisfactory result that tries to give an answer to the given question, by analyzing the change in market shares of windows and linux after end of support periods of various windows versions, starting from Windows XP up until Windows 10.

<h2>Motivation</h2>
As a Linux user, hearing people stating that users are switching from windows to linux due to recent end of support decision from Microsoft is an interesting take, and since there is no such official statistic regarding this topic, I decided to conduct my own research using various datasets.

<h2>Methodology</h2>
Data from multiple resources will be used to understand if there's a significant shift of users from windows to linux. Initially, data will be collected, then preprocessed, and then statistical tests will be implemented based on the parameters of the datasets.

<h2>Hypotheses</h2>
<strong>H0 (Null Hypothesis)</strong>: The end of support for Windows operating system versions does not lead to a increase in Linux usage.<br>
<strong>H1 (Alternative Hypothesis)</strong>: The end of support for Windows operating system versions leads to a increase in Linux usage.  

<h2>Data Source</h2>
<strong>Desktop OS Market Shares (2009-2025)</strong>
<ul>
  <li><a href="https://gs.statcounter.com/os-market-share/desktop/worldwide">https://gs.statcounter.com/os-market-share/desktop/worldwide</a></li>
</ul> 
<strong>GitHub API</strong>
<ul>
  <li>Using the URL <a href="https://api.github.com/search/repositories">https://api.github.com/search/repositories</a> with help of scraper.py
</ul>
<strong>Wikimedia Pageviews API</strong>
<ul>
  <li><a href="https://pageviews.wmcloud.org/">https://pageviews.wmcloud.org/</a></li>
</ul>

<h2>Data Collection</h2>
<ol>
  <li> Data of OS Market Shares from 2009 to 2025 is collected from <a href="https://gs.statcounter.com/os-market-share/desktop/worldwide">https://gs.statcounter.com/os-market-share/desktop/worldwide</a>. Multiple csv files with varying categories are obtained, which are combined into a single .csv file (named <strong>2009_2025_combined_out.csv</strong>) using combine_marketshare_csv.py script.</li> 
  <li>For each day, number of pageviews for wikipedia pages named <strong>Linux</strong>, <strong>Debian</strong>, <strong>Ubuntu</strong>, <strong>Red Hat Enterprise Linux</strong>, <strong>Windows XP</strong>, <strong>Windows Vista</strong> <strong>Windows 7</strong>, <strong>Windows 8</strong>, <strong>Windows 8.1</strong>, <strong>Windows 10</strong> within the range July 2015 - November 2025 are obtained from <a href="https://pageviews.wmcloud.org/">https://pageviews.wmcloud.org/</a></li>
  <li>Number of stars, watchers, owner username and URL of top 100 repositories for each month starting from January 2015 to November 2025, that include keyword "linux" are fetched with help of Github API, using scraper.py script. <strong>(DISCLOSURE)</strong> Scraper script is written with help of Gemini.
  <li>Year, Month, Name, Star Count and Watcher Count data of github repositories that include keyword "linux" are fetched with help of github API using scraper.py script. <strong>Disclaimer</strong>: Gemini Pro (Generative AI tool) was used to write this script.
</ol>

<h2>Data Preprocessing</h2>
<ol>
  <li>Redundant columns (OS X, Nintendo, PlayStation and any column that isn't windows nor linux) from the OS market shares dataset are removed.</li>
  <li>Columns with only NULL values are removed from both OS market share dataset and wikipedia pagevisit counts dataset.</li>
  <li>Due to lack of data for the year 2014, data of Windows XP is removed from pageviews dataset.</li>
  <li>Data from github repositories is aggregated with respect to month-year combinations. That is, star count for the given MM-YYYY is aggregated with help of pandas. Log-transformation will be applied when necessary (i.e., when using a parametric test), since the data is highly skewed.
</ol>

<h2>Exploratory Data Analysis</h2>
<h3>Visual Analysis</h3>
<ul>
  <li>Windows market share declines gradually, despite rare increases in a few periods.</li>
  <li>Linux market share increases steadily, despite some declines in a few periods.</li>
  <li>A moderately linear, negative relationship is seen between Linux market share and Windows market share</li>
  <li>There is a spike in pageviews count of Windows Vista around the end of support date (April 11, 2017)</li>
  <li>There is a spike in pageviews count of Windows 7 around the end of support date (January 14, 2020)</li>
  <li>There is a spike in pageviews count of Windows 8.1 around the end of support date (January 10, 2023)</li>
  <li>There is a spike in pageviews count of Windows 10 around end of the support date (October 10, 2025)</li>
</ul>

<h3>Statistical Analysis</h3>
<ul>
  <li>The heatmap of pageviews is as follows:</li>
  <img src="visuals/heatmap_pageviewsdata.svg" alt="heatmap_pageviews_data">
  <li>Mean of Windows market share throughout the years is found to be 83.144427%</li>
  <li>Mean of Linux market share throughout the years is found to be 1.704948%</li>
  <table>
    <tr>
        <th>Null Hypothesis</th>
        <th>Alternative Hypothesis</th>
        <th>Test Used</th>
        <th>Result</th>
    </tr>
    <tr>
      <td>End of support for windows 7 did not lead to an increase in pageview count of linux</td>
      <td>End of support for windows 7 lead to an increase in pageview count of linux</td>
      <td>Mann-Whitney U-test (One-tailed)</td>
      <td>p-value of 1 is obtained, fail to reject null hypothesis</td>
    </tr>
    <tr>
      <td>End of support for windows 8.1 did not lead to an increase in pageview count of linux</td>
      <td>End of support for windows 8.1 lead to an increase in pageview count of linux</td>
      <td>Mann-Whitney U-test (One-tailed)</td>
      <td>p-value of 1 is obtained, fail to reject null hypothesis</td>
    </tr>
    <tr>
      <td>End of support for windows 10 did not lead to an increase in pageview count of linux</td>
      <td>End of support for windows 10 lead to an increase in pageview count of linux</td>
      <td>Mann-Whitney U-test (One-tailed)</td>
      <td>p-value of 0.99 is obtained, fail to reject null hypothesis</td>
    </tr>
    <tr>
      <td>End of support for windows 8.1 did not lead to an increase in total star count of repositories that include keyword "linux"</td>
      <td>End of support for windows 8.1 lead to an increase in total star count of repositories that include keyword "linux"</td>
      <td>T-test (One-tailed)</td>
      <td>p-value of 1.77e-14 is obtained, reject null hypothesis</td>
    </tr>
  </table>
</ul>

<h4>The visuals and steps taken during whole EDA process can be seen via EDA.ipynb file.</h4>

<h2>Machine learning methods</h2>
<h3>Polynomial Regression</h3>
Data is splitted as 80% training, 20% testing.
Goodness of fit is evaluated via R2 score, while average distance between predicted and real values is evaluated via RMSE.
<table>
    <thead>
        <tr>
            <th>X, Y Value</th>
            <th>R2 Score (Train)</th>
            <th>R2 Score (Test)</th>
            <th>RMSE Score (Train)</th>
            <th>RMSE Score (Test)</th>         
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Date, Linux market share</td>
            <td>0.9533</td>
            <td>0.8768</td>
            <td>0.2073</td>
            <td>0.2206</td>
        </tr>
        <tr>
            <td>Date, Windows market share</td>
            <td>0.9530</td>
            <td>0.9014</td>
            <td>1.6983</td>
            <td>2.6171</td>
        </tr>
    </tbody>
</table>
<h3>Random Forest</h3>
Predictions on change in market shares of windows and linux are predicted via Random Forest. Changes are calculated initially, and the model is trained with respect to the changes, and then real market share is rebuilt.
Accuracy is evaluated via MAE (Mean absolute error).
<table>
    <thead>
        <tr>
            <th>X, Y Value</th>
            <th>MAE</th>    
            <th>R2 Score (Change)</th>
            <th>R2 Score (Final)</th>   
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>[linux pageviews, debian pageviews, ubuntu pageviews, rhel pageviews], linux market share percentage</td>
            <td>0.19896</td>
            <td>-0.18022</td>
            <td>0.41966</td>
        </tr>
        <tr>
            <td>[windows 7 pageviews, windows 8 pageviews, windows 8.1 pageviews, windows vista pageviews, windows 10 pageviews], windows market share percentage</td>
            <td>1.43177</td>
            <td>-0.02287</td>
            <td>-0.82997</td>
        </tr>
    </tbody>
</table>

<h2>Results</h2>
<h3>1. Polynomial Regression Analysis</h3>
<p>The Polynomial Regression model demonstrated a strong ability to capture the trend in market share over time for both operating systems. The model was trained on an 80% split of the dataset and evaluated on the remaining 20%.</p>
<ul>
  <li>
    <strong>Linux Market Share:</strong> The model achieved a high goodness of fit, with a Training R2 of <strong>0.9533</strong> and a Test R2 of <strong>0.8768</strong>. The Root Mean Squared Error (RMSE) remained consistent between training (<strong>0.2073</strong>) and testing (<strong>0.2206</strong>), indicating that the model generalizes well and is not suffering from significant overfitting.
  </li>
  <li>
    <strong>Windows Market Share:</strong> The model performed similarly well, yielding a Training R2 of <strong>0.9530</strong> and a Test R2 of <strong>0.9014</strong>. While the RMSE values (Train: <strong>1.6983</strong>, Test: <strong>2.6171</strong>) are numerically higher than those for Linux, this is attributable to the significantly larger scale of Windows market share percentage compared to Linux.
  </li>
</ul>
<p>Overall, the Polynomial Regression approach proved effective, maintaining high accuracy and generalization capabilities across both target variables.</p>
</section>

<h3>2. Random Forest Analysis</h3>
<p>The Random Forest model attempted to predict the <em>change</em> in market share using pageview data (e.g., Ubuntu, Windows 10 pageviews) as features, rather than predicting the raw market share directly. The final market share was then reconstructed from these predicted changes.</p>
<ul>
  <li>
    <strong>Linux Prediction:</strong> The model struggled to capture the variance in market share changes, resulting in a negative R2 score for the change predictions (<strong>-0.1802</strong>). Consequently, the reconstructed final market share showed a moderate fit with an R2 of <strong>0.4197</strong> and a Mean Absolute Error (MAE) of <strong>0.199</strong>.
  </li>
  <li>
    <strong>Windows Prediction:</strong> The model failed to predict market share changes effectively, by a negative R2 score for change (<strong>-0.0229</strong>). This inability to model the fluctuations led to a poor final reconstruction, resulting in a negative Final R2 of <strong>-0.8300</strong> and a MAE of <strong>1.43</strong>.
  </li>
</ul>
<p>These results suggest that the pageview features utilized in the Random Forest model were insufficient for predicting short-term fluctuations (changes) in market share, leading to poor reconstruction of the overall trend.</p>

<h2>Possible Improvements</h2>
<ul>
<li>More ML methods (such as Facebook Prophet) can be applied for variance.</li>
<li>Feature count can be increased by consulting to more datasets, which can help in generating better results via ML methods.</li>
</ul>

<h2>Reproduction</h2>
<ul>
<li><code>python3 -m venv .venv</code></li>
<li><code>source .venv/bin/activate</code></li>
<li><code>pip install -r requirements.txt</code></li>
<li><code>jupyter notebook</code></li>
</ul>
