# Postprocessing in R

This is a guide to setting up [R] to analyze the log files generated by [HOOMD-blue] colloids simulations in the [PRoPS Group].

See [Simulating waterDPD](/02-Simulating-waterDPD.md) for help running colloids simulations with HOOMD-blue.

This guide is optimized for MacOS

[Last Update: August 2021]

Our R workflow was developed by Mohammad (Nabi) Nabizadeh. This guide was compiled by Rob Campbell.

[R]: https://www.r-project.org/
[HOOMD-blue]: http://glotzerlab.engin.umich.edu/hoomd-blue/
[PRoPS Group]: https://web.northeastern.edu/complexfluids/
<br>

## Getting and Installing R, RStudio, and the Tidyverse

You can install R directly from the [R Project website](https://www.r-project.org/) by downloading from your preferred CRAN mirror (to get automatically redirected to an available server use "0-Cloud")<br>
*Note: If you are downloading for MacOS there are two releases of the latest version of R, one for Intel-based computers and one for the Apple silicon ARM computer. Be sure to choose the correct version for your needs.*

Once you have installed R you should install RStudio from the RStudio website, by choosing the [free desktop version](https://www.rstudio.com/products/rstudio/download/#download)<br>
*Note: The website should automatically detect your operating system and give you the correct download link.*

For getting started with R, it is recommended that you install the [tidyverse](https://www.tidyverse.org/) collection of packages designed for data science. To do this open RStudio and in the Console enter
```console
> install.packages("tidyverse")
```

You are now ready to use R!

After you open RStudio you can also modify it's appearance by going to "RStudio" and then selecting "Preferences..." to open the **Options** window. Go to the "Appearance" option on the sidebar and you can choose between "Classic," "Modern," and "Sky" themes, adjust the font and font size, and change your "Editor theme" to match your color preferences (or to match another IDE, such as "Eclipse").

**Pro Tip**: If you select "Code" from the sidebar and switch to the "Display" tab, you can turn on "Rainbow parentheses" so that each set of parentheses inside another (i.e."(())") will have a different color, making it easier to keep track of nested parentheses and avoid parentheses-related errors.

