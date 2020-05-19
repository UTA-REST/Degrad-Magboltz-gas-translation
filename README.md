# Degrad-Magboltz-gas-translation
This repo has detailed instructions on the process of translating a gas function from Degrad/Magboltz into the PyGasMix module. It also houses extra scripts that automate some parts of the translation.


## Notes: 
  Alright, so first and foremost, you need to have a decent knowledge of Fortran, enough so that you can copy the gas function from the Degrad.f code and call it from your own simplified Fortran wrapper. This will bypass all the overhead functions that you don't need to worry about when translating the gas function. The overhead functions include the Gasmix function the monte functions, and the Elim funcitons. You can do that or simply setup a breaking point before running the monte functions. (The monte functions include MONTET, MONTE, MONTEAT,MONTEBT, etc.. ). This will be helpfull so that you can compare the output arrays between the translated python version and the old fortran version.

  Note that when doing the steps above, you might want to have two files one that will have the function by itself (This is in Fortran), and one where it will have a wrapper that calls the function (Cython). You will use the first one to chip away any line that you have translated so that you can keep track of your current progress, and you will use the second one to test your translation. For instance, if you have translated the function until line X, then the first file will have X lines removed, while the second file will have X lines in python for the gas function, and some lines for the wrapper.
  
  You gotta also keep in mind that the gas function behaves differently depending on the energy limit given to it. So you need to test most of the range of this function. A good way to go about doing this is to choose a really high energy limit (look at the x values of the cross sections to determine what "very high" is ), and a couple of values in the middle.

Once the function is translated, you can do a whole system test, to ensure that the gas function is behaving as expected. You can do that by adding it the Gasmix.pyx code, and running PyBoltz and Magboltz to compare their results. Again choose a good range of energy limits.

### Some extra notes that could be helpful: 

  **Both Degrad and Magboltz have comments at the top that explain inputs, outputs, and the possible gases. 
  
  **Check the list of scripts listed below, some of them could be of great help in easing the process.
  
  **There is a suite of functions that could ease up your translation, those are in the GasUtil.pyx module in PyBoltz.
