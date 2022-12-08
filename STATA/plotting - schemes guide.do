* ==============================================================================
* 1| DATA | ====================================================================
sysuse auto, clear


* ==============================================================================
* 2| PLOT SCHEMES  AND COLORS | ================================================
* ------------------------------------------------------------------------------
ssc install schemepack, replace
* https://medium.com/the-stata-guide/stata-schemes-5ef99d099585

discard

set scheme tab1
set scheme tab2
set scheme tab3
set scheme white_tableau
set scheme myUTEP

graph set
help graph set

graph set window fontface "Roboto condensed"

ssc install palettes, replace

* ==============================================================================
* 3| PLOTS | ===================================================================
*  | SCATTER PLOTS
* ------------------------------------------------------------------------------
twoway lfitci mpg weight || scatter mpg weight,    			                 ///
	title("Binary dependent variable")                                       ///
	xlabel(,grid) ylabel(,grid)                                              ///
	plotregion(lcolor(black))                                                ///
	graphregion(fcolor(white))	
	
	
