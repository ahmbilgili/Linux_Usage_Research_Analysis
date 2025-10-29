# Linux Usage Trend and End of Lifetime of Windows Versions   

## Motivation  
With the discontinuation of Windows 10 support from Microsoft, the current users of Windows 10 (excluding LTSC and IoT versions) will not be able to receive support, including security updates. This raises concerns amongst users, primarily due to security. Some experts believe that there will be a noticeable shift towards linux systems, resulting in changes among OS market shares, while some experts believe that there won't be any noticeable shift. My research aims to come up with a satisfactory result that tries to give an answer to the given question, by analyzing the change in market shares of windows and linux after end of support periods of various windows versions, starting from Windows XP up until Windows 10

## Hypotheses  
**H0 (Null Hypothesis)**: The end of support for Windows operating system versions does not lead to a increase in Linux usage.  
**H1 (Alternative Hypothesis)**: The end of support for Windows operating system versions leads to a increase in Linux usage.

## Data Source  
<strong>Desktop OS Market Shares (2009-2025)</strong>
<ul>
  <li>https://gs.statcounter.com/os-market-share/desktop/worldwide</li>
</ul> 
<strong>GitHub Archive</strong>
<ul>
  <li>https://www.gharchive.org/</li>
</ul>
<strong>Wikimedia API </strong>
<ul>
  <li>https://pageviews.wmcloud.org/</li>
</ul>

## Data Collection  
- Data of OS Market Shares from 2009 to 2025 will be used for analyzing previous and current trends of linux and windows usage, in order to understand whether if there is a significant change in market shares.
- I believe that there's a close correlation between number of open source repositories and linux user count, so the number of repositories in GitHub that include the keywords such as "linux" and "open source" from the same period will be analyzed for further investigation, via GitHub Archive.
- Wikimedia API will be used for analyzing number of pageviews in topics such as "ubuntu", "mint", "debian", "fedora" and "open source", which are concepts related to linux, since increased/decreased interest in these topics possibly corresponds to increased/decreased interest in using linux systems, which will help in analyzing the current user base.
- I'm planning to utilize selenium for automated data collection from Wikimedia API and GitHub Archive.  
