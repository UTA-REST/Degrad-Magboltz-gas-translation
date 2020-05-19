# Degrad-Magboltz-gas-translation
This repo has detailed instructions on the process of translating a gas function from Degrad/Magboltz into the PyGasMix module. It also houses extra scripts that automate some parts of the translation.

## Steps:
* **Copy the needed gas function, this is so that you wont have to load the whole file (load gasx.f instead of MAGBOLTZ.f or DEGRAD.f) everytime.**

* **There will be hard coded arrays at the top of the function, move them into a format that is similar to the format of the Setup_npy.py in the cython directory.**

* **Also, make sure to include those arraies from the .npy file to your gas function.**

* **Now look at a gas function that is in PyBoltz. For example, DME.pyx, as its a short function. This will give you an insight on how the function should look.**

* **Make sure to map the COMMON block variables to the corresponding ones in the Gasmix object. Check the Gas.pxd object to see the list of the variables the Fortran COMMON block variables map to.**

* **Simply, start translating the function to a Cython version. Always check if the cross section calculation matches up with any of the GasUtil.pyx functions. This will reduce the number of lines, and will speedup the process once you know what functions do what.**

## Notes: 
  Alright, so first and foremost, you need to have a decent knowledge of Fortran, enough so that you can copy the gas function from the Degrad.f code and call it from your own simplified Fortran wrapper. This will bypass all the overhead functions that you don't need to worry about when translating the gas function. The overhead functions include the Gasmix function the monte functions, and the Elim funcitons. You can do that or simply setup a breaking point before running the monte functions. (The monte functions include MONTET, MONTE, MONTEAT,MONTEBT, etc.. ). This will be helpfull so that you can compare the output arrays between the translated python version and the old fortran version.

  Note that when doing the steps above, you might want to have two files one that will have the function by itself (This is in Fortran), and one where it will have a wrapper that calls the function (Cython). You will use the first one to chip away any line that you have translated so that you can keep track of your current progress, and you will use the second one to test your translation. For instance, if you have translated the function until line X, then the first file will have X lines removed, while the second file will have X lines in python for the gas function, and some lines for the wrapper.
  
  You gotta also keep in mind that the gas function behaves differently depending on the energy limit given to it. So you need to test most of the range of this function. A good way to go about doing this is to choose a really high energy limit (look at the x values of the cross sections to determine what "very high" is ), and a couple of values in the middle.

Once the function is translated, you can do a whole system test, to ensure that the gas function is behaving as expected. You can do that by adding it the Gasmix.pyx code, and running PyBoltz and Magboltz to compare their results. Again choose a good range of energy limits.

### Some extra notes that could be helpful: 
* **Both Degrad and Magboltz have comments at the top that explain inputs, outputs, and the possible gases.** 
  
* **Check the list of scripts listed below, some of them could be of great help in easing the process.**
  
* **There is a suite of functions that could ease up your translation, those are in the GasUtil.pyx module in PyBoltz.**

## Scripts:
All the scripts can be run with
```
$ python SCRIPT_NAME.py < input_file.txt > output_file.txt
```

All the scripts have comments that explain their usage.
### Scripts description:

* **Script1:** The first script has two uses. In the first use, it can translate a Fortran array that is listed out on seprate lines to a Python one. In the second use, it can translate the DATA arraies names into the corresponding gases.npy names, and include them into the gas function.

* **Script2** The second script is used to translate the names of the DATA arraies to the corresponding names of them in the gases.npy, and include them into the Setup_npy.py. This could be used instead of the 2nd usage of Script1.

* **Script3** The second script is used to translate the DATA arraies to the corresponding arraies of them in the gases.npy, and include them into the Setup_npy.py. 

* **Script4** The second script is used to translate the names of the DIMENSION arraies to a list of those arraies in Python. This is done to ease the initlization that is needed for cython.

