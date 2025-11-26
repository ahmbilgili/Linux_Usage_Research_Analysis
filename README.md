<h1>Linux Usage Trend and End of Lifetime of Windows Versions</h1>

<h2>Overview</h2>
With the discontinuation of Windows 10 support from Microsoft, the current users of Windows 10 (excluding LTSC and IoT versions) will not be able to receive support, including security updates. This raises concerns amongst users, primarily due to security. Some believe that there will be a noticeable shift towards linux systems, resulting in changes among OS market shares, while some believe that there won't be any noticeable shift. My research aims to come up with a satisfactory result that tries to give an answer to the given question, by analyzing the change in market shares of windows and linux after end of support periods of various windows versions, starting from Windows XP up until Windows 10.

<h2>Motivation</h2>
As a Linux user, hearing people stating that users are switching from windows to linux due to recent end of support decision from Microsoft is an interesting take, and since there is no such official statistic regarding this topic, I decided to conduct my own research using various datasets.

<h2>Hypotheses</h2>
<strong>H0 (Null Hypothesis)</strong>: The end of support for Windows operating system versions does not lead to a increase in Linux usage.  
<strong>H1 (Alternative Hypothesis)</strong>: The end of support for Windows operating system versions leads to a increase in Linux usage.

<h2>Data Source</h2>
<strong>Desktop OS Market Shares (2009-2025)</strong>
<ul>
  <li><a>https://gs.statcounter.com/os-market-share/desktop/worldwide</a></li>
</ul> 
<strong>GitHub Archive</strong>
<ul>
  <li><a>https://www.gharchive.org/</a></li>
</ul>
<strong>Wikimedia Pageviews API</strong>
<ul>
  <li><a>https://pageviews.wmcloud.org/</a></li>
</ul>

<h2>Data Collection and Preprocessing</h2>
<ol>
  <li> Data of OS Market Shares from 2009 to 2025 is collected from <a>https://gs.statcounter.com/os-market-share/desktop/worldwide</a>. Multiple csv files with varying categories are obtained, which are combined into a single .csv file (named <strong>2009_2025_combined_out.csv</strong>) using combine_marketshare_csv.py script.</li> 
  <li>Data of pageviews for wikipedia pages named <strong>Linux</strong>, <strong>Debian</strong>, <strong>Ubuntu</strong>, <strong>Red Hat Enterprise Linux</strong>, <strong>Windows XP</strong>, <strong>Windows 7</strong>, <strong>Windows 8</strong>, <strong>Windows 8.1</strong>, <strong>Windows Vista</strong>, <strong>Windows 10</strong> within the range July 2015 - November 2025 are obtained from <a>https://pageviews.wmcloud.org/.</a></li>
</ol>

<h2>Exploratory Data Analysis</h2>
<ol>
  <li>Redundant columns (OS X, Nintendo, PlayStation and any column that isn't windows nor linux) are removed.</li>
  <li>Columns with only NULL values are removed.</li>
</ol>